// Copyright (C) 2024-26 Meltran, Inc

// see https://learn.microsoft.com/en-us/windows/win32/dlls/using-run-time-dynamic-linking

#define DLL_NAME "SEXS.dll"
#define TMAX 5.0
// relative output path for execution from the build directory, e.g., release\test or debug\test
#define CSV_NAME "sexs.csv"

#include <windows.h> 
#include <stdio.h> 

#include "IEEE_Cigre_DLLWrapper.h"
 
void initialize_outputs (IEEE_Cigre_DLLInterface_Instance* pModel, ArrayMap *pMap, int nPorts)
{
  double Efd = 1.0;
  char *pData = (char *) pModel->ExternalOutputs;
  memcpy (pData + pMap[0].offset, &Efd, pMap[0].size);
}

void update_inputs (IEEE_Cigre_DLLInterface_Instance* pModel, ArrayMap *pMap, double t, int nPorts)
{
  double Vref = 1.0;
  double Vc = 1.0;
  double Vs = 0.0;
//  if (t >= 0.1) {
//    Vref = 1.01;
//  }
  if (t >= 0.4 && t <= 0.6) { // fault
    Vc = 0.5;
  }
  char *pData = (char *) pModel->ExternalInputs;
  memcpy (pData + pMap[0].offset, &Vref, pMap[0].size);
  memcpy (pData + pMap[1].offset, &Vc, pMap[1].size);
  memcpy (pData + pMap[2].offset, &Vs, pMap[2].size);
}

double extract_outputs (IEEE_Cigre_DLLInterface_Instance* pModel, ArrayMap *pMap, int nPorts)
{
  char *pData = (char *) pModel->ExternalOutputs;
  double Efd = 0.0;
  for (int i = 0; i < nPorts; i++) {
    memcpy (&Efd, pData + pMap[i].offset, pMap[i].size);
  }
  return Efd;
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
    update_inputs (pWrap->pModel, pWrap->pInputMap, -1.0, pWrap->pInfo->NumInputPorts);
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
