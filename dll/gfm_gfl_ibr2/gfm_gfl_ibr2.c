/* 

This model has.
- 15 inputs (input current time can be removed) 
- 13 outputs (3 ouputs are essential, rest 1O outputs can be used for debugging) 
- 54 parameters 

This model will be compiled into a DLL, and then can be used in ANY power system 
simulation program by running the "DLLImport" tool that comes with each program 

September 21, 2023, Vishal Verma 
*/ 

#include <windows.h> 
#include <stdio.h> 
#include <math.h> 
#define PI 3.14159265 

#include "IEEE_Cigre_DLLInterface.h" 
char ErrorMessage[1000]; 

// ---------------------------------------------------------------------- 
// Structures defining inputs, outputs, parameters and program structure 
// to be called by the DLLimport Tool 
// ---------------------------------------------------------------------- 

typedef struct _MyModellnputs {
	real64_T Vta; 
	real64_T Vtb, 
	real64_T Vte, 
	real64_T Ila, 
	real64_T //b; 
	real64_T Ile; 
	real64_T 12a; 
	real64_T 12b; 
	real64_T 12c; 
	real64_T Ide: 
	real64_T VdcMPPT; 
	real64_T Pref; 
	real64_T Qref; 
	real64_T Vdc_meas; 
	real64_T currTIME; 
} MyModellnputs; 

// Define Input Signals 
IEEE_Cigre_DLLInterface_Signal InputSignals [] = {
	[0] = { 
    .Name = "Vta", 
    .Description = "A phase terminal voltage", 
    .Unit = "kV", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .Width = 1 
    }, 
  [1] = { 
    .Name = "Vtb", 
    .Description = "B phase terminal voltage", 
    .Unit = "kV", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .Width = 1 
  },
  [2] = {
    .Name = "Vtc", 
    .Description = "C phase terminal voltage", 
    .Unit = "kV", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .Width = 1 
  },
  [3] = {
    .Name = "I1a" , 
    .Description = "A phase VSC current", 
    .Unit = "kA", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .Width = 1 
  }, 
  [4] = {
    .Name = "I1b", 
    .Description "B phase VSC current", 
    .Unit = "kA", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .Width = 1 
  }, 
  [5] = {
    .Name = "Ilc", 
    .Description "C phase VSC current", 
    .Unit = "kA", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .Width = 1 
  },
  [6] = {
    .Name = "12a" , 
    .Description = "A phase current after capacitor", 
    .Unit = "kA", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .Width = 1 
  },
  [7] = {
    .Name "I2b", 
    .Description "B phase current after capacitor", 
    .Unit = "kA", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_ T, 
    .Width = 1 
  },
  [8] = {
    .Name = "I2c", 
    .Description = "C phase current after capacitor", 
    .Unit = "kA", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .Width = 1 
  }, 
  [9] = {
    .Name = "Idc", 
    .Description = "Current from Primay Power Source", 
    .Unit = "kA, 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .Width = 1 
  },
  [1O] = { 
    .Name = "VdcMPPT" , 
    .Description = "Maximum power point voltage", 
    .Unit = "kV, 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .Width = 1 
  },
  [11] = {
    .Name = "Pref" , 
    .Description = "Active power reference ", 
    .Unit = "MW", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .Width = 1 
  }, 
  [12] = { 
    .Name = "Qref" , 
    .Description = "Reactive power reference" 
    .Unit = "Mvar" , 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .Width = 1 
  },
  [13] = {
    .Name = "Vdc_meas", 
    .Description = "Measured DC Voltage", 
    .Unit = "kV", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .Width = 1 
  },
  [14] = { 
    .Name = "currTime", 
    .Description = "Current Time" , 
    .Unit = "s", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .Width = 1 
  }
}; 

typedef struct _MyModelOutputs {
  real64_T m_a; 
  real64_T m_b; 
  real64_T m_c; 
  real64_T FreqPLL; 
  real64_T Output_1; 
  real64_T Output_2; 
  real64_T Output_3; 
  real64_T Output_4; 
  real64_T Output_5; 
  real64_T Output_6; 
  real64_T Output_7; 
  real64_T Output_8; 
  real64_T Output_9; 
} MyModelOutputs; 

// Define Output Signals 
IEEE_Cigre_DLLInterface_Signal OutputSignals[] = {
  [0] = { 
    .Name = "m_a, 
    .Description = "Phase A modulating signal", 
    .Unit = "N/A", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .Width = 1 
  },
  [1] = {
    .Name = "m_b", 
    .Description = "Phase B modulating signal", 
    .Unit = "N/A", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .Width = 1 
  }, 
  [2] = {
    .Name = "m_c", 
    .Description = "Phase C modulating signal" .
    .Unit = "N/A", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .Width = 1 
  },
  [3] = {
    .Name "FreqPLL" , 
    .Description = "PLL frequency", 
    .Unit = "Hz", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .Width = 1 
  }, 
  [4] = {
    .Name = "Output_1", 
    .Description = "current flag", 
    .Unit = "N/A", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .Width = 1 
  }, 
  [5] = {
    .Name = "Output_2", 
    .Description = "Positive Current d", 
    .Unit = "N/A", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .Width = 1 
  }, 
  [6] = {
    .Name = "Output_3", 
    .Description = "Positive Current q", 
    .Unit = "N/A", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .Width = 1 
  }, 
  [7] = {
    .Name = "Output_4", 
    .Description = "Negative Current d" , 
    .Unit = "N/A", 
    .DataType = IEEE_Cigre_DLLInterface Data Type_real64_T, 
    .Width = 1 
  }, 
  [8] = {
    .Name = "Output_5", 
    .Description = "Negative Current q", 
    .Unit = "N/A", 
    .DataType = IEEE_Cigre_DLLInterface Data Type_real64_T, 
    .Width = 1 
  }, 
  [9] = {
    .Name = "Output_6", 
    .Description = "Pos Current d , 
    .Unit = "N/A", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .Width = 1 
  }, 
  [10] = {
    .Name = "Output_7", 
    .Description = "Pos Current q, 
    .Unit = "N/A", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .Width = 1 
  }, 
  [11] = {
    .Name = "Output_8", 
    .Description = "Neg Current d , 
    .Unit = "N/A", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .Width = 1 
  }, 
  [12] = {
    .Name = "Output_9 
    .Description = "Neg Current q", 
    .Unit = "N/A" 
    .DataType = IEEE_Cigre_DLLinterface_DataType_real64_T, 
    .Width = 1 
  } 
}; 

typedef struct _MyModelParam eters {
  real64_T VLLbase; 
  real64_T Sbase; 
  real64_T Tflt_v; 
  real64_T Vflt_flag; 
  real64_T Tflt_i; 
  real64_T Iflt_flag; 
  real64_T Curl_flag; 
  real64_T k_PLL; 
  real64_T KpPLL; 
  real64_T KiPLL; 
  real64_T Lim_PLL; 
  real64_T w_nom; 
  real64_T tstart_up; 
  real64_T Vdc_nom; 
  real64_T VI_flag; 
  real64_T MPPT_flag; 
  real64_T b_Vdc; 
  real64_T Kp_Vdc; 
  real64_T Ki_Vdc, 
  real64_T T_frq; 
  real64_T fdbdl; 
  real64_T fdbd2; 
  real64_T Ddn; 
  real64 T Dup; 
  real64_T Tp_droop; 
  real64_T Vdc_flag; 
  real64_T f_flag.
  real64_T Id_frz_flag; 
  real64_T Ilim_pu, 
  real64_T Vt_ref; 
  real64_T Kv_p; 
  real64_T Kv_i; 
  real64_T Qmin; 
  real64_T Qmax; 
  real64_T Kq_p; 
  real64_T Kq_i; 
  real64_T dbhv_frt; 
  real64_T dblv_frt; 
  real64_T Kqvl; 
  real64_T Qctl_CL_flag; 
  real64_T Vt_flag; 
  real64_T dbl_2; 
  real64_T dbh_2; 
  real64 T Kqv2; 
  real64_T V2_flag; 
  real64_T Ipramp_up; 
  real64_T Kcc_p; 
  real64_T Kcc_i; 
  real64_T Lim_upCC; 
  real64_T Lim_lowCC; 
  real64_T Tau_ Vff; 
  real64_T Vff_flag; 
  real64_T Lchoke; 
  real64_T IR_flag; 
} MyMode!Parameters; 

// Define Parameters 

IEEE_Cigre_DLLInterface_Parameter Parameters[] = {
  [0] = { 
    .Name = "VLLbase" , 
    .Description = "RMS L-L base voltage", 
    .Unit = "V", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .FixedValue = 0, 
    .DefaultValue.Real64_Val = 600, 
    .MinValue.Real64_Val = 0.001, 
    .MaxValue.Real64_Val = 1000.0 
  }, 
  [l] = {
    .Name = "Sbase", 
    .Description = "VA base", 
    .Unit = "VA, 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .FixedValue = 0, 
    .DefaultValue.Real64_Val = le6, 
    .MinValue.Real64_Val = 0.001, 
    .MaxValue.Real64_Val = 100000000.0 
  },
  [2] = {
    .Name = "Tflt_v", 
    .Description = "LPF time constant for voltage ", 
    .Unit = "s", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .FixedValue = 0, 
    .DefaultValue.Real64_Val = 0.00001, 
    .MinValue.Real64_Val = 0.0, 
    .MaxValue.Real64_Val= 10.0 
  },
  [3] = {
    .Name = "Vflt_flag", 
    .Description = "Flag for voltage filter", 
    .Unit = "N/A", 
    .DataType = IEEE Cigre_DLLInterface_DataType_real64_T, 
    .FixedValue = 0, 
    .DefaultValue.Real64_Val = 1, 
    .MinValue.Real64_Val = 0.0, 
    .MaxValue.Real64_Val = 1.0 
  },
  [4] = {
    .Name = "Tflt_i", 
    .Description = "LPF time constant for current" 
    .Unit = "s", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .FixedValue = 0, 
    .DefaultValue.Real64_Val = 0.00001, 
    .MinValue.Real64_Val = 0.0, 
    .MaxValue.Real64_Val = 10.0 
  },
  [5] = {
    .Name = "Iflt_flag", 
    .Description = "Flag for currrent filter", 
    .Unit = "N/A", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .FixedValue = 0, 
    .DefaultValue.Real64_Val = 1.0, 
    .MinValue.Real64_Val = 0.0, 
    .MaxValue.Real64_Val = 1.0 
  },
  [6] = {
    .Name = "Cur1_flag", 
    .Description = "Flag for current selection (1: current control before LCL, \
                    0: current control after LCL)", 
    .Unit = "N/A", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .FixedValue = 0, 
    .DefaultValue.Real64_Val = 1.0, 
    .MinValue Real64_Val = 0.0, 
    .MaxValue.Real64_Val = 1.0 
  },
  [7] = {
    .Name = "k_PLL", 
    .Description = "Damping constant for SOGI filter", 
    .Unit = "N/A" , 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .FixedValue = 0, 
    .DefaultValue.Real64_Val = 1.0, 
    .MinValue.Real64_Val = 0.0, 
    .MaxValue.Real64_Val = 1000.0 
  },
  [8] = {
    .Name = "KpPLL", 
    .Description = "Proportional gain for PLL", 
    .Unit = "pu/pu", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .FixedValue = 0, 
    .DefaultValue.Real64_Val = 25.4, 
    .MinValue Real64_Val = 0.0, 
    .MaxValue.Real64_Val = 1000.0 
  },
  [9] = {
    .Name = "KiPLL" , 
    .Description = "Integral gain for PLL", 
    .Unit = "pu/pu" , 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .FixedValue = 0, 
    .DefaultValue Real64_Val = 324, 
    .MinValue.Real64_Val = 0.001, 
    .MaxValue.Real64_Val = 1000.0 
  },
  [l0] = {
    .Name = "Lim_PLL" , 
    .Description = "Windup limit for PLL", 
    .Unit = "pu/pu", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .FixedValue = 0, 
    .DefaultValue Real64_Val = 70 0, 
    .MinValue.Real64_Val = 0.0, 
    .MaxValue.Real64_Val = 1000.0 
  },
  [l1] = {
    .Name = "w _nom" , 
    .Description = "Nominal angular frequency", 
    .Unit = "rad/s", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T,
    .FixedValue = 0, 
    .DefaultValue.Real64_Val = 2 * PI 60, 
    .MinValue.Real64_Val = 1.0, 
    .MaxValue Real64_Val = 1e8 
  },
  [l2] = {
    .Name = "tstart_up", 
    .Description = "Time for start up flag of Q and Vt closed loop ",
    .Unit = "s", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .FixedValue = 0, 
    .DefaultValue.Real64_Val = 1.9, 
    .MinValue Real64_Val = 0.0, 
    .MaxValue.Real64_Val = 1000.0 
  },
  [l3] = {
    .Name = "Vdc_nom" , 
    .Description = "Nominal DC Link Voltage", 
    .Unit = "kV" , 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .FixedValue = 0, 
    .DefaultValue Real64_Val = 1200, 
    .MinValue.Real64_Val = 0.0, 
    .MaxValue.Real64_Val = 10000.0 
  },
  [l4] = {
    .Name = "VI_flag", 
    .Description = "1: enable PPS VI characteristic, 0: constant I", 
    .Unit = "N/A", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T,
    .FixedValue = 0, 
    .DefaultValue.Real64_Val = 0.0, 
    .MinValue.Real64_Val = 0.0, 
    .MaxValue Real64_Val = 1.0 
  },
  [l5] = {
    .Name = "MPPT_flag", 
    .Description = "1: enable MPPT for Vdc*, requires VI_flag=I and Vdc_flag=1", 
    .Unit = "pu/pu", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .FixedValue = 0, 
    .DefaultValue.Real64_Val = 0.0, 
    .MinValue.Real64_Val = 0.0, 
    .MaxValue Real64_Val = 1.0 
  },
  [l6] = {
    .Name = "b_Vdc", 
    .Description = "Setpoint weight for DC voltage", 
    .Unit = "N/A" , 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .FixedValue = 0, 
    .DefaultValue.Real64_Val = 0.56, 
    .MinValue Real64_Val = 0.0, 
    .MaxValue.Real64_Val= 100.0 
  },
  [l7] = {
    .Name = "Kp_Vdc", 
    .Description = "Proportional gain for Vdc", 
    .Unit = "pu/pu", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .FixedValue = 0, 
    .DefaultValue.Real64_Val = 5.18, 
    .MinValue.Real64_Val = 0.001, 
    .MaxValue.Real64_Val = 1000.0 
  },
  [l8] = {
    .Name = "Ki_Vdc", 
    .Description = "Integral gain for Vdc", 
    .Unit = "pu/pu", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .FixedValue = 0, 
    .DefaultValue.Real64_Val = 52.91, 
    .MinValue.Real64_Val = 0.0, 
    .MaxValue.Real64_Val = 1000.0 
  },
  [l9] = {
    .Name = "T_frq", 
    .Description = "Time constant for PLL frequency", 
    .Unit = "s", 
    .DataType = IEEE_Cigre_DLLinterface DataType_real64_T,
    .FixedValue = 0, 
    .DefaultValue Real64_Val = 0.1, 
    .MinValue.Real64_Val = 0.0, 
    .MaxValue Real64_Val = 1.0 
  },
  [20] = {
    .Name = "fdbd1", 
    .Description = "Lower deadband for frequency droop control",
    .Unit = "N/A", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .FixedValue = 0, 
    .DefaultValue.Real64_Val = -0.0006, 
    .MinValue.Real64_Val = -1e8, 
    .MaxValue.Real64_Val = 0.0 
  },
  [21] = {
    .Name = "fdbd2", 
    .Description = "Upper deadband for frequency droop control", 
    .Unit = "N/A", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .FixedValue = 0, 
    .DefaultValue.Real64_Val = 0.0006, 
    .MinValue.Real64_Val = 0.0, 
    .MaxValue.Real64_Val = 1e8 
  },
  [22] = {
    .Name = "Ddn" , 
    .Description = "Inverse of droop for high frequency", 
    .Unit = "******" , 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .FixedValue = 0, 
    .DefaultValue.Real64_Val = 20.0, 
    .MinValue.Real64_Val = 0.0, 
    .MaxValue.Real64_Val = 5000.0 
  },
  [23] = {
    .Name = "Dup" , 
    .Description = "Inverse of droop for low frequency", 
    .Unit = "******" , 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .FixedValue= 0, 
    .DefaultValue.Real64_Val = 0.0, 
    .MinValue.Real64_Val = 0.0, 
    .MaxValue.Real64_Val = 100.0 
  },
  [24] = {
    .Name = "Tp_droop", 
    .Description = "Time constant for first order lag block in Pf control", 
    .Unit = "s", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .FixedValue= 0, 
    .DefaultValue.Real64_Val = 0.001, 
    .MinValue.Real64_Val = 0, 
    .MaxValue.Real64_Val = 100.0 
  },
  [25] = {
    .Name = "Vdc_flag", 
    .Description = "dc control flag (1: enable, 0: const. PQ), 
    .Unit = "N/A", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .FixedValue= 0, 
    .DefaultValue.Real64_Val = 0.0, 
    .MinValue.Rcal64_Val = 0.0, 
    .MaxValue.Real64_Val = 1.0 
  },
  [26] = {
    .Name = "f_flag", 
    .Description = "Frequency flag (1: enable frequency droop control)", 
    .Unit = "N/A", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .FixedValue = 0, 
    .DefaultValue.Real64_Val = 0.0, 
    .MinValue.Real64_Val = 0.0, 
    .MaxValue.Real64_Val = 1.0 
  },
  [27] = {
    .Name = "Id_frz_flag", 
    .Description = "freeze Id during LVRT", 
    .Unit = "N/A", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .FixedValue = 0, 
    .DefaultValue.Real64_Val = 0.0, 
    .MinValue.Real64_Val = 0 0, 
    .MaxValue.Real64_Val = 1.0 
  },
  [28] = {
    .Name = "Ilim_pu", 
    .Description = "Inverter Current limit", 
    .Unit = "pu", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .FixedValue = 0, 
    .DefaultValue Real64_Val = 1.1, 
    .MinValue.Real64_Val = -10.0, 
    .MaxValue.Real64_Val = 10.0 
  },
  [29] = {
    .Name = "Vt_ref",
    .Description = "pu reference voltage for Vt control", 
    .Unit = "pu" , 
    .DataType = IEEE_Cigre_DLLinterface_DataType_real64_T, 
    .FixedValue = 0, 
    .DefaultValue.Real64_Val = 1.01, 
    .MinValue.Real64_Val = -10.0, 
    .MaxValue.Real64_Val = 10.0 
  },
  [30] = {
    .Name = "Kv_p",
    .Description = "Proportional gain for terminal voltage PI controller", 
    .Unit = "pu", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .FixedValue = 0, 
    .DefaultValue.Real64_Val = 0.0, 
    .MinValue.Real64_Val = 0.0, 
    .MaxValue.Real64_Val = 1e8 
  },
  [31] = {
    .Name = "Kv_i", 
    .Description = "Proportional gain for terminal voltage PI controller", 
    .Unit = "pu", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .FixedValue = 0, 
    .DefaultValue.Real64_Val = 100.0, 
    .MinValue.Real64_Val = 0.0, 
    .MaxValue.Real64_Val = 1e8 
  },
  [32] = {
    .Name = "Qmin", 
    .Description = "Minimum reactive power in pu", 
    .Unit = "pu",
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .FixedValue = 0, 
    .DefaultValue.Real64_Val = -0.4, 
    .MinValue.Real64_Val = -1e8, 
    .MaxValue.Real64_Val = 1e8 
  },
  [33] = {
    .Name = "Qmax", 
    .Description = "Maximum reactive power in pu", 
    .Unit = "pu",
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .FixedValue = 0, 
    .DefaultValue.Real64_Val = 0.4, 
    .MinValue.Real64_Val = -le8, 
    .MaxValue Real64_Val = 1e8 
  },
  [34] = {
    .Name = "Kq_p".
    .Description = "Q closed-loop proportional control gain 
    .Unit = "pu" 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .FixedValue = 0, 
    .DefaultValue.Real64_Val = 0.0, 
    .MinValue.Real64_Val = 0.0, 
    .MaxValue Real64_Val = 1e8 
  },
  [35] = {
    .Name = "Kq_i", 
    .Description = "Q closed-loop integral control gain", 
    .Unit = "pu", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .FixedValue = 0, 
    .DefaultValue.Real64_Val = 40.0, 
    .MinValue Real64_Val = 0.0, 
    .MaxValue.Real64_Val = 1e8 
  },
  [36] = {
    .Name = "dbhv_frt", 
    .Description = "Dead band LVRT +ve sequence HV", 
    .Unit = "pu" 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .FixedValue = 0, 
    .DefaultValue.Real64_Val = -0.1, 
    .MinValue.Real64_Val = -le8, 
    .MaxValue.Real64_Val = 1e8 
  },
  [37] = {
    .Name = "dblv_frt", 
    .Description = "Dead band HVRT +ve sequence LV", 
    .Unit = "pu", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T,
    .FixedValue = 0, 
    .DefaultValue.Real64_Val = 0.1, 
    .MinValue.Real64_Val = -le8, 
    .MaxValue.Real64_Val = 1e8 
  },
  [38] = {
    .Name = "Kqvl" , 
    .Description = "Proportional gain for positive voltage dip", 
    .Unit = "pu", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T,
    .FixedValue = 0, 
    .DefaultValue Real64_Val = 2.0, 
    .MinValue.Real64_Val = 0.0, 
    .MaxValue Real64_Val = 1e8 
  },
  [39] = {
    .Name = "Qctl_CL_flag", 
    .Description = "1: enables closed loop Q control, 0: open loop", 
    .Unit = "N/A", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T,
    .FixedValue = 0, 
    .DefaultValue.Real64_Val = 1.0, 
    .MinValue.Real64_Val = 0.0, 
    .MaxValue.Real64_Val = 1.0 
  },
  [40] = {
    .Name = "Vt_flag", 
    .Description = "l: enable inverter term. voltage control, 0: Q control", 
    .Unit = "N/A", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T,
    .FixedValue = 0, 
    .DefaultValue.Real64_Val = 1.0 .
    .MinValue.Real64_Val = 0.0, 
    .MaxValue.Real64_Val = 1.0 
  },
  [41] = {
    .Name = "dbl_2", 
    .Description = "VRT dead band (negative)", 
    .Unit = "N/A", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T,
    .FixedValue = 0, 
    .DefaultValue.Real64_Val = -0.1, 
    .MinValue.Real64_Val = -1e8, 
    .MaxValue.Real64_Val = 0.0 
  },
  [42] = {
    .Name = "dbh_2", 
    .Description = "VRT dead band (positive)", 
    .Unit = "N/A", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .FixedValue = 0, 
    .DefaultValue.Real64_Val = 0.1, 
    .MinValue.Real64_Val = 0.0, 
    .MaxValue.Real64_Val = 1e8 
  },
  [43] = {
    .Name = "Kqv?", 
    .Description = "Proportional gain for -ve voltage deviation", 
    .Unit = "pu", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T,
    .FixedValue = 0, 
    .DefaultValue.Real64_Val = 2.0, 
    .MinValue.Real64_Val = 0.0, 
    .MaxValue.Real64_Val = 1e8 
  },
  [44] = {
    .Name = "V2_flag", 
    .Description = "1: enable V2 control during FRT", 
    .Unit = "pu" , 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T,
    .FixedValue = 0, 
    .DefaultValue.Real64_Val = 1.0, 
    .MinValue.Real64_Val = 0.0, 
    .MaxValue.Real64_Val= 1.0 
  },
  [45] = {
    .Name = "Ipramp_up", 
    .Description = "Ramp up rate for active current", 
    .Unit = "pu", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T,
    .FixedValue = 0, 
    .DefaultValue.Real64_Val = 1.0, 
    .MinValue.Real64_Val 0.0, 
    .MaxValue.Real64_Val = 1e8 
  },
  [46] = {
    .Name = "Kcc_p", 
    .Description = "Proportional gain PI controller in current controller", 
    .Unit = "pu", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .FixedValue = 0, 
    .DefaultValue.Real64_Val = 0.32325, 
    .MinValue.Real64_Val = 0.0, 
    .MaxValue.Real64_Val = 1e8 
  },
  [47] = {
    .Name = "Kcc_i", 
    .Description = "Integral gain PI controller in current controller", 
    .Unit = "pu", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T,
    .FixedValue = 0, 
    .DefaultValue.Real64_Val = 324, 
    .MinValue.Real64_Val = 0.0, 
    .MaxValue.Real64_Val = 1e8 
  },
  [48] = {
    .Name = "Lim_upCC" , 
    .Description = "Current controller's anti-windup upper limit", 
    .Unit = "pu", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .FixedValue = 0, 
    .DefaultValue.Real64_Val = 99999, 
    .MinValue.Real64_Val = 0.0, 
    .MaxValue.Real64_Val = 1e8 
  },
  [49] = {
    .Name = "Lim_lowCC", 
    .Description = "Current controller's anti-windup lower limit", 
    .Unit = "pu" , 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .FixcdValue = 0, 
    .DefaultValue.Real64_Val = -99999, 
    .MinValue.Real64_Val = -le8, 
    .MaxValue.Real64_Val = 0 
  },
  [50] = {
    .Name = "Tau_Vff", 
    .Description = "Time constant of LPF for voltage current controller", 
    .Unit = "s", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .FixedValue = 0, 
    .DefaultValue.Real64_Val = 0.0001, 
    .MinValue.Real64_Val = 0.0, 
    .MaxValue.Real64_Val = 1e8 
  },
  [51] = {
    .Name "Vff_flag", 
    .Description = "Voltage filter flag (1 enable)", 
    .Unit = "N/A", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .FixcdValue= 0, 
    .DefaultValue.Real64_Val = 0.0, 
    .MinValue.Real64_Val = 0.0, 
    .MaxValue.Real64_Val = 1e8 
  },
  [52] = {
    .Name = "Lchoke", 
    .Description = "Filter inductance", 
    .Unit = "pu" , 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .FixedValue = 0, 
    .DefaultValue.Real64_Val = 0.0001, 
    .MinValue.Real64_Val = 0.000001, 
    .MaxValue.Real64_Val = 10.0 
  },
  [53] = {
    .Name = "IR_flag", 
    .Description = "Flag", 
    .Unit = "N/A", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .FixcdValue= 0, 
    .DefaultValue.Real64_Val = 1.0, 
    .MinValue.Real64_Val = 0 0, 
    .MaxValue.Real64_Val = 1.0 
  }
};

IEEE_Cigre_DLLInterface_Model_Info Model_Info = {
  .DLLInterfaceVersion = { 1, 1, 0, 0}          // Release number of the API 
  // used during code generation 
  .ModelName = "!BR-Average-Model",             // Model name   
  .ModelVersion = "1.1.0.0",                    // Model version   
  .ModelDescription = "GFD-IBR-Average",        // Model description 
  .GeneralInformation= "General Information",   // General information
  .ModelCreated = "September 21, 2023",         // Model created on  
  .ModelCreator = "Vishal Verma",               // Model created by     
  .ModelLastModifiedDate= "September 21, 2023", // Model last modified on  
  .ModelLastModifiedBy = "Vishal Verma",        // Model last modified by 
  .ModelModifiedComment = "Version 1.1.0.0 for IEEE/Cigre DLL API", // Model modified comment 
  .ModelModifiedHistory = "First instance",     // Model modified history 
  .FixedStepBaseSampleTime = 0.00001,           // Time Step sampling time (sec)  
  // Inputs 
  .NumlnputPorts = 15,                          // Number of Input Signals 
  .InputPortslnfo = InputSignals,               // Inputs structure defined above  
  // Outputs 
  .NumOutputPorts 13,                           // Number of Output Signals 
  .OutputPortslnfo = OutputSignals,             // Outputs structure defined above 
  // Parameters 
  .NumParameters = 54,                          // Number of Parameters 
  .ParametersInfo = Parameters,                 // Parameters structure defined above
   // Number of State Variables 
  .NumlntStates = 0,                            // Number of Integer states
  .NumFloatStates = 0,                          // Number of Float states
  .NumDoubleStates = 93                         // Number of Double states
};

// Subroutines that can be called by the main power system program 

__declspec(dllexport) const IEEE_Cigre_DLLInterface_Model_Info* __cdecl Model_Getlnfo () {
// Returns Model Information 
  return &Model_Info; 
}; 

__declspcc(dllexport) int32_T __cdecl Model_ChcckParameters(IEEE_Cigre_DLLInterface_Instance instance) {
/* Checks the parameters on the given range 
   Arguments: Instance specific model structure containing Inputs , Parameters and Outputs 
   Return: Integer status O (normal), 1 if messages are written, 2 for errors.
   See IEEE_Cigre_DLLInterface types.h 
*/

// Parameter checks done by the program 
// Note - standard minimax checks should be done by the higher level GUI/ Program 
  MyModelParameters# parameters= (MyModelParameters#)instance-Parameters; 

  double VLLbase = parameters->VLLbase; 
  double Sbase = parameters->Sbase, 
  double Tflt_v = parameters->Tflt_v; 
  double Vflt_flag = parameters->Vflt_flag; 
  double Tflt_i = parameters->Tflt_i; 
  double Iflt_flag = parameters->Iflt_flag; 
  double Curl_flag = parameters->Curl_flag, 
  double k_PLL = parameters->k_FLL; 
  double KpPLL = parameters->KpPLL, 
  double KiPLL = parameters->KiPLL; 
  double Lim_PLL = parameters->Lim_PLL; 
  double w_nom = parameters->w_nom; 
  double tstart_up = parameters->tstart_up; 
  double Vdc_nom = parameters->Vdc_nom; 
  double VI_flag = parameters->VI_flag; 
  double MPPT_flag = parameters->MPPT_flag; 
  double b_Vdc = parameters->b_Vdc; 
  double Kp_Vdc = parameters->Kp_Vdc; 
  double Ki_Vdc = parameters->Ki_Vdc; 
  double T_frq = parameters->T_frq; 
  double fdbdl = parameters->fdbdl; 
  double fdbd2= parameters->fdbd2; 
  double Ddn = parameters->Ddn; 
  double Dup = parameters->Dup; 
  double Tp_droop = parameters->Tp_droop; 
  double Vdc_flag = parameters->Vdc_flag; 
  double f_flag = parameters->f_flag; 
  double Id_frz_flag = parameters->Id_frz_flag; 
  double Ilim_pu = parameters->Ilim_pu; 
  double Vt_ref = parameters->Vt_ref; 
  double Kv_p = parameters->Kv_p; 
  double Kv_i = parameters->Kv_i; 
  double Qmin = parameters->Qmin; 
  double Qmax = parameters->Qmax; 
  double Kq_p = parameters->Kq_p; 
  double Kq_i = parameters->Kq_i; 
  double dbhv_frt = parameters->dbhv_frt; 
  double dblv_frt = parameters->dblv_frt; 
  double Kqvl = parameters->Kqvl; 
  double Qctl_CL_flag = parameters->Qctl_CL_flag, 
  double Vt_flag = parameters->Vt_flag; 
  double dbl_2 = parameters->dbl_2; 
  double dbh_2 = parameters->dbh_2; 
  double Kqv2 = parameters->Kqv2; 
  double V2_flag = parameters->V2_flag; 
  double Ipramp_up = parameters->Ipramp_up; 
  double Kcc_p = parameters->Kcc_p; 
  double Kcc_i = parameters->Kcc_i; 
  double Lim_upCC = parameters->Lim_upCC; 
  double Lim_lowCC = parameters->Lim_lowCC; 
  double Tau_Vff = parameters->Tau_ Vff; 
  double Vff_flag = parameters->Vff_flag; 
  double Lchoke = parameters-Lchoke; 
  double IR_flag = parameters->IR_flag; 
  // 
  double delt = ModelInfo.FixedStepBaseSampleTime; 

  ErrorMessage[0] '\0'; 

  if ((1.0 / KiPLL) < 2.0 * delt) 
    // write error message 
    sprintf_s (ErrorMessage, sizeof(ErrorMessage), "GFL-IBR Error - Parameter KiPLL is %f , \
but has been reset to be reciprocal of 2 times the time step: %f \n", KiPLL, delt); 
    parameters->KiPLL = 1.0 / (2.0 * delt); 
  } 
  if ((1.0 / Ki_Vdc) < 2.0 * delt) { 
    // write error message 
    sprintf_s(ErrorMessage, sizeof(ErrorMessage), "GFL-IBR Error - Parameter Ki_Vdc is: %f, \
but has been reset to be reciprocal of 2 times the time step %f \n", Ki_Vdc, delt); 
    parameters->Ki_Vdc = 1.0 / (2.0 * dell); 
  } 
  if ((1.0 / Kv_i) < 2.0 * delt) { 
    // write error message 
    sprintf_s (ErrorMessage, sizeof(ErrorMessage), "GFL-IBR Error - Parameter KiP is: %f, \
but has been reset to be reciprocal of 2 times the time step: %f .\n", Kv_i, delt); 
    parameters->Kv_i = 1.0 / (2.0 * delt); 
  } 
  if ((1.0 / Kq_i) < 2.0 * delt) {
    // write error message 
    sprintf_s (ErrorMessage, sizeof(ErrorMessage), "GFL-IBR Error - Parameter KiQ is: %f, \
but has been reset to be reciprocal of 2 times the time step.%f .\n", Kq_i, delt); 
    parameters->Kq_i = 1.0 / (2.0 * delt); 
  }
  if ((1.0 / Kcc_i) < 2.0 * delt) 
    // write error message 
    sprintf_s(ErrorMessage, sizeof(ErrorMessage), "GFL-IBR Error - Parameter KiV is: %f, \
but has been reset to be reciprocal of 2 times the time step: %f .\n", Kcc_i, delt); 
    parameters->Kcc_i = 1.0 / (2.0 * delt); 
  }
  instance->LastGeneralMessage = ErrorMessage; 
  return IEEE_Cigre_DLLInterface_Return_ OK; 
}; 

// -------------------------------------------------------------------------------------------
__declspec(dllexport) int32_T __cdecl Model_Initialize(IEEE_Cigre_DLLInterface_Instance* instance) 

/* Initializes the system by resetting the internal states 
   Arguments.Instance specific model structure containing Inputs, Parameters and Outputs 
   Return: Integer status 0 (normal), 1 if messages are written, 2 for errors.
   See IEEE_Cigre_DLLInterface_types.h 
*/ 

// Note that the initial conditions for all models are determined by the main calling program 
// and are passed to this routine via the instance>Externa!Outputs vector.
// instance-External Outputs is normally the output of this routine , but in the first time step 
// the main program must set the instance EternalOutputs to initial values.

  MyModelParameters parameters= (MyModelParameters*)instance-Parameters; 

// Retrieve variables from Input, Output and State 
double VLLbase = parameters->VLLbase; 
double Sbase = parameters->Sbase; 
double Tflt_ v = parameters->Tflt_ v; 
double Vflt_flag = parameters->Vflt_flag; 
double Tflt_i = parameters->Tflt_i; 
double Iflt_flag = parameters->Iflt_flag; 
double Curl_flag = parameters->Curl_flag; 
double k_PLL = parameters->k_PLL; 
double KpPLL - parameters KpPLL; 
double KiPLL = parameters->KiPLL; 
double Lim_PLL = parameters->Lim_PLL; 
double w_nom = parameters->w_nom; 
double tstart_up = parameters->tstart_up; 
double Vdc_nom = parameters->Vdc_nom; 
double VI_flag = parameters->VI_flag; 
double MPPT_flag = parameters->MPPT_flag; 
double b_Vdc = parameters->b_Vdc; 
double Kp_Vdc = parameters->Kp_Vdc; 
double Ki_Vdc = parameters->Ki_Vdc; 
double T_frq = parameters->T_frq; 
double fdbdl - parameters fdbdl; 
double fdbd2 = parameters->fdbd2; 
double Ddn = parameters->Ddn; 
double Dup = parameters->Dup; 
double Tp_droop = parameters->Tp_droop; 
double Vdc_flag = parameters->Vdc_flag; 
double f_fl ag = parameters ->f_fl ag; 
double Id_frz_flag = parameters->Id_frz_flag; 
double Ilim_pu = parameters->Ilim_pu; 
double Vt_ref parameters»Vt_ref; 
double Kv_p = parameters->Kv_p; 
double Kv_i = parameters->Kv_i; 
double Qmin = parameters-Qmin; 
double Qmax = parameters->Qmax; 
double Kq_p = parameters Kq_p, 
double Kq_i = parameters->Kq_i; 
double dbhv_frt = parameters->dbhv_frt; 
double dblv_frt = parameters->dblv_frt; 
double Kqvl = parameters ->Kqvl; 

B-16 

double Qetl_CL_flag = parameters->Qetl_CL_flag; 
double Vt_flag = parameters->Vt_flag; 
double dbl_2 = parameters->dbl_2; 
double dbh_2 = parameters->dbh_2; 
double Kqv2 = parameters->Kqv2; 
double V2_flag = parameters->V2_flag; 
double Ipramp_up = parameters->Ipramp_up; 
double Kee_p = parameters->Kee_p; 
double Kcc_i = parameters->Kcc_i; 
double Lim_upCC = parameters Lim_upCC, 
double Lim_lowCC = parameters->Lim_lowCC; 
double Tau_ Vff = parameters->Tau_ Vff; 
double Vff_flag = parameters->Vff_flag; 
double Lchoke = parameters ->Lchoke; 
double IR_flag = parameters->IR_flag; 
double delt = Model_Info.FixedStepBaseSampleTime; 
// 

MyModelInputs inputs = (MyModelInputs)instance ExternalInputs; 

double Vta inputs->Vta;   
double Vtb inputs->Vtb;   
double Vtc inputs->Vtc;   
double Ila inputs->Ila;   
double lib inputs->Ilb;   
double Ile inputs->Ilc;   
double 12a inputs->12a;   
double I2b inputs-I2b;   
double I2c inputs->I2c;   
double Ide inputs->Idc;   
double VdcMPPT = inputs->VdcMPPT;   
double   Pref= inputs->Pref;   
double   Qref = inputs->Qref;   
double Vde meas =   inputs-> V de_meas;   
double   eurrTIME =   inputs ->currTIME;   // Working back from initial output 

M yModelOutputs outputs= (MyModelOnutputs#) instance->ExternalOutputs; 
double m_a = outputs ->m_a; 
double m_b = outputs->m_b; 
double mc = outputs m_c, 
double FreqPLL = outputs->FreqPLL; 
double Output_! = outputs->Output_l; 
double Output_2 = outputs->Output_2; 
double Output_3 = outputs->Output_3; 
double Output_ 4 = outputs output_4; 
double Output_5 = outputs->Output_5; 
double Output_6 = outputs->Output_6; 
double Output_ 7 = outputs->Output_ 7; 
double Output_8 = outputs->Output_8; 
double Output_9 = outputs->Output_9; 
ErrorMessage [0]= \0; 

// save state variables 
instance ->DoubleStates [OJ 
instanee->DoubleStates [I] 
instance ->DoubleStates[2] 
instanee->DoubleStates [3] 
instance->DoubleStates [4] 
instance ->DoubleStates [5] 
instance ->DoubleStates [6] 
instance ->DoubleStates [7] 
instance ->DoubleStates [8] 
instance -»DoubleStates[9] 
instance ->DoubleStates [I OJ 
instance->DoubleStates [11] 
instance ->DoubleStates [I 2] 
instance->DoubleStates [13] 

0 0; 
0.0; 
0.0; 
0.0; 
0.0; 
0 0; 

0.0; 
0 0; 

0.0; 
0.0; 

0.0 
0.0 
0.0 
0.0 

B-17 

instance ->DoubleStates [14 J 
instance ->DoubleStates [15J 
instance ->DoubleStates [16J 
instance->DoubleStates [1 7J 
instance ->DoubleStates [18J 
instance ->DoubleStates [19J 
instance ->DoubleStates [20J 
instance->DoubleStates [21J 
instance ->DoubleStates [22J 
instance->DoubleStates [23J 
instance ->DoubleStates [24 J 
instance ->DoubleStates [25J 
instance ->DoubleStates [26J 
instance ->DoubleStates [2 7J 
instance ->DoubleStates [28J 
instance ->DoubleStates [29J 
instance ->DoubleStates [3 OJ 
instance ->DoubleStates [31 J 
instance ->DoubleStates [3 2J 
instance ->DoubleStates [3 3 J 
instance->DoubleStates [34J 
instance ->DoubleStates [3 5J 
instance ->DoubleStates [3 6J 
instance ->DoubleStates [3 7J 
instance ->DoubleStates [3 8J 
instance ->DoubleStates [3 9J 
instance ->DoubleStates [40J 
instance->DoubleStates [41J 
instance ->DoubleStates [42J 
instance ->DoubleStates [43 J 
instance ->DoubleStates [44 J 
instance ->DoubleStates [45J 
instance ->DoubleStates [46J 
instance ->DoubleStates [4 7J 
instance ->DoubleStates [48J 
instance ->DoubleStates [49J 
instance ->DoubleStates [5 OJ 
instance ->DoubleStates [51 J 
instance ->DoubleStates [5 2J 
instance->DoubleStates [53J 
instance->DoubleStates [54J 
instance ->DoubleStates [5 5J 
instance ->DoubleStates [5 6J 
instance ->DoubleStates [5 7J 
instance ->DoubleStates [5 8J 
instance ->DoubleStates [5 9J 
instance ->DoubleStates [60J 
instance->DoubleStates [61J 
instance ->DoubleStates [62J 
instance->DoubleStates [63J 
instance -Double States [64] 
instance ->DoubleStates [65J 
instance ->DoubleStates [66J 
instance ->DoubleStates [67J 
instance ->DoubleStates [68J 
instance ->DoubleStates [69J 
instance ->DoubleStates [70J 
instance ->DoubleStates [71 J 
instance -Double States[72] 
instance->DoubleStates [73J 
instance-DoubleStates[74] 
instance->DoubleStates [75J 
instance ->DoubleStates [76J 
instance ->DoubleStates [77J 
instance ->DoubleStates [78J 
instance ->DoubleStates [79J 
instance -DoubleStates [80] 
instance->DoubleStates [81J 

0.0, 
0.0, 

0.0, 
0.0; 
0.0, 

2 * PI * 60; 
0.0; 

0.0, 

0.0; 

0.0, 

0.0; 

0.0; 

0.0, 

0.0; 

0.0, 

0.0; 

0.0, 

0.0, 

0.0; 

0.0, 

0.0; 

0.0; 

0.0; 

0.0; 

0.0, 

0.0, 

0.0, 

0.0, 

0.0; 

0.0, 

0.0; 

0.0; 

0.0, 

0.0; 

60.O; 

0.0, 

0.0, 

0.0, 

0.0; 

0.0, 

0.0; 

0.0; 

0.0, 

0.0; 

0.0, 

0.0; 

0.0, 

0.0, 

0.0; 

0.0, 

0.0; 

0.0, 

0.0, 

0.0, 

0.0, 

0.0; 

0.0; 

0.0; 

0.0; 

0.0, 

0.0; 

0.0, 

0.0, 

0.0; 

0.0, 

0.0; 

0.0; 

0.0; 

B-18 

instance DoubleStates[82] =   0.0;   
instance-DoubleStates [83]=   0.0;   
instance->DoubleSlates [84] =   0 0;   
instance->DoubleStates [85] =   0.0;   
instance->DoubleSlates [86] =   0.0;   
instance->DoubleStates [87] =   0.0;   
instance->DoubleSlates [88] =   0.0;   
instance-DonubleStates[89] =   0 0;   
instance >DoubleStates [90]=   0.0;   
instance-DonubleStates[91]=   0 0;   
instance DoubleStates[92] =   0.0;   instance >LastGeneralMessag = ErrorMessage, 
return IEEE_Cigre_DLLInterface_Return_ OK; 

}; 

// Integrator with time constant T 

double INIEGRATOR(double T, double x, double x_old, double y old, double dell) { 
double y, 

double Kint = ( delt k 0.5) 1 T; 

y = y_old + Kint (x + x_old); 

return y; 

}; 

// Integrator with time constant T and reset value rst_val 

double IN1EGRATORRESET(double T, double rst_flag, double rst val, double x, double x_old, double y_old, 
double dell) { 

double y; 

double Kint = ( delt # 0.5) / T, 

y = y_old + Kint R (x + x_old); 
if (rst_flag) { 

y = rst val; 

return y, 

}; 

// PI with gain Kand integrator with time constant T 

double PICONTROLLER(double K, double T, double x, double x_old, double y_old, double dell) { 
double y; 
double Kint = ( delt # 0.5) / T; 
y = y_old + K * (x - x_old) + Kint * (x + x_old); 
return y, 
}; 

// first order lag with gain G, time constant T, with non-windup internal limits 

double REALPOLE(double G, double T, double x, double x_old, double y_old, double ymin, double ymax, double dell) { 
double y; 
double Kint= (dell * 0.5) T; 
y = (y_old + Kint * (G * x + G * x_old - y_old)) I (1.0 + Kint); 
if (y > ymax) y = ymax; 
if y < ymin) y = ymin; 
return y; 
}; 

// second order complex pole with gain G, time constant T, damping B.Only first state represented as C junction 
double CMPLXPOLE(double G, double T, double B, double x, double x_old, double yp_old, double y_old, 

double dell) { 

double yp; 
double Kint 

( delt # 0.5) / T, 

B-19 

yp = ((1 - Kint * B - Kint * Kint) * yp_old + Kint * (G * x + G * x_old - 2 * y_old)) 
/ (I + Kint * B + Kint * Kint); 

// In main code, use yp to evaluate integration of final output y 
return yp; 

}; 

// first order differential pole with gain G, time constant T Total numerator gain is GT 
double DIFFPOLE(double G, double T, double x, double x_old, double y_old, double dell) { 
double y; 

double Kint = (dell * 0.5) / T; 

y = (G * (x - x old) + (1 - Kint) * y_old) / (1 + Kint); 
return y; 

}; 

// first order leadlag with gain G, lead time constant Tl, lag time constant T2, with non windup internal limits 
double LEADLAG(double G, double Tl, double T2, double x, double x_old, double y_old, double ymin, double ymax, 
double dell) { 

double y; 
double Kint = (dell * 0.5) / T2; 
if (Tl < l .0E-8) { 
y - REALPOLE(G, T2, x, x old, y_old, ymin, ymax, delt): 
else 
y = (y_old + (G * Tl / T2) * (x - x_old) + Kint * (G * x + G * x_old - y_old)) I (1.0 + Kint); 
if (y > ymax) y = ymax, 
if (y < ymin) y - ymin; 

return y; 

}; 

// rectangular to polar transformation 

void RECTANGULAR2POLAR(double real, double imag, double# mag, double# ang) { 
mag= sqrt(pow(real, 2) + pow(imag, 2)); 
ang atan(imag, real); 
}; 

// polar to rectangular transformation 

void POLAR2RECTANGULAR(double mag, double ang, double real, double imag) { 
;real = mag k cosfang ), 

imag mag sin fang ); 
}; 

// comparatror to compare two inputs 

double COMPARATOR(double input_A, double input_B) 
return ((input_A > input_B) ? 1 O); 
}; 

// limiter to limit the output within bounds 

double LIMITER(double upper_limit, double lower limit, double <lat) { 
if (dat > upper_limit) 
return upper_limit; 
if (dat < lower_limit) 
return lower_limit; 
return <lat, 
}; 

// selector selects a input based on flag condition , input_A if FLAG is true 
double SELECTOR(double input_A, double input_B, double FLAG) { 

return (FLAG ? input_ A 

input_B ); 

}; 

B-20 

// sample and hold block to hold the output to its last value if a flag is provided 
void SAMPLEHOLD(double signal_in , double FLAG, double FLAG OLD, double sample_hold) 

// sample_hold[O} = output ( signal_out) 

llsample_hold[J} = hold value (signal_hold) 
if (FLAG_OLD == 1 && FLAG= 1) { 
sample_hold [OJ = sample_hold [l]; 
sample_hold [l J = sample_hold [l]; 
else 
s amp I e_hold [OJ 
sample_hold [1 J 
); 

signal_in, 
signal_in: 

// for DB block 

double DB(double signal_in, double f_dbdl, double f_dbd2) { 

double sum! = (signal_in - f_dbd2) * CDMPARATOR(signal_in, f_dbd2); 
double sum2 = (signal_in - f_dbdl) * CDMPARATOR(f_dbdl, signal_in ); 
return (sum! + sum2); 

); 

// deadband, no output is generated if input lies within the deadband range .

double DEADBAND(double signal_in, double db_range, double db_gain, double db offest) 
if (fabs(signal_in) > db_range / 2.0) 

return (signal_in > 0 ? db_offest + db_gain * (signal_in - db_range / 2.0) : 
db_offest + db_gain * (signal_in + db_range / 2.0)); 

else 

return 0; 

); 

// rate limiter to limit the rate of change of output 

double RATEL!l\://TER(double f_input, double Oldf_output, double rate_up, double rate_down, double dell) { 
double rate = (f_input - Oldf_output) / delt; 

if (rate > rate_up) 

return ( rate_up * delt + Oldf_output); 
if (rate < -rate_down) 

return (-rate_down * dell + Oldf_output ); 
return f_input; 

); 

// to convert DQ quantities to ABC 

void DQ2ABC(double fd, double fq, double phi, double fabc) { 

fabc [0] 
fabc[1] 
fabe[2] 
(fd * cos(ph) - fq * sin(phi)); 
(fd * cos(ph - (2.0 * PI / 3 0)) 
(fd * cos(ph + (2.0 * PI 1 3.0)) 
fq * sin(phi - (2.0 * PI 
fq * sin(phi + (2.0 PI 
3 0))); 
3 0))); 
); 

// to convert ABC quantities to Alpha-Beta 

void ABC2ALPHABETA double fa, double fb, double fc, double alpha_beta) { 
alpha_beta [0]= (fa 0.5 * fb - 0.5 * fc) * 2 / 3; 
alpha_beta[1] (fb * sqrt(3.0) I 2 - fc * sqrt (3.0) I 2.0) * 2.0 I 3.0; 
); 

// to convert ABC to DQ 

void ABC2DQ(double fa, double fb, double fc, double phi, double# DDQ) { 
fDQ[0]= 2.0 / 3.0 ¥ (cos(phi) k fa cos(phi (2.0 PI / 3.0)) fb 
+ cos(phi + (2.0 * PI / 3.0)) * fc); 
fDQ[l] = 2.0 / 3.0 * (-sin (phi) * fa - sin(phi - (2.0 * PI / 3.0)) * fb 
- sin(phi + (2.0 * PI / 3.0)) * fc); 
); 

// to convert alpha beta to DQ 

void ALPHABETA2DQ(double falpha, double feta , double theta , double# DDQ) { 
fDQ[0J = falpha * cos(theta) + fbeta * sin(theta); 
fDQ[l] = -falpha sin(theta) + fbeta k cos(theta ), 

B-21 

}; 

// to calculate mod of 2 float numbers 

double MCDULO(double signal_in , double den) { 
double y; 
y = signal_iu - floor(signal_iu / den) den; 
return y; 
); 

// real power using alpha beta 

double REALPOWER(double v_alpha, double i_alpha, double v_beta, double i_beta) 
double y; 
y = v_alpha * i_alpha + v_beta * i_beta, 
return y; 
}; 

// reactive power using alpha beta 

double REACTIVEPOWER(double v_alpha, double i_alpha, double v_beta, double i_beta) 
double y; 
y = v_alpha i_beta + v_beta i_ alpha; 
return y; 
}; 

//---------------------------------------------------------------- 

__declspec(dllexport) int32_T __cdccl Model_Outputs(IEEE _Cigre_DLLInterface_Instance instance) 

/* Calculates output equation 
Arguments: Instance specific model structure containing Inputs, Parameters and Outputs 
Return.· Integer status 0 (normal), l if messages are written, 2 for errors.
See IEEE_Cigre_DLLInterface_types.h 
*/ 

Error Message [0]= '0'; 

My Mode/Parameters parameters = (MyMode!Parameters)instance>Parameters; 
l Retrieve variables from Input, Output and State 

double VLLbase = parameters ->VLLbase; 
double Sbase = parameters->Sbase; 
double Tflt_v = parameters->Tflt_v, 
double Vflt_flag = parameters->Vflt_flag; 
double Tflt_i - parameters Tflt_i, 
double Iflt_flag = parameters->Iflt_flag; 
double Curl_flag = parameters->Curl_flag; 
double k_PLL = parameters->k_PLL; 
double KpPLL = parameters->KpPLL; 
double KiPLL = parameters->KiPLL; 
double Lim_PLL = parameters ->Lim_PLL; 
double w_nom = parameters->w_nom; 
double tstart_up = parameters->tstart_up; 
double Vdc_nom = parameters->Vdc_nom; 
double Vl_flag = parameters->Vl_flag; 
double MPPT_flag = parameters->MPPT_flag; 
double b_Vdc = parameters->b_ Vdc; 
double Kp_Vdc = parameters->Kp_Vdc; 
double Ki_Vdc = parameters->Ki_Vdc; 
double T_frq = parameters->T_frq; 
double fdbdl = parameters->fdbdl; 
double fdbd2 = parameters->fdbd2; 
double Ddn = parameters->Ddn; 
double Dup = parameters->Dup; 
double Tp_droop = parameters->Tp_droop; 
double Vdc_flag = parameters->Vdc_flag; 
double f_flag = parameters->f_flag, 
double Id_frz_flag = parameters->Id_frz_flag; 
double Ilim_pu = parameters ->Ilim_pu; 

B-22 

double Vt_ref = parameters->Vt_ref; 
double Kv_p = parameters->Kv_p; 
double Kv_i = parameters->Kv_i; 
double Qmin = parameters->Qmin; 
double Qmax = parameters->Qmax; 
double Kq_p = parameters->Kq_p; 
double Kq_i = parameters ->Kq_i; 
double dbhv_frt parameters-dbhv frt; 
double dblv_frt = parameters->dblv_frt; 
double Kqvl = parameters ->Kqvl; 
double Qctl_CL_flag = parameters->Qctl_CL_flag; 
double Vt_flag = parameters->Vt_flag; 
double dbl_2 = parameters->dbl_2; 
double dbh_2 = parameters->dbh_2; 
double Kqv2 = parameters->Kqv2; 
double V2_flag = parameters->V2_flag; 
double Ipramp_up = parameters->Ipramp_up; 
double Kcc_p = parameters->Kcc_p; 
double Kcc_i = parameters->Kcc_i; 
double Lim_upCC = parameters-Lim_upCC; 
double Lim_lowCC = parameters->Lim_lowCC; 
double Tau_ Vff = parameters->Tau_ Vff; 
double Vff_flag = parameters->Vff_flag, 
double Lchoke= parameters >Lchoke; 
double IR_flag = parameters->IR_flag; 

// 

double delt = Model_Info.FixedStepBaseSampleTime; 
// 

MyModelInputsx inputs = (MyModelInputs)instance >ExternalInputs; 
double Vta = inputs->Vta; 
double Vtb = inputs->Vtb; 
double Vtc = inputs->Vtc; 
double Ila= inputs->Ila; 
double lib = inputs->Ilb; 
double Ile= inputs->Ilc; 
double 12a = inputs->l2a; 
double I2b = inputs->l2b; 
double 12c = inputs->l2c; 
double Ide = inputs->Idc; 
double VdcMPPT = inputs->VdcMPPT; 
double Pref = inputs->Pref; 
double Qref = inputs->Qref; 
double Vdc meas = inputs->Vdc_meas; 
double currTIME = inputs ->currTIME; 
// 

double OldTIME = instance->DoubleStates [0]; 
// Signal Processing block 

double OldVta_pu = instance->DoubleStates [I];   
double OldVta_fltl = instance ->DoubleStates [2];   
double OldVtb_pu = instance->DoubleStates [3];   
double OldVtb_fltl = instance->DoubleStates [4].
double OldVtc_pu = instance->DoubleStates [5];   
double   OldVtc fill   = instance->DoubleStates [6];   
double   OldI1a_pu= instance >DoubleStates[7];   
double   Oldlla_fltl = instance->DoubleStates [8];   
double   Oldllb_pu = instance->DoubleStates [9];   
double   Oldllb flt!   = instance->DoubleStates [IO];   
double   Oldllc_pu = instance->DoubleStates [11];   
double   Oldllc_fltl = instance >DoubleStates[12]   
double   OldI2a_pu = instance->DoubleStates [I 3];   
double   Oldl2a_fltl = instance->DoubleStates [14];   
double   OldI2b_pu= instance-DoubleStates [15];   
double   Oldl2b_fltl = instance->DoubleStates [16];   
double   Oldl2c_pu = instance->DoubleStates [17];   
double OldI2c_fltl = instance->DoubleStates [18];   
double OldOmega_PLL -= instance >Double$States [19],   
double   OldVt_alpha = instance->DoubleStates [20];   
double   OldVt_alpha_pr = instance->DoubleStates [21];   B-23 

double OldVt_qalpha_pr = instance->DoubleStates [22]; 
double OldVt_beta = instance-doubleStates [23], 
double OldVt_beta_pr = instance->DoubleStates [24], 
double OldVt_qbeta_pr = instance->DoubleStates [25]; 
double OldTheta_PLL = instance-DoubleStates [26]; 
double OldDelOmegaAWerr = instance->DoubleStates [2 7]; 
double OldDelomegalin instance-DoubleStates[28], 
double OldDelOmegal = instance->DoubleStates [29]; 
double OldTheta_DSOGIPLLcont = instance-DoubleStates [30]; 
double Oldldl_ref = instance->DoubleStates [31], 
double OldOldldl_ref = instance->DoubleStates [32]; 
double Old!dlr_flt = instance->DoubleStates[33]; 
double Oldlql_ref = instance->DoubleStates [34]; 
double Oldoldlq1_ref instance-Doble$States [35]; 
double Oldlqlr_flt = instance->DoubleStates[36]; 
double Old!d2_ref = instance ->DoubleStates [3 7]; 
double OldOldl d2_ref = instance ->Doub leStates [3 8], 
double Old!d2r_flt = instance->DoubleStates[39]; 
double Oldlq?_ref instance-doubleStates [40], 
double Oldoldlq2_ref= instance >Double~States [41]; 
double Oldlq2r_flt = instance->DoubleStates[42]; 

// P, Q control block 

double Oldldl_FFin = instance->DoubleStates[43]; 
double Old!dl_FFnolimit = instance->DoubleStates [44]; 
double Oldldl_VdcAWerr = instance->DoubleStates [45]; 
double Old!dl_Vdclin = instance->DoubleStates [46]; 
double Oldldl_ Vdcl = instance ->DoubleStates [ 4 7]; 
double Oldf PLL = instance->DoubleStates [48]; 
double Oldfpu_flt = instance->DoubleStates [49]; 
double OldVtd_l_y2 = instance ->DoubleStates [5 0]; 
double OldVtd_l_y = instance ->DoubleStates [5 l]; 
double Oldldref_droop_x = instance->DoubleStates [52]; 
double Oldldrcf_droop= instance >Double$States[53]; 
double OldId1ref_hold = instance-DoubleStates[54]; 
double Oldlq_VtdCLAWerr = instance->DoubleStates [55]; 
double Oldlq_VtdCL//n = instance-DoubleStates[56]; 
double Oldlq_ VtdCLI = instance ->DoubleStates [5 7]; 
double OldQdq_x = instance >DoubleStates [58]; 
double OldQdq = instance->DoubleStates [59]; 
double Oldlq_QCLAWerr= instance-DoubleStates[60]; 
double Oldlq_QCL!in = instance->DoubleStates [61]; 
double Oldlq_QCLI = instance->DoubleStates [62], 
double OldVdql = instance->DoubleStates [63]; 
double OldVdql_y = instance->DoubleStates [64], 
double Oldlql_i = instance->DoubleStates[65]; 

// Current Control 

double Oldldref_l = instance ->DoubleStates [66]; 
double Olductrld_lAWerr = instance->DoubleStates [67]; 
double Olductrld_1//n = instance >Doubl€States[68]; 
double Olductrld_ll = instance->DoubleStates [69]; 
double Oldlqref_l = instance ->DoubleStates [70]; 
double Olductrlq_lAWerr = instance->DoubleStates [71]; 
double Oldnuctrlq_//in instance-DoubleStates[72]; 
double Olductrlq_ll = instance->DoubleStates [73]; 
double Oldldref_2 = instance ->DoubleStates [74]; 
double Olductrld_2AWerr = instance->DoubleStates [75]; 
double Olductrld_2//n= instance DoubleStates[76], 
double Olductrld_21 = instance->DoubleStates [77]; 
double Oldlqref_2 = instance ->DoubleStates [78]; 
double Olductrlq_2AWerr = instance->DoubleStates [79]; 
double Olductrlq_2//n = instance->DoubleStates[80], 
double Olductrlq_21 = instance >DoubleStates [81]; 
double OldVtd_l = instance->DoubleStates [82]; 
double OldVtd_ly = instance ->DoubleStates [83]; 
double OldVtq_l = instance ->DoubleStates [84]; 
double OldVtq_ly = instance ->DoubleStates [85]; 

B-24 

double OldVtd_2 = instance->DoubleStates [86]; 
double OldVtd_2y = instance->DoubleStates [87]; 
double OldVtq_2 = instance->DoubleStates [88]; 
double OldVtq_2y = instance->DoubleStates [89]; 

// Flags for SH 

double OldFRT_flag = instance->DoubleStates [90]; 

// Added states for SH 

double Oldldlref_hold_SH = instance->DoubleStates [91], 
double OldIql_i_SH = instance >DoubleStates[92] 

MyModelOutputs« outputs = (MyModeloutputsw)instance >External Outputs; 
double ma outputs-m_a, 
double m_b = outputs ->m_b, 
double m_c = outputs->m_c; 
double FreqPLL = outputs->FreqPLL, 
double Output_! = outputs->Output_l; 
double Output_2 = outputs->Output_2; 
double Output_3 = outputs->Output_3; 
double Output_ 4 = outputs->Output_ 4; 
double Output_5 = outputs->Output_5; 
double Output_6 = outputs->Output_6; 
double Output_7 = outputs->Output_7; 
double Output_8 = outputs->Output_8; 
double Output_9 = outputs->Output_9; 

// local variables 

// double currTIME; removed on 3/14 
// Signal Processing block 

double Vdq_base; 
double Idq_base, 
double Vta_pu, Vtb_pu, Vtc_pu; 
double Ila_pu, Ilb_pu, Ilc_pu, 
double 12a_pu, l2b_pu, l2c_pu; 
double Vta_fltl Vtb_fltl Vtc_fltl; 
double Ila_fltl, Ilb_fltl, Ilc_fltl; 
double 12a_fltl , 12b_fltl , 12c_fltl; 
double Vta_flt, Vtb_flt, Vtc_flt; 
double Ila_flt, Ilb_flt, Ilc_flt; 
double l2a_flt, l2b_flt, l2c_flt; 
double la_flt, Ib_flt, lc_flt; 
double Vt_alphabeta[2], Vt_alpha, Vt_beta; 
double Vt_alpha_pr, Vt_qalpha_pr; 
double Vt_beta_pr, Vt_qbeta_pr; 
double Vt_alpha_pos, Vt_beta_pos; 
double Vt_alpha_neg, Vt_beta_neg; 
double Vtdq_I [2], Vtd_I, Vtq_I; 
double Vtdq_2 [2], Vtd_2, Vtq_2; 
double DelOmegaP, Delomegalin, Delomegal , DelomegaAW, Del Omega, DelOmegaAWerr, Omega_PLL; 
double Theta_DSOGIPLLcont, Theta_PLL; 
double Idlr_flt, Iqlr_flt, Id2r_flt, Iq2r_flt; 
double Idql_flt [2], Idq2_flt [2]; 
double Id_I , Iq_I , Id_2, Iq_2; 
double Il_alphabeta [2], 12_alphabeta [2]; 
double Piab pu, Qiab _pu, Ptab pu, Qtab _pu; 
// P, Q block 
double Vdql, 
double FR T _flag; 
double Startup_flag; 
double Idl_FFnolimit, Idl_FFin, Idl_FF; 
double Vdc_ref; 
double Idl_VdcP, Idl_Vdclin, Idl_Vdcl, Id! Vdc, Idl_VdcAW, Idl_VdcAWerr, Idlref_Vdc; 
double fpu_flt; 
double f_PLL; 
double Droop_down, Droop_up; 
double Pref_droop; 
double Vtd_l_y, Vtd_l_y2 = O; 

B-25 

double ldref_droop_x, ldref_droop; 
double ldlref_P; 
double ld_droopl, ld_droop, 
double Idlref_cont, Idlref_hold, Idlref_nolimit, Idlref, Idlref_hold_SH [2]; 
double Iq_VtdCLe, Iq_ VtdCLP, Iq_ VtdCL//n, Iq_VtdCLI, Iq VtdCLAW, Iq_VtdCL, Iq_ VtdCLAWerr; 
double Qdq_x, Qdq; 
double lq_ QCLe, Iq _QCLP, Iq_QCL//n, IA_QCLI, Iq QCLAW, Iq QCL, IA QCLAWerr; 
double lq_QOL, 
double Vdql_y; 
double Iql_frt; 
double lq_Qctl; 
double lql_icont, lql_i, Iql_i_SH [2]; 
double Iqlref; 
double Vdq_2mag, Vdq_2ang; 
double Idq2_refmag, Idq2_refang, 
double Id2ref, Iq2ref; 
double 12m_ref_upper; 
double 12m_refmag, lq2ref_Lang; 
double llm_ref, 12m_ref; 
double llim_L; 
double IROL_flag, 
double scale, scale_phmax; 
double 12m_ref_L, 
double ldlref_L, Iqlref_L, ld2ref_L, lq2ref_L, ldlmax_FRT; 
double Magldql, Magldq2, Angldq_12; 
double Ia_max, Ib_max, Ic_max , lph_max, Ilim_phmax; 
double IOL_flag; 
double Magldqref_l_L, Angldqref_l_L, Magldqref_2_L, Angldqref_2_L; 
double Id1ref_L2, Iqlref_L2, Id2ref_L2, Iq2ref_L2: 
double Idlref_max, Idlref_Ll, lqlref_Ll; 
double ldref_l, Iqref_l, Idref_2, Iqref_2; 

// Current Control 

double t_release.
double current_control; 
double Iramp_up; 
double ldl_ref, Iql_ref, Id2_ref, Iq2_ref; 
double Idl_e, Iql_e, Id2_e, Iq2_e; 
double uctrld IP uctrld !Jin uctrld // 

- - - 

double uctrlq_lP uctrlq_llin uctrlq_ll 
double uctrld 2P uctrld 2//n uctrld 21 

- - - 

double uctrlq_2P uctrlq_21in uctrlq_21 
double Vtd_ly, Vtq_ly, Vtd_2y, Vtq_2y; 
double Ed_!, Eq_l, Ed_2, Eq_2; 
double Eab_I[3], Eabc_2 [3]; 
double Ea_m, Eb_m, Ec_m; 
uctrld_lAW, 
uctrlq_lAW, 
uctrld_2AW, 
uctrlq_2AW, 
uctrld_lAWerr, 
uctrlq_lAWerr, 
uctrld_2AWerr, 
uctrlq_2AWerr, 
uctrld_I; 
uctrlq_1.
uctrld_2; 
uctrlq_2, 

/k Signal   Processing Block   ±'           
// Per   unit   conversion             
Vdq_base = VLLbase * sqrt (2 0   I   3.0);       
Idq_base (Sbase   / VLLbase) * sqrt(2.0   I   3.0);   
Vta_pu = Via   Vdq_base * 1000;         
Vtb_pu = Vtb   Vdq_base * 1000;         
Vtc_pu = Vtc   Vdq_base * 1000;         
Ila_pu = Ila   Idq_base * 1000;         
Ilb_pu = Ilb   Idq_base * 1000;         
Ilc_pu = Ile   Idq_base * 1000;         B-26 
I2a_pu 
12b_p 
I2c_pu 
I2a 
I2b 
I2c 
Idq_base * 1000; 
Idq_base * 1000; 
Idq_base * 1000; 

// Voltage Filtering 

Vta flt! = REALPOLE(l, Tflt_v, Vta_pu, OldVta_pu, OldVta_fltl, -le8, le8, dell); 
Vta_flt = SELECTOR(Vta_fltl, Vta_pu, Vflt_flag ); 
Vtb_fltl =REALPOLE(l, TFIt_V, Vtb_pu, OIdVtb_pu, OIdVtb_flt1, -1e8, 1e8, delt ): 
Vtb_flt = SELECTOR(Vtb_fltl, Vtb_pu, Vflt_flag ); 
Vtc_f// = REALPOLE(I, TfIt_V, VIC_Pu, OIdVtc_pu, OldVtc_f//, Ie8, Ie8, delt); 
Vtc flt = SELECTOR(Vtc flt!, Vtc_pu, Vflt_flag ); 

// Current Filtering 

Ila flt! = REALPOLE(l, TFIt_i, Ila_pu, OldI1a_pu, OldI1a_fIt1, 1e8, 1e8, delt ): 
Ila_flt = SELECTOR(Ila_fltl, Ila_pu, Iflt_flag ); 

//b_fItI= REALPOLE(I, TfIt_i, //b_pu, OldHIb_pu, Old//b_fItI,-Ie8, 1e8, delt); 
// b _flt = SELECTOR( // b _flt 1.// b _pu, I flt_ flag ) ; 

//c_//I= REALPOLEI, TRI_i , //€_pu, OId//c_Pu, Old//c_f//, le8, 1e8, delt); 
// c _flt = SELECTOR( // c _ fl t1, Ilc_pu, I flt_ flag ) , 

I2a_flt! - REALPOLEI, TTI_i, I2a pu.Old[2a_pu, OldI2a_fItl, le8.1e8.delt); 
I2a_flt = SELECTOR(l2a_fltl, I2a_pu, Iflt_flag ), 
I2b_fIt1= REALPOLE(I, TRIt_i, I2b_pu, Old12b_pu, Old12b_fIt1, -1e8, 1e8, delt ): 
I2b_flt = SELECTOR(l2b_fltl, I2b_pu, Iflt_flag ); 
I2c_fItI= REALPOLEI, TfIL_i, I2c_p, OldI2e_pu, OldI2c_flt1, 1e8, 1e8, delt); 
I2c_flt = SELECTOR(l2c_fltl, I2c_pu, Iflt_flag ); 
I a flt 
lb flt 
I c flt 

SELECTOR(Ila_flt, I2a_flt, Curl_flag); 
SELECTOR(Ilb_flt, I2b_flt, Curl_flag); 
SELECTOR(Ilc_flt, I2c_flt, Curl_flag); 

// DSOGI PLL 

// Alpha beta transformation 

ABC2ALPHABETA(Vta_flt, Vtb_flt, Vtc_flt, Vt_alphabeta); 

Vt_alpha = Vt_alphabeta [OJ; 
Vt_beta = Vt_alphabeta [1], 

// DSOGI block 

// Alpha SOGI 

Vt_alpha_pr = CMPLXPOLE(k_PLL, I / OldOmega_PLL, k_PLL, Vt_alpha, OldVt_alpha, 
OldVt_alpha_pr, OldVt_qalpha_pr, dell); 

B-27 

Vl_qalpha_pr = INTEGRATOR(! I OldOmega_PLL, Vt_alpha_pr, OldVt_alpha_pr, OldVt_qalpha_pr, delt); 
// Beta SOGI 

Vl_beta_pr = CMPLXPOLE(k PLL, 
I OldOmega_PLL, k_PLL, Vl_beta, OldVt_beta, 
OldVt_beta_pr, OldVt_qbeta_pr, delt ); 
Vt_qbeta_pr = INTEGRATOR(I ' Oldomega_PLL, Vt_beta_pr, OldVt_beta_pr, OldVt_qbeta_pr, delt); 

// Positive Sequence Extraction 

Vt_alpha_pos = ( Vt_alpha_pr - Vt_qbeta_pr) 0 .5; 
Vt_beta_pos= (Vt_qalpha_pr + Vt_beta_pr) 0.5; 

/ Negative Sequence Extraction 
Vt_alpha_neg = ( Vt_alpha_pr + Vt_qbeta_pr) * 0 .5, 
Vl_beta_neg = (-Vt_qalpha_pr + Vt_beta_pr) * 0 5; 
// ALPHA-BETA to LQ Block 

ALPHABETA2DQ(Vt_alpha_pos, Vt_bela_pos, OldTheta_PLL, Vtdq_l ); 
Vtd 1 
Vtq_l 
Vtdq_l [ 0]; // Output #I 
Vtdq_l [ l]; // Output #2 

// ALPHA-BETA to LQ Block 

ALPHABETA2DQ(Vt_alpha_neg, Vt_beta_neg, -OldTheta_PLL, Vtdq_2), 
Vtd 2 
Vtq_2 
Vtdq_2 [0]; // Output #3 
Vtdq_2[1]; // Output #4 
/ Anti Wind Up Code Begin w! 

DelOmegaP = vtq_1 KpPLL; // Proportional term 
DelOmegalin = (Vtq_l - OldDelOmegaAWerr) KiPLL; 

// Input lo Integral Controller 

Del Omega! = INTEGRATORRESET(1, 0, 0, DelOmegalin, OldDelOmegalin, OldDelOmegal, de It); 
DelOmegaAW = DelOmegaP + Del Omega!; 
DelOmega = LIMITER(Lim_PLL, -Lim_PLL, DelOmegaAW); 
DelOmegaAWerr = DelOmegaAW - DelOmega; 
/ Anti Wind Up Code Ends w 
Omega_PLL = w_nom + Del Omega; // Output #5 

// Update DelOmegaAWerr for next time step 

Thela_DSOGIPLLcont = INTEGRATOR(!, Omega_PLL, OldOmega_PLL, OldThela_DSOGIPLLconl, delt); 
Thela_PLL - MODULO Theta_DSOGIPLL cont, 2 PI); 

/1 Since only DSOGI is used, Output ##6 

// Currents block of Signal and Processing (DDSRF approach)         
// Inputs :   Ta_fit   Ib_jlt,   Ic_jlt,   Iref (Idql2ref)         
Id 1 r flt = REALPOLE(l ,   1.0   3142.0,   O1dId1_ref ,   OldOldldl ref,   Oldldlr_flt, -le8,   1e8,   de It);   
I q 1 r _flt = REALPOLE(l ,   1.0   3142.0,   01 di ql _ref,   OldOldlql_ref,   Oldlqlr_flt, -le8,   1e8,   de It);   
Id 2r flt = REALPOLE(l ,   1.0   3142.0,   Oldld2_ref,   OldOldld2_ref,   Oldld2r_flt, -le8,   1e8,   de It);   B-28 
Iq2r _flt = REALPOLE(l, I 0 / 3142.0, Oldlq2_ref, OldOldlq2_ref, Oldlq2r_flt, -le8, le8, dell); 
// ABC2DQ conversion 

ABC2DQ(Ia_fIt,   Ib_flt ,   I c_fl t ,   Theta_PLL,   Idql _flt);     
ABC2DQ(Ia_fIt_.Ib_flt ,   lc_flt, -Theta_PLL, Idq2_flt );     
// Decoupling             
Id I = Idql_flt [OJ   Id2r flt R cos(Theta PLL 4 2)   Iq2r_flt # sin(Theta PLL # 2)   
Iq_l = Idq1_flt[I] + Id2r flt w sin(Theta PLL # 2)   I q 2 r flt cos (Theta PL L * 2);   
Id 2 = Idq2_flt [OJ   Idlr flt R cos(Theta PLL 2) + Iqlr flt sin(Theta PLL # 2)   
Iq_2 = Idq2_flt [IJ   Idlr flt k sin(Theta PLL % 2)   Iqlr_flt cos(Theta PLL k 2),   // Power Calculations 

// ABC to ALPHA-BETA.values used from DSOGI calculations 
// ABC to ALPHA-BETA currents 

ABC2ALPHABETA(Ila_flt, Ilb_flt, Ilc_flt, Il_alphabeta); 
ABC2ALPHABETA(I2a_flt, I2b_flt, I2c_flt, I2_alphabeta); 
Piab_pu = REALPOWER.(Vt_alpha, Il_alphabeta[0], Vt_beta, Il_alphabeta[l]); 
Qiab_pu = REACTIVEPOWER(Vt_alpha, Il_alphabeta [OJ, Vt_beta, Il_alphabeta [I]); 
Ptab_pu =REALPOWER.(Vt_alpha, 12_alphabeta[0J, Vt_beta, 12_alphabeta[l]); 
Qtab_pu = REACTIVEPOWER(Vt_alpha, I2_alphabeta [OJ, Vt_beta, 12_alphabeta [I]); 
/ Outer P,Q LOOP l 

Vdql = sqrt(Vtd_l * Vtd I + Vtq_l * Vtq_l), 

// Input Flag to Current Controller, Vdip logic 

FRT_flag = (COMPARATOR((Vt ref - Vtd 1), dblv frt) + COMPARATOR(dbhv frt, (Vt ref - Vtd !))) > 0; 
// Start UP Flag 

Startup_flag 

CDMPARATOR(tstart_up, currTIME); 

Id! FFin = 2.0 / 3.0 Vdc_nom k Ide sw 1000; 
Idl_FFnolimit = REALPOLE(l, 0.005, Idl_FFin, Oldidl_FFin, Oldidl_FFnolimit, -999999, 999999, delt), 
Idl_FF = LIMITER(Idq_base Ilim_pu, -Idq_base Ilim_pu.Idl_FFnolimit / Vdq_base); 
Vdc ref= SELECTOR(VdcMPPT, Vdc_nom, (VI_flag * MPPT_flag)); 

/ Anti Wind Up Code Begin 

Idl VdcP = (Vde ref b Vdc Vde meas k 1000) Kp Vde; / Proportional term 
Id! Vdc//n = (Vdc ref Vdc meas * 1000 - Oldidl VdcAWerr) * Ki Vdc; 

// Input lo Integral Controller 

Id! VdcI = INI'EGRATORRESET(l, Startup_flag, 0, Idl_Vdc//n, Old!dl_Vdclin, Oldidl_Vdcl, dell); 
Id! VdcAW = Id!_ VdcP + Id!_ VdcI; 
Id! Vdc = LIMITER(dq_base Ilim_pu, Idq_base w Ilim_pu, Idl_VdeAW); 
Id! VdcAWerr 
Id! VdcAW 
Id1 Vde; 

// Update Idl_VdcAWerr for next time step 

B-29 

Idlref Vdc 
// Droop 

(-Idl_ Vdc + Idl_FF) / Idq_base; 
f PLL = Omega_PLL / (2 * PI); 
fpu_flt= REALPOLE(I, T_frq.f_PLL ' 60.0, Oldf_PLL / 60.0, Oldfpu_flt, 999999.0, 999999.0, delt); 
Droop_down = DB(l - fpu_flt, fdbdl, fdbd2) Ddn; 
Droop_up = DB(l fpu_flt, fdbd1 , fdbd2) ¥ Dup.
Pref_droop = LIMITER(0, -9999, Droop_down) + LIMITER(9999, 0, Droop_up); 
Vtd_I_y REALPOLE(1.0, 0.01, Vtd_I, OldVtd_I, OldVtd_1_y, -99999.0, 99999.0, delt ); 

// Vtd_J _y2 = REALPOLE(1.0, 0.002, d_I, OldVrd_I, Oldrd_I_y2, 99999.0, 99999.0, de lt); 
Idref_droop_x = Pref_droop / (Vtd_l_y + 0.0001); 
Idref_droop = REALPOLE(l .0, Tp_droop, Idref_droop_x, Oldldref_droop_x, Oldldref_droop, 
-99999, 99999, delt ); 

// Idlref_P calculation 

Idlref P = Pref / (0.0001 + Vtd_l_y); 

// Outer control id 

Id_droopl = SELECTOR(SELECTOR(Pref, 0, COMPARATOR(currTIME, 1)), 
SELECTOR(Idlref_ Vdc, Idlref_P, Vdc_flag), Startup_flag ); 
Id_droop = SELECTOR(Idref_droop, 0, f_flag ); 
Idlref_conl = Id_droop + Id_droopl; 
Id1ref hold SH[I]= Old!dlref hold SH; 

// Idlref_cont continuous 

SAMPLEHOLD(Idlref_conl, FRT_flag, OldFRT_flag, Idlref_hold_SH); 

// Idlref_hold = S4MPLEHOLD(Idlref_cont, Oldidlref_hold, FRT_Jlag); 
Idlref_hold = Idlref_hold_SH [OJ, // Idlref_hold is output of Sample and Hold 
Idlref_nolimil = SELECTOR(Idlref_hold, Idlref_cont, Id_frz_flag ); 
Idlref = LIMITER(Ilim_pu, -Ilim_pu, Idlref_nolimil ); 

// Vt Closed Loop 

Iq_VtdCLe = SELECTOR(0, DEADBAND((Vl_ref - Vtd_l_y), 0.001, 1, 0), FRT_flag); 

/k Anti id Up Code Begin 
Iq_VtdCLP= Iq_VtdCLe KV_p; // Proportional term 
lq_VtdCL!in = (Iq_VtdCLe - Oldlq_VtdCLAWerr) * Kv_i; 

// Input to Integral Controller 

lq_ VtdCLI = INI'EGRATORRESET(l, Startup_flag, 0, lq_ VtdCL!in, Oldlq_ VtdCL!in, Oldlq_ VtdCLI, dell); 
Iq_ VtdCLAW = lq_ VtdCLP + lq_ VldCLI; 
Iq_VtdCL = LIMITER(Qmax, Qmin, Iq_VtdCLAW); 
Iq_ VtdCLAWerr = Iq_VtdCLAW - Iq_ VtdCL; 
/s Anti Wind Up Code Ends % 

// Update AWerr for next time step 

B-30 

// Q Closed Loop 
Qdq_x Qtab_pu ; 
Qdq = REALPOLE(l, 0.005, Qdq_x, OldQdq_x, OldQdq, 999999, 999999, delt): 
Iq_QCLe = LIMITER(Qmax, Qmin, Qref) - Qdq; 
/ Anti ind Up Code Begin 

Iq_QCLP = Iq_QCLe * Kq_p; // Proportional term 
Iq_QCL!in = (Iq_QCLe - Oldlq_QCLAWerr) * Kq_i; 

// Input to Integral Controller 

Iq_QCLI = INTEGRATORRESET(I, Startup_flag .0, Iq_QCL//n, Oldlq_QCL//n, Oldlq QCLI, delt); 
lq_QCLAW = Iq_QCLP + Iq_QCLI; 
Iq_QCL = LIMITER(Qmax, Qmin, Iq_QCLAW); 
Iq_QCLAWerr = Iq_QCLAW - Iq_QCL; 
/ Anti Wind Up Code Ends w 

// Q Open Loop 

Iq_QOL = LIMITER(Qmax, Qmin, Qref) / (Vtd_l_y + 0.0001); 
// LVRTI HVRT 

// Update AWerr for next time step 

Vdql_y = REALPOLE(l, 0.002, Vdql, OldVdql, OldVdql_y, -99999, 99999.delt); 
Iql_frt = DB(Vt_ref - Vtd_l - 0.0001, dbhv_frt, dblv_frt) * -Kqvl; 
Iq_Qctl = SELECTOR(Iq_QCL, Iq_QOL, Qctl_CL_flag); 
lql_icont = SELECTOR(Iq_VtdCL, lq_Qctl, Vt_flag); 
Iq1_i_SH[I] Oldlq1_i_SH; 
SAMPLEHOLD(LIMITER(l, -1, -1 * Iql_icont), FRT_flag, OldFRT_flag, Iql_i_SH ); 
Iql_i = Iql_i_SH [0]; 

//Iql_i - SAMPLEHOLDLIMITER(I,-I,-I w Iql_icont), Old1qI_i, FRT flag); 
Iqlref = Iql_frt + Iql_i; 

// V2 Control 

RECTANGULAR2POLAR(Vld_2, Vtq_2, &Vdq_2mag, &Vdq_2ang); 

Idq2_refmag = DB(Vdq_2mag, 0, dbh_2) * Kqv2; //CHANGED dbl 2 to 0 on 4/19 
Idq2_refang = Vdq_2ang - (PI / 2); 
POLAR2RECTANGULAR Idq2_refmag, Idq2_refang, &ld2ref, &lq2ref), 
/ Current Limit Logic Block v! 

// Generating Idlref_L, Iqlref_L, Jdref_2_L, Iq2ref_L 

12m_ref_upper = SELECTOR(SELECTOR(fabs(Iql_frt), fabs(Iqlref), IR_flag), 9999, l); 
RECTANGULAR2POLAR(Id2ref, Iq2ref, &12m_refmag, &Iq2ref_Lang); 
12m ref = LIMITER(I2m_ref_upper, 0, 12m_refmag ); 

B-31 

Ilm_ref - sqrt(pow(Id1ref, 2) + pow(Iqlref, 2)); 
Ilim_L = SELECTOR((Ilim_pu Iql_i), (Clim pu + Iql_i), COMPARATOR(IqI_frt .0)); 
IROL_flag = COMPARATOR(fabs(Iqlref) + fabs(l2m_ref), llim_pu); 
scale= SELECTOR((Ilim_L I (fabs(lql_frt) + I2m_ref)), I, IROL_flag); 
I2m_ref_L = I2m_ref scale; 
POLAR2RECTANGULAR(I2m_ref_L, Iq2ref_Lang, &Id2ref_L, &Iq2ref_L); 
Iqlref_L = Iql_i + (Iql_frt * scale); 
ldlmax FRT = sqrt(LIM1TER(999999.0, 0.0, (pow((llim_pu - 12m ref L), 2) - pow(lqlref_L, 2)))); 
I di ref L = LIMITER(ldlmax_FRT, -Idlmax_FRT, ldlref); 

// Calculation for Him_phmax 

Magidql 
Magidq2 

sqrt(pow(ldlref_L, 2) + pow(Iqlref_L, 2)); 
sqrt(pow(Id2ref_L, 2) + pow(Iq2ref_L, 2)), 

Angidq_12 = atan2 (Iqlref_L, Id I ref L) + atan2 (Iq2ref_L, Id2ref L) 

// Cont ..Calculate Ia_max , Ib_max, Jc_max 
Ia max= sqrt(pow(Magldq1, 2) + pow(Magldq2, 2) + 2 Magldql Magldq2 cos(Angldq_12)); 
Ib max= sqrt(pow(Magldql, 2) + pow(Magldq2, 2) + 2# Magldql Magldq2 

* cos(Angidq_12 + (2 PI / 3))); 

le max = sqrt (pow(Magldql, 2) + pow(Magldq2, 2) + 2 Magldql Magldq? 

* cos(Angidq_12 - (2 * PI / 3))); 

Iph_max = fmax (Ia_max, fmax (Ib_max, Ic_max )) 
IOL_flag = COMPARAIDR(Ilm_ref + I2m_ref, Ilim_pu); 
Ilim_phmax = SELECTOR(L!MlTER((llim_pu 1 0.877), 1, llim_pu / Iph_max), I, IOL_flag); 
// Generating Jdlref_L2, Iqlref_L2, Jdref_2_L2, Iq2ref_L2 

scale_phmax = SELECTOR(llim_phmax, I, I * lOL_flag); 
RECTANGULAR2POLAR(Idlref_L, Iqlref_L, &Magidqref_l_L, &Angidqref_l_L); 
POLAR2RECTANGULAR( Magldqref_1_L scale _phmax, Angldqref_1_L, &Idlref_L2, &lqlref_L2).
RECTANGULAR2POLAR(Id2ref_L, Iq2ref_L, &Magldqref_2_L.&Angldqref_2_L), 
POLAR2RECTANGULAR(Magldqref_2_L scale phmax, Angldqref_2_L, &ld2ref_L2, &lq2ref_L2): 

/x Positive Sequence Current Limit Logic Block x 

Idlref_max = sqrt(LIM1TER(999999, 0, pow(llim_pu, 2) - pow(Iqlref, 2))); 
Idlref LI 
Iqlref_Ll 
LIMITER(Id1ref_max, 0, Id1ref); 
LIMITER(Ilim_pu, -Ilim_pu, Iqlref); 

// Input Currents lo Current Controller 

1 dr ef I 
lqref_l 
SELECTOR(Idlref_L2, Idlref_Ll, V2_flag); 
SELECTOR(Iqlref_L2, Iqlref_Ll, V2_flag); 

B-32 

I dr ef 2 
Iqref_2 
SELECTOR(Id2ref_L2, 0.0, V2_flag); 
SELECTOR(Iq2ref_L2, 0.0, V2_flag); 

// Current control loop 

t_release = fmax(( tstarl_up 1), 0.0); 
Current_control = (Curr'TIME > t_release ); 
if (1 current_control) { 
Idref_1 - 0.0; 
Idref_2 = 0.0; 
Iqref_l = 0.0; 
Iqref_2 = 0.0; 

/ Check is Current Control is disabled 

Iramp_up = SELECTOR(99, Ipramp_up, FRT_flag), 

Id! ref= RATELIMITER(Idref_l, Oldldl_ref, Iramp_up, 1000, delt); 
!di e = (Idl_ref - Id_!) * Idq_base; 

/ Anti ind Up Code Begin w/ 

uctrld IP = Idl_e * Kcc_p; // Proportional term 

uetrld 1//n = (Id1 e Olductrld IAWerr) Kc i; 

// Input to Integral Controller 

uetrld // = INI'EGRATORRESET(l, 0, 0, uetrld //in Olduelrld //in, Olduetrld //, dell); 

uctrld 1AW = uctrld 1P + uctrld //; 

// Input to AW 

uctrld I = LIMITER(Lim_upCC, Lim lowCC, uctrld 1AW); 
uctrld IAWerr= uctrld 1AW ctrld 1; 

// Update AWerr for next time step 

/ Anti ind Up Code Ends w! 

!qi _ref = RATELIMITER( Iqrcf_I, Oldlql_ref, 99999, 99999, delt): 
Iql_e = (Iql_ref - lq_l) * Idq_base; 

/k Anti ind Up Code Begin / 

uclrlq_lP = Iql_e * Kcc_p; // Proportional term 
uclrlq_llin = (Iql_e - Oldnuctrlq_1AWerr) # Kcc_i; 

// Input to Integral Controller 

uetrlq_lI = INI'EGRATORRESET(l, 0, 0, uetrlq_l//n, Olduelrlq_l//n, Olduetrlq_lI, dell); 
uetrlq_lAW = uetrlq_lP + uetrlq_lI; 

// Input to AW 

uelrlq_l = LIMITER(Lim_upCC, Lim lowCC, uetrlq_lAW); 

uctrlq_lAWerr = uclrlq_lAW - uclrlq_l; 
/ Anti ind Up Code Ends w! 

// Update AWerr for next time step 

Id2 ref = RATELIMITER( Idref_2, Oldid2_ref, 99999, 99999, delt); 
Id2 e = (Id2_ref - Id_2) * Idq_base; 

/ Anti ind Up Code Begin kl 

uctrld 2P = Id2_e * Kcc_p; // Proportional term 
uetrld 2//n 

(Id2 e 

Olductrld 2AWerr) * Kec_i; 

// Input to Integral Controller 

B-33 

uelrld 21 = INTEGRATORRESET(1, 0, 0, uctrld 2//n Olduclrld 2lin, Olduelrld 21, dell); 
uetrld 2AW = uetrld 2P + uetrld 21; 

/ Iput to AW 

uetrld 2 = LIMITER(Lim_upCC, Lim lowCC, uetrld 2AW); 
uctrld 2AWerr = uctrld 2AW - uctrld 2; 

// Update AWerr for next time step 

/k Anti Wind Up Code Ends / 

lq2_ref = RATELIMITER(lqref_2, Oldlq2_ref, 99999, 99999, delt), 
lq2_e = (lq2_ref - lq_2) * ldq_base; 

/ Anti ind Up Code Begin »/ 

uetrlq_2P = lq2_e * Kee_p; // Proportional term 
uelrlq_2lin = (lq2_e - Olduelrlq_2AWerr) * Kee i; 

// Input to Integral Controller 

uclrlq_2I = INTEGRATORRESET(l, 0, 0, uctrlq_2lin, Olductrlq_2lin, Olductrlq_2I, dell); 
uctrlq_2AW = uctrlq_2P + uctrlq_2I; 

// Input to AW 

uctrlq_2 = LIMITER(Lim_upCC, Lim lowCC, uctrlq_2AW); 
uctrlq_2AWerr = uctrlq_2AW - uctrlq_2, 
/t Anti Wind Up Code Ends / 

// Generate Ed_l, Eq_l, Ed_2, and Eq_2 

// Update AWerr for next time step 

Vtd_ly = REALPOLE(l, Tau_Vff, Vtd_1, OldVtd_1, OldVtd_1y, 99999, 99999, delt); 
Ed 1 = SELECTOR(Vtd_ly, 0,0, Vff_flag) * Vdq_base - (Iq_l * Lehoke * w_nom * ldq_base) + uelrld_l; 
Vtq_ly = REALPOLE(l, Tau_ Vff, Vtq_l, OldVtq_l, OldVtq_ly, -99999, 99999, delt); 
Eq_l = SELECTOR(Vtq_ly, 0.0, Vff_flag) * Vdq_base + (Id_! * Lehoke * w_nom Idq_base) + uelrlq_l; 
Vtd_2y = REALPOLE(I, Tau_VI, Vtd_2, Oldvd_2, Oldvtd_2y, 99999, 99999, de It); 
Ed 2 = SELECTOR(Vtd_2y, 0.0, Vff_flag) * Vdq_base + (lq_2 * Lchoke * w_nom * ldq_base) + uclrld_2; 
Vtq_2y = REALPOLE(I, Tau_V//, Vtq_2, Oldvtq_2, Oldvtq_2y, 99999, 99999, de It); 
Eq_2 = SELECTOR(Vtq_2y, 0.0, Vff_flag) * Vdq_base - (Id_2 * Lchoke * w_nom * ldq_base) + uctrlq_2, 

// Generate output Eal, Ebl, Eel 

DQ2ABC(Ed_1.Eq_l, Theta PLL.Eabc_1).

// Generate output Ea2, Eb2, Ec2 

DQ2ABC(Ed_2, Eq_2, -Theta_PLL, Eabc_2); 

// Check modulation index 

Ea m = Eabe 1 [OJ + Eabe 2 [OJ; 

Eb m = Eabe l[l] + Eabe 2[1]; 
Ee m= Eab I[2] + Eabc 2[2]; 

// Outputs 

outputs->m_a = Ea_m * 2.0 / Vdc nom; 

B-34 

outputs ->m_b 
outputs ->m_c 
Eb_m * 2.0 
Ec_m * 2.0 
Vdc_nom, 
Vdc_nom; 
outputs ->FreqPLL = f_PLL; 
outputs ->Output_! 

Id 1; 

outputs ->Output_2 = lq_l; 
outputs ->Output_3 = Id_2; 
outputs ->Output_ 4 = Iq_2; 
outputs ->Output_5 = Vtd_l; 
outputs->Output_6 = Vtq_l; 
outputs->Output_7 = Vtd_2; 
outputs ->Output_8 = Vtq_2; 
outputs ->Output_9 = FRT_flag; 
// Added outputs for debugging 

// save state variables 

instance->DoubleStates [OJ 
instance->DoubleStates [l] 
instance->DoubleStates [2] 
instance->DoubleStates [3] 
instance->DoubleStates [4] 
instance->DoubleStates [5] 
instance-DoubleStates [6] 
instance->DoubleStates [7] 
instance-DoubleStates[8] 
instance->DoubleStates [9] 
instance->DoubleStates [10] 
instance->DoubleStates [11] 
instance->DoubleStates [12] 
instance-DoubleStates[13] 
instance->DoubleStates [14] 
instance-DoubleStates[15] 
instance DoubleStates[16] 
instance->DoubleStates [17] 
instance DoubleStates[18] 
instance->DoubleStates [19] 
instance->DoubleStates [20] 
instance->DoubleStates [21] 
instance->DoubleStates [22] 
instance->DoubleStates [23] 
instance->DoubleStates [24] 
instance->DoubleStates [25] 
instance->DoubleStates[26] 
instance->DoubleStates [27] 
instance-DoubleStates[28] 
instance DoubleStates[29] 
instance->DoubleStates [30] 
instance->DoubleStates [31] 
instance->DoubleStates [32] 
instance-DoubleStates[33] 
instance->DoubleStates [34] 
instance-DoubleStates[35] 
instance->DoubleStates [36] 
instance->DoubleStates [37] 
instance->DoubleStates [38] 
instance->DoubleStates [39] 
instance->DoubleStates [40] 
instance->DoubleStates [41] 
instance->DoubleStates [42] 
instance->DoubleStates [43] 
instance->DoubleStates [44] 
instance->DoubleStates [45] 

O; 

Vta_pu; 
Vta_fltl; 
Vw_pu, 
Vtb_fltl; 
Vte_pu; 
Vtc_fltl; 
Il a_pu; 
Ila_fltl; 
11 b _pu; 
Ilb_fltl; 
I1c_pu, 
Ilc_fltl; 
I2a_pu 
12a_fltl; 
12b_pu: 
I2b_fltl; 
12¢_pu: 
I2c_fltl; 
Omega_PLL; 
Vt_alpha: 
Vt_alpha_pr; 
Vt_qalpha_pr; 
Vt_beta; 
Vt_beta_pr; 
Vt_qbeta_pr; 
Theta_PLL; 
DelOmegaAWerr; 
DelOmegalin; 
DelOmegal; 
Theta_DSOGIPLLcont; 
Idl_ref; 
OldIdI_ref; 
Id1r_fIt; 
Iql_ref; 
Old1q1_ref; 
lqlr_flt; 
Id2_ref; 
Oldld2_ref; 
Id2r _flt; 
1q2_ref; 
Oldlq2_ref; 
Iq2r _flt; 
Idl_FFin; 
Idl_FFnolimit; 
Id1 VdeAWerr, 

B-35 

instance->DoubleStates [46] = Idl_ Vdclin, 
instance->DoubleStates [47] = Id!_ Vdcl; 
instance->DoubleStates[48] = f_PLL; 
instance->DoubleStates [49] = fpu_flt; 
instance->DoubleStates[50] = Vtd_l_y2; 
instance->DoubleStates [5 I] = Vtd_l_y; 
instance->DoubleStates [52] = Idref_droop_x; 
instance->DoubleStates [53] = Idref_droop; 
instance->DoubleStates[54] = Idlref_hold; 
instance >DoubleStates[55] = Iq_ VtdCLAWerr; 
instance->DoubleStates[56] = Iq_VtdCL!in; 
instance->DoubleStates [57] = lq_ VtdCLI; 
instance->DoubleStates [58] = Qdq_x; 
instance->DoubleStates [59] = Qdq; 
instance->DoubleStates [60] = Iq_QCLAWerr; 
instance->DoubleStates [61] = Iq_QCL!in; 
instance-DoubleStates[62]= Iq_QCLI; 

instance DoubleStates[63] = Vdql; 
instance->DoubleStates [64] = Vdql_y; 
instance->DoubleStates [65] - Iql_i.
instance->DoubleStates [66] = Idref_l; 
instance->DoubleStates [67] = uctrld_lAWerr; 
instance->DoubleStates [68] = uctrld_llin; 
instance-DoubleStates[69] = uctrld_ll; 
instance->DoubleStates [70] = lqref_l; 
instance->DoubleStates [71] = uctrlq_lAWerr; 
instance->DoubleStates [72] = uctrlq_llin; 
instance-DoubleStates[73]= uctrlq_ll; 
instance->DoubleStates [74] = Idref_2; 
instance-DoubleStates[75]= uctrld_2AWerr; 
instance->DoubleStates [76] = uctrld_2lin; 
instance->DoubleStates [77] = uctrld_21; 
instance-DoubleStates[78]= Iqref_2; 
instance->DoubleStates [79] = uctrlq_2AWerr; 
instance-DoubleStates[80]= uctrlq_2//n; 
instance->DoubleStates[81] = uctrlq_21; 
instance->DoubleStates [82] = Vtd_l; 
instance->DoubleStates [83] = Vtd_ly, 
instance->DoubleStates [84] = Vtq_l; 
instance->DoubleStates[85] = Vtq_ly; 
instance->DoubleStates[86] = Vtd_2; 
instance->DoubleStates [87] = Vtd_2y, 
instance->DoubleStates[88] = Vtq_2; 
instance->DoubleStates [89] = Vtq_2y, 

instance >DoubleStates[90]= FRT_flag; 
instance-DoubleStates[91]= Idlref_hold_SH [I]; 
instance->DoubleStates [92] = Iql_i_SH [I]; 
instance->LastGeneralMessage = ErrorMessage; 
return IEEE_Cigre_DLLInterface_Return_ OK; 

}; 

//---------------------------------------------------------------- 

_declspec(dllexport) int32 T cdecl Model_Terminate(IEEE_Cigre_DLL Interface_Instance instance) { 

/k Destroys any objects allocated by the model code- not used 

R/ 

return IEEE_Cigre_DLLInterface_Return_ OK; 

}; 

declspec(dllexport) int32_T cdecl Model_FirstCall(IEEE_Cigre DLLInterface_Instance instance) { 

/ Destroys any objects allocated by the model code not used 

k/ 

return O; 

}; 

_declspec(dllexport) int32 T cdecl Model_Iterate(IEEE Cigre_DLLInterface_Instance instance) { 

/w Destroys any objects allocated by the model code not used 

k/ 

B-36 

returu O; 

}; 
// 

__ declspec ( dllexport) int32_T cdecl Model_Printlnfo () 

Prints Model Information once 

k/ 

int Printed = O; 
if (! Printed) { 
printf (" Cigre /IEEE DLL Standard In"); 
printf("Model name: %sn", Model_Info .ModelName); 
printf ("Model version: %s\n", Model_Info.Model Version); 
printf("Model description: %s\n", Model_Info.ModelDescription ); 
printf("Model general info: %s\n", Model_Info.GeneralIn formation ); 
printf("Model created on: %sn", Model_Info.Model Created); 
printf("Model created by: %s\n", Model_Info.ModelCreator), 
printf("Model last modified %s\n", Model_Info.ModelLastModifiedDate ); 
printf("Model last modified by: %sin", Model_Info.ModelLastModifiedBy), 

printf("Model modified comment: %s\n" , Model_Info.ModelModifiedComment); 
printf ("Model modified history: %s\n", Model_Info.ModelModifiedHistory ); 
printf("Time Step Sampling Time (sec): %0.5gln", Model_Info.FixedStepBaseSampleTime), 
switch (Model_Info .EMT_RMS_Mode) 

case 1: 
printf ("EMT/RMS mode: 
break; 
case 2: 
printf ( "EMT/RMS mode: 
break; 
case 3: 
printf ( "EMT/RMS mode: 
break; 
default: 
printf ("EMT/RMS mode : 

EMT\n" ) 

RMS\n" ); 

EMT and RMSln"); 

<not available >In"); 

printf ("Number of inputs: %d\n", Model_Info.NumInputPorts ); 
printf("Input description\n"); 

for (int k = 0; k < Model_Info.NuminputPorts; k++) { 
printf" %s\n", Model_Info.InputPortsinfo [k] Name); 
} 

printf("Number of outputs: %d\n", Model_Info.NumOutputPorts); 
printf"output description .n); 

for (int k = 0; k < Model_Info.NumOutputPorts, k++) { 
printf(" %sin", Model_Info.OutputPortsinfo [k] .Name); 
printf("Number of parameters: %d\n", Model_Info .NumParameters): 
printf (" Parameter description:"): 

for (int k = 0; k < Model_Info.NumParameters; k++) { 
printf(" %sin", Model_Info.Parametersinfo [kl .Name); 
printf("Number of int state variables: 
printf("Number of float state variables: 
printf("Number of double state variables: 
printf ("\n"); 

fflush ( stdout); 

%d\n" , Model_Info.NumIntStates); 
%d\n" , Model_Info .NumFloatStates); 
%dn" , Model_Info .NumDouble States ); 

Printed = 1; 
return IEEE_Cigre_DLLInterface_Return_ OK; 
}; 

