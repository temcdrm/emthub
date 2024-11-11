// Copyright (C) 2024 Meltran, Inc

/*
This is an example of a power system model written in C, according to the IEEE/Cigre DLL Modeling Standard (API V2).

This hwpv model implements generalized block diagrams per https://pecblocks.readthedocs.io/en/latest/.

Tested only with the bal3_fhf.json model.

November 11, 2024, TEMc
*/

#include <stdio.h>

#include "IEEE_Cigre_DLLInterface.h"
char ErrorMessage[1000];

// ----------------------------------------------------------------------
// Structures defining inputs, outputs, parameters and program structure
// to be called by the DLLImport Tool
// ----------------------------------------------------------------------

typedef struct _MyModelInputs {
  real64_T T;
  real64_T G;
  real64_T Fc;
  real64_T Ud;
  real64_T Uq;
  real64_T Vd;
  real64_T Vq;
  real64_T GVrms;
  real64_T Ctl;
} MyModelInputs;

IEEE_Cigre_DLLInterface_Signal InputSignals[] = {
  [0] = {
    .Name = "T",
    .Description = "Panel temperature",
    .Unit = "C",
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T,
    .Width = 1
  },
  [1] = {
    .Name = "G",
    .Description = "Solar irradiance",
    .Unit = "W/m2",
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T,
    .Width = 1
  },
  [2] = {
    .Name = "Fc",
    .Description = "Frequency control",
    .Unit = "Hz",
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T,
    .Width = 1
  },
  [3] = {
    .Name = "Ud",
    .Description = "d-axis voltage control",
    .Unit = "pu",
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T,
    .Width = 1
  },
  [4] = {
    .Name = "Uq",
    .Description = "q-axis voltage control",
    .Unit = "pu",
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T,
    .Width = 1
  },
  [5] = {
    .Name = "Vd",
    .Description = "d-axis terminal voltage",
    .Unit = "V",
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T,
    .Width = 1
  },
  [6] = {
    .Name = "Vq",
    .Description = "q-axis terminal voltage",
    .Unit = "V",
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T,
    .Width = 1
  },
  [7] = {
    .Name = "GVrms",
    .Description = "Product of G and AC terminal voltage",
    .Unit = "V*kW/m2",
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T,
    .Width = 1
  },
  [8] = {
    .Name = "Ctl",
    .Description = "State 0=start,1=grid formed,2=grid following",
    .Unit = "",
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T,
    .Width = 1
  }
};

typedef struct _MyModelOutputs {
  real64_T Vdc;
  real64_T Idc;
  real64_T Id;
  real64_T Iq;
} MyModelOutputs;

IEEE_Cigre_DLLInterface_Signal OutputSignals[] = {
  [0] = {
    .Name = "Vdc",
    .Description = "DC Bus Voltage",
    .Unit = "V",
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T,
    .Width = 1
  },
  [1] = {
    .Name = "Idc",
    .Description = "DC Current",
    .Unit = "A",
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T,
    .Width = 1
  },
  [2] = {
    .Name = "Id",
    .Description = "AC d-axis Current Injection",
    .Unit = "A",
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T,
    .Width = 1
  },
  [3] = {
    .Name = "Iq",
    .Description = "AC q-axis Current Injection",
    .Unit = "A",
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T,
    .Width = 1
  }
};

typedef struct _MyModelParameters {
  char_T *pFileName;
} MyModelParameters;

// Define Parameters
IEEE_Cigre_DLLInterface_Parameter Parameters[] = {
  [0] = {
    .Name = "JSONfile",
    .Description = "JSON file with trained model",
    .Unit = "",
    .DataType = IEEE_Cigre_DLLInterface_DataType_c_string_T,
    .FixedValue = 1,  // 0 for parameters which can be modified at any time, 1 for parameters which need to be defined at T0 but cannot be changed.
    .DefaultValue.Char_Ptr = "bal3_fhf.json" // no minimum or maximum value
  }
};

IEEE_Cigre_DLLInterface_Model_Info Model_Info = {
  .DLLInterfaceVersion = { 0, 0, 0, 8 },
  .ModelName = "hwpv",
  .ModelVersion = "0.0.0.8",
  .ModelDescription = "hwpv; generalized block diagram models",
  .GeneralInformation = "General Information",
  .ModelCreated = "November 11, 2024",
  .ModelCreator = "temc",
  .ModelLastModifiedDate = "November 11, 2024",
  .ModelLastModifiedBy = "temc",
  .ModelModifiedComment = "Version 0.0.0.8 for IEEE/Cigre DLL API V2",
  .ModelModifiedHistory = "History of Changes: V0.0.0.8 Initial model for API V1",
  .FixedStepBaseSampleTime = 0.002,                   // Time Step sampling time (sec) VARIABLE

  // Inputs
  .NumInputPorts = 9,
  .InputPortsInfo = InputSignals,

  // Outputs
  .NumOutputPorts = 4,
  .OutputPortsInfo = OutputSignals,

  // Parameters
  .NumParameters = 1,
  .ParametersInfo = Parameters,

  // Number of State Variables - this DLL will create its own internal storage
  .NumIntStates = 0,
  .NumFloatStates = 0,
  .NumDoubleStates = 0
};

// ----------------------------------------------------------------
// Subroutines that can be called by the main power system program
// ----------------------------------------------------------------
__declspec(dllexport) const IEEE_Cigre_DLLInterface_Model_Info* __cdecl Model_GetInfo() {
  /* Returns Model Information
  */
  return &Model_Info;
};

// ----------------------------------------------------------------
__declspec(dllexport) int32_T __cdecl Model_CheckParameters(IEEE_Cigre_DLLInterface_Instance* instance) {
  /*   Checks the parameters on the given range
     Arguments: Instance specific model structure containing Inputs, Parameters and Outputs
     Return:  Integer status 0 (normal), 1 if messages are written, 2 for errors.  See IEEE_Cigre_DLLInterface_types.h
  */
  // Parameter checks done by the program
  // Note - standard min/max checks should be done by the higher level GUI/Program
  MyModelParameters* parameters = (MyModelParameters*)instance->Parameters;

  char_T *pFileName = parameters->pFileName;

  FILE *fp = fopen (pFileName, "rt");
  printf("  read trained model from %s, opened as %p\n", pFileName, fp);
  fclose (fp);
  //
  double delt = Model_Info.FixedStepBaseSampleTime;

  ErrorMessage[0] = '\0';
//if (TE < 2.0*delt) {
//  // write error message
//  sprintf_s(ErrorMessage, sizeof(ErrorMessage), "SCRX9 Error - Parameter TE is: %f, but has been reset to be 2 times the time step: %f .\n", TE, delt);
//  parameters->TE = 2.0*delt;
//}
//if (TB < 2.0*delt) {
//  // write error message
//  sprintf_s(ErrorMessage, sizeof(ErrorMessage), "SCRX9 Error - Parameter TB is: %f, but has been reset to be 2 times the time step: %f .\n", TB, delt);
//  parameters->TB = 2.0*delt;
//}
  instance->LastGeneralMessage = ErrorMessage;
  return IEEE_Cigre_DLLInterface_Return_OK;
};

// ----------------------------------------------------------------
__declspec(dllexport) int32_T __cdecl Model_Initialize(IEEE_Cigre_DLLInterface_Instance* instance) {
  /*   Initializes the system by resetting the internal states
     Arguments: Instance specific model structure containing Inputs, Parameters and Outputs
     Return:  Integer status 0 (normal), 1 if messages are written, 2 for errors.  See IEEE_Cigre_DLLInterface_types.h
  */
  //
  // Note that the initial conditions for all models are determined by the main calling program
  // and are passed to this routine via the instance->ExternalOutputs vector.
  // instance->ExternalOutputs is normally the output of this routine, but in the first time step
  // the main program must set the instance->ExternalOutputs to initial values.
  //
  MyModelParameters* parameters = (MyModelParameters*)instance->Parameters;
  double delt = Model_Info.FixedStepBaseSampleTime;
  MyModelInputs* inputs = (MyModelInputs*)instance->ExternalInputs;
  MyModelOutputs* outputs = (MyModelOutputs*)instance->ExternalOutputs;
  ErrorMessage[0] = '\0';

  instance->LastGeneralMessage = ErrorMessage;
  return IEEE_Cigre_DLLInterface_Return_OK;
};

// ----------------------------------------------------------------
__declspec(dllexport) int32_T __cdecl Model_Outputs(IEEE_Cigre_DLLInterface_Instance* instance) {
  /*   Calculates output equation
     Arguments: Instance specific model structure containing Inputs, Parameters and Outputs
     Return:  Integer status 0 (normal), 1 if messages are written, 2 for errors.  See IEEE_Cigre_DLLInterface_types.h
  */
  ErrorMessage[0] = '\0';

  MyModelParameters* parameters = (MyModelParameters*)instance->Parameters;
  double delt = Model_Info.FixedStepBaseSampleTime;
  MyModelInputs* inputs = (MyModelInputs*)instance->ExternalInputs;
  MyModelOutputs* outputs = (MyModelOutputs*)instance->ExternalOutputs;

  instance->LastGeneralMessage = ErrorMessage;
  return IEEE_Cigre_DLLInterface_Return_OK;
};

// ----------------------------------------------------------------
__declspec(dllexport) int32_T __cdecl Model_Terminate(IEEE_Cigre_DLLInterface_Instance* instance) {
  /*   Destroys any objects allocated by the model code - not used
  */
  ErrorMessage[0] = '\0';
  instance->LastGeneralMessage = ErrorMessage;

  return IEEE_Cigre_DLLInterface_Return_OK;
};

// ----------------------------------------------------------------
__declspec(dllexport) int32_T __cdecl Model_PrintInfo() {
  /* Prints Model Information once
  */
  int Printed = 0;
  if (!Printed) {
    printf("Cigre/IEEE DLL Standard\n");
    printf("Model name:       %s\n", Model_Info.ModelName);
    printf("Model version:      %s\n", Model_Info.ModelVersion);
    printf("Model description:    %s\n", Model_Info.ModelDescription);
    printf("Model general info:   %s\n", Model_Info.GeneralInformation);
    printf("Model created on:     %s\n", Model_Info.ModelCreated);
    printf("Model created by:     %s\n", Model_Info.ModelCreator);
    printf("Model last modified:  %s\n", Model_Info.ModelLastModifiedDate);
    printf("Model last modified by: %s\n", Model_Info.ModelLastModifiedBy);
    printf("Model modified comment: %s\n", Model_Info.ModelModifiedComment);
    printf("Model modified history: %s\n", Model_Info.ModelModifiedHistory);
    printf("Time Step Sampling Time (sec): %0.5g\n", Model_Info.FixedStepBaseSampleTime);
    switch (Model_Info.EMT_RMS_Mode) {
      case 1:
        printf("EMT/RMS mode:       EMT\n");
        break;
      case 2:
        printf("EMT/RMS mode:       RMS\n");
        break;
      case 3:
        printf("EMT/RMS mode:       EMT and RMS\n");
        break;
      default:
        printf("EMT/RMS mode:       <not available>\n");
    }
    printf("Number of inputs:     %d\n", Model_Info.NumInputPorts);
    printf("Input description:\n");
    for (int k = 0; k < Model_Info.NumInputPorts; k++) {
      printf("  %s\n", Model_Info.InputPortsInfo[k].Name);
    }
    printf("Number of outputs:    %d\n", Model_Info.NumOutputPorts);
    printf("Output description:\n");
    for (int k = 0; k < Model_Info.NumOutputPorts; k++) {
      printf("  %s\n", Model_Info.OutputPortsInfo[k].Name);
    }

    printf("Number of parameters:   %d\n", Model_Info.NumParameters);
    printf("Parameter description:");
    for (int k = 0; k < Model_Info.NumParameters; k++) {
      printf("  %s\n", Model_Info.ParametersInfo[k].Name);
    }

    printf("Number of int  state variables:   %d\n", Model_Info.NumIntStates);
    printf("Number of float  state variables:   %d\n", Model_Info.NumFloatStates);
    printf("Number of double state variables:   %d\n", Model_Info.NumDoubleStates);
    printf("\n");
    fflush(stdout);
  }
  Printed = 1;

  return IEEE_Cigre_DLLInterface_Return_OK;
};
