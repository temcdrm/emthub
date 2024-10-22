// Copyright (C) 2024 Meltran, Inc

// see https://learn.microsoft.com/en-us/windows/win32/dlls/using-run-time-dynamic-linking

#define DLL_NAME "SCRX9.dll"
#define TMAX 10.0
// relative output path for execution from the build directory, e.g., release\test or debug\test
#define CSV_NAME "..\\..\\plots\\scrx9.csv"

#include <windows.h> 
#include <stdio.h> 

#include "IEEE_Cigre_DLLInterface.h"
 
typedef int32_T (__cdecl *DLL_INFO_FCN)(void); 
typedef const IEEE_Cigre_DLLInterface_Model_Info * (__cdecl *DLL_STRUCT_FCN)(void);
typedef int32_T (__cdecl *DLL_MODEL_FCN)(IEEE_Cigre_DLLInterface_Instance *);

typedef struct _ArrayMap {  // we will have arrays of these for Parameters, ExternalInputs and ExternalOutputs
  int size;    // size of the value from IEEE_Cigre_DLLInterface_types.h
  int offset;  // byte offset into the malloced memory for this value
} ArrayMap;

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

int get_datatype_size (int dtype)
{
  if (dtype == IEEE_Cigre_DLLInterface_DataType_char_T) return sizeof (char_T);
  if (dtype == IEEE_Cigre_DLLInterface_DataType_int8_T) return sizeof (int8_T);
  if (dtype == IEEE_Cigre_DLLInterface_DataType_uint8_T) return sizeof (uint8_T);
  if (dtype == IEEE_Cigre_DLLInterface_DataType_int16_T) return sizeof (int16_T);
  if (dtype == IEEE_Cigre_DLLInterface_DataType_uint16_T) return sizeof (uint16_T);
  if (dtype == IEEE_Cigre_DLLInterface_DataType_int32_T) return sizeof (int32_T);
  if (dtype == IEEE_Cigre_DLLInterface_DataType_uint32_T) return sizeof (uint32_T);
  if (dtype == IEEE_Cigre_DLLInterface_DataType_real32_T) return sizeof (real32_T);
  if (dtype == IEEE_Cigre_DLLInterface_DataType_real64_T) return sizeof (real64_T);
  if (dtype == IEEE_Cigre_DLLInterface_DataType_c_string_T) return sizeof (const char *);
  return 0;
}

void assign_dll_value (char *pVals, int offset, int dtype, int dsize, union DefaultValueU val)
{
  printf(" assigning: %d %d %d\n", offset, dtype, dsize);
  if (dtype == IEEE_Cigre_DLLInterface_DataType_char_T) memcpy (pVals+offset, &val.Char_Val, dsize);
  if (dtype == IEEE_Cigre_DLLInterface_DataType_int8_T) memcpy (pVals+offset, &val.Int8_Val, dsize);
  if (dtype == IEEE_Cigre_DLLInterface_DataType_uint8_T) memcpy (pVals+offset, &val.Uint8_Val, dsize);
  if (dtype == IEEE_Cigre_DLLInterface_DataType_int16_T) memcpy (pVals+offset, &val.Int16_Val, dsize);
  if (dtype == IEEE_Cigre_DLLInterface_DataType_uint16_T) memcpy (pVals+offset, &val.Uint16_Val, dsize);
  if (dtype == IEEE_Cigre_DLLInterface_DataType_int32_T) {memcpy (pVals+offset, &val.Int32_Val, dsize);printf("   %d\n", val.Int32_Val);}
  if (dtype == IEEE_Cigre_DLLInterface_DataType_uint32_T) memcpy (pVals+offset, &val.Uint32_Val, dsize);
  if (dtype == IEEE_Cigre_DLLInterface_DataType_real32_T) memcpy (pVals+offset, &val.Real32_Val, dsize);
  if (dtype == IEEE_Cigre_DLLInterface_DataType_real64_T) {memcpy (pVals+offset, &val.Real64_Val, dsize);printf("   %g\n", val.Real64_Val);}
//  if (dtype == IEEE_Cigre_DLLInterface_DataType_c_string_T) pVals[offset] = val.Char_Ptr;
}

IEEE_Cigre_DLLInterface_Instance* CreateModelInstance (const IEEE_Cigre_DLLInterface_Model_Info *pInfo,
                                                       ArrayMap **pParameterMap,
                                                       ArrayMap **pInputMap,
                                                       ArrayMap **pOutputMap)
{
  printf("creating pModel\n");
  IEEE_Cigre_DLLInterface_Instance *pModel = malloc (sizeof *pModel);
  pModel->Time = 0.0;
  // allocate memory
  pModel->IntStates = NULL;
  pModel->FloatStates = NULL;
  pModel->DoubleStates = NULL;
  pModel->ExternalInputs = NULL;
  pModel->ExternalOutputs = NULL;
  pModel->Parameters = NULL;
  if (pInfo->NumInputPorts > 0) {
    ArrayMap *pTest = malloc (pInfo->NumInputPorts * sizeof (ArrayMap));
    *pInputMap = pTest;
    int input_size = 0;
    for (int i = 0; i < pInfo->NumInputPorts; i++) {
      int dtype = pInfo->InputPortsInfo[i].DataType;
      int dsize = get_datatype_size (dtype);
      pTest[i].size = dsize;
      pTest[i].offset = input_size;
      input_size += dsize;
    }
//    printf ("%d inputs of total size %d\n", pInfo->NumInputPorts, input_size);
    pModel->ExternalInputs = malloc(input_size);
  }
  if (pInfo->NumOutputPorts > 0) {
    ArrayMap *pTest = malloc (pInfo->NumOutputPorts * sizeof (ArrayMap));
    *pOutputMap = pTest;
    int output_size = 0;
    for (int i = 0; i < pInfo->NumOutputPorts; i++) {
      int dtype = pInfo->OutputPortsInfo[i].DataType;
      int dsize = get_datatype_size (dtype);
      pTest[i].size = dsize;
      pTest[i].offset = output_size;
      output_size += dsize;
    }
//    printf ("%d outputs of total size %d\n", pInfo->NumOutputPorts, output_size);
    pModel->ExternalOutputs = malloc(output_size);
  }
  if (pInfo->NumIntStates > 0) {
    pModel->IntStates = (int32_T *) malloc(pInfo->NumIntStates * sizeof(int32_T));
  }
  if (pInfo->NumFloatStates > 0) {
    pModel->FloatStates = (real32_T *) malloc(pInfo->NumFloatStates * sizeof(real32_T));
  }
  if (pInfo->NumDoubleStates > 0) {
    pModel->DoubleStates = (real64_T *) malloc(pInfo->NumDoubleStates * sizeof(real64_T));
  }
  if (pInfo->NumParameters > 0) {
    ArrayMap *pTest = malloc (pInfo->NumParameters * sizeof (ArrayMap));
    *pParameterMap = pTest;
    int parm_size = 0;
    for (int i = 0; i < pInfo->NumParameters; i++) {
      int dtype = pInfo->ParametersInfo[i].DataType;
      int dsize = get_datatype_size (dtype);
      pTest[i].size = dsize;
      pTest[i].offset = parm_size;
//      printf ("parm %d type %d size %d\n", i, dtype, dsize);
      parm_size += dsize;
    }
//    printf("parm_size = %d\n", parm_size);
    pModel->Parameters = malloc (parm_size);
    // initialize the parameters to default values
    int offset = 0;
    for (int i = 0; i < pInfo->NumParameters; i++) {
      int dtype = pInfo->ParametersInfo[i].DataType;
      int dsize = get_datatype_size (dtype);
      assign_dll_value ((char *)pModel->Parameters, offset, dtype, dsize, pInfo->ParametersInfo[i].DefaultValue);
      offset += dsize;
    }
  }
  return pModel;
}

void FreeModelInstance (IEEE_Cigre_DLLInterface_Instance *pModel, ArrayMap *pParameterMap,
                        ArrayMap *pInputMap, ArrayMap *pOutputMap)
{
  printf("freeing pModel\n");
  if (NULL != pModel->ExternalInputs) {
    free (pModel->ExternalInputs);
  }
  if (NULL != pModel->ExternalOutputs) {
    free (pModel->ExternalOutputs);
  }
  if (NULL != pModel->IntStates) {
    free (pModel->IntStates);
  }
  if (NULL != pModel->FloatStates) {
    free (pModel->FloatStates);
  }
  if (NULL != pModel->DoubleStates) {
    free (pModel->DoubleStates);
  }
  if (NULL != pModel->Parameters) {
    free (pModel->Parameters);
  }
  free (pModel);
  if (NULL != pInputMap) {
    free (pInputMap);
  }
  if (NULL != pOutputMap) {
    free (pOutputMap);
  }
  if (NULL != pParameterMap) {
    free (pParameterMap);
  }
  return;
}

void check_messages (const char *loc, IEEE_Cigre_DLLInterface_Instance *pModel)
{
  if (NULL != pModel->LastGeneralMessage) {
    if (strlen (pModel->LastGeneralMessage) > 0) {
      printf("  %s says %s\n", loc, pModel->LastGeneralMessage);
    }
  }
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

void write_csv_header (FILE *fp, const IEEE_Cigre_DLLInterface_Model_Info *pInfo)
{
  char buf[16384];
  buf[0] = '\0';
  strcat (buf, "t");
  for (int i = 0; i < pInfo->NumInputPorts; i++) {
    strcat (buf, ",");
    strcat (buf, pInfo->InputPortsInfo[i].Name);
  }
  for (int i = 0; i < pInfo->NumOutputPorts; i++) {
    strcat (buf, ",");
    strcat (buf, pInfo->OutputPortsInfo[i].Name);
  }
  fprintf (fp, "%s\n", buf);
}

void write_csv_values (FILE *fp, IEEE_Cigre_DLLInterface_Instance *pModel, const IEEE_Cigre_DLLInterface_Model_Info *pInfo, 
                       ArrayMap *pInputMap, ArrayMap *pOutputMap, double t)
{
  char buf[256];
  char line[16384];
  line[0] = '\0';
  sprintf (buf, "%g", t);
  strcat (line, buf);
  char *pData = (char *) pModel->ExternalInputs;
  double val;
  for (int i = 0; i < pInfo->NumInputPorts; i++) {
    memcpy (&val, pData + pInputMap[i].offset, pInputMap[i].size);
    sprintf (buf, ",%g", val);
    strcat (line, buf);
  }
  pData = (char *) pModel->ExternalOutputs;
  for (int i = 0; i < pInfo->NumOutputPorts; i++) {
    memcpy (&val, pData + pOutputMap[i].offset, pOutputMap[i].size);
    sprintf (buf, ",%g", val);
    strcat (line, buf);
  }
  fprintf (fp, "%s\n", line);
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
      // we seem to only need Model_GetInfo to run the DLL
//      Model_PrintInfo (); 
    }
    // find the required DLL functions
    Model_GetInfo = (DLL_STRUCT_FCN) GetProcAddress(hLib, "Model_GetInfo");
    Model_CheckParameters = LoadModelFunction (hLib, "Model_CheckParameters"); 
    Model_Initialize = LoadModelFunction (hLib, "Model_Initialize");
    Model_Outputs = LoadModelFunction (hLib, "Model_Outputs");
    Model_Terminate = LoadModelFunction (hLib, "Model_Terminate");
    // look for the new (optional) DLL functions
    Model_FirstCall = LoadModelFunction (hLib, "Model_FirstCall");
    Model_Iterate = LoadModelFunction (hLib, "Model_Iterate");
    // retrieve the DLL interface points
    const IEEE_Cigre_DLLInterface_Model_Info *pModelInfo = Model_GetInfo();
    // create a model instance, initialized to default values
    ArrayMap *pParameterMap;//  = NULL;
    ArrayMap *pInputMap;// = NULL;
    ArrayMap *pOutputMap;// = NULL;
    IEEE_Cigre_DLLInterface_Instance* pModel = CreateModelInstance (pModelInfo, &pParameterMap, &pInputMap, &pOutputMap);
    real64_T *pInputs = (real64_T *) pModel->ExternalInputs;
    real64_T *pOutputs = (real64_T *) pModel->ExternalOutputs;
    // display the DLL interface schema
    printf("Model Name = %s\n", pModelInfo->ModelName);
    printf("Model Version = %s\n", pModelInfo->ModelVersion);
    printf("Updated %s by %s\n", pModelInfo->ModelLastModifiedDate, pModelInfo->ModelLastModifiedBy);
    printf("Time Step: %0.5g [s]\n", pModelInfo->FixedStepBaseSampleTime);
    printf("EMT/RMS Mode: %s\n", modeEMTorRMS (pModelInfo->EMT_RMS_Mode));
    printf("Parameters (idx,size,offset,desc,units,default,min,max:\n");
    for (int k=0; k < pModelInfo->NumParameters; k++) {
      printf("  %2d %4d %4d %-12s %-70s %-10s %g \t %g \t %g\n", k, pParameterMap[k].size, pParameterMap[k].offset,
             pModelInfo->ParametersInfo[k].Name, pModelInfo->ParametersInfo[k].Description, 
             pModelInfo->ParametersInfo[k].Unit, pModelInfo->ParametersInfo[k].DefaultValue.Real64_Val,
             pModelInfo->ParametersInfo[k].MinValue.Real64_Val, pModelInfo->ParametersInfo[k].MaxValue.Real64_Val);
    }
    printf("Input Signals (idx,size,offset,name,desc,units):\n");
    for (int k=0; k < pModelInfo->NumInputPorts; k++) {
      printf("  %2d %4d %4d %-12s %-70s %-10s\n", k, pInputMap[k].size, pInputMap[k].offset,
             pModelInfo->InputPortsInfo[k].Name, pModelInfo->InputPortsInfo[k].Description, pModelInfo->InputPortsInfo[k].Unit);
    }
    printf("Output Signals (idx,size,offset,name,desc,units):\n");
    for (int k=0; k < pModelInfo->NumOutputPorts; k++) {
      printf("  %2d %4d %4d %-12s %-70s %-10s\n", k, pOutputMap[k].size, pOutputMap[k].offset,
             pModelInfo->OutputPortsInfo[k].Name, pModelInfo->OutputPortsInfo[k].Description, pModelInfo->OutputPortsInfo[k].Unit);
    }
    printf("Internal State Variables: %d int, %d float, %d double\n", pModelInfo->NumIntStates, pModelInfo->NumFloatStates, pModelInfo->NumDoubleStates);

    // initialize the model
    if (NULL != Model_FirstCall) {
      Model_FirstCall (pModel);
    }
    printf("calling CheckParameters\n");
    Model_CheckParameters (pModel);
    check_messages ("Model_CheckParameters", pModel);

    // initialize time-stepping
    printf("calling Initialize\n");
    Model_Initialize (pModel);
    check_messages ("Model_Initialize", pModel);

    // time step loop, matching the DLL's desired time step
    double dt = pModelInfo->FixedStepBaseSampleTime;
    printf("Looping with dt=%g, tmax=%g\n", dt, TMAX);
    double t = 0.0;
    printf("opening %s\n", CSV_NAME);
    FILE *fp = fopen (CSV_NAME, "w");
    write_csv_header (fp, pModelInfo);
    double tstop = TMAX + 0.5 * dt;
    while (t <= tstop) {
      // update the inputs for this next DLL step
      pModel->Time = t;
      update_inputs (pModel, pInputMap, t, pModelInfo->NumInputPorts);
      // execute the DLL
      Model_Outputs (pModel);
      double efd = extract_outputs (pModel, pOutputMap, pModelInfo->NumOutputPorts);
      write_csv_values (fp, pModel, pModelInfo, pInputMap, pOutputMap, t);
      // printf("  efd[t] = %g %g\n", t, efd);
      check_messages ("Model_Outputs", pModel);
      // printf("t=%g, efd=%g\n", pModel->Time, pOutputs[0]);
      // save the outputs and states from this DLL step
      t += dt;
    }
    fclose (fp);
    // free the Model data and library
    printf("calling Terminate\n");
    Model_Terminate (pModel);
    check_messages ("Model_Terminate", pModel);
    FreeModelInstance (pModel, pParameterMap, pInputMap, pOutputMap);
    fFreeResult = FreeLibrary(hLib);
    printf("normal finish\n"); 
  } else {
    printf ("LoadLibrary failed on %s\n", DLL_NAME);
  }

  if (!fRunTimeLinkSuccess) {
    printf ("Unable to call Model_PrintInfo from %s\n", DLL_NAME);
  }
  return 0;
}
