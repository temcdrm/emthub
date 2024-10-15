// Copyright (C) 2024 Meltran, Inc

// see https://learn.microsoft.com/en-us/windows/win32/dlls/using-run-time-dynamic-linking
 
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
    printf("Failed to load %s\n", name);
  }
  return fcn;
}

int main( void ) 
{ 
  HINSTANCE hLib; 
  DLL_INFO_FCN Model_PrintInfo;
  DLL_STRUCT_FCN Model_GetInfo;
  DLL_MODEL_FCN Model_CheckParameters, Model_Initialize, Model_Outputs, Model_FirstCall, Model_Iterate, Model_Terminate; 
  BOOL fFreeResult, fRunTimeLinkSuccess = FALSE;
 
  hLib = LoadLibrary(TEXT("GFM_GFL_IBR.dll")); 
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
    }
    Model_CheckParameters = LoadModelFunction (hLib, "Model_CheckParameters"); 
    Model_FirstCall = LoadModelFunction (hLib, "Model_FirstCall");
    Model_Initialize = LoadModelFunction (hLib, "Model_Initialize");
    Model_Outputs = LoadModelFunction (hLib, "Model_Outputs");
    Model_Iterate = LoadModelFunction (hLib, "Model_Iterate");
    Model_Terminate = LoadModelFunction (hLib, "Model_Terminate");
    fFreeResult = FreeLibrary(hLib); 
  } 

  if (!fRunTimeLinkSuccess) {
    printf ("Unable to call Model_PrintInfo from the DLL.\n");
  }
  return 0;
}
