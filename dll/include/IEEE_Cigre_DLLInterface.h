/*
See:
  Cigre Joint Working Group B4.82/IEEE,
  “Guidelines for use of real-code in EMT models for HVDC, FACTs and inverter based generators in power systems analysis,”
  Technical Brochure 958, Paris, FRANCE, February 2025.
  https://www.e-cigre.org/publications/detail/958-guidelines-for-use-of-real-code-in-emt-models-for-hvdc-facts-and-inverter-based-generators-in-power-systems-analysis.html.
*/
#ifndef __IEEE_Cigre_DLLInterface__
#define __IEEE_Cigre_DLLInterface__

#include "IEEE_Cigre_DLLInterface_types.h"

typedef struct _IEEE_Cigre_DLLInterface_Signal
{
    const char_T * const                        Name;
    const char_T * const                        Description;
    const char_T * const                        Unit;
    const enum IEEE_Cigre_DLLInterface_DataType DataType;
    const int32_T                               Width;
} IEEE_Cigre_DLLInterface_Signal;

union DefaultValueU {
    const char_T            Char_Val;
    const char_T * const    Char_Ptr;
    const int8_T            Int8_Val;
    const uint8_T           Uint8_Val;
    const int16_T           Int16_Val;
    const uint16_T          Uint16_Val;
    const  int32_T           Int32_Val;
    const uint32_T          Uint32_Val;
    const real32_T          Real32_Val;
    const real64_T          Real64_Val;
};

union MinMaxValueU {
    const char_T            Char_Val;
    const int8_T            Int8_Val;
    const uint8_T           Uint8_Val;
    const int16_T           Int16_Val;
    const uint16_T          Uint16_Val;
    const int32_T           Int32_Val;
    const uint32_T          Uint32_Val;
    const real32_T          Real32_Val;
    const real64_T          Real64_Val;
};

typedef struct _IEEE_Cigre_DLLInterface_Parameter
{
    const char_T * const                        Name;
    const char_T * const                        GroupName;
    const char_T * const                        Description;
    const char_T * const                        Unit;
    const enum IEEE_Cigre_DLLInterface_DataType DataType;
    const int32_T                               FixedValue;
    union DefaultValueU DefaultValue;
    union MinMaxValueU  MinValue;
    union MinMaxValueU  MaxValue;
} IEEE_Cigre_DLLInterface_Parameter;

typedef struct _IEEE_Cigre_DLLInterface_Model_Info
{
    const uint8_T                                   DLLInterfaceVersion[4];
    const char_T * const                            ModelName;
    const char_T * const                            ModelVersion;
    const char_T * const                            ModelDescription;
    const char_T * const                            GeneralInformation;
    const char_T * const                            ModelCreated;
    const char_T * const                            ModelCreator;
    const char_T * const                            ModelLastModifiedDate;
    const char_T * const                            ModelLastModifiedBy;
    const char_T * const                            ModelModifiedComment;
    const char_T * const                            ModelModifiedHistory;
    const real64_T                                  FixedStepBaseSampleTime;
    const uint8_T                                   EMT_RMS_Mode;

    const int32_T                                   NumInputPorts;
    const IEEE_Cigre_DLLInterface_Signal * const    InputPortsInfo;
    const int32_T                                   NumOutputPorts;
    const IEEE_Cigre_DLLInterface_Signal * const    OutputPortsInfo;
    const int32_T                                   NumParameters;
    const IEEE_Cigre_DLLInterface_Parameter * const ParametersInfo;

    const int32_T                                   NumIntStates;
    const int32_T                                   NumFloatStates;
    const int32_T                                   NumDoubleStates;
} IEEE_Cigre_DLLInterface_Model_Info;

typedef struct _IEEE_Cigre_DLLInterface_Instance
{
    void *          ExternalInputs;
    void *          ExternalOutputs;
    void *          Parameters;
    real64_T        Time;
    const uint8_T   SimTool_EMT_RMS_Mode;
    const char_T *  LastErrorMessage;
    const char_T *  LastGeneralMessage;
    int32_T *       IntStates;
    real32_T *      FloatStates;
    real64_T *      DoubleStates;
} IEEE_Cigre_DLLInterface_Instance;

/* Function signatures the DLL should implement.
   All return IEEE_Cigre_DLLInterface_Return_Value. */
/*
typedef const IEEE_Cigre_DLLInterface_Model_Info *(__cdecl* Model_GetInfo)(void);
typedef int32_T (__cdecl* Model_FirstCall) (IEEE_Cigre_DLLInterface_Instance *pModelInstance);
typedef int32_T (__cdecl* Model_CheckParameters) (IEEE_Cigre_DLLInterface_Instance *pModelInstance);
typedef int32_T (__cdecl* Model_Initialize) (IEEE_Cigre_DLLInterface_Instance *pModelInstance);
typedef int32_T (__cdecl* Model_Outputs) (IEEE_Cigre_DLLInterface_Instance *pModelInstance);
typedef int32_T (__cdecl* Model_Iterate) (IEEE_Cigre_DLLInterface_Instance *pModelInstance);
typedef int32_T (__cdecl* Model_Terminate) (IEEE_Cigre_DLLInterface_Instance *pModelInstance);
typedef int32_T (__cdecl* Model_PrintInfo) (void)
*/

#endif /* __IEEE_Cigre_DLLInterface__ */

