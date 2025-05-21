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
    }
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
  static double next_time = 0.0;
  double atp_time = xin_ar[7];
  double atp_stop = xin_ar[8];
//  printf ("Executing model 'scrx9'\n");
  if (NULL == pSCRX9) {
//    printf("  the DLL was not loaded\n");
    return;
  }

  if (atp_time <= 0.0) { // apply initial conditions here
    xout_ar[0] = 1.0;
    xin_ar[0] = 1.0;
    xin_ar[1] = 1.0;
    xin_ar[4] = 1.0;
    initialize_dll_outputs (pSCRX9, xout_ar);
    transfer_dll_inputs (pSCRX9, xin_ar);
    transfer_dll_parameters (pSCRX9, xdata_ar);
    pSCRX9->Model_CheckParameters (pSCRX9->pModel);
    pSCRX9->Model_Initialize (pSCRX9->pModel);
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
    //initialize_dll_outputs (pIBR, xout_ar);
    //printf("initialized pIBR outputs\n");
    //transfer_dll_parameters (pIBR, xdata_ar);
    //printf("pIBR transfer parameters\n");
    //pIBR->Model_CheckParameters (pIBR->pModel);
    //printf("pIBR check parameters\n");
    //pIBR->Model_Initialize (pIBR->pModel);
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

  if (atp_time <= 0.0) { // apply initial conditions here
    //xin_ar[9] = 950.0;
    //xin_ar[10] = -50.0;
    //xin_ar[11] = 1.0;
    initialize_dll_outputs (pIBR, xout_ar);
    transfer_dll_inputs (pIBR, xin_ar);
    transfer_dll_parameters (pIBR, xdata_ar);
    pIBR->Model_CheckParameters (pIBR->pModel);
    pIBR->Model_Initialize (pIBR->pModel);
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

/* ====== GFM_GFL_IBR2 interface (singleton only) =======================

   Sample Time: 10.0e-6
*/

static Wrapped_IEEE_Cigre_DLL *pIBR2 = NULL;

void dll_gfm_gfl_ibr2_i__(double xdata_ar[],
                         double xin_ar[],
                         double xout_ar[],
                         double xvar_ar[])
{
  char *pData;
  if ((pIBR2 = CreateFirstDLLModel("gfm_gfl_ibr2.dll")) != NULL) {
    //printf("created pIBR2\n");
    if (NULL != pIBR2->Model_FirstCall) {
      pIBR2->Model_FirstCall (pIBR2->pModel);
      //printf("pIBR2 first call\n");
    }
    //initialize_dll_outputs (pIBR2, xout_ar);
    //printf("initialized pIBR2 outputs\n");
    //transfer_dll_parameters (pIBR2, xdata_ar);
    //printf("pIBR2 transfer parameters\n");
    //pIBR2->Model_CheckParameters (pIBR2->pModel);
    //printf("pIBR2 check parameters\n");
    //pIBR2->Model_Initialize (pIBR2->pModel);
    //printf("pIBR2 initialize\n");
  }
  if (pIBR2 != NULL) {
    //printf ("DLL: Initialized pIBR\n");
  } else {
    printf ("DLL: *** Failed to initialize pIBR2\n");
  }
  return;
}

void dll_gfm_gfl_ibr2_m__(double xdata_ar[],
                         double xin_ar[],
                         double xout_ar[],
                         double xvar_ar[])
{
  int i;
  static double next_time = 0.0;
  double atp_time = xin_ar[14];
  double atp_stop = xin_ar[15];
  if (NULL == pIBR2) {
    return;
  }

  // convert inputs to kV, kA, MW, MVAR
  if (atp_time >= next_time) {
    for (i=0; i < 11; i++) {
      xin_ar[i] *= 0.001;
    }
    xin_ar[11] *= 0.000001;
    xin_ar[12] *= 0.000001;
    xin_ar[13] *= 0.001;
  }

  if (atp_time <= 0.0) { // apply initial conditions here
    //xin_ar[9] = 950.0;
    //xin_ar[10] = -50.0;
    //xin_ar[11] = 1.0;
    initialize_dll_outputs (pIBR2, xout_ar);
    transfer_dll_inputs (pIBR2, xin_ar);
    transfer_dll_parameters (pIBR2, xdata_ar);
    pIBR2->Model_CheckParameters (pIBR2->pModel);
    pIBR2->Model_Initialize (pIBR2->pModel);
  }

  while (atp_time >= next_time) {
    //printf("  trying a step at %lf with %lf, %lf\n", atp_time, xin_ar[0], xin_ar[1]);
    transfer_dll_inputs (pIBR2, xin_ar);
    //printf("  transferred inputs\n");
    pIBR2->Model_Outputs (pIBR2->pModel);
    //printf("  called the DLL step\n");
    extract_dll_outputs (pIBR2, xout_ar);
    //printf("  extracted output %lf\n", xout_ar[0]);
    next_time += pIBR2->pInfo->FixedStepBaseSampleTime;
  }

  // convert m_a, m_b, and m_c from the modulation index to something else?
  for (i=0; i < 3; i++) {
    xout_ar[i] *= 1.0;
  }

  if (atp_time >= atp_stop - MINDELTAT) {
    FreeFirstDLLModel (pIBR2);
    pIBR2 = NULL;
    //printf ("DLL: Finalized pIBR2\n");
  }
  return;
}


/* ========================= GFM_GFL_IBR2 Info printout ============================================= 
Time Step: 1e-05 [s]
EMT/RMS Mode: n/a
Parameters (idx,size,offset,name,val,desc,units,default,min,max:
   0    8    0 VLLbase               600 RMS L-L base voltage                                                   V          600   0.001   1000
   1    8    8 Sbase               1e+06 VA base                                                                VA         1e+06         0.001   1e+08
   2    8   16 Tflt_v              1e-05 LPF time constant for voltage                                          s          1e-05         0       10
   3    8   24 Vflt_flag               1 Flag for voltage filter                                                N/A        1     0       1
   4    8   32 Tflt_i              1e-05 LPF time constant for current                                          s          1e-05         0       10
   5    8   40 Iflt_flag               1 Flag for currrent filter                                               N/A        1     0       1
   6    8   48 Cur1_flag               1 Current control at (1: before LCL, 0: after LCL)                       N/A        1     0       1
   7    8   56 k_PLL                   1 Damping constant for SOGI filter                                       N/A        1     0       1000
   8    8   64 KpPLL                25.4 Proportional gain for PLL                                              pu/pu      25.4          0       1000
   9    8   72 KiPLL                 324 Integral gain for PLL                                                  pu/pu      324   0.001   1000
  10    8   80 Lim_PLL                70 Windup limit for PLL                                                   pu/pu      70    0       1000
  11    8   88 w_nom             376.991 Nominal angular frequency                                              rad/s      376.991       1       1e+08
  12    8   96 tstart_up             1.9 Time for start up flag of Q and Vt closed loop                         s          1.9   0       1000
  13    8  104 Vdc_nom              1200 Nominal DC Link Voltage                                                kV         1200          0       10000
  14    8  112 VI_flag                 0 1: enable PPS VI characteristic, 0: constant I                         N/A        0     0       1
  15    8  120 MPPT_flag               0 1: enable MPPT for Vdc*, requires VI_flag=I and Vdc_flag=1             pu/pu      0     0       1
  16    8  128 b_Vdc                0.56 Setpoint weight for DC voltage                                         N/A        0.56          0       100
  17    8  136 Kp_Vdc               5.18 Proportional gain for Vdc                                              pu/pu      5.18          0.001   1000
  18    8  144 Ki_Vdc              52.91 Integral gain for Vdc                                                  pu/pu      52.91         0       1000
  19    8  152 T_frq                 0.1 Time constant for PLL frequency                                        s          0.1   0       1
  20    8  160 fdbd1             -0.0006 Lower deadband for frequency droop control                             N/A        -0.0006       -1e+08          0
  21    8  168 fdbd2              0.0006 Upper deadband for frequency droop control                             N/A        0.0006        0       1e+08
  22    8  176 Ddn                    20 Inverse of droop for high frequency                                    ******     20    0       5000
  23    8  184 Dup                     0 Inverse of droop for low frequency                                     ******     0     0       100
  24    8  192 Tp_droop            0.001 Time constant for first order lag block in Pf control                  s          0.001         0       100
  25    8  200 Vdc_flag                0 dc control flag (1: enable, 0: const. PQ)                              N/A        0     0       1
  26    8  208 f_flag                  0 Frequency flag (1: enable frequency droop control)                     N/A        0     0       1
  27    8  216 Id_frz_flag             0 freeze Id during LVRT                                                  N/A        0     0       1
  28    8  224 Ilim_pu               1.1 Inverter Current limit                                                 pu         1.1   -10     10
  29    8  232 Vt_ref               1.01 pu reference voltage for Vt control                                    pu         1.01          -10     10
  30    8  240 Kv_p                    0 Proportional gain for terminal voltage PI controller                   pu         0     0       1e+08
  31    8  248 Kv_i                  100 Proportional gain for terminal voltage PI controller                   pu         100   0       1e+08
  32    8  256 Qmin                 -0.4 Minimum reactive power in pu                                           pu         -0.4          -1e+08          1e+08
  33    8  264 Qmax                  0.4 Maximum reactive power in pu                                           pu         0.4   -1e+08          1e+08
  34    8  272 Kq_p                    0 Q closed-loop proportional control gain                                pu         0     0       1e+08
  35    8  280 Kq_i                   40 Q closed-loop integral control gain                                    pu         40    0       1e+08
  36    8  288 dbhv_frt             -0.1 Dead band LVRT +ve sequence HV                                         pu         -0.1          -1e+08          1e+08
  37    8  296 dblv_frt              0.1 Dead band HVRT +ve sequence LV                                         pu         0.1   -1e+08          1e+08
  38    8  304 Kqv1                    2 Proportional gain for positive voltage dip                             pu         2     0       1e+08
  39    8  312 Qctl_CL_flag            1 1: enables closed loop Q control, 0: open loop                         N/A        1     0       1
  40    8  320 Vt_flag                 1 1: enable inverter term. voltage control, 0: Q control                 N/A        1     0       1
  41    8  328 dbl_2                -0.1 VRT dead band (negative)                                               N/A        -0.1          -1e+08          0
  42    8  336 dbh_2                 0.1 VRT dead band (positive)                                               N/A        0.1   0       1e+08
  43    8  344 Kqv2                    2 Proportional gain for -ve voltage deviation                            pu         2     0       1e+08
  44    8  352 V2_flag                 1 1: enable V2 control during FRT                                        pu         1     0       1
  45    8  360 Ipramp_up               1 Ramp up rate for active current                                        pu         1     0       1e+08
  46    8  368 Kcc_p             0.32325 Proportional gain PI controller in current controller                  pu         0.32325       0       1e+08
  47    8  376 Kcc_i                 324 Integral gain PI controller in current controller                      pu         324   0       1e+08
  48    8  384 Lim_upCC            99999 Current controller's anti-windup upper limit                           pu         99999         0       1e+08
  49    8  392 Lim_lowCC          -99999 Current controller's anti-windup lower limit                           pu         -99999        -1e+08          0
  50    8  400 Tau_Vff            0.0001 Time constant of LPF for voltage current controller                    s          0.0001        0       1e+08
  51    8  408 Vff_flag                0 Voltage filter flag (1 enable)                                         N/A        0     0       1e+08
  52    8  416 Lchoke             0.0001 Filter inductance                                                      pu         0.0001        1e-06   10
  53    8  424 IR_flag                 1 Flag                                                                   N/A        1     0       1
Input Signals (idx,size,offset,name,desc,units):
   0    8    0 Vta          A phase terminal voltage                                               kV
   1    8    8 Vtb          B phase terminal voltage                                               kV
   2    8   16 Vtc          C phase terminal voltage                                               kV
   3    8   24 I1a          A phase VSC current                                                    kA
   4    8   32 I1b          B phase VSC current                                                    kA
   5    8   40 Ilc          C phase VSC current                                                    kA
   6    8   48 12a          A phase current after capacitor                                        kA
   7    8   56 I2b          B phase current after capacitor                                        kA
   8    8   64 I2c          C phase current after capacitor                                        kA
   9    8   72 Idc          Current from Primay Power Source                                       kA
  10    8   80 VdcMPPT      Maximum power point voltage                                            kV
  11    8   88 Pref         Active power reference                                                 MW
  12    8   96 Qref         Reactive power reference                                               Mvar
  13    8  104 Vdc_meas     Measured DC Voltage                                                    kV
  14    8  112 currTime     Current Time                                                           s
Output Signals (idx,size,offset,name,desc,units):
   0    8    0 m_a          Phase A modulating signal                                              N/A
   1    8    8 m_b          Phase B modulating signal                                              N/A
   2    8   16 m_c          Phase C modulating signal                                              N/A
   3    8   24 FreqPLL      PLL frequency                                                          Hz
   4    8   32 Id1          Positive Current d                                                     pu
   5    8   40 Iq1          Positive Current q                                                     pu
   6    8   48 Id2          Negative Current d                                                     pu
   7    8   56 Iq2          Negative Current q                                                     pu
   8    8   64 Vtd1         Positive Voltage d                                                     pu
   9    8   72 Vtq1         Positive Voltage q                                                     pu
  10    8   80 Vtd2         Negative Voltage d                                                     pu
  11    8   88 Vtq2         Negative Voltage q                                                     pu
  12    8   96 FRT_Flag     Fault ride-through                                                     N/A
Internal State Variables: 0 int, 0 float, 93 double
*/

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
