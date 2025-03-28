// Copyright (C) 2024-25 Meltran, Inc

// see https://learn.microsoft.com/en-us/windows/win32/dlls/using-run-time-dynamic-linking
 
#ifdef ATP_MINGW
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
#include <stdlib.h>
#include <stddef.h>
#else
#include <windows.h>
#include <stdio.h> 
#endif

#include "IEEE_Cigre_DLLWrapper.h"
 
struct MyCharPtrStruct {
  char_T c;
  char_T *v;
};

struct MyCharStruct {
  char_T c;
  char_T v;
};

struct MyInt16Struct {
  char_T c;
  int16_T v;
};

struct MyInt32Struct {
  char_T c;
  int32_T v;
};

struct MyReal32Struct {
  char_T c;
  real32_T v;
};

struct MyReal64Struct {
  char_T c;
  real64_T v;
};

void show_struct_alignment_requirements () {
#ifndef ATP_MINGW
  printf ("Char alignment requirement: %zu\n", offsetof(struct MyCharStruct, v));
  printf ("CharPtr alignment requirement: %zu\n", offsetof(struct MyCharPtrStruct, v));
  printf ("Int16 alignment requirement: %zu\n", offsetof(struct MyInt16Struct, v));
  printf ("Int32 alignment requirement: %zu\n", offsetof(struct MyInt32Struct, v));
  printf ("Real32 alignment requirement: %zu\n", offsetof(struct MyReal32Struct, v));
  printf ("Real64 alignment requirement: %zu\n", offsetof(struct MyReal64Struct, v));
#endif
}

DLL_MODEL_FCN LoadModelFunction (HINSTANCE hLib, char *name, char *dll_name)
{
  DLL_MODEL_FCN fcn = (DLL_MODEL_FCN) GetProcAddress (hLib, name);
#ifndef ATP_MINGW
  if (NULL == fcn) {
    printf("Failed to load %s from %s\n", name, dll_name);
  }
#endif
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

size_t get_alignment_requirement (enum IEEE_Cigre_DLLInterface_DataType dtype)
{
  if (dtype == IEEE_Cigre_DLLInterface_DataType_char_T) return offsetof(struct MyCharStruct, v);
  if (dtype == IEEE_Cigre_DLLInterface_DataType_int8_T) return offsetof(struct MyCharStruct, v);
  if (dtype == IEEE_Cigre_DLLInterface_DataType_uint8_T) return offsetof(struct MyCharStruct, v);
  if (dtype == IEEE_Cigre_DLLInterface_DataType_int16_T) return offsetof(struct MyInt16Struct, v);
  if (dtype == IEEE_Cigre_DLLInterface_DataType_uint16_T) return offsetof(struct MyInt16Struct, v);
  if (dtype == IEEE_Cigre_DLLInterface_DataType_int32_T) return offsetof(struct MyInt32Struct, v);
  if (dtype == IEEE_Cigre_DLLInterface_DataType_uint32_T) return offsetof(struct MyInt32Struct, v);
  if (dtype == IEEE_Cigre_DLLInterface_DataType_real32_T) return offsetof(struct MyReal32Struct, v);
  if (dtype == IEEE_Cigre_DLLInterface_DataType_real64_T) return offsetof(struct MyReal64Struct, v);
  if (dtype == IEEE_Cigre_DLLInterface_DataType_c_string_T) return offsetof(struct MyCharPtrStruct, v);
  return 0;
}

int get_datatype_size (enum IEEE_Cigre_DLLInterface_DataType dtype)
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

void assign_default_value (char *pVals, int offset, enum IEEE_Cigre_DLLInterface_DataType dtype, int dsize, union DefaultValueU val)
{
  // printf(" assigning: %d %d %d\n", offset, dtype, dsize);
  if (dtype == IEEE_Cigre_DLLInterface_DataType_char_T) memcpy (pVals+offset, &val.Char_Val, dsize);
  if (dtype == IEEE_Cigre_DLLInterface_DataType_int8_T) memcpy (pVals+offset, &val.Int8_Val, dsize);
  if (dtype == IEEE_Cigre_DLLInterface_DataType_uint8_T) memcpy (pVals+offset, &val.Uint8_Val, dsize);
  if (dtype == IEEE_Cigre_DLLInterface_DataType_int16_T) memcpy (pVals+offset, &val.Int16_Val, dsize);
  if (dtype == IEEE_Cigre_DLLInterface_DataType_uint16_T) memcpy (pVals+offset, &val.Uint16_Val, dsize);
  if (dtype == IEEE_Cigre_DLLInterface_DataType_int32_T) memcpy (pVals+offset, &val.Int32_Val, dsize);
  if (dtype == IEEE_Cigre_DLLInterface_DataType_uint32_T) memcpy (pVals+offset, &val.Uint32_Val, dsize);
  if (dtype == IEEE_Cigre_DLLInterface_DataType_real32_T) memcpy (pVals+offset, &val.Real32_Val, dsize);
  if (dtype == IEEE_Cigre_DLLInterface_DataType_real64_T) memcpy (pVals+offset, &val.Real64_Val, dsize);
  if (dtype == IEEE_Cigre_DLLInterface_DataType_c_string_T) memcpy (pVals+offset, &val.Char_Ptr, dsize);
}

void edit_dll_value (char *pVals, int offset, enum IEEE_Cigre_DLLInterface_DataType dtype, int dsize, union EditValueU val)
{
  // printf(" assigning: %d %d %d\n", offset, dtype, dsize);
  if (dtype == IEEE_Cigre_DLLInterface_DataType_char_T) memcpy (pVals+offset, &val.Char_Val, dsize);
  if (dtype == IEEE_Cigre_DLLInterface_DataType_int8_T) memcpy (pVals+offset, &val.Int8_Val, dsize);
  if (dtype == IEEE_Cigre_DLLInterface_DataType_uint8_T) memcpy (pVals+offset, &val.Uint8_Val, dsize);
  if (dtype == IEEE_Cigre_DLLInterface_DataType_int16_T) memcpy (pVals+offset, &val.Int16_Val, dsize);
  if (dtype == IEEE_Cigre_DLLInterface_DataType_uint16_T) memcpy (pVals+offset, &val.Uint16_Val, dsize);
  if (dtype == IEEE_Cigre_DLLInterface_DataType_int32_T) memcpy (pVals+offset, &val.Int32_Val, dsize);
  if (dtype == IEEE_Cigre_DLLInterface_DataType_uint32_T) memcpy (pVals+offset, &val.Uint32_Val, dsize);
  if (dtype == IEEE_Cigre_DLLInterface_DataType_real32_T) memcpy (pVals+offset, &val.Real32_Val, dsize);
  if (dtype == IEEE_Cigre_DLLInterface_DataType_real64_T) memcpy (pVals+offset, &val.Real64_Val, dsize);
  if (dtype == IEEE_Cigre_DLLInterface_DataType_c_string_T) memcpy (pVals+offset, &val.Char_Ptr, dsize);
}

int get_next_struct_offset (int offset, int dsize, size_t align)
{
  offset += 1;
  if (dsize > 1) {
    while (offset % align != 0) {
      ++offset;
    }
  }
  return offset;
}

IEEE_Cigre_DLLInterface_Instance* CreateModelInstance (const IEEE_Cigre_DLLInterface_Model_Info *pInfo,
                                                       ArrayMap **pParameterMap,
                                                       ArrayMap **pInputMap,
                                                       ArrayMap **pOutputMap)
{
  int i, input_size, output_size, parm_size, dsize;
  ArrayMap *pTest;

#ifndef ATP_MINGW
  printf("creating pModel on %s [%d,%d,%d]\n", pInfo->ModelName, pInfo->NumInputPorts, pInfo->NumOutputPorts, pInfo->NumParameters);
#endif
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
    size_t input_align = 0;
    for (i = 0; i < pInfo->NumInputPorts; i++) {
      enum IEEE_Cigre_DLLInterface_DataType dtype = pInfo->InputPortsInfo[i].DataType;
      size_t this_align = get_alignment_requirement (dtype);
      if (this_align > input_align) {
        input_align = this_align;
      }
    }
#ifndef ATP_MINGW
    printf("  Input Struct Alignment Requirement = %zu\n", input_align);
#endif
    pTest = malloc (pInfo->NumInputPorts * sizeof (ArrayMap));
    *pInputMap = pTest;
    input_size = 0;
    for (i = 0; i < pInfo->NumInputPorts; i++) {
      enum IEEE_Cigre_DLLInterface_DataType dtype = pInfo->InputPortsInfo[i].DataType;
      int dsize = get_datatype_size (dtype);
      pTest[i].size = dsize;
      pTest[i].offset = input_size;
      pTest[i].dtype = dtype;
      input_size = get_next_struct_offset (input_size, dsize, input_align);
    }
//    printf ("%d inputs of total size %d\n", pInfo->NumInputPorts, input_size);
    pModel->ExternalInputs = malloc(input_size);
  }
  if (pInfo->NumOutputPorts > 0) {
    size_t output_align = 0;
    for (i = 0; i < pInfo->NumOutputPorts; i++) {
      enum IEEE_Cigre_DLLInterface_DataType dtype = pInfo->OutputPortsInfo[i].DataType;
      size_t this_align = get_alignment_requirement (dtype);
      if (this_align > output_align) {
        output_align = this_align;
      }
    }
#ifndef ATP_MINGW
    printf("  Output Struct Alignment Requirement = %zu\n", output_align);
#endif
    pTest = malloc (pInfo->NumOutputPorts * sizeof (ArrayMap));
    *pOutputMap = pTest;
    output_size = 0;
    for (i = 0; i < pInfo->NumOutputPorts; i++) {
      enum IEEE_Cigre_DLLInterface_DataType dtype = pInfo->OutputPortsInfo[i].DataType;
      int dsize = get_datatype_size (dtype);
      pTest[i].size = dsize;
      pTest[i].offset = output_size;
      pTest[i].dtype = dtype;
      output_size = get_next_struct_offset (output_size, dsize, output_align);
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
    size_t parm_align = 0;
    for (i = 0; i < pInfo->NumParameters; i++) {
      enum IEEE_Cigre_DLLInterface_DataType dtype = pInfo->ParametersInfo[i].DataType;
      size_t this_align = get_alignment_requirement (dtype);
      if (this_align > parm_align) {
        parm_align = this_align;
      }
    }
#ifndef ATP_MINGW
    printf("  Parameter Struct Alignment Requirement = %zu\n", parm_align);
#endif
    pTest = malloc (pInfo->NumParameters * sizeof (ArrayMap));
    *pParameterMap = pTest;
    parm_size = 0;
    for (i = 0; i < pInfo->NumParameters; i++) {
      enum IEEE_Cigre_DLLInterface_DataType dtype = pInfo->ParametersInfo[i].DataType;
      dsize = get_datatype_size (dtype);
      pTest[i].size = dsize;
      pTest[i].offset = parm_size;
      pTest[i].dtype = dtype;
      parm_size = get_next_struct_offset (parm_size, dsize, parm_align);
    }
//    printf("parm_size = %d\n", parm_size);
    pModel->Parameters = malloc (parm_size);
    // initialize the parameters to default values
    for (i = 0; i < pInfo->NumParameters; i++) {
      assign_default_value ((char *)pModel->Parameters, pTest[i].offset, pTest[i].dtype, 
                            pTest[i].size, pInfo->ParametersInfo[i].DefaultValue);
    }
  }
  return pModel;
}

void FreeModelInstance (IEEE_Cigre_DLLInterface_Instance *pModel, ArrayMap *pParameterMap,
                        ArrayMap *pInputMap, ArrayMap *pOutputMap)
{
#ifndef ATP_MINGW
  printf("freeing pModel\n");
#endif
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
#ifndef ATP_MINGW
  if (NULL != pModel->LastGeneralMessage) {
    if (strlen (pModel->LastGeneralMessage) > 0) {
      printf("  %s says %s\n", loc, pModel->LastGeneralMessage);
    }
  }
#endif
}

void print_parameter_info (int k, IEEE_Cigre_DLLInterface_Parameter parm, char *pData, ArrayMap sMap)
{
#ifndef ATP_MINGW
  if (sMap.dtype == IEEE_Cigre_DLLInterface_DataType_char_T) {
    char_T val;
    memcpy (&val, pData + sMap.offset, sMap.size);
    printf("  %2d %4d %4d %-12s %12c %-70s %-10s %c \t %c \t %c\n", k, sMap.size, sMap.offset,
           parm.Name, val, parm.Description, parm.Unit, parm.DefaultValue.Char_Val,
           parm.MinValue.Char_Val, parm.MaxValue.Char_Val);
  } else if (sMap.dtype == IEEE_Cigre_DLLInterface_DataType_int8_T) {
    int8_T val;
    memcpy (&val, pData + sMap.offset, sMap.size);
    printf("  %2d %4d %4d %-12s %12hd %-70s %-10s %hhd \t %hhd \t %hhd\n", k, sMap.size, sMap.offset,
           parm.Name, val, parm.Description, parm.Unit, parm.DefaultValue.Int8_Val,
           parm.MinValue.Int8_Val, parm.MaxValue.Int8_Val);
  } else if (sMap.dtype == IEEE_Cigre_DLLInterface_DataType_uint8_T) {
    uint8_T val;
    memcpy (&val, pData + sMap.offset, sMap.size);
    printf("  %2d %4d %4d %-12s %12hhu %-70s %-10s %hhu \t %hhu \t %hhu\n", k, sMap.size, sMap.offset,
           parm.Name, val, parm.Description, parm.Unit, parm.DefaultValue.Uint8_Val,
           parm.MinValue.Uint8_Val, parm.MaxValue.Uint8_Val);
  } else if (sMap.dtype == IEEE_Cigre_DLLInterface_DataType_int16_T) {
    int16_T val;
    memcpy (&val, pData + sMap.offset, sMap.size);
    printf("  %2d %4d %4d %-12s %12hd %-70s %-10s %hd \t %hd \t %hd\n", k, sMap.size, sMap.offset,
           parm.Name, val, parm.Description, parm.Unit, parm.DefaultValue.Int16_Val,
           parm.MinValue.Int16_Val, parm.MaxValue.Int16_Val);
  } else if (sMap.dtype == IEEE_Cigre_DLLInterface_DataType_uint16_T) {
    uint16_T val;
    memcpy (&val, pData + sMap.offset, sMap.size);
    printf("  %2d %4d %4d %-12s %12hu %-70s %-10s %hu \t %hu \t %hu\n", k, sMap.size, sMap.offset,
           parm.Name, val, parm.Description, parm.Unit, parm.DefaultValue.Uint16_Val,
           parm.MinValue.Uint16_Val, parm.MaxValue.Uint16_Val);
  } else if (sMap.dtype == IEEE_Cigre_DLLInterface_DataType_int32_T) {
    int32_T val;
    memcpy (&val, pData + sMap.offset, sMap.size);
    printf("  %2d %4d %4d %-12s %12d %-70s %-10s %d \t %d \t %d\n", k, sMap.size, sMap.offset,
           parm.Name, val, parm.Description, parm.Unit, parm.DefaultValue.Int32_Val,
           parm.MinValue.Int32_Val, parm.MaxValue.Int32_Val);
  } else if (sMap.dtype == IEEE_Cigre_DLLInterface_DataType_uint32_T) {
    uint32_T val;
    memcpy (&val, pData + sMap.offset, sMap.size);
    printf("  %2d %4d %4d %-12s %12u %-70s %-10s %u \t %u \t %u\n", k, sMap.size, sMap.offset,
           parm.Name, val, parm.Description, parm.Unit, parm.DefaultValue.Uint32_Val,
           parm.MinValue.Uint32_Val, parm.MaxValue.Uint32_Val);
  } else if (sMap.dtype == IEEE_Cigre_DLLInterface_DataType_real32_T) {
    real32_T val;
    memcpy (&val, pData + sMap.offset, sMap.size);
    printf("  %2d %4d %4d %-12s %12g %-70s %-10s %g \t %g \t %g\n", k, sMap.size, sMap.offset,
           parm.Name, val, parm.Description, parm.Unit, parm.DefaultValue.Real32_Val,
           parm.MinValue.Real32_Val, parm.MaxValue.Real32_Val);
  } else if (sMap.dtype == IEEE_Cigre_DLLInterface_DataType_real64_T) {
    real64_T val;
    memcpy (&val, pData + sMap.offset, sMap.size);
    printf("  %2d %4d %4d %-12s %12g %-70s %-10s %g \t %g \t %g\n", k, sMap.size, sMap.offset,
           parm.Name, val, parm.Description, parm.Unit, parm.DefaultValue.Real64_Val,
           parm.MinValue.Real64_Val, parm.MaxValue.Real64_Val);
  } else if (sMap.dtype == IEEE_Cigre_DLLInterface_DataType_c_string_T) {
    char_T *val;
    memcpy (&val, pData + sMap.offset, sMap.size);
    printf("  %2d %4d %4d %-12s %s %-70s %-10s\n", k, sMap.size, sMap.offset,
           parm.Name, val, parm.Description, parm.Unit);
  } else {
    printf("  %2d %4d %4d %12s %12s %-70s %-10s [Unknown Type]\n", k, sMap.size, sMap.offset,
           parm.Name, "??", parm.Description, parm.Unit);
  }
#endif
}

#ifndef ATP_MINGW

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

void PrintDLLModelParameters (Wrapped_IEEE_Cigre_DLL *pWrap)
{
  // display the DLL interface schema
  printf("Model Name = %s\n", pWrap->pInfo->ModelName);
  printf("Model Version = %s\n", pWrap->pInfo->ModelVersion);
  printf("Updated %s by %s\n", pWrap->pInfo->ModelLastModifiedDate, pWrap->pInfo->ModelLastModifiedBy);
  printf("Time Step: %0.5g [s]\n", pWrap->pInfo->FixedStepBaseSampleTime);
  printf("EMT/RMS Mode: %s\n", modeEMTorRMS (pWrap->pInfo->EMT_RMS_Mode));
  printf("Parameters (idx,size,offset,name,val,desc,units,default,min,max:\n");
  for (int k=0; k < pWrap->pInfo->NumParameters; k++) {
    print_parameter_info (k, pWrap->pInfo->ParametersInfo[k], pWrap->pModel->Parameters, pWrap->pParameterMap[k]);
  }
  printf("Input Signals (idx,size,offset,name,desc,units):\n");
  for (int k=0; k < pWrap->pInfo->NumInputPorts; k++) {
    printf("  %2d %4d %4d %-12s %-70s %-10s\n", k, pWrap->pInputMap[k].size, pWrap->pInputMap[k].offset,
           pWrap->pInfo->InputPortsInfo[k].Name, pWrap->pInfo->InputPortsInfo[k].Description, pWrap->pInfo->InputPortsInfo[k].Unit);
  }
  printf("Output Signals (idx,size,offset,name,desc,units):\n");
  for (int k=0; k < pWrap->pInfo->NumOutputPorts; k++) {
    printf("  %2d %4d %4d %-12s %-70s %-10s\n", k, pWrap->pOutputMap[k].size, pWrap->pOutputMap[k].offset,
           pWrap->pInfo->OutputPortsInfo[k].Name, pWrap->pInfo->OutputPortsInfo[k].Description, pWrap->pInfo->OutputPortsInfo[k].Unit);
  }
  printf("Internal State Variables: %d int, %d float, %d double\n", pWrap->pInfo->NumIntStates, 
         pWrap->pInfo->NumFloatStates, pWrap->pInfo->NumDoubleStates);
}

#endif

Wrapped_IEEE_Cigre_DLL * CreateFirstDLLModel (char *dll_name)
{
  Wrapped_IEEE_Cigre_DLL *pWrap = malloc (sizeof (*pWrap));

  pWrap->hLib = LoadLibrary(TEXT(dll_name)); 
  if (pWrap->hLib != NULL) { 
    // this function is not used in the wrapper
    pWrap->Model_PrintInfo = (DLL_INFO_FCN) GetProcAddress(pWrap->hLib, "Model_PrintInfo"); 
    // find the required DLL functions for this wrapper
    pWrap->Model_GetInfo = (DLL_STRUCT_FCN) GetProcAddress(pWrap->hLib, "Model_GetInfo");
    if (NULL == pWrap->Model_GetInfo) {
      printf("Failed to load Model_GetInfo from %s\n", dll_name);
    }
    pWrap->Model_CheckParameters = LoadModelFunction (pWrap->hLib, "Model_CheckParameters", dll_name); 
    pWrap->Model_Initialize = LoadModelFunction (pWrap->hLib, "Model_Initialize", dll_name);
    pWrap->Model_Outputs = LoadModelFunction (pWrap->hLib, "Model_Outputs", dll_name);
    pWrap->Model_Terminate = LoadModelFunction (pWrap->hLib, "Model_Terminate", dll_name);
    // look for the new (optional) DLL functions
    pWrap->Model_FirstCall = LoadModelFunction (pWrap->hLib, "Model_FirstCall", dll_name);
    pWrap->Model_Iterate = LoadModelFunction (pWrap->hLib, "Model_Iterate", dll_name);
    // make sure we have all of the required functions
    if (NULL == pWrap->Model_GetInfo || NULL == pWrap->Model_CheckParameters || NULL == pWrap->Model_Outputs || 
        NULL == pWrap->Model_Initialize || NULL == pWrap->Model_Terminate) {
      printf ("Unable to load all of the required functions from %s\n", dll_name);
      free (pWrap);
      return NULL;
    }
    // retrieve the DLL interface points
    pWrap->pInfo = pWrap->Model_GetInfo();
    // create a model instance, initialized to default values
    pWrap->pModel = CreateModelInstance (pWrap->pInfo, &pWrap->pParameterMap, &pWrap->pInputMap, &pWrap->pOutputMap);
  } else {
    printf ("LoadLibrary failed on %s\n", dll_name);
    free (pWrap);
    return NULL;
  }
  return pWrap;
}

void FreeFirstDLLModel (Wrapped_IEEE_Cigre_DLL *pWrap)
{
  // free the Model data and library
  int val = pWrap->Model_Terminate (pWrap->pModel);
//  if (IEEE_Cigre_DLLInterface_Return_OK != val) { // messages not initialized if the model was never used
    check_messages ("Model_Terminate", pWrap->pModel);
//  }
  FreeModelInstance (pWrap->pModel, pWrap->pParameterMap, pWrap->pInputMap, pWrap->pOutputMap);
  FreeLibrary (pWrap->hLib);
  free (pWrap);
#ifndef ATP_MINGW
  printf ("normal finish\n"); 
#endif
}

