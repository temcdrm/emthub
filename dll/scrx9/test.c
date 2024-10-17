// Copyright (C) 2024 Meltran, Inc

// see https://learn.microsoft.com/en-us/windows/win32/dlls/using-run-time-dynamic-linking

#define DLL_NAME "SCRX9.dll"

#include <windows.h> 
#include <stdio.h> 

#include "IEEE_Cigre_DLLInterface.h"
 
typedef int32_T (__cdecl *DLL_INFO_FCN)(void); 
typedef const IEEE_Cigre_DLLInterface_Model_Info * (__cdecl *DLL_STRUCT_FCN)(void);
typedef int32_T (__cdecl *DLL_MODEL_FCN)(IEEE_Cigre_DLLInterface_Instance *);

DLL_MODEL_FCN LoadModelFunction (HINSTANCE hLib, char *name)
{
  DLL_MODEL_FCN fcn = (DLL_MODEL_FCN) GetProcAddress (hLib, name);
  if (NULL == fcn) {
    printf("Failed to load %s from %s\n", name, DLL_NAME);
  }
  return fcn;
}

const char *modeEMTorRMS (int val)
{
  if (val == 1) {
    return "EMT";
  } else if (val == 2) {
    return "RMS";
  } else if (val == 3) {
    return "EMT+RMS";
  }
  return "n/a";
}

int main( void ) 
{ 
  HINSTANCE hLib; 
  DLL_INFO_FCN Model_PrintInfo;
  DLL_STRUCT_FCN Model_GetInfo;
  DLL_MODEL_FCN Model_CheckParameters, Model_Initialize, Model_Outputs, Model_FirstCall, Model_Iterate, Model_Terminate; 
  BOOL fFreeResult, fRunTimeLinkSuccess = FALSE;
 
  hLib = LoadLibrary(TEXT(DLL_NAME)); 
  if (hLib != NULL) { 
    Model_PrintInfo = (DLL_INFO_FCN) GetProcAddress(hLib, "Model_PrintInfo"); 
    if (NULL != Model_PrintInfo) {
      fRunTimeLinkSuccess = TRUE;
//      Model_PrintInfo (); 
    }
    Model_GetInfo = (DLL_STRUCT_FCN) GetProcAddress(hLib, "Model_GetInfo");
    if (NULL != Model_GetInfo) {
      const IEEE_Cigre_DLLInterface_Model_Info *pModelInfo = Model_GetInfo();
      printf("Model Name = %s\n", pModelInfo->ModelName);
      printf("Model Version = %s\n", pModelInfo->ModelVersion);
      printf("Updated %s by %s\n", pModelInfo->ModelLastModifiedDate, pModelInfo->ModelLastModifiedBy);
      printf("Time Step: %0.5g [s]\n", pModelInfo->FixedStepBaseSampleTime);
      printf("EMT/RMS Mode: %s\n", modeEMTorRMS (pModelInfo->EMT_RMS_Mode));
      printf("Parameters/Description/Default:\n");
      for (int k=0; k < pModelInfo->NumParameters; k++) {
        printf("  %2d %-12s %-70s %-10s %g\n", k, pModelInfo->ParametersInfo[k].Name, pModelInfo->ParametersInfo[k].Description, 
               pModelInfo->ParametersInfo[k].Unit, pModelInfo->ParametersInfo[k].DefaultValue.Real64_Val);
      }
      printf("Input Signals:\n");
      for (int k=0; k < pModelInfo->NumInputPorts; k++) {
        printf("  %2d %-12s %-70s %-10s\n", k, pModelInfo->InputPortsInfo[k].Name, pModelInfo->InputPortsInfo[k].Description, 
               pModelInfo->InputPortsInfo[k].Unit);
      }
      printf("Output Signals:\n");
      for (int k=0; k < pModelInfo->NumOutputPorts; k++) {
        printf("  %2d %-12s %-70s %-10s\n", k, pModelInfo->OutputPortsInfo[k].Name, pModelInfo->OutputPortsInfo[k].Description, 
               pModelInfo->OutputPortsInfo[k].Unit);
      }
      printf("Internal State Variables: %d int, %d float, %d double\n", pModelInfo->NumIntStates, pModelInfo->NumFloatStates, pModelInfo->NumDoubleStates);
    }
    Model_CheckParameters = LoadModelFunction (hLib, "Model_CheckParameters"); 
    Model_FirstCall = LoadModelFunction (hLib, "Model_FirstCall");
    Model_Initialize = LoadModelFunction (hLib, "Model_Initialize");
    Model_Outputs = LoadModelFunction (hLib, "Model_Outputs");
    Model_Iterate = LoadModelFunction (hLib, "Model_Iterate");
    Model_Terminate = LoadModelFunction (hLib, "Model_Terminate");
    fFreeResult = FreeLibrary(hLib); 
  } else {
    printf ("LoadLibrary failed on %s\n", DLL_NAME);
  }

  if (!fRunTimeLinkSuccess) {
    printf ("Unable to call Model_PrintInfo from %s\n", DLL_NAME);
  }
  return 0;
}
