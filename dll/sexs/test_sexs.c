// Copyright (C) 2024-26 Meltran, Inc

// see https://learn.microsoft.com/en-us/windows/win32/dlls/using-run-time-dynamic-linking

#define DLL_NAME "SEXS.dll"
#define TMAX 0.8
// relative output path for execution from the build directory, e.g., release\test or debug\test
#define CSV_NAME "sexs.csv"

#include <windows.h> 
#include <stdio.h> 

#include "IEEE_Cigre_DLLWrapper.h"
 
//void initialize_outputs (IEEE_Cigre_DLLInterface_Instance* pModel, ArrayMap *pMap, int nPorts)
//{
//  double Efd = 1.0;
//  char *pData = (char *) pModel->ExternalOutputs;
//  memcpy (pData + pMap[0].offset, &Efd, pMap[0].size);
//}
//
//void update_inputs (IEEE_Cigre_DLLInterface_Instance* pModel, ArrayMap *pMap, double t, int nPorts)
//{
//  double Vref = 1.0;
//  double Vc = 1.0;
//  double Vs = 0.0;
////  if (t >= 0.1) {
////    Vref = 1.01;
////  }
//  if (t >= 0.2 && t <= 0.35) { // fault
//    Vc = 0.5;
//  }
//  char *pData = (char *) pModel->ExternalInputs;
//  memcpy (pData + pMap[0].offset, &Vref, pMap[0].size);
//  memcpy (pData + pMap[1].offset, &Vc, pMap[1].size);
//  memcpy (pData + pMap[2].offset, &Vs, pMap[2].size);
//}

int main( void ) 
{
  int idxTc, idxKc, idxEmin, idxEmax, idxEfdMin, idxEfdMax, idxVref, idxVs, idxVc, idxEfd;
  double t, Vref = 1.0, Vs = 0.0, VcOLD, VcOLS, VcCL, EfdOLD = 1.0, EfdOLS = 1.0, EfdCL = 1.0;
  show_struct_alignment_requirements ();

  // create three instances of the DLL for testing
  Wrapped_IEEE_Cigre_DLL *pWrap = CreateFirstDLLModel (DLL_NAME); // pWrap for open-loop test, dynamic limiters
  IEEE_Cigre_DLLInterface_Instance *pMdlOLD = pWrap->pModel;
  IEEE_Cigre_DLLInterface_Instance *pMdlOLS = AddModelInstance (pWrap);
  IEEE_Cigre_DLLInterface_Instance *pMdlCL = AddModelInstance (pWrap);
  // parameter indexes from the wrapper
  idxKc = find_dll_parameter_index (pWrap->pInfo, "Kc");
  idxTc = find_dll_parameter_index (pWrap->pInfo, "Tc");
  idxEmin = find_dll_parameter_index (pWrap->pInfo, "Emin");
  idxEmax = find_dll_parameter_index (pWrap->pInfo, "Emax");
  idxEfdMin = find_dll_parameter_index (pWrap->pInfo, "EfdEmin");
  idxEfdMax = find_dll_parameter_index (pWrap->pInfo, "EfdEmin");
  // input signal indexes from the wrapper
  idxVref = find_dll_signal_index (pWrap->pInfo->InputPortsInfo, pWrap->pInfo->NumInputPorts, "Vref");
  idxVs = find_dll_signal_index (pWrap->pInfo->InputPortsInfo, pWrap->pInfo->NumInputPorts, "Vs");
  idxVc = find_dll_signal_index (pWrap->pInfo->InputPortsInfo, pWrap->pInfo->NumInputPorts, "Vc");
  // output signal indexes from the wrapper
  idxEfd = find_dll_signal_index (pWrap->pInfo->OutputPortsInfo, pWrap->pInfo->NumOutputPorts, "Efd");

  // configure the different tests
  set_dll_real_value ((char *) pMdlOLD->Parameters, pWrap->pParameterMap, idxKc, 1.0);
  set_dll_real_value ((char *) pMdlOLD->Parameters, pWrap->pParameterMap, idxTc, 1.0);
  // set the constant inputs
  set_dll_real_value ((char *) pMdlOLD->ExternalInputs, pWrap->pInputMap, idxVref, Vref);
  set_dll_real_value ((char *) pMdlOLS->ExternalInputs, pWrap->pInputMap, idxVref, Vref);
  set_dll_real_value ((char *) pMdlCL->ExternalInputs, pWrap->pInputMap, idxVref, Vref);
  set_dll_real_value ((char *) pMdlOLD->ExternalInputs, pWrap->pInputMap, idxVs, Vs);
  set_dll_real_value ((char *) pMdlOLS->ExternalInputs, pWrap->pInputMap, idxVs, Vs);
  set_dll_real_value ((char *) pMdlCL->ExternalInputs, pWrap->pInputMap, idxVs, Vs);
  // initialize the outputs
  set_dll_real_value ((char *) pMdlOLD->ExternalOutputs, pWrap->pOutputMap, idxEfd, EfdOLD);
  set_dll_real_value ((char *) pMdlOLS->ExternalOutputs, pWrap->pOutputMap, idxEfd, EfdOLS);
  set_dll_real_value ((char *) pMdlCL->ExternalOutputs, pWrap->pOutputMap, idxEfd, EfdCL);

  if (NULL != pWrap) {
    PrintDLLModelParameters (pWrap);
    // initialize all the models
    if (NULL != pWrap->Model_FirstCall) {
      pWrap->Model_FirstCall (pMdlOLD);
      pWrap->Model_FirstCall (pMdlOLS);
      pWrap->Model_FirstCall (pMdlCL);
    }
    printf("calling CheckParameters\n");
    pWrap->Model_CheckParameters (pMdlOLD);
    check_messages ("Model_CheckParameters", pMdlOLD);
    pWrap->Model_CheckParameters (pMdlOLS);
    check_messages ("Model_CheckParameters", pMdlOLS);
    pWrap->Model_CheckParameters (pMdlCL);
    check_messages ("Model_CheckParameters", pMdlCL);

    // initialize time-stepping
    printf("calling Initialize\n");
    pWrap->Model_Initialize (pMdlOLD);
    check_messages ("Model_Initialize", pMdlOLD);

    // time step loop, matching the DLL's desired time step
    double dt = pWrap->pInfo->FixedStepBaseSampleTime;
    printf("Looping with dt=%g, tmax=%g\n", dt, TMAX);
    double t = 0.0;
    printf("opening %s\n", CSV_NAME);
    FILE *fp = fopen (CSV_NAME, "w");
    fprintf (fp, "t,Vref,Vs,VcOLS,EfdOLS,VcOLD,EfdOLD,VcCL,EfdCL\n"); // csv header
    double tstop = TMAX + 0.5 * dt;
    while (t <= tstop) {
      // update the inputs for this next DLL step
      if (t >= 0.2 && t <= 0.35) {
        VcOLD = VcOLS = VcCL = 0.5;
      } else {
        VcOLD = VcOLS = VcCL = 1.0;
      }
      pMdlOLD->Time = t;
      pMdlOLS->Time = t;
      pMdlCL->Time = t;
      set_dll_real_value ((char *) pMdlOLD->ExternalInputs, pWrap->pInputMap, idxVc, VcOLD);
      set_dll_real_value ((char *) pMdlOLS->ExternalInputs, pWrap->pInputMap, idxVc, VcOLS);
      set_dll_real_value ((char *) pMdlCL->ExternalInputs, pWrap->pInputMap, idxVc, VcCL);
      // execute the DLL
      pWrap->Model_Outputs (pMdlOLD);
      pWrap->Model_Outputs (pMdlOLS);
      pWrap->Model_Outputs (pMdlCL);
      // extract and write the outputs
      EfdOLD = get_dll_real_value (pMdlOLD->ExternalOutputs, pWrap->pOutputMap, idxEfd);
      EfdOLS = get_dll_real_value (pMdlOLS->ExternalOutputs, pWrap->pOutputMap, idxEfd);
      EfdCL = get_dll_real_value (pMdlCL->ExternalOutputs, pWrap->pOutputMap, idxEfd);
      fprintf (fp, "%g,%g,%g,%g,%g,%g,%g,%g,%g\n", 
               t, Vref, Vs, VcOLS, EfdOLS, VcOLD, EfdOLD, VcCL, EfdCL); // csv values
      check_messages ("Model_Outputs", pMdlOLD);
      check_messages ("Model_Outputs", pMdlOLS);
      check_messages ("Model_Outputs", pMdlCL);
      t += dt;
    }
    fclose (fp);
    FreeAllDLLModels (pWrap);
  }
  return 0;
}
