// Copyright (C) 2024 Meltran, Inc

// see https://learn.microsoft.com/en-us/windows/win32/dlls/using-run-time-dynamic-linking

#define DLL_NAME "SCRX9.dll"
#define TMAX 10.0
// relative output path for execution from the build directory, e.g., release\test or debug\test
#define CSV_NAME "scrx9.csv"

#include <windows.h> 
#include <stdio.h> 

#include "IEEE_Cigre_DLLWrapper.h"
 
void initialize_outputs (IEEE_Cigre_DLLInterface_Instance* pModel, ArrayMap *pMap, int nPorts)
{
  double EFD = 1.0;
  char *pData = (char *) pModel->ExternalOutputs;
  memcpy (pData + pMap[0].offset, &EFD, pMap[0].size);
}

void update_inputs (IEEE_Cigre_DLLInterface_Instance* pModel, ArrayMap *pMap, double t, int nPorts)
{
  double Vref = 1.0;
  double Ec = 1.0;
  double Vs = 0.0;
  double IFD = 0.0;
  double VT = 1.0;
  double VUEL = -5.0;
  double VOEL = 5.0;
  if (t >= 2.0 && t <= 2.15) { // fault
    Ec = 0.5;
    VT = Ec;
  }
  char *pData = (char *) pModel->ExternalInputs;
  memcpy (pData + pMap[0].offset, &Vref, pMap[0].size);
  memcpy (pData + pMap[1].offset, &Ec, pMap[1].size);
  memcpy (pData + pMap[2].offset, &Vs, pMap[2].size);
  memcpy (pData + pMap[3].offset, &IFD, pMap[3].size);
  memcpy (pData + pMap[4].offset, &VT, pMap[4].size);
  memcpy (pData + pMap[5].offset, &VUEL, pMap[5].size);
  memcpy (pData + pMap[6].offset, &VOEL, pMap[6].size);
}

double extract_outputs (IEEE_Cigre_DLLInterface_Instance* pModel, ArrayMap *pMap, int nPorts)
{
  char *pData = (char *) pModel->ExternalOutputs;
  double efd = 0.0;
  for (int i = 0; i < nPorts; i++) {
    memcpy (&efd, pData + pMap[i].offset, pMap[i].size);
  }
  return efd;
}

int main( void ) 
{
  show_struct_alignment_requirements ();
  Wrapped_IEEE_Cigre_DLL *pWrap = CreateFirstDLLModel (DLL_NAME);
  if (NULL != pWrap) {
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
    while (t <= tstop) {
      // update the inputs for this next DLL step
      pWrap->pModel->Time = t;
      update_inputs (pWrap->pModel, pWrap->pInputMap, t, pWrap->pInfo->NumInputPorts);
      // execute the DLL
      pWrap->Model_Outputs (pWrap->pModel);
      double efd = extract_outputs (pWrap->pModel, pWrap->pOutputMap, pWrap->pInfo->NumOutputPorts);
      write_csv_values (fp, pWrap->pModel, pWrap->pInfo, pWrap->pInputMap, pWrap->pOutputMap, t);
      check_messages ("Model_Outputs", pWrap->pModel);
      t += dt;
    }
    fclose (fp);
    FreeFirstDLLModel (pWrap);
  }
  return 0;
}
