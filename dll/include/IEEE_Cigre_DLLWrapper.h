// Copyright (C) 2024 Meltran, Inc

#ifndef __IEEE_Cigre_DLLWrapper__
#define __IEEE_Cigre_DLLWrapper__

#include "IEEE_Cigre_DLLInterface.h"
 
typedef int32_T (__cdecl *DLL_INFO_FCN)(void); 
typedef const IEEE_Cigre_DLLInterface_Model_Info * (__cdecl *DLL_STRUCT_FCN)(void);
typedef int32_T (__cdecl *DLL_MODEL_FCN)(IEEE_Cigre_DLLInterface_Instance *);

typedef struct _ArrayMap {  // we will have arrays of these for Parameters, ExternalInputs and ExternalOutputs
  int size;    // size of the value from IEEE_Cigre_DLLInterface_types.h
  int offset;  // byte offset into the malloced memory for this value
  enum IEEE_Cigre_DLLInterface_DataType dtype;
} ArrayMap;

union EditValueU {
  char_T   Char_Val;
  char_T  *Char_Ptr;
  int8_T   Int8_Val;
  uint8_T  Uint8_Val;
  int16_T  Int16_Val;
  uint16_T Uint16_Val;
  int32_T  Int32_Val;
  uint32_T Uint32_Val;
  real32_T Real32_Val;
  real64_T Real64_Val;
};

typedef struct _Wrapped_IEEE_Cigre_DLL_ {
  HINSTANCE hLib;
  DLL_INFO_FCN Model_PrintInfo;
  DLL_STRUCT_FCN Model_GetInfo;
  DLL_MODEL_FCN Model_CheckParameters;
  DLL_MODEL_FCN Model_Initialize;
  DLL_MODEL_FCN Model_Outputs;
  DLL_MODEL_FCN Model_FirstCall;
  DLL_MODEL_FCN Model_Iterate;
  DLL_MODEL_FCN Model_Terminate;
  const IEEE_Cigre_DLLInterface_Model_Info *pInfo;
  IEEE_Cigre_DLLInterface_Instance *pModel;
  ArrayMap *pParameterMap; 
  ArrayMap *pInputMap; 
  ArrayMap *pOutputMap; 
} Wrapped_IEEE_Cigre_DLL;

Wrapped_IEEE_Cigre_DLL * CreateFirstDLLModel (char *dll_name);

void PrintDLLModelParameters (Wrapped_IEEE_Cigre_DLL *pWrap);

void FreeFirstDLLModel (Wrapped_IEEE_Cigre_DLL *pWrap);

void show_struct_alignment_requirements ();

const char *modeEMTorRMS (int val);

size_t get_alignment_requirement (enum IEEE_Cigre_DLLInterface_DataType dtype);

int get_datatype_size (enum IEEE_Cigre_DLLInterface_DataType dtype);

void edit_dll_value (char *pVals, int offset, enum IEEE_Cigre_DLLInterface_DataType dtype, int dsize, union EditValueU val);

IEEE_Cigre_DLLInterface_Instance* CreateModelInstance (const IEEE_Cigre_DLLInterface_Model_Info *pInfo,
                                                       ArrayMap **pParameterMap,
                                                       ArrayMap **pInputMap,
                                                       ArrayMap **pOutputMap);

void FreeModelInstance (IEEE_Cigre_DLLInterface_Instance *pModel, ArrayMap *pParameterMap,
                        ArrayMap *pInputMap, ArrayMap *pOutputMap);

void check_messages (const char *loc, IEEE_Cigre_DLLInterface_Instance *pModel);

void get_parm_value_string (char *pBuf, char *pData, ArrayMap sMap);

void write_csv_header (FILE *fp, const IEEE_Cigre_DLLInterface_Model_Info *pInfo);

void write_csv_values (FILE *fp, IEEE_Cigre_DLLInterface_Instance *pModel, const IEEE_Cigre_DLLInterface_Model_Info *pInfo, 
                       ArrayMap *pInputMap, ArrayMap *pOutputMap, double t);

#endif
