#undef RC_INVOKED
#define _WINGDI_H
#define _WINUSER_H
#define _WINNLS_H
#define _WINVER_H
#define _WINNETWK_H
#define _WINREG_H
#define _WINSVC_H
#define WIN32_LEAN_AND_MEAN
#include <windows.h>

#include "IEEE_Cigre_DLLWrapper.h"

#define MINDELTAT 1.0e-10

typedef int (*DLLFUNC)(double[]);

double cfundll_(double argv[])
{
	/* argv[0] = Time */
	/* argv[1] = StopTime */

	static HINSTANCE hDLL=NULL;
	static DLLFUNC   DllFunc=NULL;
	static int nval=0;
	int end;

	if(argv[0]<=0.0&&DllFunc==NULL){
    printf("\nTry to load DLL.\n");
		if( (hDLL=LoadLibrary("DLLfunc.dll"))!=NULL){
      printf("  LoadLibrary succeeded.\n");
			DllFunc=(DLLFUNC)GetProcAddress(hDLL,"cdllfun_");
			printf("  GetProcAddress succeeded on cdllfun_.\n");
		}
	}
	if( DllFunc!=NULL ){
		if(argv[0]>=argv[1]-MINDELTAT) end=1;
		else end=0;
		nval = (DllFunc)(argv);
		if(end==1){
			FreeLibrary(hDLL);
			DllFunc=NULL;
			hDLL   =NULL;
			printf("\nDLL is unloaded\n");
		}
	}
	return nval;
}

/* Helper functions to transfer data between ATP/MODELS and the IEEE/Cigre DLLs.
   Assumes all inputs and outputs are doubles, but
   some of the parameters may be integers.
*/

void transfer_dll_inputs (Wrapped_IEEE_Cigre_DLL *pWrap, double x[])
{
  int i;
  double *pDoubles = (double *) pWrap->pModel->ExternalInputs;
  for (i=0; i < pWrap->pInfo->NumInputPorts; i++) {
    pDoubles[i] = x[i];
  }
}

void extract_dll_outputs (Wrapped_IEEE_Cigre_DLL *pWrap, double x[])
{
  int i;
  double *pDoubles = (double *) pWrap->pModel->ExternalOutputs;
  for (i=0; i < pWrap->pInfo->NumOutputPorts; i++) {
    x[i] = pDoubles[i];
  }
}

void initialize_dll_outputs (Wrapped_IEEE_Cigre_DLL *pWrap, double x[])
{
  int i;
  double *pDoubles = (double *) pWrap->pModel->ExternalOutputs;
  for (i=0; i < pWrap->pInfo->NumOutputPorts; i++) {
    pDoubles[i] = x[i];
  }
}

void transfer_dll_parameters (Wrapped_IEEE_Cigre_DLL *pWrap, double x[])
{
  int i, iParm;
  double dParm;
  ArrayMap *pMap;

  char *pData = (char *) pWrap->pModel->Parameters;
  pMap = pWrap->pParameterMap;
  for (i=0; i < pWrap->pInfo->NumParameters; i++) {
    if (pMap[i].dtype == IEEE_Cigre_DLLInterface_DataType_int32_T) {
      iParm = (int) x[i];
      memcpy (pData + pMap[i].offset, &iParm, pMap[i].size);
    } else { // IEEE_Cigre_DLLInterface_DataType_real64_T
      dParm = x[i];
      memcpy (pData + pMap[i].offset, &dParm, pMap[i].size);
    }
  }
}

/* ====== SCRX9 interface (singleton only) =======================

   Inputs:                Outputs:         Parameters (Data):
     0 - Vref               0 - EFD          0 - TAdTB = 0.1
     1 - Ec                                  1 - TB = 10.0
     2 - Vs                                  2 - K = 100.0
     3 - IFD                                 3 - TE = 0.05
     4 - Vt                                  4 - Emin = -5.0
     5 - VUEL                                5 - Emax = 5.0
     6 - VOEL                                6 - Cswitch (int) = 1
     7 - Time (ATP)                          7 - RCdRFD = 10.0
     8 - StopTime (ATP)

   States: 6 doubles, created by the Wrapper, not ATP/MODELS
   Sample Time: 0.005
*/

static Wrapped_IEEE_Cigre_DLL *pSCRX9 = NULL;

void dll_scrx9_i__(double xdata_ar[],
                   double xin_ar[],
                   double xout_ar[],
                   double xvar_ar[])
{
  char *pData;
//  printf ("Initializing model 'scrx9'\n");
  if ((pSCRX9 = CreateFirstDLLModel("SCRX9.dll")) != NULL) {
    if (NULL != pSCRX9->Model_FirstCall) {
      pSCRX9->Model_FirstCall (pSCRX9->pModel);
//      printf("  FirstCall\n");
    }
    initialize_dll_outputs (pSCRX9, xout_ar);
//    printf("  initialized outputs\n");
    transfer_dll_parameters (pSCRX9, xdata_ar);
//    printf("  transferred parameters\n");
    pSCRX9->Model_CheckParameters (pSCRX9->pModel);
//    printf("  checked parameters\n");
    pSCRX9->Model_Initialize (pSCRX9->pModel);
//    printf("  initialized model\n");
  }
  if (pSCRX9 != NULL) {
    //printf ("DLL: Initialized pSCRX9\n");
  } else {
    printf ("DLL: *** Failed to initialize pSCRX9\n");
  }
  return;
}

void dll_scrx9_m__(double xdata_ar[],
                   double xin_ar[],
                   double xout_ar[],
                   double xvar_ar[])
{
  int i;
  double *pDoubles;
  static double next_time = 0.0;
  double atp_time = xin_ar[7];
  double atp_stop = xin_ar[8];
//  printf ("Executing model 'scrx9'\n");
  if (NULL == pSCRX9) {
//    printf("  the DLL was not loaded\n");
    return;
  }

  while (atp_time >= next_time) {
//    printf("  trying a step at %lf with %lf, %lf\n", atp_time, xin_ar[0], xin_ar[1]);
    transfer_dll_inputs (pSCRX9, xin_ar);
//    printf("  transferred inputs\n");
    pSCRX9->Model_Outputs (pSCRX9->pModel);
//    printf("  called the DLL step\n");
    extract_dll_outputs (pSCRX9, xout_ar);
//    printf("  extracted output %lf\n", xout_ar[0]);
    next_time += pSCRX9->pInfo->FixedStepBaseSampleTime;
  }

  if (atp_time >= atp_stop - MINDELTAT) {
//    printf("Reached the end of DLL execution\n");
    FreeFirstDLLModel (pSCRX9);
//    printf("  freed the model\n");
    pSCRX9 = NULL;
    //printf ("DLL: Finalized pSCRX9\n");
  }
  return;
}

/* ====== HWPV interface (singleton only) =======================

   Sample Time: 0.002 (embedded in JSON file)
*/

#define JSON_FILE1 "C:\\src\\pecblocks\\examples\\hwpv\\bal3\\bal3_fhf.json"
#define JSON_FILE2 "C:\\src\\pecblocks\\examples\\hwpv\\ucf4t\\ucf4t_fhf.json"
#define JSON_FILE3 "C:\\src\\pecblocks\\examples\\hwpv\\unb3\\unb3_fhf.json"
#define JSON_FILE4 "C:\\src\\pecblocks\\examples\\hwpv\\osg4\\osg4_fhf.json"
#define JSON_FILE5 "C:\\src\\pecblocks\\examples\\hwpv\\bal3n\\bal3n_fhf.json"

static Wrapped_IEEE_Cigre_DLL *pHWPV = NULL;

void dll_hwpv_i__(double xdata_ar[],
                  double xin_ar[],
                  double xout_ar[],
                  double xvar_ar[])
{
  char *pData;
  if ((pHWPV = CreateFirstDLLModel("HWPV.dll")) != NULL) {
    // overwrite default JSON file with an actual one, knowing this is parameter 0
    union EditValueU val;
    val.Char_Ptr = JSON_FILE5;
    edit_dll_value ((char *)pHWPV->pModel->Parameters, 
                      pHWPV->pParameterMap[0].offset, 
                      pHWPV->pParameterMap[0].dtype, 
                      pHWPV->pParameterMap[0].size,
                      val);
    if (NULL != pHWPV->Model_FirstCall) {
      pHWPV->Model_FirstCall (pHWPV->pModel);
    }
    initialize_dll_outputs (pHWPV, xout_ar);
    // DO NOT CALL the generic transfer_dll_parameters (pHWPV, xdata_ar);
    pHWPV->Model_CheckParameters (pHWPV->pModel);  
    pHWPV->Model_Initialize (pHWPV->pModel);
  }
  if (pHWPV != NULL) {
    //printf ("DLL: Initialized pHWPV\n");
  } else {
    printf ("DLL: *** Failed to initialize pHWPV\n");
  }
  return;
}

void dll_hwpv_m__(double xdata_ar[],
                  double xin_ar[],
                  double xout_ar[],
                  double xvar_ar[])
{
  int i;
  double *pDoubles;
  static double next_time = 0.0;
  double atp_time = xin_ar[9];
  double atp_stop = xin_ar[10];
  if (NULL == pHWPV) {
    return;
  }

  while (atp_time >= next_time) {
    transfer_dll_inputs (pHWPV, xin_ar);
    pHWPV->Model_Outputs (pHWPV->pModel);
    extract_dll_outputs (pHWPV, xout_ar);
    next_time += pHWPV->pInfo->FixedStepBaseSampleTime;
  }

  if (atp_time >= atp_stop - MINDELTAT) {
    FreeFirstDLLModel (pHWPV);
    pHWPV = NULL;
    //printf ("DLL: Finalized pHWPV\n");
  }
  return;
}

/* ====== GFM_GFL_IBR interface (singleton only) =======================

   Sample Time: 10.0e-6
*/

static Wrapped_IEEE_Cigre_DLL *pIBR = NULL;

void dll_gfm_gfl_ibr_i__(double xdata_ar[],
                         double xin_ar[],
                         double xout_ar[],
                         double xvar_ar[])
{
  char *pData;
  if ((pIBR = CreateFirstDLLModel("gfm_gfl_ibr.dll")) != NULL) {
    //printf("created pIBR\n");
    if (NULL != pIBR->Model_FirstCall) {
      pIBR->Model_FirstCall (pIBR->pModel);
      //printf("pIBR first call\n");
    }
    initialize_dll_outputs (pIBR, xout_ar);
    //printf("initialized pIBR outputs\n");
    transfer_dll_parameters (pIBR, xdata_ar);
    //printf("pIBR transfer parameters\n");
    pIBR->Model_CheckParameters (pIBR->pModel);
    //printf("pIBR check parameters\n");
    pIBR->Model_Initialize (pIBR->pModel);
    //printf("pIBR initialize\n");
  }
  if (pIBR != NULL) {
    //printf ("DLL: Initialized pIBR\n");
  } else {
    printf ("DLL: *** Failed to initialize pIBR\n");
  }
  return;
}

void dll_gfm_gfl_ibr_m__(double xdata_ar[],
                         double xin_ar[],
                         double xout_ar[],
                         double xvar_ar[])
{
  int i;
  double *pDoubles;
  static double next_time = 0.0;
  double atp_time = xin_ar[12];
  double atp_stop = xin_ar[13];
  if (NULL == pIBR) {
    return;
  }

  // convert inputs to kV and kA
  if (atp_time >= next_time) {
    for (i=0; i < 9; i++) {
      xin_ar[i] *= 0.001;
    }
  }
  while (atp_time >= next_time) {
    //printf("  trying a step at %lf with %lf, %lf\n", atp_time, xin_ar[0], xin_ar[1]);
    transfer_dll_inputs (pIBR, xin_ar);
    //printf("  transferred inputs\n");
    pIBR->Model_Outputs (pIBR->pModel);
    //printf("  called the DLL step\n");
    extract_dll_outputs (pIBR, xout_ar);
    //printf("  extracted output %lf\n", xout_ar[0]);
    next_time += pIBR->pInfo->FixedStepBaseSampleTime;
  }

  // convert Ea, Eb, and Ec from kV to volts
  for (i=0; i < 3; i++) {
    xout_ar[i] *= 1000.0;
  }

  if (atp_time >= atp_stop - MINDELTAT) {
    FreeFirstDLLModel (pIBR);
    pIBR = NULL;
    //printf ("DLL: Finalized pIBR\n");
  }
  return;
}


/* ========================= SCRX9 Model Info printout ============================================= 
Time Step: 0.005 [s]
EMT/RMS Mode: n/a
Parameters (idx,size,offset,name,val,desc,units,default,min,max:
   0    8    0 TAdTB                 0.1 Smoothing Time Constant                                                sec        0.1   0.001   100
   1    8    8 TB                     10 Smoothing Time Constant                                                sec        10    0.001   100
   2    8   16 K                     100 Gain                                                                   pu         100   0.001   1000
   3    8   24 TE                   0.05 Time Constant                                                          sec        0.05          0.001   100
   4    8   32 EMin                   -5 Min Field Voltage                                                      pu         -5    -100    -1
   5    8   40 EMax                    5 Max Field Voltage                                                      pu         5     1       100
   6    4   48 CSwitch                 1 Power source: 0=VT, 1=1.0                                                         1     0       1
   7    8   56 RCdRFD                 10 Field resistance ratio                                                            10    0.001   100
Input Signals (idx,size,offset,name,desc,units):
   0    8    0 VRef         Reference voltage                                                      pu
   1    8    8 Ec           Measured voltage                                                       pu
   2    8   16 Vs           Stabilizer signal                                                      pu
   3    8   24 IFD          Field Current                                                          pu
   4    8   32 VT           Terminal voltage                                                       pu
   5    8   40 VUEL         Under excitation limit                                                 pu
   6    8   48 VOEL         Over excitation limit                                                  pu
Output Signals (idx,size,offset,name,desc,units):
   0    8    0 EFD          Output Field Voltage                                                   pu
Internal State Variables: 0 int, 0 float, 6 double
*/

/* ========================= HWPV Model Info printout ============================================= 
Time Step: 0.002 [s]
EMT/RMS Mode: n/a
Parameters (idx,size,offset,name,val,desc,units,default,min,max:
   0    8    0 JSONfile     C:\src\pecblocks\examples\hwpv\bal3n\bal3n_fhf.json JSON file with trained model            
Input Signals (idx,size,offset,name,desc,units):
   0    8    0 T            Panel temperature                                                      C
   1    8    8 G            Solar irradiance                                                       W/m2
   2    8   16 Fc           Frequency control                                                      Hz
   3    8   24 Ud           d-axis voltage control                                                 pu
   4    8   32 Uq           q-axis voltage control                                                 pu
   5    8   40 Vd           d-axis terminal voltage                                                V
   6    8   48 Vq           q-axis terminal voltage                                                V
   7    8   56 GVrms        Product of G and AC terminal voltage                                   V*kW/m2
   8    8   64 Ctl          State 0=start,1=grid formed,2=grid following
Output Signals (idx,size,offset,name,desc,units):
   0    8    0 Vdc          DC Bus Voltage                                                         V
   1    8    8 Idc          DC Current                                                             A
   2    8   16 Id           AC d-axis Current Injection                                            A
   3    8   24 Iq           AC q-axis Current Injection                                            A
Internal State Variables: 4 int, 0 float, 0 double
*/

/* ========================= GFM_GFL_IBR Info printout ============================================= 
Time Step: 1e-05 [s]
EMT/RMS Mode: n/a
Parameters (idx,name,val,desc,units,default,min,max:
   0 Vbase         0.65 RMS L-L base voltage                                          kV       0.65  0.001   1000
   1 Sbase         1000 MVA base                                                      MVA      1000  0.001   10000
   2 Vdcbase        1.3 dc base voltage                                               kV       1.3   0.001   1000
   3 KpI            0.5 Current control proportional gain                             pu/pu    0.5   0.001   100
   4 KiI              1 Current control integral gain                                 pu/pu    1     0       100
   5 Wtype            0 Frequency generation control type                             N/A      0     0       100
   6 KpPLL           20 PLL proportional gain                                         pu/rad/s 20    1       500
   7 KiPLL          200 PLL integral gain                                             pu/rad/s 200   0.1     5000
   8 del_f_limit     12 Delta Frequency Limit                                         Hz       12    10      20
   9 KpP            0.5 Active power control proportional gain                        pu/pu    0.5   0.001   100
  10 KiP             10 Active power control integral gain                            pu/pu    10    0       100
  11 Qflag            1 Q control (0-Q,1-V)                                           N/A      1     0       1
  12 KpQ            0.5 Reactive power control proportional gain                      pu/pu    0.5   0.001   100
  13 KiQ             20 Reactive power control integral gain                          pu/pu    20    0       100
  14 KpV            0.5 Voltage magnitude control (PLL-base) proportional gain        pu/pu    0.5   0.001   100
  15 KiV            150 Voltage magnitude control (PLL-base) integral gain            pu/pu    150   0       1000
  16 KpVq             0 q-axis voltage magnitude control (PLL-base) proportional gain pu/pu    0     0       100
  17 KiVq             0 q-axis voltage magnitude control (PLL-base) integral gain     pu/pu    0     0       1000
  18 Imax           1.2 Maximum value of current magnitude                            pu       1.2   1       1.7
  19 Pmax             1 Maximum value of active power                                 pu       1     0       1
  20 Pmin             0 Minimum value of active power                                 pu       0     -1      0
  21 Qmax             1 Maximum value of reactive power                               pu       1     0       1
  22 Qmin            -1 Minimum value of reactive power                               pu       -1    -1      0
  23 PQflag           1 PQ priority (0-P,1-Q)                                         N/A      1     0       1
  24 KfDroop         30 Frequency droop gain                                          pu/pu    30    0       500
  25 KvDroop      22.22 Voltage droop gain                                            pu/pu    22.22 0       500
  26 K_POD            0 Power Oscillation Damper Gain                                 pu/pu    0     0       50
  27 T_POD         0.01 Power Oscillation Damper Time constant                        s        0.01  0.001   1
  28 T1_POD        0.01 Power Oscillation Damper Lead                                 s        0.01  0.001   1
  29 T2_POD       0.001 Power Oscillation Damper Lag                                  s        0.001 0.001   1
  30 POD_min       -0.5 Power Oscillation Damper Min Limit                            pu       -0.5  -1      0
  31 POD_max        0.5 Power Oscillation Damper Max Limit                            pu       0.5   0       1
  32 Vdip           0.8 Under voltage threshold to freeze                             pu       0.8   0.7     0.9
  33 Vup            1.2 Over voltage threshold to freeze                              pu       1.2   1.1     1.3
  34 KpVdq            3 Vd and Vq proportional gain                                   pu       3     0       100
  35 KiVdq           10 Vd and Vq proportional gain                                   pu       10    0       100
  36 Tr           0.001 Power measurement transducer                                  s        0.001 0       0.1
  37 Rchoke           0 Filter resistance                                             pu       0     0       1
  38 Lchoke        0.15 Filter inductance                                             pu       0.15  0.001   1
  39 Cfilt      0.01666 Filter capacitance                                            pu     0.01666 0.001   1
  40 Rdamp       9.4868 Filter damper resistance                                      pu     9.4868  0.001   10
Input Signals (idx,size,offset,name,desc,units):
   0    8    0 Va           A phase point of control voltage                                       kV
   1    8    8 Vb           B phase point of control voltage                                       kV
   2    8   16 Vc           C phase point of control voltage                                       kV
   3    8   24 Ia           A phase point of control current                                       kA
   4    8   32 Ib           B phase point of control current                                       kA
   5    8   40 Ic           C phase point of control current                                       kA
   6    8   48 IaL1         A phase before capacitor current                                       kA
   7    8   56 IbL1         B phase before capacitor current                                       kA
   8    8   64 IcL1         C phase before capacitor current                                       kA
   9    8   72 Pref         Active power reference                                                 MW
  10    8   80 Qref         Reactive power reference                                               Mvar
  11    8   88 Vref         Voltage magnitude reference                                            pu
Output Signals (idx,size,offset,name,desc,units):
   0    8    0 Ea           A phase inverter voltage                                               kV
   1    8    8 Eb           B phase inverter voltage                                               kV
   2    8   16 Ec           C phase inverter voltage                                               kV
   3    8   24 Idref        d reference current                                                    pu
   4    8   32 Id           d axis current                                                         pu
   5    8   40 Iqref        q reference current                                                    pu
   6    8   48 Iq           q axis current                                                         pu
   7    8   56 Vd           d axis voltage                                                         pu
   8    8   64 Vq           q axis voltage                                                         pu
   9    8   72 Freq_pll     PLL frequency                                                          Hz
  10    8   80 Pout         Output active power                                                    MW
  11    8   88 Qout         Output reactive power                                                  Mvar
Internal State Variables: 0 int, 0 float, 36 double
*/
