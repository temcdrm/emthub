// Legacy static exciter model, SEXS, written to the IEEE CIGRE DLL interface
#include <stdio.h>
#include <math.h>

#include "IEEE_Cigre_DLLInterface.h"
char ErrorMessage[1000];

//static inline int32_t MAX(int32_t a, int32_t b) { return((a) > (b) ? a : b); }
//static inline int32_t MIN(int32_t a, int32_t b) { return((a) < (b) ? a : b); }
#define MAX(a, b) ((a) > (b) ? (a) : (b))
#define MIN(a, b) ((a) < (b) ? (a) : (b))

// define model input signals
typedef struct _MyModelInputs {
  real64_T Vref;
  real64_T Vc;
  real64_T Vs;
} MyModelInputs;

IEEE_Cigre_DLLInterface_Signal InputSignals[] = {
  {
    .Name = "Vref",
    .Description = "Reference voltage (+)",
    .Unit = "pu",
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T,
    .Width = 1
  },
  {
    .Name = "Vc",
    .Description = "Measured voltage (-)",
    .Unit = "pu",
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T,
    .Width = 1
  },
  {
    .Name = "Vs",
    .Description = "Stabilizer plus over/under excitation limiter signals (+)",
    .Unit = "pu",
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T,
    .Width = 1
  }
};

// define model output signals
typedef struct _MyModelOutputs {
  real64_T Efd;
} MyModelOutputs;

IEEE_Cigre_DLLInterface_Signal OutputSignals[] = {
  {
    .Name = "Efd",
    .Description = "Output field voltage",
    .Unit = "pu",
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T,
    .Width = 1
  }
};

// define model parameters
typedef struct _MyModelParameters {
  real64_T TaTb;
  real64_T Tb;
  real64_T K;
  real64_T Te;
  real64_T Emin;
  real64_T Emax;
  real64_T Kc;
  real64_T Tc;
  real64_T EfdMin;
  real64_T EfdMax;
} MyModelParameters;

IEEE_Cigre_DLLInterface_Parameter Parameters[] = {
  {
    .Name = "TaTb",
    .Description = "Ratio of lead/lag time constants",
    .Unit = "sec",
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T,
    .FixedValue = 1,
    .DefaultValue.Real64_Val = 0.1,
    .MinValue.Real64_Val = 0.05,
    .MaxValue.Real64_Val = 1.0
    },
  {
    .Name = "Tb",
    .Description = "Lag time constant",
    .Unit = "sec",
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T,
    .FixedValue = 1,
    .DefaultValue.Real64_Val = 10.0,
    .MinValue.Real64_Val = 5.0,
    .MaxValue.Real64_Val = 20.0
    },
  {
    .Name = "K",
    .Description = "Gain",
    .Unit = "pu",
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T,
    .FixedValue = 1,
    .DefaultValue.Real64_Val = 100.0,
    .MinValue.Real64_Val = 20.0,
    .MaxValue.Real64_Val = 500.0
    },
  {
    .Name = "Te",
    .Description = "Gain time constant",
    .Unit = "sec",
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T,
    .FixedValue = 1,
    .DefaultValue.Real64_Val = 0.05,
    .MinValue.Real64_Val = 0.0,
    .MaxValue.Real64_Val = 0.5
    },
  {
    .Name = "Emin",
    .Description = "Minimum field voltage (anti-windup limit)",
    .Unit = "pu",
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T,
    .FixedValue = 1,
    .DefaultValue.Real64_Val = -5.0,
    .MinValue.Real64_Val = -6.0,
    .MaxValue.Real64_Val = -1.0
    },
  {
    .Name = "Emax",
    .Description = "Maximum field voltage (anti-windup limit)",
    .Unit = "pu",
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T,
    .FixedValue = 1,
    .DefaultValue.Real64_Val = 5.0,
    .MinValue.Real64_Val = 1.0,
    .MaxValue.Real64_Val = 6.0
    },
  {
    .Name = "Kc",
    .Description = "PI controller gain, >0 if TC >0",
    .Unit = "pu",
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T,
    .FixedValue = 1,
    .DefaultValue.Real64_Val = 0.08,
    .MinValue.Real64_Val = 0.0,
    .MaxValue.Real64_Val = 1000.0
    },
  {
    .Name = "Tc",
    .Description = "PI controller phase lead time constant (0 disables PI)",
    .Unit = "sec",
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T,
    .FixedValue = 1,
    .DefaultValue.Real64_Val = 0.0,
    .MinValue.Real64_Val = 0.0,
    .MaxValue.Real64_Val = 100.0
    },
  {
    .Name = "EfdMin",
    .Description = "Minimum field voltage (static clipping)",
    .Unit = "pu",
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T,
    .FixedValue = 1,
    .DefaultValue.Real64_Val = -5.0,
    .MinValue.Real64_Val = -6.0,
    .MaxValue.Real64_Val = -1.0
    },
  {
    .Name = "EfdMax",
    .Description = "Maximum field voltage (static clipping)",
    .Unit = "pu",
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T,
    .FixedValue = 1,
    .DefaultValue.Real64_Val = 5.0,
    .MinValue.Real64_Val = 1.0,
    .MaxValue.Real64_Val = 6.0
    }
};

// top-level model metadata
IEEE_Cigre_DLLInterface_Model_Info Model_Info = {
  .DLLInterfaceVersion = { 1, 1, 0, 0 },
  .ModelName = "SEXS",
  .ModelVersion = "1.0.0.0",
  .ModelDescription = "The CIM ExcSEXS, a legacy static excitation system model",
  .GeneralInformation = "Prohibited by NERC",
  .ModelCreated = "August 14, 2026",
  .ModelCreator = "temc",
  .ModelLastModifiedDate = "August 14, 2026",
  .ModelLastModifiedBy = "temc",
  .ModelModifiedComment = "",
  .ModelModifiedHistory = "",
  .FixedStepBaseSampleTime = 0.005,

  // Inputs
  .NumInputPorts = 3,
  .InputPortsInfo = InputSignals,

  // Outputs
  .NumOutputPorts = 1,
  .OutputPortsInfo = OutputSignals,

  // Parameters
  .NumParameters = 10,
  .ParametersInfo = Parameters,

  // Number of State Variables
  .NumIntStates = 0,
  .NumFloatStates = 0,
  .NumDoubleStates = 6
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
  Return:    Integer status 0 (normal), 1 if messages are written, 2 for errors.  See IEEE_Cigre_DLLInterface_types.h
  Note: Simple min/max checks should be done by the higher level GUI/Program
  */
  enum IEEE_Cigre_DLLInterface_Return_Value ret = IEEE_Cigre_DLLInterface_Return_OK;
  ErrorMessage[0] = '\0';
  double delt = Model_Info.FixedStepBaseSampleTime;
  MyModelParameters* parameters = (MyModelParameters*)instance->Parameters;

  if (parameters->Te < 2.0*delt) {
    sprintf_s(ErrorMessage, sizeof(ErrorMessage), "SEXS Warning - Parameter Te is: %f, but has been reset to be 2 times the time step: (%f).\n", parameters->Te, delt);
    parameters->Te = 2.0*delt;
    ret = MAX (ret,IEEE_Cigre_DLLInterface_Return_Message);
  }
  if (parameters->Tb < 2.0*delt) {
    sprintf_s(ErrorMessage, sizeof(ErrorMessage), "SEXS Warning - Parameter Tb is: %f, but has been reset to be 2 times the time step: (%f).\n", parameters->Tb, delt);
    parameters->Tb = 2.0*delt;
    ret = MAX (ret,IEEE_Cigre_DLLInterface_Return_Message);
  }
  if (parameters->Tc > 0.0) { // PI block enabled
    if (parameters->Tc < 2.0*delt) {
      sprintf_s(ErrorMessage, sizeof(ErrorMessage), "SEXS Warning - Parameter Tc is: %f, but has been reset to be 2 times the time step (%f).\n", parameters->Tc, delt);
      parameters->Tc = 2.0*delt;
      ret = MAX (ret,IEEE_Cigre_DLLInterface_Return_Message);
    }
    if (parameters->Kc <= 0.0) {
      sprintf_s(ErrorMessage, sizeof(ErrorMessage), "SEXS Error - Parameter Kc may not be zero when Tc is greater than zero (%f).\n", parameters->Tc);
      ret = MAX (ret,IEEE_Cigre_DLLInterface_Return_Error);
    }
  } else { // PI block disabled
    parameters->Kc = 1.0;
  }
  double product = parameters->TaTb * parameters->K;
  if (product < 5.0 || product > 15.0) {
    sprintf_s(ErrorMessage, sizeof(ErrorMessage), "SEXS Warning - Parameter TaTb*K (%f) should range from 5 to 15.\n", product);
    ret = MAX (ret,IEEE_Cigre_DLLInterface_Return_Message);
  }
  instance->LastGeneralMessage = ErrorMessage;
  return ret;
};

// returns the input u0
double initialize_leadlag (double k, double tau1, double tau2, double y0, double *two_states) {
  two_states[0] = y0;
  two_states[1] = y0/k;
  return two_states[1];
}

// returns the input u0
double initialize_realpole (double k, double tau, double y0, double *two_states) {
  two_states[0] = y0;
  two_states[1] = y0/k;
  return two_states[1];
}

// returns the total input u0, typically zero if the proportional output is assumed zero
double initialize_PIblock (double kp, double ki, double y0, double *two_states) {
  two_states[0] = y0; // the integrator maintains the total initial output
  two_states[1] = 0.0;
  return two_states[1];
}

// returns the input u0, assumed to be zero
double initialize_integrator (double k, double y0, double *two_states) {
  two_states[0] = y0;
  two_states[1] = 0.0;
  return two_states[1];
}

// ----------------------------------------------------------------
__declspec(dllexport) int32_T __cdecl Model_Initialize(IEEE_Cigre_DLLInterface_Instance* instance) {
  /*   Initializes the system by resetting the internal states
  Arguments: Instance specific model structure containing Inputs, Parameters and Outputs
  Return:    Integer status 0 (normal), 1 if messages are written, 2 for errors.  See IEEE_Cigre_DLLInterface_types.h
  */
  //
  // Note that the initial conditions for all models are determined by the main calling program
  // and are passed to this routine via the instance->ExternalOutputs vector.
  // instance->ExternalOutputs is normally the output of this routine, but in the first time step
  // the main program must set the instance->ExternalOutputs to initial values.
  //
  enum IEEE_Cigre_DLLInterface_Return_Value ret = IEEE_Cigre_DLLInterface_Return_OK;
  ErrorMessage[0] = '\0';
  double delt = Model_Info.FixedStepBaseSampleTime;
  MyModelInputs* inputs = (MyModelInputs*)instance->ExternalInputs;
  MyModelOutputs* outputs = (MyModelOutputs*)instance->ExternalOutputs;
  MyModelParameters* parameters = (MyModelParameters*)instance->Parameters;
  double *states = instance->DoubleStates;

  // local variables
  double Verr = inputs->Vref + inputs->Vs - inputs->Vc;
  double y2, y1, y0;

  // test Efd initial condition against the clipping limit.
  if (outputs->Efd < parameters->EfdMin) {
    sprintf_s(ErrorMessage, sizeof(ErrorMessage), "SEXS Warning - initial field voltage (%f) corrected to EfdMin (%f).\n", outputs->Efd, parameters->EfdMin);
    outputs->Efd = parameters->EfdMin;
    ret = MAX (ret,IEEE_Cigre_DLLInterface_Return_Message);
  }
  if (outputs->Efd > parameters->EfdMax) {
    sprintf_s(ErrorMessage, sizeof(ErrorMessage), "SEXS Warning - initial field voltage (%f) corrected to EfdMax (%f).\n", outputs->Efd, parameters->EfdMax);
    outputs->Efd = parameters->EfdMax;
    ret = MAX (ret,IEEE_Cigre_DLLInterface_Return_Message);
  }
  // Working back from initial output
  y2 = initialize_realpole (parameters->K, parameters->Te, outputs->Efd, &states[4]);
  if (parameters->Tc > 0.0) {
    y1 = initialize_PIblock (parameters->Kc, parameters->Kc/parameters->Tc, y2, &states[2]);
  } else {
    y1 = y2;
  }
  y0 = initialize_leadlag (1.0, parameters->TaTb*parameters->Tb, parameters->Tb, y1, &states[0]);

  // how close is the error signal based on the initial input values?
  sprintf_s(ErrorMessage, sizeof(ErrorMessage), "SEXS Message - input Verr (%f) compared to back-calculated Verr (%f).\n", Verr, y0);
  ret = MAX (ret,IEEE_Cigre_DLLInterface_Return_Message);

  printf("Initial y2=%0.5g, y1=%0.5g, y0=%0.5g\n", y2, y1, y0);
  for (int i = 0; i < 6; i++) {
    printf("  State %1d=%0.5g\n", i, states[i]);
  }

  instance->LastGeneralMessage = ErrorMessage;
  return ret;
};

// Pure integrator with gain, anti-windup and static clipping.
// The two_states are y and u from the previous step, updated within this function.
double integrator (double k, double dt, double u, double *two_states, 
                   double aw_min, double aw_max, double clip_min, double clip_max) {
  double y = two_states[0];
  double dy = 0.5*k*dt*(u+two_states[1]);
  // anti-windup clipping by conditional integration
  if (dy > 0.0 && y <= aw_max) {
    y += dy;
  } else if (dy < 0.0 && y >= aw_min) {
    y += dy;
  }
  // static clipping
  y = fmin (y, clip_max);
  y = fmax (y, clip_min);
  // update states for the next step
  two_states[0] = y;
  two_states[1] = u;
  return y;
}

// Proportional-Integral control block with optional anti-windup and static clipping
// The two_states are integrator (Ki/s) y and total u from the previous step, updated within this function.
double PIblock (double kp, double ki, double dt, double u, double *two_states,
                double aw_min, double aw_max, double clip_min, double clip_max) {
  double yp = kp*u; // the proportional term
  // check for windup using the previous integrator state
  double yi = two_states[0];
  double dyi = 0.5*ki*dt*(u+two_states[1]);
  double ytest = yp + yi + dyi;
  double y;
  if (ytest > aw_max && dyi > 0.0) {
    y = aw_max;
    yi = y - yp;
  } else if (ytest < aw_min && dyi < 0.0) {
    y = aw_min;
    yi = y + yp;
  } else {
    y = ytest;
    yi += dyi;
  }
  // static clipping
  y = fmin (y, clip_max);
  y = fmax (y, clip_min);
  two_states[0] = yi;
  two_states[1] = u;
  return y;
}

// First-order lag block with gain and static clipping.
// The two_states are y and u from the previous step, updated within this function.
double realpole (double k, double tau, double dt, double u, double *two_states, 
                 double clip_min, double clip_max) {
  double ktau = 0.5*dt/tau;
  double y = (two_states[0]*(1.0-ktau) + (u+two_states[1])*k*ktau) / (1.0+ktau);
  // static clipping
  y = fmin (y, clip_max);
  y = fmax (y, clip_min);
  // update states for the next step
  two_states[0] = y;
  two_states[1] = u;
  return y;
}

// First-order lead-lag block with gain and static clipping.
// The two_states are y and u from the previous step, updated within this function.
double leadlag (double k, double tau1, double tau2, double dt, double u, double *two_states,
                double clip_min, double clip_max) {
  double y, ktau2;
  if (tau1 < 1.0e-8) {
    return realpole (k, tau2, dt, u, two_states, clip_min, clip_max);
  }
  ktau2 = 0.5*dt/tau2;
  y = (two_states[0] + (u-two_states[1])*k*tau1/tau2 + ktau2*(k*u+k*two_states[1]-two_states[0])) / (1.0 + ktau2);
  // static clipping
  y = fmin (y, clip_max);
  y = fmax (y, clip_min);
  // update states for the next step
  two_states[0] = y;
  two_states[1] = u;
  return y;
}

// ----------------------------------------------------------------
__declspec(dllexport) int32_T __cdecl Model_Outputs(IEEE_Cigre_DLLInterface_Instance* instance) {
  /*   Calculates output equation
  Arguments: Instance specific model structure containing Inputs, Parameters and Outputs
  Return:    Integer status 0 (normal), 1 if messages are written, 2 for errors.  See IEEE_Cigre_DLLInterface_types.h
  */
  enum IEEE_Cigre_DLLInterface_Return_Value ret = IEEE_Cigre_DLLInterface_Return_OK;
  ErrorMessage[0] = '\0';
  double delt = Model_Info.FixedStepBaseSampleTime;
  MyModelInputs* inputs = (MyModelInputs*)instance->ExternalInputs;
  MyModelOutputs* outputs = (MyModelOutputs*)instance->ExternalOutputs;
  MyModelParameters* parameters = (MyModelParameters*)instance->Parameters;
  double *states = instance->DoubleStates;
  // local variables
  double Verr, y1, y2;

  // Voltage summation loop
  Verr = inputs->Vref + inputs->Vs - inputs->Vc;
  y1 = leadlag (1.0, parameters->TaTb*parameters->Tb, parameters->Tb, delt, Verr, &states[0], -1.0e8, 1.0e8);
  if (parameters->Tc > 0.0) {
    // apply anti-windup limit on the PI block
    y2 = PIblock (parameters->Kc, parameters->Kc/parameters->Tc, delt, y1, &states[2], parameters->Emin, parameters->Emax, -1.0e8, 1.0e8);
  } else {
    y2 = y1;
  }
  // apply static limit on the output low-pass block
  outputs->Efd = realpole (parameters->K, parameters->Te, delt, y2, &states[4], parameters->EfdMin, parameters->EfdMax);

  printf("Verr=%0.5g, y1=%0.5g, y2=%0.5g, Efd=%0.5g\n", Verr, y1, y2, outputs->Efd);

  instance->LastGeneralMessage = ErrorMessage;
  return ret;
};

// ----------------------------------------------------------------
__declspec(dllexport) int32_T __cdecl Model_Terminate(IEEE_Cigre_DLLInterface_Instance* instance) {
  /*   Destroys any objects allocated by the model code - not used in this case
  */
  enum IEEE_Cigre_DLLInterface_Return_Value ret = IEEE_Cigre_DLLInterface_Return_OK;
  ErrorMessage[0] = '\0';

  instance->LastGeneralMessage = ErrorMessage;
  return ret;
};
// ----------------------------------------------------------------
__declspec(dllexport) int32_T __cdecl Model_PrintInfo() {
  /* Prints Model Information once
  */
  enum IEEE_Cigre_DLLInterface_Return_Value ret = IEEE_Cigre_DLLInterface_Return_OK;
  ErrorMessage[0] = '\0';
  static int Printed = 0;
  if (!Printed) {
    printf("Cigre/IEEE DLL Standard\n");
    printf("Model name:    %s\n", Model_Info.ModelName);
    printf("Model version:    %s\n", Model_Info.ModelVersion);
    printf("Model description:   %s\n", Model_Info.ModelDescription);
    printf("Model general info:  %s\n", Model_Info.GeneralInformation);
    printf("Model created on:    %s\n", Model_Info.ModelCreated);
    printf("Model created by:    %s\n", Model_Info.ModelCreator);
    printf("Model last modified:    %s\n", Model_Info.ModelLastModifiedDate);
    printf("Model last modified by: %s\n", Model_Info.ModelLastModifiedBy);
    printf("Model modified comment: %s\n", Model_Info.ModelModifiedComment);
    printf("Model modified history: %s\n", Model_Info.ModelModifiedHistory);
    printf("Time Step Sampling Time (sec): %0.5g\n", Model_Info.FixedStepBaseSampleTime);
    switch (Model_Info.EMT_RMS_Mode) {
     case 1:
      printf("EMT/RMS mode:  EMT\n");
      break;
     case 2:
      printf("EMT/RMS mode:  RMS\n");
      break;
     case 3:
      printf("EMT/RMS mode:  EMT and RMS\n");
      break;
     default:
      printf("EMT/RMS mode:  <not available>\n");
    }
    printf("Number of inputs:    %d\n", Model_Info.NumInputPorts);
    printf("Input description:\n");
    for (int k = 0; k < Model_Info.NumInputPorts; k++) {
     printf("  %s\n", Model_Info.InputPortsInfo[k].Name);
    }
    printf("Number of outputs:   %d\n", Model_Info.NumOutputPorts);
    printf("Output description:\n");
    for (int k = 0; k < Model_Info.NumOutputPorts; k++) {
     printf("  %s\n", Model_Info.OutputPortsInfo[k].Name);
    }
    printf("Number of parameters:   %d\n", Model_Info.NumParameters);
    printf("Parameter description:");
    for (int k = 0; k < Model_Info.NumParameters; k++) {
     printf("  %s\n", Model_Info.ParametersInfo[k].Name);
    }
    printf("Number of int    state variables:   %d\n", Model_Info.NumIntStates);
    printf("Number of float  state variables:   %d\n", Model_Info.NumFloatStates);
    printf("Number of double state variables:   %d\n", Model_Info.NumDoubleStates);
    printf("\n");
    fflush(stdout);
  }
  Printed = 1;
  return ret;
};
