// Copyright (C) 2024-26 Meltran, Inc

// see https://learn.microsoft.com/en-us/windows/win32/dlls/using-run-time-dynamic-linking

#define DLL_NAME "GFM_GFL_IBR.dll"

#define TMAX 0.5
#define VBASE 600.0
#define SBASE 1.0e6
#define XPU 0.20
#define RPU 0.01

// relative output path for execution from the build directory, e.g., release\test or debug\test
#define CSV_NAME "ibr.csv"

#include <windows.h> 
#include <stdio.h> 
#define _USE_MATH_DEFINES
#include <math.h>

#include "IEEE_Cigre_DLLWrapper.h"
 
void initialize_outputs (IEEE_Cigre_DLLInterface_Instance* pModel, ArrayMap *pMap, int nPorts)
{
  double val = 0.0;
  char *pData = (char *) pModel->ExternalOutputs;
  for (int i = 0; i < nPorts; i++) {
    memcpy (pData + pMap[i].offset, &val, pMap[i].size);
  }
}

void update_inputs (IEEE_Cigre_DLLInterface_Instance* pModel, ArrayMap *pMap, double t, 
                    double kVa, double kVb, double kVc, double kIa, double kIb, double kIc)
{
  double Pref = 0.9, Qref = 0.0, Vref = 1.05; // units MW, MVar, pu
  char *pData = (char *) pModel->ExternalInputs;
  memcpy (pData + pMap[0].offset, &kVa, pMap[0].size);
  memcpy (pData + pMap[1].offset, &kVb, pMap[1].size);
  memcpy (pData + pMap[2].offset, &kVc, pMap[2].size);
  memcpy (pData + pMap[3].offset, &kIa, pMap[3].size);
  memcpy (pData + pMap[4].offset, &kIb, pMap[4].size);
  memcpy (pData + pMap[5].offset, &kIc, pMap[5].size);
  memcpy (pData + pMap[6].offset, &kIa, pMap[6].size);
  memcpy (pData + pMap[7].offset, &kIb, pMap[7].size);
  memcpy (pData + pMap[8].offset, &kIc, pMap[8].size);
  if (t > 0.1) {
    memcpy (pData + pMap[9].offset, &Pref, pMap[9].size);
    memcpy (pData + pMap[10].offset, &Qref, pMap[10].size);
    memcpy (pData + pMap[11].offset, &Vref, pMap[11].size);
  }
}

void set_parameter (Wrapped_IEEE_Cigre_DLL *pWrap, double val, int idx)
{
  char *pData = (char *) pWrap->pModel->Parameters;
  ArrayMap *pMap = pWrap->pParameterMap;
  memcpy (pData + pMap[idx].offset, &val, pMap[idx].size);
}

double extract_output (IEEE_Cigre_DLLInterface_Instance* pModel, ArrayMap *pMap, int idx)
{
  char *pData = (char *) pModel->ExternalOutputs;
  double val = 0.0;
  memcpy (&val, pData + pMap[idx].offset, pMap[idx].size);
  return val;
}

int main( void ) 
{
  double Ea = 0.0, Eb = 0.0, Ec = 0.0; // inverter voltage outputs from the DLL
  double Vsa, Vsb, Vsc; // infinite bus source voltages
  double Ia, Ib, Ic; // currents in the SMIB impedance
  double Ha = 0.0, Hb = 0.0, Hc = 0.0; // RL integration history currents
  double rl_y, rl_zi, rl_yi; // RL adjustments
  double omega = 120.0 * M_PI;
  double Zbase = VBASE * VBASE / SBASE;
  double res = Zbase * RPU;
  double x = Zbase * XPU;
  double ind = x / omega;
  double Vmag = VBASE * sqrt (2.0 / 3.0);
  double rad120 = 120.0 * M_PI / 180.0;

  show_struct_alignment_requirements ();
  Wrapped_IEEE_Cigre_DLL *pWrap = CreateFirstDLLModel (DLL_NAME);
  if (NULL != pWrap) {
    set_parameter (pWrap, 1.0, 1);  // Sbase
    set_parameter (pWrap, 0.0, 37); // Rchoke
    set_parameter (pWrap, 0.0, 38); // Lchoke
    set_parameter (pWrap, 0.0, 39); // Cfilt
    set_parameter (pWrap, 1.0e8, 40); // Rdamp
    PrintDLLModelParameters (pWrap);
    // initialize the model
    if (NULL != pWrap->Model_FirstCall) {
      pWrap->Model_FirstCall (pWrap->pModel);
    }
    printf("calling CheckParameters\n");
    pWrap->Model_CheckParameters (pWrap->pModel);
    check_messages ("Model_CheckParameters", pWrap->pModel);

    // initialize time-stepping
    printf("calling Initialize\n");
    initialize_outputs (pWrap->pModel, pWrap->pOutputMap, pWrap->pInfo->NumOutputPorts);
    pWrap->Model_Initialize (pWrap->pModel);
    check_messages ("Model_Initialize", pWrap->pModel);

    // time step loop, matching the DLL's desired time step
    double dt = pWrap->pInfo->FixedStepBaseSampleTime;
    printf("Looping with dt=%g, tmax=%g\n", dt, TMAX);
    double t = 0.0;
    printf("opening %s\n", CSV_NAME);
    FILE *fp = fopen (CSV_NAME, "w");
    write_csv_header (fp, pWrap->pInfo);
    double tstop = TMAX + 0.5 * dt;

    // setting up for trapezoidal integration
    rl_y = 1.0 / (res + 2.0 * ind / dt);
    rl_zi = 1.0 - 2.0 * res * rl_y;
    rl_yi = 2.0 * rl_y * (1.0 - res * rl_y);

    while (t <= tstop) {
      // simulate the SMIB impedance
      // infinite bus source voltages behind the impedance
      Vsa = Vmag * sin (omega*t);
      Vsb = Vmag * sin (omega*t - rad120);
      Vsc = Vmag * sin (omega*t + rad120);
      // SMIB impedance currents at this time step
      Ia = Ha + rl_y * (Ea - Vsa);
      Ib = Hb + rl_y * (Eb - Vsb);
      Ic = Hc + rl_y * (Ec - Vsc);
      // updating the history terms
      Ha = rl_zi * Ha + rl_yi * (Ea - Vsa);
      Hb = rl_zi * Hb + rl_yi * (Eb - Vsb);
      Hc = rl_zi * Hc + rl_yi * (Ec - Vsc);

      // update the inputs for this next DLL step
      pWrap->pModel->Time = t;
      update_inputs (pWrap->pModel, pWrap->pInputMap, t, Ea/1000.0, Eb/1000.0, Ec/1000.0, Ia/1000.0, Ib/1000.0, Ic/1000.0);

      // execute the DLL for updated inverter voltages and other outputs
      pWrap->Model_Outputs (pWrap->pModel);
      Ea = 1000.0 * extract_output (pWrap->pModel, pWrap->pOutputMap, 0);
      Eb = 1000.0 * extract_output (pWrap->pModel, pWrap->pOutputMap, 1);
      Ec = 1000.0 * extract_output (pWrap->pModel, pWrap->pOutputMap, 2);

      write_csv_values (fp, pWrap->pModel, pWrap->pInfo, pWrap->pInputMap, pWrap->pOutputMap, t);
      check_messages ("Model_Outputs", pWrap->pModel);
      t += dt;
    }
    fclose (fp);
    FreeFirstDLLModel (pWrap);
  }
  return 0;
}
