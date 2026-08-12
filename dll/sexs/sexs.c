// Legacy static exciter model, SEXS, written to the IEEE CIGRE DLL interface
#include <stdio.h>

#include "IEEE_Cigre_DLLInterface.h"
char ErrorMessage[1000];

// define model input signals
typedef struct _MyModelInputs {
    real64_T VRef;
    real64_T Ec;
    real64_T Vs;
    real64_T IFD;
    real64_T VT;
    real64_T VUEL;
    real64_T VOEL;
} MyModelInputs;

IEEE_Cigre_DLLInterface_Signal InputSignals[] = {
    [0] = {
        .Name = "VRef",                                        
        .Description = "Reference voltage",                    
        .Unit = "pu",                                          
        .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
        .Width = 1                                             
    },
    [1] = {
        .Name = "Ec",                                          
        .Description = "Measured voltage",                     
        .Unit = "pu",                                          
        .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
        .Width = 1                                             
    },
    [2] = {
        .Name = "Vs",                                          
        .Description = "Stabilizer signal",                    
        .Unit = "pu",                                          
        .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
        .Width = 1                                             
    },
    [3] = {
        .Name = "IFD",                                         
        .Description = "Field Current",                        
        .Unit = "pu",                                          
        .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
        .Width = 1                                             
    },
    [4] = {
        .Name = "VT",                                          
        .Description = "Terminal voltage",                     
        .Unit = "pu",                                          
        .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
        .Width = 1                                             
    },
    [5] = {
        .Name = "VUEL",                                        
        .Description = "Under excitation limit",               
        .Unit = "pu",                                          
        .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
        .Width = 1                                             
    },
    [6] = {
        .Name = "VOEL",                                        
        .Description = "Over excitation limit",                
        .Unit = "pu",                                          
        .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
        .Width = 1                                             
    }
};

// define model output signals
typedef struct _MyModelOutputs {
    real64_T EFD;
} MyModelOutputs;

IEEE_Cigre_DLLInterface_Signal OutputSignals[] = {    
    [0] = {
        .Name = "EFD",                                         
        .Description = "Output Field Voltage",                 
        .Unit = "pu",                                          
        .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
        .Width = 1                                             
    }
};

// define model parameters
typedef struct _MyModelParameters {
    real64_T TAdTB;
    real64_T TB;
    real64_T K;
    real64_T TE;
    real64_T EMin;
    real64_T EMax;
    int32_T  CSwitch;
    real64_T RCdRFD;
} MyModelParameters;

IEEE_Cigre_DLLInterface_Parameter Parameters[] = {
    [0] = {
        .Name = "TAdTB",                                       
        .Description = "Smoothing Time Constant",              
        .Unit = "sec",                                         
        .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
        .FixedValue = 0,                                       
        .DefaultValue.Real64_Val = 0.1,                        
        .MinValue.Real64_Val = 0.001,                          
        .MaxValue.Real64_Val = 100.0                           
    },
    [1] = {
        .Name = "TB",                                          
        .Description = "Smoothing Time Constant",              
        .Unit = "sec",                                         
        .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
        .FixedValue = 0,                                       
        .DefaultValue.Real64_Val = 10.0,                       
        .MinValue.Real64_Val = 0.001,                          
        .MaxValue.Real64_Val = 100.0                           
    },    
    [2] = {
        .Name = "K",                                           
        .Description = "Gain",                                 
        .Unit = "pu",                                          
        .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
        .FixedValue = 0,                                       
        .DefaultValue.Real64_Val = 100.0,                      
        .MinValue.Real64_Val = 0.001,                          
        .MaxValue.Real64_Val = 1000.0                          
    },
    [3] = {
        .Name = "TE",                                          
        .Description = "Time Constant",                        
        .Unit = "sec",                                         
        .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
        .FixedValue = 0,                                       
        .DefaultValue.Real64_Val = 0.05,                       
        .MinValue.Real64_Val = 0.001,                          
        .MaxValue.Real64_Val = 100.0                           
    },
    [4] = {
        .Name = "EMin",                                        
        .Description = "Min Field Voltage",                    
        .Unit = "pu",                                          
        .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
        .FixedValue = 0,                                       
        .DefaultValue.Real64_Val = -5.0,                       
        .MinValue.Real64_Val = -100.0,                         
        .MaxValue.Real64_Val = -1.0                            
    },
    [5] = {
        .Name = "EMax",                                        
        .Description = "Max Field Voltage",                    
        .Unit = "pu",                                          
        .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
        .FixedValue = 0,                                       
        .DefaultValue.Real64_Val = 5.0,                        
        .MinValue.Real64_Val = 1.0,                            
        .MaxValue.Real64_Val = 100.0                           
    },
    [6] = {
        .Name = "CSwitch",                                     
        .Description = "Power source: 0=VT, 1=1.0",            
        .Unit = "",                                            
        .DataType = IEEE_Cigre_DLLInterface_DataType_int32_T,  
        .FixedValue = 0,                                       
        .DefaultValue.Int32_Val = 1,                           
        .MinValue.Int32_Val = 0,                               
        .MaxValue.Int32_Val = 1                                
    },
    [7] = {
        .Name = "RCdRFD",                                      
        .Description = "Field resistance ratio",               
        .Unit = "",                                            
        .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
        .FixedValue = 0,                                       
        .DefaultValue.Real64_Val = 10.0,                       
        .MinValue.Real64_Val = 0.001,                          
        .MaxValue.Real64_Val = 100.0                           
    }
};

// top-level model metadata
IEEE_Cigre_DLLInterface_Model_Info Model_Info = {
    .DLLInterfaceVersion = { 1, 1, 0, 1 }, 
    .ModelName = "SEXS",                                             
    .ModelVersion = "1.0.0.0",                                        
    .ModelDescription = "SEXS - Legacy static excitation system model",
    .GeneralInformation = "Prohibited by NERC",                      
    .ModelCreated = "August 10, 2026",                             
    .ModelCreator = "gdi",                                            
    .ModelLastModifiedDate = "August 10, 2026",                      
    .ModelLastModifiedBy = "temc",                                    
    .ModelModifiedComment = "Version 1.1.0.1 for IEEE/Cigre DLL API V2",
    .ModelModifiedHistory = "", 
    .FixedStepBaseSampleTime = 0.005,

    // Inputs
    .NumInputPorts = 7,              
    .InputPortsInfo = InputSignals,  

    // Outputs
    .NumOutputPorts = 1,             
    .OutputPortsInfo = OutputSignals,

    // Parameters
    .NumParameters = 8,              
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
    */
    // Parameter checks done by the program
    // Note - standard min/max checks should be done by the higher level GUI/Program
    MyModelParameters* parameters = (MyModelParameters*)instance->Parameters;

    double TAdTB = parameters->TAdTB;
    double TB = parameters->TB;
    double K = parameters->K;
    double TE = parameters->TE;
    double EMin = parameters->EMin;
    double EMax = parameters->EMax;
    int CSwitch = parameters->CSwitch;
    double RCdRFD = parameters->RCdRFD;
    //
    double delt = Model_Info.FixedStepBaseSampleTime;

    ErrorMessage[0] = '\0';
    if (TE < 2.0*delt) {
        // write error message
        sprintf_s(ErrorMessage, sizeof(ErrorMessage), "SEXS Error - Parameter TE is: %f, but has been reset to be 2 times the time step: %f .\n", TE, delt);
        parameters->TE = 2.0*delt;
    }
    if (TB < 2.0*delt) {
        // write error message
        sprintf_s(ErrorMessage, sizeof(ErrorMessage), "SEXS Error - Parameter TB is: %f, but has been reset to be 2 times the time step: %f .\n", TB, delt);
        parameters->TB = 2.0*delt;
    }
    instance->LastGeneralMessage = ErrorMessage;
    return IEEE_Cigre_DLLInterface_Return_OK;
};

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
    MyModelParameters* parameters = (MyModelParameters*)instance->Parameters;
    // local variables
    double OControl;
    double OLeadLag;
    double Verr;
    double VOffset;
    // Retrieve variables from Input, Output and State
    double TAdTB = parameters->TAdTB;
    double TB = parameters->TB;
    double K = parameters->K;
    double TE = parameters->TE;
    double EMin = parameters->EMin;
    double EMax = parameters->EMax;
    int CSwitch = parameters->CSwitch;
    double RCdRFD = parameters->RCdRFD;
    //
    double delt = Model_Info.FixedStepBaseSampleTime;
    //
    MyModelInputs* inputs = (MyModelInputs*)instance->ExternalInputs;
    double VRef = inputs->VRef;
    double Ec = inputs->Ec;
    double Vs = inputs->Vs;
    double IFD = inputs->IFD;
    double VT = inputs->VT;
    double VUEL = inputs->VUEL;
    double VOEL = inputs->VOEL;

    // Working back from initial output
    MyModelOutputs* outputs = (MyModelOutputs*)instance->ExternalOutputs;
    double EFD = outputs->EFD;
    ErrorMessage[0] = '\0';
    // test if  initial conditions use negative field logic
    if (IFD < 0.0) {
        sprintf_s(ErrorMessage, sizeof(ErrorMessage), "SEXS Warning - initial field current: %f is negative.\n", IFD);
    }

    // check if bus-fed or independent supply
    if (CSwitch == 1) {
        OControl = EFD;
    } else {
        OControl = EFD / VT;
    }
    // test EFD initial condition is on a EMax or EMin limit
    if (OControl < EMin) {
        sprintf_s(ErrorMessage, sizeof(ErrorMessage), "SEXS Warning - initial field voltage is %f and is < EMin: %f.\n", OControl, EMin);
        OControl = EMin;
    }
    if (OControl > EMax) {
        sprintf_s(ErrorMessage, sizeof(ErrorMessage), "SEXS Warning - initial field voltage is %f and is > EMax: %f.\n", OControl, EMax);
        OControl = EMax;
    }
    OLeadLag = OControl / K;
    Verr = OLeadLag;
    VOffset = Verr;

    // save state variables
    instance->DoubleStates[0] = OLeadLag;
    instance->DoubleStates[1] = Verr;
    instance->DoubleStates[2] = OControl;
    instance->DoubleStates[3] = VOffset;  // offset needed to add to input voltage summation loop (constant)
    instance->DoubleStates[4] = OControl;
    instance->DoubleStates[5] = OLeadLag*(1.0 - TAdTB);
    instance->LastGeneralMessage = ErrorMessage;
    return IEEE_Cigre_DLLInterface_Return_OK;
};

// first order lag with gain G, time constant T, with non-windup internal limits
double REALPOLE(double G, double T, double x, double x_old, double y_old, double ymin, double ymax, double delt) {
    double y;
    double Kint = (delt*0.5) / T;

    y = (y_old + Kint*(G*x + G*x_old - y_old)) / (1.0 + Kint);
    if (y > ymax)  y = ymax;
    if (y < ymin)  y = ymin;
    return y;
};


// first order leadlag with gain G, lead time constant T1, lag time constant T2, with non-windup internal limits
double LEADLAG(double G, double T1, double T2, double x, double x_old, double y_old, double ymin, double ymax, double delt) {
    double y;
    double Kint = (delt*0.5) / T2;
    if (T1 < 1.0E-8) {
        y = REALPOLE(G, T2, x, x_old, y_old, ymin, ymax, delt);
    } else {
        y = (y_old + (G*T1 / T2)*(x - x_old) + Kint*(G*x + G*x_old - y_old)) / (1.0 + Kint);
        if (y > ymax)  y = ymax;
        if (y < ymin)  y = ymin;
    }
    return y;
};


// ----------------------------------------------------------------
__declspec(dllexport) int32_T __cdecl Model_Outputs(IEEE_Cigre_DLLInterface_Instance* instance) {
    /*   Calculates output equation
       Arguments: Instance specific model structure containing Inputs, Parameters and Outputs
       Return:    Integer status 0 (normal), 1 if messages are written, 2 for errors.  See IEEE_Cigre_DLLInterface_types.h
    */
    ErrorMessage[0] = '\0';

    MyModelParameters* parameters = (MyModelParameters*)instance->Parameters;
    // Retrieve variables from Input, Output and State
    double TAdTB = parameters->TAdTB;
    double TB = parameters->TB;
    double K = parameters->K;
    double TE = parameters->TE;
    double EMin = parameters->EMin;
    double EMax = parameters->EMax;
    int CSwitch = parameters->CSwitch;
    double RCdRFD = parameters->RCdRFD;
    //
    double delt = Model_Info.FixedStepBaseSampleTime;
    //
    MyModelInputs* inputs = (MyModelInputs*)instance->ExternalInputs;
    double VRef = inputs->VRef;
    double Ec = inputs->Ec;
    double Vs = inputs->Vs;
    double IFD = inputs->IFD;
    double VT = inputs->VT;
    double VUEL = inputs->VUEL;
    double VOEL = inputs->VOEL;
    //
    double OldOLeadlag = instance->DoubleStates[0];
    double OldVerr = instance->DoubleStates[1];
    double OldOControl = instance->DoubleStates[2];
    // offset needed to add to input voltage summation loop (constant)
    double VOffset = instance->DoubleStates[3];
    double S_OControl = instance->DoubleStates[4];
    double S_OLeadLag = instance->DoubleStates[5];

    MyModelOutputs* outputs = (MyModelOutputs*)instance->ExternalOutputs;
    double EFD = outputs->EFD;
    // local variables
    double Verr;
    double OLeadlag;
    double OControl;
    double OControl2;

    // Code:
    // Voltage summation loop (including initial offset from initial conditions - needed due to proportional gain control)
    Verr = VRef - Ec + Vs + VUEL + VOEL + VOffset;
    // Leadlag with no limits
    OLeadlag = LEADLAG(1.0, (TAdTB*TB), TB, Verr, OldVerr, OldOLeadlag, -1.0E10, 1.0E10, delt);
    // Real pole with limits
    OControl = REALPOLE(K, TE, OLeadlag, OldOLeadlag, OldOControl, EMin, EMax, delt);
    if (CSwitch == 1) {
        OControl2 = OControl;
    } else {
        OControl2 = OControl * VT;
    }
    // negative current logic
    if ((IFD < 0.0) && (RCdRFD > 1.0E-8)) {
        EFD = -1.0 * IFD * RCdRFD;
    } else {
        EFD = OControl2;
    }
    // hack - should final EFD be limited to EMin/EMax?

    // Outputs
    outputs->EFD = EFD;
    // save state variables
    instance->DoubleStates[0] = OLeadlag;
    instance->DoubleStates[1] = Verr;
    instance->DoubleStates[2] = OControl;
    // Note:   IN->DoubleStates[3] is VERR and is the constant Offset - do not update this (as it is set in Initialize)
    instance->DoubleStates[4] = S_OControl;
    instance->DoubleStates[5] = S_OLeadLag;
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
        printf("Model name:             %s\n", Model_Info.ModelName);
        printf("Model version:          %s\n", Model_Info.ModelVersion);
        printf("Model description:      %s\n", Model_Info.ModelDescription);
        printf("Model general info:     %s\n", Model_Info.GeneralInformation);
        printf("Model created on:       %s\n", Model_Info.ModelCreated);
        printf("Model created by:       %s\n", Model_Info.ModelCreator);
        printf("Model last modified:    %s\n", Model_Info.ModelLastModifiedDate);
        printf("Model last modified by: %s\n", Model_Info.ModelLastModifiedBy);
        printf("Model modified comment: %s\n", Model_Info.ModelModifiedComment);
        printf("Model modified history: %s\n", Model_Info.ModelModifiedHistory);
        printf("Time Step Sampling Time (sec): %0.5g\n", Model_Info.FixedStepBaseSampleTime);
        switch (Model_Info.EMT_RMS_Mode) {
            case 1:
                printf("EMT/RMS mode:           EMT\n");
                break;
            case 2:
                printf("EMT/RMS mode:           RMS\n");
                break;
            case 3:
                printf("EMT/RMS mode:           EMT and RMS\n");
                break;
            default:
                printf("EMT/RMS mode:           <not available>\n");
        }
        printf("Number of inputs:       %d\n", Model_Info.NumInputPorts);
        printf("Input description:\n");
        for (int k = 0; k < Model_Info.NumInputPorts; k++) {
            printf("  %s\n", Model_Info.InputPortsInfo[k].Name);
        }
        printf("Number of outputs:      %d\n", Model_Info.NumOutputPorts);
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

    return IEEE_Cigre_DLLInterface_Return_OK;
};
