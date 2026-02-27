/* 

This model has.
- 15 inputs (input current time has been removed, Vref added) 
- 15 outputs (3 ouputs are essential, others can be used for debugging) 
- 58 parameters 

This model will be compiled into a DLL, and then can be used in ANY power system 
simulation program by running the "DLLImport" tool that comes with each program 

September 21, 2023, Vishal Verma 
*/ 

#include <windows.h> 
#include <stdio.h> 
#include <math.h> 

#define PI       3.141592654
#define PI2      1.570796327
#define TWOPI    6.283185307
#define TWOPI3   2.094395102
#define SQRT3    1.732050808
#define SQRT23RD 0.816496581
#define TWO3RD   0.666666667
#define SQRT3H   0.866025404

#include "IEEE_Cigre_DLLInterface.h" 
char ErrorMessage[1000];

// ---------------------------------------------------------------------- 
// Structures defining inputs, outputs, parameters and program structure 
// to be called by the DLLimport Tool 
// ---------------------------------------------------------------------- 

typedef struct _MyModelInputs { // removed currTIME
	real64_T Vta;
	real64_T Vtb;
	real64_T Vtc;
	real64_T I1a;
	real64_T I1b;
	real64_T I1c;
	real64_T I2a;
	real64_T I2b;
	real64_T I2c;
	real64_T Idc;
	real64_T VdcMPPT;
	real64_T Pref;
	real64_T Qref;
	real64_T Vdc_meas;
  real64_T Vref; // new
} MyModelInputs;

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
    .Description = "B phase VSC current", 
    .Unit = "kA", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .Width = 1 
  }, 
  [5] = {
    .Name = "I1c", 
    .Description = "C phase VSC current", 
    .Unit = "kA", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .Width = 1 
  },
  [6] = {
    .Name = "I2a" , 
    .Description = "A phase current after capacitor", 
    .Unit = "kA", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .Width = 1 
  },
  [7] = {
    .Name = "I2b", 
    .Description = "B phase current after capacitor", 
    .Unit = "kA", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
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
    .Description = "Current from Primary Power Source", 
    .Unit = "kA", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .Width = 1 
  },
  [10] = { 
    .Name = "VdcMPPT", 
    .Description = "Maximum power point voltage", 
    .Unit = "kV", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .Width = 1 
  },
  [11] = {
    .Name = "Pref" , 
    .Description = "Active power reference ", 
    .Unit = "pu", // was MW
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .Width = 1 
  }, 
  [12] = { 
    .Name = "Qref" , 
    .Description = "Reactive power reference", 
    .Unit = "pu", // was Mvar
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
    .Name = "Vref", // new
    .Description = "Voltage magnitude reference", 
    .Unit = "pu", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .Width = 1 
  }
};

typedef struct _MyModelOutputs {
  real64_T m_a;
  real64_T m_b;
  real64_T m_c;
  real64_T FreqPLL;
  real64_T ID1;
  real64_T IQ1;
  real64_T ID2;
  real64_T IQ2;
  real64_T VD1;
  real64_T VQ1;
  real64_T VD2;
  real64_T VQ2;
  real64_T FRT_flag;
  real64_T Pout; // new
  real64_T Qout; // new
} MyModelOutputs;

// Define Output Signals 
IEEE_Cigre_DLLInterface_Signal OutputSignals[] = {
  [0] = { 
    .Name = "m_a", 
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
    .Description = "Phase C modulating signal",
    .Unit = "N/A", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .Width = 1 
  },
  [3] = {
    .Name = "FreqPLL" , 
    .Description = "PLL frequency", 
    .Unit = "Hz", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .Width = 1 
  }, 
  [4] = {
    .Name = "Id1", 
    .Description = "Positive Sequence Current d", 
    .Unit = "pu", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .Width = 1 
  }, 
  [5] = {
    .Name = "Iq1", 
    .Description = "Positive Sequence Current q", 
    .Unit = "pu", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .Width = 1 
  }, 
  [6] = {
    .Name = "Id2", 
    .Description = "Negative Sequence Current d" , 
    .Unit = "pu", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .Width = 1 
  }, 
  [7] = {
    .Name = "Iq2", 
    .Description = "Negative Sequence Current q", 
    .Unit = "pu", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .Width = 1 
  }, 
  [8] = {
    .Name = "Vtd1", 
    .Description = "Positive Sequence Voltage d", 
    .Unit = "pu", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .Width = 1 
  }, 
  [9] = {
    .Name = "Vtq1", 
    .Description = "Positive Sequence Voltage q", 
    .Unit = "pu", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .Width = 1 
  }, 
  [10] = {
    .Name = "Vtd2", 
    .Description = "Negative Sequence Voltage d", 
    .Unit = "pu", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .Width = 1 
  }, 
  [11] = {
    .Name = "Vtq2", 
    .Description = "Negative Sequence Voltage q", 
    .Unit = "pu", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .Width = 1 
  },
  [12] = {
    .Name = "FRT_Flag", 
    .Description = "Fault ride-through", 
    .Unit = "N/A", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .Width = 1 
  }, 
  [13] = {
    .Name = "Pout", // new 
    .Description = "Active power output at terminal", 
    .Unit = "pu", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .Width = 1 
  }, 
  [14] = {
    .Name = "Qout", // new
    .Description = "Reactive power output at terminal", 
    .Unit = "pu", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .Width = 1 
  } 
};

typedef struct _MyModelParameters { // removed Vt_ref
  real64_T VLLbase;
  real64_T Sbase;
  real64_T Tflt_v;
  real64_T Vflt_flag;
  real64_T Tflt_i;
  real64_T Iflt_flag;
  real64_T Cur1_flag;
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
  real64_T Ki_Vdc;
  real64_T T_frq;
  real64_T fdbd1;
  real64_T fdbd2;
  real64_T Ddn;
  real64_T Dup;
  real64_T Tp_droop;
  real64_T Vdc_flag;
  real64_T f_flag;
  real64_T Id_frz_flag;
  real64_T Ilim_pu;
  real64_T Kv_p;
  real64_T Kv_i;
  real64_T Qmin;
  real64_T Qmax;
  real64_T Kq_p;
  real64_T Kq_i;
  real64_T dbhv_frt;
  real64_T dblv_frt;
  real64_T Kqv1;
  real64_T Qctl_CL_flag;
  real64_T Vt_flag;
  real64_T dbl_2;
  real64_T dbh_2;
  real64_T Kqv2;
  real64_T V2_flag;
  real64_T Ipramp_up;
  real64_T Kcc_p;
  real64_T Kcc_i;
  real64_T Lim_upCC;
  real64_T Lim_lowCC;
  real64_T Tau_Vff;
  real64_T Vff_flag;
  real64_T IR_flag;
  real64_T Tr;     // new
  real64_T Lchoke;
  real64_T Rchoke; // new
  real64_T Cfilt;  // new
  real64_T Rdamp;  // new
  real64_T Tv;     // new
} MyModelParameters;

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
  [1] = {
    .Name = "Sbase", 
    .Description = "VA base", 
    .Unit = "VA", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .FixedValue = 0, 
    .DefaultValue.Real64_Val = 1e6, 
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
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .FixedValue = 0, 
    .DefaultValue.Real64_Val = 1, 
    .MinValue.Real64_Val = 0.0, 
    .MaxValue.Real64_Val = 1.0 
  },
  [4] = {
    .Name = "Tflt_i", 
    .Description = "LPF time constant for current", 
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
    .Description = "Current control at (1: before LCL, 0: after LCL)", 
    .Unit = "N/A", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .FixedValue = 0, 
    .DefaultValue.Real64_Val = 1.0, 
    .MinValue.Real64_Val = 0.0, 
    .MaxValue.Real64_Val = 1.0 
  },
  [7] = {
    .Name = "k_PLL", 
    .Description = "Damping constant for SOGI filter", 
    .Unit = "N/A", 
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
    .MinValue.Real64_Val = 0.0, 
    .MaxValue.Real64_Val = 1000.0 
  },
  [9] = {
    .Name = "KiPLL" , 
    .Description = "Integral gain for PLL", 
    .Unit = "pu/pu" , 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .FixedValue = 0, 
    .DefaultValue.Real64_Val = 324, 
    .MinValue.Real64_Val = 0.001, 
    .MaxValue.Real64_Val = 1000.0 
  },
  [10] = {
    .Name = "Lim_PLL" , 
    .Description = "Windup limit for PLL", 
    .Unit = "pu/pu", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .FixedValue = 0, 
    .DefaultValue.Real64_Val = 70.0, 
    .MinValue.Real64_Val = 0.0, 
    .MaxValue.Real64_Val = 1000.0 
  },
  [11] = {
    .Name = "w_nom" , 
    .Description = "Nominal angular frequency", 
    .Unit = "rad/s", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T,
    .FixedValue = 0, 
    .DefaultValue.Real64_Val = TWOPI * 60, 
    .MinValue.Real64_Val = 1.0, 
    .MaxValue.Real64_Val = 1e8 
  },
  [12] = {
    .Name = "tstart_up", 
    .Description = "Time for start up flag of Q and Vt closed loop",
    .Unit = "s", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .FixedValue = 0, 
    .DefaultValue.Real64_Val = 1.9, 
    .MinValue.Real64_Val = 0.0, 
    .MaxValue.Real64_Val = 1000.0 
  },
  [13] = {
    .Name = "Vdc_nom" , 
    .Description = "Nominal DC Link Voltage", 
    .Unit = "kV", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .FixedValue = 0, 
    .DefaultValue.Real64_Val = 1200, 
    .MinValue.Real64_Val = 0.0, 
    .MaxValue.Real64_Val = 10000.0 
  },
  [14] = {
    .Name = "VI_flag", 
    .Description = "1: enable PPS VI characteristic, 0: constant I", 
    .Unit = "N/A", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T,
    .FixedValue = 0, 
    .DefaultValue.Real64_Val = 0.0, 
    .MinValue.Real64_Val = 0.0, 
    .MaxValue.Real64_Val = 1.0 
  },
  [15] = {
    .Name = "MPPT_flag", 
    .Description = "1: enable MPPT for Vdc*, requires VI_flag=1 and Vdc_flag=1", 
    .Unit = "pu/pu", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .FixedValue = 0, 
    .DefaultValue.Real64_Val = 0.0, 
    .MinValue.Real64_Val = 0.0, 
    .MaxValue.Real64_Val = 1.0 
  },
  [16] = {
    .Name = "b_Vdc", 
    .Description = "Setpoint weight for DC voltage", 
    .Unit = "N/A" , 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .FixedValue = 0, 
    .DefaultValue.Real64_Val = 0.56, 
    .MinValue.Real64_Val = 0.0, 
    .MaxValue.Real64_Val= 100.0 
  },
  [17] = {
    .Name = "Kp_Vdc", 
    .Description = "Proportional gain for Vdc", 
    .Unit = "pu/pu", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .FixedValue = 0, 
    .DefaultValue.Real64_Val = 5.18, 
    .MinValue.Real64_Val = 0.001, 
    .MaxValue.Real64_Val = 1000.0 
  },
  [18] = {
    .Name = "Ki_Vdc", 
    .Description = "Integral gain for Vdc", 
    .Unit = "pu/pu", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .FixedValue = 0, 
    .DefaultValue.Real64_Val = 52.91, 
    .MinValue.Real64_Val = 0.0, 
    .MaxValue.Real64_Val = 1000.0 
  },
  [19] = {
    .Name = "T_frq", 
    .Description = "Time constant for PLL frequency", 
    .Unit = "s", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T,
    .FixedValue = 0, 
    .DefaultValue.Real64_Val = 0.1, 
    .MinValue.Real64_Val = 0.0, 
    .MaxValue.Real64_Val = 1.0 
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
    .Description = "Time constant for first order lag block in P-f control", 
    .Unit = "s", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .FixedValue= 0, 
    .DefaultValue.Real64_Val = 0.001, 
    .MinValue.Real64_Val = 0, 
    .MaxValue.Real64_Val = 100.0 
  },
  [25] = {
    .Name = "Vdc_flag", 
    .Description = "Vdc control flag (1: enable, 0: const. PQ)", 
    .Unit = "N/A", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .FixedValue= 0, 
    .DefaultValue.Real64_Val = 0.0, 
    .MinValue.Real64_Val = 0.0, 
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
    .MinValue.Real64_Val = 0.0, 
    .MaxValue.Real64_Val = 1.0 
  },
  [28] = {
    .Name = "Ilim_pu", 
    .Description = "Inverter Current limit", 
    .Unit = "pu", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .FixedValue = 0, 
    .DefaultValue.Real64_Val = 1.1, 
    .MinValue.Real64_Val = -10.0, 
    .MaxValue.Real64_Val = 10.0 
  },
  [29] = {
    .Name = "Kv_p",
    .Description = "Proportional gain for terminal voltage PI controller", 
    .Unit = "pu", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .FixedValue = 0, 
    .DefaultValue.Real64_Val = 0.0, 
    .MinValue.Real64_Val = 0.0, 
    .MaxValue.Real64_Val = 1e8 
  },
  [30] = {
    .Name = "Kv_i", 
    .Description = "Integral gain for terminal voltage PI controller", 
    .Unit = "pu", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .FixedValue = 0, 
    .DefaultValue.Real64_Val = 100.0, 
    .MinValue.Real64_Val = 0.0, 
    .MaxValue.Real64_Val = 1e8 
  },
  [31] = {
    .Name = "Qmin", 
    .Description = "Minimum reactive power in pu", 
    .Unit = "pu",
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .FixedValue = 0, 
    .DefaultValue.Real64_Val = -0.4, 
    .MinValue.Real64_Val = -1e8, 
    .MaxValue.Real64_Val = 1e8 
  },
  [32] = {
    .Name = "Qmax", 
    .Description = "Maximum reactive power in pu", 
    .Unit = "pu",
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .FixedValue = 0, 
    .DefaultValue.Real64_Val = 0.4, 
    .MinValue.Real64_Val = -1e8, 
    .MaxValue.Real64_Val = 1e8 
  },
  [33] = {
    .Name = "Kq_p",
    .Description = "Q closed-loop proportional control gain", 
    .Unit = "pu", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .FixedValue = 0, 
    .DefaultValue.Real64_Val = 0.0, 
    .MinValue.Real64_Val = 0.0, 
    .MaxValue.Real64_Val = 1e8 
  },
  [34] = {
    .Name = "Kq_i", 
    .Description = "Q closed-loop integral control gain", 
    .Unit = "pu", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .FixedValue = 0, 
    .DefaultValue.Real64_Val = 40.0, 
    .MinValue.Real64_Val = 0.0, 
    .MaxValue.Real64_Val = 1e8 
  },
  [35] = {
    .Name = "dbhv_frt", 
    .Description = "Dead band LVRT +ve sequence HV", 
    .Unit = "pu", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .FixedValue = 0, 
    .DefaultValue.Real64_Val = -0.1, 
    .MinValue.Real64_Val = -1e8, 
    .MaxValue.Real64_Val = 1e8 
  },
  [36] = {
    .Name = "dblv_frt", 
    .Description = "Dead band HVRT +ve sequence LV", 
    .Unit = "pu", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T,
    .FixedValue = 0, 
    .DefaultValue.Real64_Val = 0.1, 
    .MinValue.Real64_Val = -1e8, 
    .MaxValue.Real64_Val = 1e8 
  },
  [37] = {
    .Name = "Kqv1" , 
    .Description = "Proportional gain for positive voltage dip", 
    .Unit = "pu", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T,
    .FixedValue = 0, 
    .DefaultValue.Real64_Val = 2.0, 
    .MinValue.Real64_Val = 0.0, 
    .MaxValue.Real64_Val = 1e8 
  },
  [38] = {
    .Name = "Qctl_CL_flag", 
    .Description = "1: enables closed loop Q control, 0: open loop", 
    .Unit = "N/A", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T,
    .FixedValue = 0, 
    .DefaultValue.Real64_Val = 1.0, 
    .MinValue.Real64_Val = 0.0, 
    .MaxValue.Real64_Val = 1.0 
  },
  [39] = {
    .Name = "Vt_flag", 
    .Description = "1: enable inverter term. voltage control, 0: Q control", 
    .Unit = "N/A", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T,
    .FixedValue = 0, 
    .DefaultValue.Real64_Val = 1.0,
    .MinValue.Real64_Val = 0.0, 
    .MaxValue.Real64_Val = 1.0 
  },
  [40] = {
    .Name = "dbl_2", 
    .Description = "VRT dead band (negative)", 
    .Unit = "N/A", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T,
    .FixedValue = 0, 
    .DefaultValue.Real64_Val = -0.1, 
    .MinValue.Real64_Val = -1e8, 
    .MaxValue.Real64_Val = 0.0 
  },
  [41] = {
    .Name = "dbh_2", 
    .Description = "VRT dead band (positive)", 
    .Unit = "N/A", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .FixedValue = 0, 
    .DefaultValue.Real64_Val = 0.1, 
    .MinValue.Real64_Val = 0.0, 
    .MaxValue.Real64_Val = 1e8 
  },
  [42] = {
    .Name = "Kqv2", 
    .Description = "Proportional gain for -ve voltage deviation", 
    .Unit = "pu", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T,
    .FixedValue = 0, 
    .DefaultValue.Real64_Val = 2.0, 
    .MinValue.Real64_Val = 0.0, 
    .MaxValue.Real64_Val = 1e8 
  },
  [43] = {
    .Name = "V2_flag", 
    .Description = "1: enable V2 control during FRT", 
    .Unit = "pu" , 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T,
    .FixedValue = 0, 
    .DefaultValue.Real64_Val = 1.0, 
    .MinValue.Real64_Val = 0.0, 
    .MaxValue.Real64_Val= 1.0 
  },
  [44] = {
    .Name = "Ipramp_up", 
    .Description = "Ramp up rate for active current", 
    .Unit = "pu", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T,
    .FixedValue = 0, 
    .DefaultValue.Real64_Val = 1.0, 
    .MinValue.Real64_Val = 0.0, 
    .MaxValue.Real64_Val = 1e8 
  },
  [45] = {
    .Name = "Kcc_p", 
    .Description = "Proportional gain PI controller in current controller", 
    .Unit = "pu", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .FixedValue = 0, 
    .DefaultValue.Real64_Val = 0.32325, 
    .MinValue.Real64_Val = 0.0, 
    .MaxValue.Real64_Val = 1e8 
  },
  [46] = {
    .Name = "Kcc_i", 
    .Description = "Integral gain PI controller in current controller", 
    .Unit = "pu", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T,
    .FixedValue = 0, 
    .DefaultValue.Real64_Val = 324, 
    .MinValue.Real64_Val = 0.0, 
    .MaxValue.Real64_Val = 1e8 
  },
  [47] = {
    .Name = "Lim_upCC" , 
    .Description = "Current controller's anti-windup upper limit", 
    .Unit = "pu", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .FixedValue = 0, 
    .DefaultValue.Real64_Val = 99999, 
    .MinValue.Real64_Val = 0.0, 
    .MaxValue.Real64_Val = 1e8 
  },
  [48] = {
    .Name = "Lim_lowCC", 
    .Description = "Current controller's anti-windup lower limit", 
    .Unit = "pu" , 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .FixedValue = 0, 
    .DefaultValue.Real64_Val = -99999, 
    .MinValue.Real64_Val = -1e8, 
    .MaxValue.Real64_Val = 0 
  },
  [49] = {
    .Name = "Tau_Vff", 
    .Description = "Time constant of LPF for voltage current controller", 
    .Unit = "s", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .FixedValue = 0, 
    .DefaultValue.Real64_Val = 0.0001, 
    .MinValue.Real64_Val = 0.0, 
    .MaxValue.Real64_Val = 1e8 
  },
  [50] = {
    .Name = "Vff_flag", 
    .Description = "Voltage filter flag (1 enable)", 
    .Unit = "N/A", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .FixedValue= 0, 
    .DefaultValue.Real64_Val = 0.0, 
    .MinValue.Real64_Val = 0.0, 
    .MaxValue.Real64_Val = 1e8 
  },
  [51] = {
    .Name = "IR_flag", 
    .Description = "1: limit Iq2 to delta Id2, 0: limit Iq2 to Id2", 
    .Unit = "N/A", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .FixedValue= 0, 
    .DefaultValue.Real64_Val = 1.0, 
    .MinValue.Real64_Val = 0.0, 
    .MaxValue.Real64_Val = 1.0 
  },
  [52] = {
    .Name = "Tr", // new
    .Description = "Power measurement transducer time constant", 
    .Unit = "s", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .FixedValue = 0, 
    .DefaultValue.Real64_Val = 0.001, 
    .MinValue.Real64_Val = 0.0, 
    .MaxValue.Real64_Val = 0.1 
  },
  [53] = {
    .Name = "Lchoke", 
    .Description = "Series filter inductance", 
    .Unit = "H", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .FixedValue = 0, 
    .DefaultValue.Real64_Val = 0.0001, 
    .MinValue.Real64_Val = 0.000001, 
    .MaxValue.Real64_Val = 10.0 
  },
  [54] = {
    .Name = "Rchoke", // new
    .Description = "Series filter resistance", 
    .Unit = "Ohm", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .FixedValue = 0, 
    .DefaultValue.Real64_Val = 0.00075, 
    .MinValue.Real64_Val = 0.000001, 
    .MaxValue.Real64_Val = 10.0 
  },
  [55] = {
    .Name = "Cfilt", // new
    .Description = "Parallel wye filter capacitance", 
    .Unit = "F", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .FixedValue = 0, 
    .DefaultValue.Real64_Val = 0.0015, 
    .MinValue.Real64_Val = 0.000001, 
    .MaxValue.Real64_Val = 10.0 
  },
  [56] = {
    .Name = "Rdamp", // new
    .Description = "Parallel wye filter series resistance", 
    .Unit = "Ohm", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .FixedValue = 0, 
    .DefaultValue.Real64_Val = 0.01667, 
    .MinValue.Real64_Val = 0.000001, 
    .MaxValue.Real64_Val = 10.0 
  },
  [57] = {
    .Name = "Tv", // new
    .Description = "Voltage control filter time constant", 
    .Unit = "s", 
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, 
    .FixedValue = 0, 
    .DefaultValue.Real64_Val = 0.010, 
    .MinValue.Real64_Val = 0.0, 
    .MaxValue.Real64_Val = 0.1 
  }
};

IEEE_Cigre_DLLInterface_Model_Info Model_Info = {
  .DLLInterfaceVersion = { 1, 1, 0, 0},         // Release number of the API 
  // used during code generation 
  .ModelName = "IBR-Average-Model",             // Model name   
  .ModelVersion = "1.1.0.5",                    // Model version   
  .ModelDescription = "GFD-IBR-Average",        // Model description 
  .GeneralInformation= "General Information",   // General information
  .ModelCreated = "September 21, 2023",         // Model created on  
  .ModelCreator = "EPRI",                       // Model created by     
  .ModelLastModifiedDate= "February 27, 2026",  // Model last modified on  
  .ModelLastModifiedBy = "IEEE EMTIOP WG",      // Model last modified by 
  .ModelModifiedComment = "Remove currTime input, edit parameter descriptions, add Pout and Qout\nAdd Vref input signal and more filter parameters\nFix choke units, Q control, AW clamps\nPre-windup protection for Qcl, added Tv", // Model modified comment 
  .ModelModifiedHistory = "Second instance",    // Model modified history 
  .FixedStepBaseSampleTime = 0.00001,           // Time Step sampling time (sec)  
  // Inputs 
  .NumInputPorts = 15,                          // Number of Input Signals 
  .InputPortsInfo = InputSignals,               // Inputs structure defined above  
  // Outputs 
  .NumOutputPorts = 15,                         // Number of Output Signals 
  .OutputPortsInfo = OutputSignals,             // Outputs structure defined above 
  // Parameters 
  .NumParameters = 58,                          // Number of Parameters 
  .ParametersInfo = Parameters,                 // Parameters structure defined above
   // Number of State Variables 
  .NumIntStates = 0,                            // Number of Integer states
  .NumFloatStates = 0,                          // Number of Float states
  .NumDoubleStates = 84                         // Number of Double states
};

// Subroutines that can be called by the main power system program 

__declspec(dllexport) const IEEE_Cigre_DLLInterface_Model_Info* __cdecl Model_GetInfo () {
// Returns Model Information 
  return &Model_Info;
};

__declspec(dllexport) int32_T __cdecl Model_CheckParameters(IEEE_Cigre_DLLInterface_Instance* instance) {
/* Checks the parameters on the given range 
   Arguments: Instance specific model structure containing Inputs, Parameters and Outputs 
   Return: Integer status O (normal), 1 if messages are written, 2 for errors.
   See IEEE_Cigre_DLLInterface types.h 
*/

// Parameter checks done by the program 
// Note - standard minimax checks should be done by the higher level GUI/Program 
  MyModelParameters* parameters = (MyModelParameters*)instance->Parameters;

  double VLLbase = parameters->VLLbase;
  double Sbase = parameters->Sbase;
  double Tflt_v = parameters->Tflt_v;
  double Vflt_flag = parameters->Vflt_flag;
  double Tflt_i = parameters->Tflt_i;
  double Iflt_flag = parameters->Iflt_flag;
  double Cur1_flag = parameters->Cur1_flag;
  double k_PLL = parameters->k_PLL;
  double KpPLL = parameters->KpPLL;
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
  double fdbd1 = parameters->fdbd1;
  double fdbd2= parameters->fdbd2;
  double Ddn = parameters->Ddn;
  double Dup = parameters->Dup;
  double Tp_droop = parameters->Tp_droop;
  double Vdc_flag = parameters->Vdc_flag;
  double f_flag = parameters->f_flag;
  double Id_frz_flag = parameters->Id_frz_flag;
  double Ilim_pu = parameters->Ilim_pu;
  double Kv_p = parameters->Kv_p;
  double Kv_i = parameters->Kv_i;
  double Qmin = parameters->Qmin;
  double Qmax = parameters->Qmax;
  double Kq_p = parameters->Kq_p;
  double Kq_i = parameters->Kq_i;
  double dbhv_frt = parameters->dbhv_frt;
  double dblv_frt = parameters->dblv_frt;
  double Kqv1 = parameters->Kqv1;
  double Qctl_CL_flag = parameters->Qctl_CL_flag;
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
  double Tau_Vff = parameters->Tau_Vff;
  double Vff_flag = parameters->Vff_flag;
  double Tr = parameters->Tr;
  double Lchoke = parameters->Lchoke;
  double Rchoke = parameters->Rchoke;
  double Cfilt = parameters->Cfilt;
  double Rdamp = parameters->Rdamp;
  double IR_flag = parameters->IR_flag;
  double Tv = parameters->Tv;
  // 
  double delt = Model_Info.FixedStepBaseSampleTime;

  int bWarning = 0;
  int bError = 0;

  ErrorMessage[0] = '\0';

  if ((1.0 / KiPLL) < 2.0 * delt) {
    // write error message 
    sprintf_s (ErrorMessage, sizeof(ErrorMessage), "GFL-IBR Error - Parameter KiPLL is %f , \
but has been reset to be reciprocal of 2 times the time step: %f \n", KiPLL, delt);
    parameters->KiPLL = 1.0 / (2.0 * delt);
    bWarning = 1;
  } 
  if ((1.0 / Ki_Vdc) < 2.0 * delt) { 
    // write error message 
    sprintf_s(ErrorMessage, sizeof(ErrorMessage), "GFL-IBR Error - Parameter Ki_Vdc is: %f, \
but has been reset to be reciprocal of 2 times the time step %f \n", Ki_Vdc, delt);
    parameters->Ki_Vdc = 1.0 / (2.0 * delt);
    bWarning = 1;
  } 
  if ((1.0 / Kv_i) < 2.0 * delt) { 
    // write error message 
    sprintf_s (ErrorMessage, sizeof(ErrorMessage), "GFL-IBR Error - Parameter KiP is: %f, \
but has been reset to be reciprocal of 2 times the time step: %f .\n", Kv_i, delt);
    parameters->Kv_i = 1.0 / (2.0 * delt);
    bWarning = 1;
  } 
  if ((1.0 / Kq_i) < 2.0 * delt) {
    // write error message 
    sprintf_s (ErrorMessage, sizeof(ErrorMessage), "GFL-IBR Error - Parameter KiQ is: %f, \
but has been reset to be reciprocal of 2 times the time step.%f .\n", Kq_i, delt);
    parameters->Kq_i = 1.0 / (2.0 * delt);
    bWarning = 1;
  }
  if ((1.0 / Kcc_i) < 2.0 * delt) {
    // write error message 
    sprintf_s(ErrorMessage, sizeof(ErrorMessage), "GFL-IBR Error - Parameter KiV is: %f, \
but has been reset to be reciprocal of 2 times the time step: %f .\n", Kcc_i, delt);
    parameters->Kcc_i = 1.0 / (2.0 * delt);
    bWarning = 1;
  }
  instance->LastGeneralMessage = ErrorMessage;
  if (bError) {
    return IEEE_Cigre_DLLInterface_Return_Error;
  }
  if (bWarning) {
    return IEEE_Cigre_DLLInterface_Return_Message;
  }
  return IEEE_Cigre_DLLInterface_Return_OK;
};

// -------------------------------------------------------------------------------------------
__declspec(dllexport) int32_T __cdecl Model_Initialize(IEEE_Cigre_DLLInterface_Instance* instance) {

/* Initializes the system by resetting the internal states 
   Arguments.Instance specific model structure containing Inputs, Parameters and Outputs 
   Return: Integer status 0 (normal), 1 if messages are written, 2 for errors.
   See IEEE_Cigre_DLLInterface_types.h 
*/ 

// Note that the initial conditions for all models are determined by the main calling program 
// and are passed to this routine via the instance->Externa!Outputs vector.
// instance->External Outputs is normally the output of this routine, but in the first time step 
// the main program must set the instance ExternalOutputs to initial values.

  MyModelParameters* parameters = (MyModelParameters*)instance->Parameters;

  // Retrieve variables from Input, Output and State 
  double VLLbase = parameters->VLLbase;
  double Sbase = parameters->Sbase;
  double Tflt_v = parameters->Tflt_v;
  double Vflt_flag = parameters->Vflt_flag;
  double Tflt_i = parameters->Tflt_i;
  double Iflt_flag = parameters->Iflt_flag;
  double Cur1_flag = parameters->Cur1_flag;
  double k_PLL = parameters->k_PLL;
  double KpPLL = parameters->KpPLL;
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
  double fdbd1 = parameters->fdbd1;
  double fdbd2 = parameters->fdbd2;
  double Ddn = parameters->Ddn;
  double Dup = parameters->Dup;
  double Tp_droop = parameters->Tp_droop;
  double Vdc_flag = parameters->Vdc_flag;
  double f_flag = parameters->f_flag;
  double Id_frz_flag = parameters->Id_frz_flag;
  double Ilim_pu = parameters->Ilim_pu;
  double Kv_p = parameters->Kv_p;
  double Kv_i = parameters->Kv_i;
  double Qmin = parameters->Qmin;
  double Qmax = parameters->Qmax;
  double Kq_p = parameters->Kq_p;
  double Kq_i = parameters->Kq_i;
  double dbhv_frt = parameters->dbhv_frt;
  double dblv_frt = parameters->dblv_frt;
  double Kqv1 = parameters->Kqv1;
  double Qctl_CL_flag = parameters->Qctl_CL_flag;
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
  double Tau_Vff = parameters->Tau_Vff;
  double Vff_flag = parameters->Vff_flag;
  double Tr = parameters->Tr;
  double Lchoke = parameters->Lchoke;
  double Rchoke = parameters->Rchoke;
  double Cfilt = parameters->Cfilt;
  double Rdamp = parameters->Rdamp;
  double IR_flag = parameters->IR_flag;
  double Tv = parameters->Tv;

  double delt = Model_Info.FixedStepBaseSampleTime;
 
  MyModelInputs* inputs = (MyModelInputs*)instance->ExternalInputs;
  double Vta = inputs->Vta;
  double Vtb = inputs->Vtb;
  double Vtc = inputs->Vtc;
  double I1a = inputs->I1a;
  double I1b = inputs->I1b;
  double I1c = inputs->I1c;
  double I2a = inputs->I2a;
  double I2b = inputs->I2b;
  double I2c = inputs->I2c;
  double Idc = inputs->Idc;
  double VdcMPPT = inputs->VdcMPPT;
  double Pref = inputs->Pref;
  double Qref = inputs->Qref;
  double Vdc_meas = inputs->Vdc_meas;
  double Vref = inputs->Vref;

  // Working back from initial output 

  MyModelOutputs* outputs= (MyModelOutputs*) instance->ExternalOutputs;
  double m_a = outputs->m_a;
  double m_b = outputs->m_b;
  double m_c = outputs->m_c;
  double FreqPLL = outputs->FreqPLL;
  double ID1 = outputs->ID1;
  double IQ1 = outputs->IQ1;
  double ID2 = outputs->ID2;
  double IQ2 = outputs->IQ2;
  double VD1 = outputs->VD1;
  double VQ1 = outputs->VQ1;
  double VD2 = outputs->VD2;
  double VQ2 = outputs->VQ2;
  double FRT_flag = outputs->FRT_flag;
  double Pout = outputs->Pout;
  double Qout = outputs->Qout;

  ErrorMessage [0]= '\0';

  // save state variables 
  instance->DoubleStates[0]  = 0.0;
  instance->DoubleStates[1]  = 0.0;
  instance->DoubleStates[2]  = 0.0;
  instance->DoubleStates[3]  = 0.0;
  instance->DoubleStates[4]  = 0.0;
  instance->DoubleStates[5]  = 0.0;
  instance->DoubleStates[6]  = 0.0;
  instance->DoubleStates[7]  = 0.0;
  instance->DoubleStates[8]  = 0.0;
  instance->DoubleStates[9]  = 0.0;
  instance->DoubleStates[10] = 0.0;
  instance->DoubleStates[11] = 0.0;
  instance->DoubleStates[12] = 0.0;
  instance->DoubleStates[13] = 0.0;
  instance->DoubleStates[14] = 0.0;
  instance->DoubleStates[15] = 0.0;
  instance->DoubleStates[16] = 0.0;
  instance->DoubleStates[17] = 0.0;
  instance->DoubleStates[18] = 0.0;
  instance->DoubleStates[19] = TWOPI * 60; // Omega_PLL
  instance->DoubleStates[20] = 0.0;
  instance->DoubleStates[21] = 0.0;
  instance->DoubleStates[22] = 0.0;
  instance->DoubleStates[23] = 0.0;
  instance->DoubleStates[24] = 0.0;
  instance->DoubleStates[25] = 0.0;
  instance->DoubleStates[26] = 0.0;
  instance->DoubleStates[27] = 0.0;
  instance->DoubleStates[28] = 0.0;
  instance->DoubleStates[29] = 0.0;
  instance->DoubleStates[30] = 0.0;
  instance->DoubleStates[31] = 0.0;
  instance->DoubleStates[32] = 0.0;
  instance->DoubleStates[33] = 0.0;
  instance->DoubleStates[34] = 0.0;
  instance->DoubleStates[35] = 0.0;
  instance->DoubleStates[36] = 0.0;
  instance->DoubleStates[37] = 0.0;
  instance->DoubleStates[38] = 0.0;
  instance->DoubleStates[39] = 0.0;
  instance->DoubleStates[40] = 0.0;
  instance->DoubleStates[41] = 0.0;
  instance->DoubleStates[42] = 0.0;
  instance->DoubleStates[43] = 0.0;
  instance->DoubleStates[44] = 0.0;
  instance->DoubleStates[45] = 0.0;
  instance->DoubleStates[46] = 60.0;  // f_PLL
  instance->DoubleStates[47] = 0.0;
  instance->DoubleStates[48] = 0.0;
  instance->DoubleStates[49] = 0.0;
  instance->DoubleStates[50] = 0.0;
  instance->DoubleStates[51] = 0.0;
  instance->DoubleStates[52] = 0.0;
  instance->DoubleStates[53] = 0.0;
  instance->DoubleStates[54] = 0.0;
  instance->DoubleStates[55] = 0.0;
  instance->DoubleStates[56] = 0.0;
  instance->DoubleStates[57] = 0.0;
  instance->DoubleStates[58] = 0.0;
  instance->DoubleStates[59] = 0.0;
  instance->DoubleStates[60] = 0.0;
  instance->DoubleStates[61] = 0.0;
  instance->DoubleStates[62] = 0.0;
  instance->DoubleStates[63] = 0.0;
  instance->DoubleStates[64] = 0.0;
  instance->DoubleStates[65] = 0.0;
  instance->DoubleStates[66] = 0.0;
  instance->DoubleStates[67] = 0.0;
  instance->DoubleStates[68] = 0.0;
  instance->DoubleStates[69] = 0.0;
  instance->DoubleStates[70] = 0.0;
  instance->DoubleStates[71] = 0.0;
  instance->DoubleStates[72] = 0.0;
  instance->DoubleStates[73] = 0.0;
  instance->DoubleStates[74] = 0.0;
  instance->DoubleStates[75] = 0.0;
  instance->DoubleStates[76] = 0.0;
  instance->DoubleStates[77] = 0.0;
  instance->DoubleStates[78] = 0.0;
  instance->DoubleStates[79] = 0.0;
  instance->DoubleStates[80] = 0.0;
  instance->DoubleStates[81] = 0.0;
  instance->DoubleStates[82] = 0.0;
  instance->DoubleStates[83] = 0.0;

  instance->LastGeneralMessage = ErrorMessage;
  return IEEE_Cigre_DLLInterface_Return_OK;
};

// Integrator with time constant T 
double INTEGRATOR(double T, double x, double x_old, double y_old, double delt) { 
  double y;
  double Kint = (delt * 0.5) / T;
  y = y_old + Kint * (x + x_old);
  return y;
};

// Integrator with time constant T and reset value rst_val 
double INTEGRATORRESET(double T, double rst_flag, double rst_val, double x, double x_old, double y_old, double delt) { 
  double y;
  double Kint = (delt * 0.5) / T;
  y = y_old + Kint * (x + x_old);
  if (rst_flag) {
    y = rst_val;
  }
  return y;
};

// PI with gain K and integrator with time constant T 
double PICONTROLLER(double K, double T, double x, double x_old, double y_old, double delt) { 
  double y;
  double Kint = (delt * 0.5) / T;
  y = y_old + K * (x - x_old) + Kint * (x + x_old);
  return y;
};

// first order lag with gain G, time constant T, with non-windup internal limits 
double REALPOLE(double G, double T, double x, double x_old, double y_old, double ymin, double ymax, double delt) {
  double y;
  double Kint = (delt * 0.5) / T;
  y = (y_old + Kint * (G * x + G * x_old - y_old)) / (1.0 + Kint);
  if (y > ymax) y = ymax;
  if (y < ymin) y = ymin;
  return y;
};

// second order complex pole with gain G, time constant T, damping B. Only first state represented as C function 
double CMPLXPOLE(double G, double T, double B, double x, double x_old, double yp_old, double y_old, double delt) { 
  double yp;
  double Kint = (delt * 0.5) / T;
  yp = ((1 - Kint * B - Kint * Kint) * yp_old + Kint * (G * x + G * x_old - 2 * y_old)) 
    / (1 + Kint * B + Kint * Kint);
  // In main code, use yp to evaluate integration of final output y 
  return yp;
};

// first order differential pole with gain G, time constant T. Total numerator gain is G*T 
double DIFFPOLE(double G, double T, double x, double x_old, double y_old, double delt) { 
  double y;
  double Kint = (delt * 0.5) / T;
  y = (G * (x - x_old) + (1 - Kint) * y_old) / (1 + Kint);
  return y;
};

// first order leadlag with gain G, lead time constant T1, lag time constant T2, with non windup internal limits 
double LEADLAG(double G, double T1, double T2, double x, double x_old, double y_old, double ymin, double ymax, double delt) { 
  double y;
  double Kint = (delt * 0.5) / T2;
  if (T1 < 1.0E-8) { 
    y = REALPOLE(G, T2, x, x_old, y_old, ymin, ymax, delt);
  } else { 
    y = (y_old + (G * T1 / T2) * (x - x_old) + Kint * (G * x + G * x_old - y_old)) / (1.0 + Kint);
    if (y > ymax) y = ymax;
    if (y < ymin) y = ymin;
  }
  return y;
};

// rectangular to polar transformation 
void RECTANGULAR2POLAR(double real, double imag, double* mag, double* ang) { 
  *mag = sqrt (real*real + imag*imag);
  *ang = atan2 (imag, real);
};

// polar to rectangular transformation 
void POLAR2RECTANGULAR(double mag, double ang, double* real, double* imag) { 
  *real = mag * cos(ang);
  *imag = mag * sin(ang);
};

// comparator to compare two inputs 
double COMPARATOR(double input_A, double input_B) {
  return ((input_A > input_B) ? 1 : 0);
};

// limiter to limit the output within bounds 
double LIMITER(double upper_limit, double lower_limit, double dat) { 
  if (dat > upper_limit) 
    return upper_limit;
  if (dat < lower_limit) 
    return lower_limit;
  return dat;
};

// selector selects an input based on flag condition , input_A if FLAG is true 
double SELECTOR(double input_A, double input_B, double FLAG) { 
  return (FLAG ? input_A : input_B);
};

// sample and hold block to hold the output to its last value if a flag is provided 
void SAMPLEHOLD(double signal_in , double FLAG, double FLAG_OLD, double* sample_hold) {
  if (FLAG_OLD == 1 && FLAG == 1) { 
    sample_hold[0] = sample_hold[1];
  } else { 
    sample_hold[0] = signal_in;
    sample_hold[1] = signal_in;
  }
};

// for DB block 
double DB(double signal_in, double f_dbd1, double f_dbd2) { 
  double sum1 = (signal_in - f_dbd2) * COMPARATOR(signal_in, f_dbd2);
  double sum2 = (signal_in - f_dbd1) * COMPARATOR(f_dbd1, signal_in);
  return (sum1 + sum2);
};

// deadband, no output is generated if input lies within the deadband range .
double DEADBAND(double signal_in, double db_range, double db_gain, double db_offest) {
  if (fabs(signal_in) > db_range / 2.0) 
    return (signal_in > 0 ? db_offest + db_gain * (signal_in - db_range / 2.0) : 
            -db_offest + db_gain * (signal_in + db_range / 2.0));
  else 
    return 0;
};

// rate limiter to limit the rate of change of output 
double RATELIMITER(double f_input, double Oldf_output, double rate_up, double rate_down, double delt) { 
  double rate = (f_input - Oldf_output) / delt;
  if (rate > rate_up) 
    return (rate_up * delt + Oldf_output);
  if (rate < -rate_down) 
    return (-rate_down * delt + Oldf_output);
  return f_input;
};

// to convert DQ quantities to ABC 
void DQ2ABC(double fd, double fq, double phi, double* fabc) { 
  fabc[0] = (fd * cos(phi) - fq * sin(phi));
  fabc[1] = (fd * cos(phi - TWOPI3) - fq * sin(phi - TWOPI3));
  fabc[2] = (fd * cos(phi + TWOPI3) - fq * sin(phi + TWOPI3));
};

// to convert ABC quantities to Alpha-Beta 
void ABC2ALPHABETA(double fa, double fb, double fc, double* alpha_beta) { 
  alpha_beta[0] = (fa - 0.5 * fb - 0.5 * fc) * TWO3RD;
  alpha_beta[1] = (fb * SQRT3H - fc * SQRT3H) * TWO3RD;
};

// to convert ABC to DQ 
void ABC2DQ(double fa, double fb, double fc, double phi, double* fDQ) { 
  fDQ[0] = TWO3RD * (cos(phi) * fa + cos(phi - TWOPI3) * fb + cos(phi + TWOPI3) * fc);
  fDQ[1] = TWO3RD * (-sin (phi) * fa - sin(phi - TWOPI3) * fb - sin(phi + TWOPI3) * fc);
};

// to convert alpha beta to DQ 
void ALPHABETA2DQ(double falpha, double fbeta, double theta, double* fDQ) { 
  fDQ[0] = falpha * cos(theta) + fbeta * sin(theta);
  fDQ[1] = -falpha * sin(theta) + fbeta * cos(theta);
};

// to calculate mod of 2 float numbers 
double MODULO(double signal_in, double den) { 
  double y;
  y = signal_in - floor(signal_in / den) * den;
  return y;
};

// real power using alpha beta 
double REALPOWER(double v_alpha, double i_alpha, double v_beta, double i_beta) {
  double y;
  y = v_alpha * i_alpha + v_beta * i_beta;
  return y;
};

// reactive power using alpha beta 
double REACTIVEPOWER(double v_alpha, double i_alpha, double v_beta, double i_beta) { 
  double y;
  y = -v_alpha * i_beta + v_beta * i_alpha;
  return y;
};

// anti-windup clamp if PI output (y) has been limited, and the integrator output is same sign as its input
double AWCLAMP(double ki, double y, double ymax, double ymin, double iin, double iout) {
//  if (y >= ymax || y <= ymin) {
//    if (iin * iout > 0.0) {
//      return 0.0;
//    }
//  }
  double next_iin = ki * iin;
  if (y >= ymax && next_iin > 0.0) return 0.0;
  if (y <= ymin && next_iin < 0.0) return 0.0;
  return ki;
}

//---------------------------------------------------------------- 

__declspec(dllexport) int32_T __cdecl Model_Outputs(IEEE_Cigre_DLLInterface_Instance* instance) {

/* Calculates output equation 
  Arguments: Instance specific model structure containing Inputs, Parameters and Outputs 
  Return: Integer status 0 (normal), 1 if messages are written, 2 for errors.
  See IEEE_Cigre_DLLInterface_types.h 
*/ 

  ErrorMessage [0]= '\0';

  MyModelParameters* parameters = (MyModelParameters*)instance->Parameters;
  // Retrieve variables from Input, Output and State 
  double VLLbase = parameters->VLLbase;
  double Sbase = parameters->Sbase;
  double Tflt_v = parameters->Tflt_v;
  double Vflt_flag = parameters->Vflt_flag;
  double Tflt_i = parameters->Tflt_i;
  double Iflt_flag = parameters->Iflt_flag;
  double Cur1_flag = parameters->Cur1_flag;
  double k_PLL = parameters->k_PLL;
  double KpPLL = parameters->KpPLL;
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
  double fdbd1 = parameters->fdbd1;
  double fdbd2 = parameters->fdbd2;
  double Ddn = parameters->Ddn;
  double Dup = parameters->Dup;
  double Tp_droop = parameters->Tp_droop;
  double Vdc_flag = parameters->Vdc_flag;
  double f_flag = parameters->f_flag;
  double Id_frz_flag = parameters->Id_frz_flag;
  double Ilim_pu = parameters->Ilim_pu;
  double Kv_p = parameters->Kv_p;
  double Kv_i = parameters->Kv_i;
  double Qmin = parameters->Qmin;
  double Qmax = parameters->Qmax;
  double Kq_p = parameters->Kq_p;
  double Kq_i = parameters->Kq_i;
  double dbhv_frt = parameters->dbhv_frt;
  double dblv_frt = parameters->dblv_frt;
  double Kqv1 = parameters->Kqv1;
  double Qctl_CL_flag = parameters->Qctl_CL_flag;
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
  double Tau_Vff = parameters->Tau_Vff;
  double Vff_flag = parameters->Vff_flag;
  double Tr = parameters->Tr;
  double Lchoke = parameters->Lchoke;
  double Rchoke = parameters->Rchoke;
  double Cfilt = parameters->Cfilt;
  double Rdamp = parameters->Rdamp;
  double IR_flag = parameters->IR_flag;
  double Tv = parameters->Tv;

  double delt = Model_Info.FixedStepBaseSampleTime;

  MyModelInputs* inputs = (MyModelInputs*)instance->ExternalInputs;
  double Vta = inputs->Vta;
  double Vtb = inputs->Vtb;
  double Vtc = inputs->Vtc;
  double I1a = inputs->I1a;
  double I1b = inputs->I1b;
  double I1c = inputs->I1c;
  double I2a = inputs->I2a;
  double I2b = inputs->I2b;
  double I2c = inputs->I2c;
  double Idc = inputs->Idc;
  double VdcMPPT = inputs->VdcMPPT;
  double Pref = inputs->Pref;
  double Qref = inputs->Qref;
  double Vdc_meas = inputs->Vdc_meas;
  double Vref = inputs->Vref;
  double currTIME = instance->Time;

  double OldTIME = instance->DoubleStates[0];  // not used
  // Signal Processing block 
  double OldVta_pu = instance->DoubleStates[1];
  double OldVta_flt1 = instance->DoubleStates[2];
  double OldVtb_pu = instance->DoubleStates[3];
  double OldVtb_flt1 = instance->DoubleStates[4];
  double OldVtc_pu = instance->DoubleStates[5];
  double OldVtc_flt1 = instance->DoubleStates[6];
  double OldI1a_pu = instance->DoubleStates[7];
  double OldI1a_flt1 = instance->DoubleStates[8];
  double OldI1b_pu = instance->DoubleStates[9];
  double OldI1b_flt1 = instance->DoubleStates[10];
  double OldI1c_pu = instance->DoubleStates[11];
  double OldI1c_flt1 = instance->DoubleStates[12];
  double OldI2a_pu = instance->DoubleStates[13];
  double OldI2a_flt1 = instance->DoubleStates[14];
  double OldI2b_pu = instance->DoubleStates[15];
  double OldI2b_flt1 = instance->DoubleStates[16];
  double OldI2c_pu = instance->DoubleStates[17];
  double OldI2c_flt1 = instance->DoubleStates[18];
  double OldOmega_PLL = instance->DoubleStates[19];
  double OldVt_alpha = instance->DoubleStates[20];
  double OldVt_alpha_pr = instance->DoubleStates[21];
  double OldVt_qalpha_pr = instance->DoubleStates[22];
  double OldVt_beta = instance->DoubleStates[23];
  double OldVt_beta_pr = instance->DoubleStates[24];
  double OldVt_qbeta_pr = instance->DoubleStates[25];
  double OldTheta_PLL = instance->DoubleStates[26];
  double OldDelOmegaIin = instance->DoubleStates[27];
  double OldDelOmegaI = instance->DoubleStates[28];
  double OldTheta_DSOGIPLLcont = instance->DoubleStates[29];
  double OldId1_ref = instance->DoubleStates[30];
  double OldOldId1_ref = instance->DoubleStates[31];
  double OldId1r_flt = instance->DoubleStates[32];
  double OldIq1_ref = instance->DoubleStates[33];
  double OldOldIq1_ref = instance->DoubleStates[34];
  double OldIq1r_flt = instance->DoubleStates[35];
  double OldId2_ref = instance->DoubleStates[36];
  double OldOldId2_ref = instance->DoubleStates[37];
  double OldId2r_flt = instance->DoubleStates[38];
  double OldIq2_ref = instance->DoubleStates[39];
  double OldOldIq2_ref = instance->DoubleStates[40];
  double OldIq2r_flt = instance->DoubleStates[41];
  // P: Q control block 
  double OldId1_FFin = instance->DoubleStates[42];
  double OldId1_FFnolimit = instance->DoubleStates[43];
  double OldId1_VdcIin = instance->DoubleStates[44];
  double OldId1_VdcI = instance->DoubleStates[45];
  double Oldf_PLL = instance->DoubleStates[46];
  double Oldfpu_flt = instance->DoubleStates[47];
  double OldVtd_1_y = instance->DoubleStates[48];
  double OldIdref_droop_x = instance->DoubleStates[49];
  double OldIdref_droop = instance->DoubleStates[50];
  double OldId1ref_hold = instance->DoubleStates[51];
  double OldIq_VtdCLIin = instance->DoubleStates[52];
  double OldIq_VtdCLI = instance ->DoubleStates[53];
  double OldIq_QCLIin = instance->DoubleStates[54];
  double OldIq_QCLI = instance->DoubleStates[55];
  double OldIq1_i = instance->DoubleStates[56];
  // Current Control 
  double OldIdref_1 = instance->DoubleStates[57];
  double Olductrld_1Iin = instance->DoubleStates[58];
  double Olductrld_1I = instance->DoubleStates[59];
  double OldIqref_1 = instance ->DoubleStates[60];
  double Olductrlq_1Iin = instance->DoubleStates[61];
  double Olductrlq_1I = instance->DoubleStates[62];
  double OldIdref_2 = instance->DoubleStates[63];
  double Olductrld_2Iin = instance->DoubleStates[64];
  double Olductrld_2I = instance->DoubleStates[65];
  double OldIqref_2 = instance->DoubleStates[66];
  double Olductrlq_2Iin = instance->DoubleStates[67];
  double Olductrlq_2I = instance->DoubleStates[68];
  double OldVtd_1 = instance->DoubleStates[69];
  double OldVtd_1y = instance->DoubleStates[70];
  double OldVtq_1 = instance ->DoubleStates[71];
  double OldVtq_1y = instance->DoubleStates[72];
  double OldVtd_2 = instance->DoubleStates[73];
  double OldVtd_2y = instance->DoubleStates[74];
  double OldVtq_2 = instance->DoubleStates[75];
  double OldVtq_2y = instance->DoubleStates[76];
  // Flags for SH 
  double OldFRT_flag = instance->DoubleStates[77];
  // Added states for SH 
  double OldId1ref_hold_SH = instance->DoubleStates[78];
  double OldIq1_i_SH = instance->DoubleStates[79];
  // added states for P, Q measurement
  double OldPelec = instance->DoubleStates[80];
  double OldPelec_meas = instance->DoubleStates[81];
  double OldQelec = instance->DoubleStates[82];
  double OldQelec_meas = instance->DoubleStates[83];

  MyModelOutputs* outputs = (MyModelOutputs*)instance->ExternalOutputs;

  // local variables 

  // Signal Processing block 
  double Vdq_base;
  double Idq_base;
  double Vta_pu, Vtb_pu, Vtc_pu;
  double I1a_pu, I1b_pu, I1c_pu;
  double I2a_pu, I2b_pu, I2c_pu;
  double Vta_flt1, Vtb_flt1, Vtc_flt1;
  double I1a_flt1, I1b_flt1, I1c_flt1;
  double I2a_flt1, I2b_flt1, I2c_flt1;
  double Vta_flt, Vtb_flt, Vtc_flt;
  double I1a_flt, I1b_flt, I1c_flt;
  double I2a_flt, I2b_flt, I2c_flt;
  double Ia_flt, Ib_flt, Ic_flt;
  double Vt_alphabeta[2], Vt_alpha, Vt_beta;
  double Vt_alpha_pr, Vt_qalpha_pr;
  double Vt_beta_pr, Vt_qbeta_pr;
  double Vt_alpha_pos, Vt_beta_pos;
  double Vt_alpha_neg, Vt_beta_neg;
  double Vtdq_1[2], Vtd_1, Vtq_1;
  double Vtdq_2[2], Vtd_2, Vtq_2;
  double DelOmegaP, DelOmegaIin, DelOmegaI, DelOmega, Omega_PLL;
  double Theta_DSOGIPLLcont, Theta_PLL;
  double Id1r_flt, Iq1r_flt, Id2r_flt, Iq2r_flt;
  double Idq1_flt[2], Idq2_flt[2];
  double Id_1, Iq_1, Id_2, Iq_2;
  double I1_alphabeta[2], I2_alphabeta[2];
  //double Piab_pu, Qiab_pu, Ptab_pu, Qtab_pu;
  double Pelec, Pelec_meas, Qelec, Qelec_meas;
  // P, Q block 
  double Vdq1;
  double FRT_flag;
  double Startup_flag;
  double Id1_FFnolimit, Id1_FFin, Id1_FF;
  double Vdc_ref, Vdc_e;
  double Id1_VdcP, Id1_VdcIin, Id1_VdcI, Id1_Vdc, Id1ref_Vdc;
  double fpu_flt;
  double f_PLL;
  double Droop_down, Droop_up;
  double Pref_droop;
  double Vtd_1_y; 
  double Idref_droop_x, Idref_droop;
  double Id1ref_P;
  double Id_droop1, Id_droop;
  double Id1ref_cont, Id1ref_hold, Id1ref_nolimit, Id1ref, Id1ref_hold_SH[2];
  double Iq_VtdCLe, Iq_VtdCLP, Iq_VtdCLIin, Iq_VtdCLI, Iq_VtdCL;
  double Iq_QCLe, Iq_QCLP, Iq_QCLIin, Iq_QCLI, Iq_QCL;
  double Iq_QOL;
  double Iq1_frt;
  double Iq_Qctl;
  double Iq1_icont, Iq1_i, Iq1_i_SH[2];
  double Iq1ref;
  double Vdq_2mag, Vdq_2ang;
  double Idq2_refmag, Idq2_refang;
  double Id2ref, Iq2ref;
  double I2m_ref_upper;
  double I2m_refmag, Iq2ref_Lang;
  double I1m_ref, I2m_ref;
  double Ilim_L;
  double IROL_flag;
  double scale, scale_phmax;
  double I2m_ref_L;
  double Id1ref_L, Iq1ref_L, Id2ref_L, Iq2ref_L, Id1max_FRT;
  double MagIdq1, MagIdq2, AngIdq_12;
  double Ia_max, Ib_max, Ic_max, Iph_max, Ilim_phmax;
  double IOL_flag;
  double MagIdqref_1_L, AngIdqref_1_L, MagIdqref_2_L, AngIdqref_2_L;
  double Id1ref_L2, Iq1ref_L2, Id2ref_L2, Iq2ref_L2;
  double Id1ref_max, Id1ref_L1, Iq1ref_L1;
  double Idref_1, Iqref_1, Idref_2, Iqref_2;
  // Current Control 
  double t_release;
  double current_control;
  double Iramp_up;
  double Id1_ref, Iq1_ref, Id2_ref, Iq2_ref;
  double Id1_e, Iq1_e, Id2_e, Iq2_e;
  double uctrld_1P, uctrld_1Iin, uctrld_1I, uctrld_1;
  double uctrlq_1P, uctrlq_1Iin, uctrlq_1I, uctrlq_1;
  double uctrld_2P, uctrld_2Iin, uctrld_2I, uctrld_2;
  double uctrlq_2P, uctrlq_2Iin, uctrlq_2I, uctrlq_2;
  double Vtd_1y, Vtq_1y, Vtd_2y, Vtq_2y;
  double Ed_1, Eq_1, Ed_2, Eq_2;
  double Eabc_1[3], Eabc_2[3];
  double Ea_m, Eb_m, Ec_m;

  // Signal Processing Block           
  // Per unit conversion             
  Vdq_base = VLLbase * SQRT23RD;
  Idq_base = (Sbase / VLLbase) * SQRT23RD;
  Vta_pu = Vta / Vdq_base * 1000;
  Vtb_pu = Vtb / Vdq_base * 1000;
  Vtc_pu = Vtc / Vdq_base * 1000;
  I1a_pu = I1a / Idq_base * 1000;
  I1b_pu = I1b / Idq_base * 1000;
  I1c_pu = I1c / Idq_base * 1000;
  I2a_pu = I2a / Idq_base * 1000;
  I2b_pu = I2b / Idq_base * 1000;
  I2c_pu = I2c / Idq_base * 1000;
 
  // Voltage Filtering 
  Vta_flt1 = REALPOLE(1, Tflt_v, Vta_pu, OldVta_pu, OldVta_flt1, -1e8, 1e8, delt);
  Vta_flt = SELECTOR(Vta_flt1, Vta_pu, Vflt_flag);
  Vtb_flt1 = REALPOLE(1, Tflt_v, Vtb_pu, OldVtb_pu, OldVtb_flt1, -1e8, 1e8, delt);
  Vtb_flt = SELECTOR(Vtb_flt1, Vtb_pu, Vflt_flag);
  Vtc_flt1 = REALPOLE(1, Tflt_v, Vtc_pu, OldVtc_pu, OldVtc_flt1, -1e8, 1e8, delt);
  Vtc_flt = SELECTOR(Vtc_flt1, Vtc_pu, Vflt_flag);

  // Current Filtering 
  I1a_flt1 = REALPOLE(1, Tflt_i, I1a_pu, OldI1a_pu, OldI1a_flt1, -1e8, 1e8, delt);
  I1a_flt = SELECTOR(I1a_flt1, I1a_pu, Iflt_flag);
  I1b_flt1 = REALPOLE(1, Tflt_i, I1b_pu, OldI1b_pu, OldI1b_flt1, -1e8, 1e8, delt);
  I1b_flt = SELECTOR(I1b_flt1, I1b_pu, Iflt_flag);
  I1c_flt1 = REALPOLE(1, Tflt_i, I1c_pu, OldI1c_pu, OldI1c_flt1, -1e8, 1e8, delt);
  I1c_flt = SELECTOR(I1c_flt1, I1c_pu, Iflt_flag);
  I2a_flt1 = REALPOLE(1, Tflt_i, I2a_pu, OldI2a_pu, OldI2a_flt1, -1e8, 1e8, delt);
  I2a_flt = SELECTOR(I2a_flt1, I2a_pu, Iflt_flag);
  I2b_flt1 = REALPOLE(1, Tflt_i, I2b_pu, OldI2b_pu, OldI2b_flt1, -1e8, 1e8, delt);
  I2b_flt = SELECTOR(I2b_flt1, I2b_pu, Iflt_flag);
  I2c_flt1 = REALPOLE(1, Tflt_i, I2c_pu, OldI2c_pu, OldI2c_flt1, -1e8, 1e8, delt);
  I2c_flt = SELECTOR(I2c_flt1, I2c_pu, Iflt_flag);
  Ia_flt = SELECTOR(I1a_flt, I2a_flt, Cur1_flag);
  Ib_flt = SELECTOR(I1b_flt, I2b_flt, Cur1_flag);
  Ic_flt = SELECTOR(I1c_flt, I2c_flt, Cur1_flag);

  // DSOGI PLL 
  // Alpha beta transformation 
  ABC2ALPHABETA(Vta_flt, Vtb_flt, Vtc_flt, Vt_alphabeta);
  Vt_alpha = Vt_alphabeta[0];
  Vt_beta = Vt_alphabeta[1];

  // DSOGI block 
  // Alpha SOGI 
  Vt_alpha_pr = CMPLXPOLE(k_PLL, 1/OldOmega_PLL, k_PLL, Vt_alpha, OldVt_alpha, 
                          OldVt_alpha_pr, OldVt_qalpha_pr, delt);
  Vt_qalpha_pr = INTEGRATOR(1/OldOmega_PLL, Vt_alpha_pr, OldVt_alpha_pr, OldVt_qalpha_pr, delt);

  // Beta SOGI 
  Vt_beta_pr = CMPLXPOLE(k_PLL, 1/OldOmega_PLL, k_PLL, Vt_beta, OldVt_beta, 
                         OldVt_beta_pr, OldVt_qbeta_pr, delt);
  Vt_qbeta_pr = INTEGRATOR(1/OldOmega_PLL, Vt_beta_pr, OldVt_beta_pr, OldVt_qbeta_pr, delt);

  // Positive Sequence Extraction 
  Vt_alpha_pos = (Vt_alpha_pr - Vt_qbeta_pr) * 0.5;
  Vt_beta_pos = (Vt_qalpha_pr + Vt_beta_pr) * 0.5;

  // Negative Sequence Extraction 
  Vt_alpha_neg = (Vt_alpha_pr + Vt_qbeta_pr) * 0.5;
  Vt_beta_neg = (-Vt_qalpha_pr + Vt_beta_pr) * 0.5;

  // ALPHA-BETA to DQ Block 
  ALPHABETA2DQ(Vt_alpha_pos, Vt_beta_pos, OldTheta_PLL, Vtdq_1);
  Vtd_1 = Vtdq_1[0];  // Output #8, Vtd_1
  Vtq_1 = Vtdq_1[1];  // Output #9, Vtq_1 

  // ALPHA-BETA to DQ Block 
  ALPHABETA2DQ(Vt_alpha_neg, Vt_beta_neg, -OldTheta_PLL, Vtdq_2);
  Vtd_2 = Vtdq_2[0];  // Output #10, Vtd_2 
  Vtq_2 = Vtdq_2[1];  // Output #11, Vtq_2 

  // Clamped Anti Wind Up Code for Omega from Vtq_1
  DelOmegaP = Vtq_1 * KpPLL;
  DelOmegaIin = Vtq_1 * AWCLAMP (KiPLL, DelOmegaP + OldDelOmegaI, Lim_PLL, -Lim_PLL, Vtq_1, OldDelOmegaI);
  DelOmegaI = INTEGRATORRESET(1, 0, 0, DelOmegaIin, OldDelOmegaIin, OldDelOmegaI, delt);
  DelOmega = LIMITER(Lim_PLL, -Lim_PLL, DelOmegaP + DelOmegaI);

  Omega_PLL = w_nom + DelOmega;  // Output #3, Freq_PLL*TWPI 
  Theta_DSOGIPLLcont = INTEGRATOR(1, Omega_PLL, OldOmega_PLL, OldTheta_DSOGIPLLcont, delt);
  Theta_PLL = MODULO(Theta_DSOGIPLLcont, TWOPI);  // Since only DSOGI is used

  // Currents block of Signal and Processing (DDSRF approach)         
  // Inputs:   Ia_flt   Ib_flt,   Ic_flt,   Iref (Idq12ref) 
  // 1/3142 corresponds to the time constant for 500 Hz low-pass filter        
  Id1r_flt = REALPOLE(1, 1.0/3142.0, OldId1_ref, OldOldId1_ref, OldId1r_flt, -1e8, 1e8, delt);
  Iq1r_flt = REALPOLE(1, 1.0/3142.0, OldIq1_ref, OldOldIq1_ref, OldIq1r_flt, -1e8, 1e8, delt);
  Id2r_flt = REALPOLE(1, 1.0/3142.0, OldId2_ref, OldOldId2_ref, OldId2r_flt, -1e8, 1e8, delt);
  Iq2r_flt = REALPOLE(1, 1.0/3142.0, OldIq2_ref, OldOldIq2_ref, OldIq2r_flt, -1e8, 1e8, delt);

  // ABC2DQ conversion 
  ABC2DQ(Ia_flt, Ib_flt, Ic_flt, Theta_PLL, Idq1_flt);
  ABC2DQ(Ia_flt, Ib_flt, Ic_flt, -Theta_PLL, Idq2_flt);

  // Decoupling             
  Id_1 = Idq1_flt[0] - Id2r_flt * cos(Theta_PLL * 2) - Iq2r_flt * sin(Theta_PLL * 2);
  Iq_1 = Idq1_flt[1] + Id2r_flt * sin(Theta_PLL * 2) - Iq2r_flt * cos(Theta_PLL * 2);
  Id_2 = Idq2_flt[0] - Id1r_flt * cos(Theta_PLL * 2) + Iq1r_flt * sin(Theta_PLL * 2);
  Iq_2 = Idq2_flt[1] - Id1r_flt * sin(Theta_PLL * 2) - Iq1r_flt * cos(Theta_PLL * 2);

  // Power Calculations 
  // ABC to ALPHA-BETA: values used from DSOGI calculations 
  // ABC to ALPHA-BETA currents 
  ABC2ALPHABETA(I1a_flt, I1b_flt, I1c_flt, I1_alphabeta);
  ABC2ALPHABETA(I2a_flt, I2b_flt, I2c_flt, I2_alphabeta);
  if (Cur1_flag >= 0.99) { // before LCL
    Pelec = REALPOWER(Vt_alpha, I1_alphabeta[0], Vt_beta, I1_alphabeta[1]); // was Piab_pu
    Qelec = REACTIVEPOWER(Vt_alpha, I1_alphabeta[0], Vt_beta, I1_alphabeta[1]); // was Qiab_pu
  } else { // after LCL
    Pelec = REALPOWER(Vt_alpha, I2_alphabeta[0], Vt_beta, I2_alphabeta[1]); // was Ptab_pu
    Qelec = REACTIVEPOWER(Vt_alpha, I2_alphabeta[0], Vt_beta, I2_alphabeta[1]); // was Qtab_pu
  }
  // Measurement transducer for power, both output and control. TODO: Proper limits?
  Pelec_meas = REALPOLE(1.0, Tr, Pelec, OldPelec, OldPelec_meas, -1.2, 1.2, delt);
  Qelec_meas = REALPOLE(1.0, Tr, Qelec, OldQelec, OldQelec_meas, -1.2, 1.2, delt);

  // Outer P,Q LOOP
  Vdq1 = sqrt(Vtd_1 * Vtd_1 + Vtq_1 * Vtq_1);

  // Input Flag to Current Controller, Vdip logic 
  FRT_flag = (COMPARATOR((Vref - Vtd_1), dblv_frt) + COMPARATOR(dbhv_frt, (Vref - Vtd_1))) > 0;

  // Start UP Flag 
  Startup_flag = COMPARATOR(tstart_up, currTIME);
  Id1_FFin = TWO3RD * Vdc_nom * Idc * 1000;
  Id1_FFnolimit = REALPOLE(1, 0.005, Id1_FFin, OldId1_FFin, OldId1_FFnolimit, -999999, 999999, delt);
  Id1_FF = LIMITER(Idq_base * Ilim_pu, -Idq_base * Ilim_pu, Id1_FFnolimit / Vdq_base);

  Vdc_ref = SELECTOR(VdcMPPT, Vdc_nom, (VI_flag * MPPT_flag));
  Vdc_e = Vdc_ref * b_Vdc - Vdc_meas * 1000;
  Id1_VdcP = Vdc_e * Kp_Vdc;
  Id1_VdcIin = Vdc_e * AWCLAMP (Ki_Vdc, Id1_VdcP + OldId1_VdcI, Idq_base * Ilim_pu, -Idq_base * Ilim_pu, Vdc_e, OldId1_VdcI);
  Id1_VdcI = INTEGRATORRESET(1, Startup_flag, 0, Id1_VdcIin, OldId1_VdcIin, OldId1_VdcI, delt);
  Id1_Vdc = LIMITER(Idq_base * Ilim_pu, -Idq_base * Ilim_pu, Id1_VdcP + Id1_VdcI);
  Id1ref_Vdc = (-Id1_Vdc + Id1_FF) / Idq_base;

  // Droop 
  f_PLL = Omega_PLL / TWOPI;
  fpu_flt = REALPOLE(1, T_frq, f_PLL / 60.0, Oldf_PLL / 60.0, Oldfpu_flt, -999999.0, 999999.0, delt);
  Droop_down = DB(1 - fpu_flt, fdbd1, fdbd2) * Ddn;
  Droop_up = DB(1 - fpu_flt, fdbd1, fdbd2) * Dup;
  Pref_droop = LIMITER(0, -9999, Droop_down) + LIMITER(9999, 0, Droop_up);
  Vtd_1_y = REALPOLE(1.0, Tv, Vtd_1, OldVtd_1, OldVtd_1_y, -99999.0, 99999.0, delt);  // 0.01 is now adjustable as Tv
  Idref_droop_x = Pref_droop / (Vtd_1_y + 0.0001);
  Idref_droop = REALPOLE(1.0, Tp_droop, Idref_droop_x, OldIdref_droop_x, OldIdref_droop, 
                         -99999, 99999, delt);

  // Id1ref_P calculation 
  Id1ref_P = Pref / (0.0001 + Vtd_1_y);

  // Outer control id 
  Id_droop1 = SELECTOR(SELECTOR(Pref, 0, COMPARATOR(currTIME, 1)), 
                       SELECTOR(Id1ref_Vdc, Id1ref_P, Vdc_flag), Startup_flag);
  Id_droop = SELECTOR(Idref_droop, 0, f_flag);
  Id1ref_cont = Id_droop + Id_droop1;  // Id1ref_cont continuous 
  Id1ref_hold_SH[1]= OldId1ref_hold_SH;
  SAMPLEHOLD(Id1ref_cont, FRT_flag, OldFRT_flag, Id1ref_hold_SH);
  Id1ref_hold = Id1ref_hold_SH[0];  // Id1ref_hold is output of Sample and Hold 
  Id1ref_nolimit = SELECTOR(Id1ref_hold, Id1ref_cont, Id_frz_flag);
  Id1ref = LIMITER(Ilim_pu, -Ilim_pu, Id1ref_nolimit);

  // Vt Closed Loop 
  Iq_VtdCLe = SELECTOR(0, DEADBAND((Vref - Vtd_1_y), 0.001, 1, 0), FRT_flag);
  Iq_VtdCLP= Iq_VtdCLe * Kv_p;
  Iq_VtdCLIin = Iq_VtdCLe * AWCLAMP (Kv_i, Iq_VtdCLP + OldIq_VtdCLI, Qmax, Qmin, Iq_VtdCLe, OldIq_VtdCLI);
  Iq_VtdCLI = INTEGRATORRESET(1, Startup_flag, 0, Iq_VtdCLIin, OldIq_VtdCLIin, OldIq_VtdCLI, delt);
  Iq_VtdCL = LIMITER(Qmax, Qmin, Iq_VtdCLP + Iq_VtdCLI);

  // Q Closed Loop
  //Iq_QCLe = LIMITER(Qmax, Qmin, Qref) - Qelec_meas;
  Iq_QCLe = SELECTOR(0.0, LIMITER(Qmax, Qmin, Qref) - Qelec_meas, FRT_flag); // REVISIT: added pre-windup protection per figure 2-16
  Iq_QCLP = Iq_QCLe * Kq_p;
  Iq_QCLIin = Iq_QCLe * AWCLAMP (Kq_i, Iq_QCLP + OldIq_QCLI, Qmax, Qmin, Iq_QCLe, OldIq_QCLI);
  Iq_QCLI = INTEGRATORRESET(1, Startup_flag, 0, Iq_QCLIin, OldIq_QCLIin, OldIq_QCLI, delt);
  Iq_QCL = LIMITER(Qmax, Qmin, Iq_QCLP + Iq_QCLI);

  // Q Open Loop 
  Iq_QOL = LIMITER(Qmax, Qmin, Qref) / (Vtd_1_y + 0.0001);

  // LVRT/ HVRT 
  Iq1_frt = DB(Vref - Vtd_1 - 0.0001, dbhv_frt, dblv_frt) * -Kqv1; // TODO: should this be Vtd_1 or Vtd_1_y?
  Iq_Qctl = SELECTOR(Iq_QCL, Iq_QOL, Qctl_CL_flag);
  Iq1_icont = SELECTOR(Iq_VtdCL, Iq_Qctl, Vt_flag);
  Iq1_i_SH[1] = OldIq1_i_SH;
  SAMPLEHOLD(LIMITER(1, -1, -1 * Iq1_icont), FRT_flag, OldFRT_flag, Iq1_i_SH);
  Iq1_i = Iq1_i_SH[0];
  Iq1ref = Iq1_frt + Iq1_i;

  // V2 Control 
  RECTANGULAR2POLAR(Vtd_2, Vtq_2, &Vdq_2mag, &Vdq_2ang);
  Idq2_refmag = DB(Vdq_2mag, 0.0, dbh_2) * Kqv2;  // CHANGED dbl_2 to 0 on 4/19 {TODO: investigate the impact}
  Idq2_refang = Vdq_2ang - PI2;
  POLAR2RECTANGULAR(Idq2_refmag, Idq2_refang, &Id2ref, &Iq2ref);

  // Current Limit Logic Block
  // Generating Id1ref_L, Iq1ref_L, Idref_2_L, Iq2ref_L 
  I2m_ref_upper = SELECTOR(SELECTOR(fabs(Iq1_frt), fabs(Iq1ref), IR_flag), 9999, 1); // outer SELECTOR only to match PSCAD diagram, Fig 3-24 of PVMOD milestone report
  RECTANGULAR2POLAR(Id2ref, Iq2ref, &I2m_refmag, &Iq2ref_Lang);
  I2m_ref = LIMITER(I2m_ref_upper, 0, I2m_refmag);
  I1m_ref = sqrt(Id1ref*Id1ref + Iq1ref*Iq1ref);
  Ilim_L = SELECTOR((Ilim_pu - Iq1_i), (Ilim_pu + Iq1_i), COMPARATOR(Iq1_frt, 0));
  IROL_flag = COMPARATOR(fabs(Iq1ref) + fabs(I2m_ref), Ilim_pu);
  scale = SELECTOR((Ilim_L / (fabs(Iq1_frt) + I2m_ref)), 1, IROL_flag);
  I2m_ref_L = I2m_ref * scale;
  POLAR2RECTANGULAR(I2m_ref_L, Iq2ref_Lang, &Id2ref_L, &Iq2ref_L);
  Iq1ref_L = Iq1_i + (Iq1_frt * scale);
  Id1max_FRT = sqrt(LIMITER(999999.0, 0.0, (Ilim_pu - I2m_ref_L)*(Ilim_pu - I2m_ref_L) - Iq1ref_L*Iq1ref_L));
  Id1ref_L = LIMITER(Id1max_FRT, -Id1max_FRT, Id1ref);

  // Calculation for Ilim_phmax 
  MagIdq1 = sqrt(Id1ref_L*Id1ref_L + Iq1ref_L*Iq1ref_L);
  MagIdq2 = sqrt(Id2ref_L*Id2ref_L + Iq2ref_L*Iq2ref_L);
  AngIdq_12 = atan2(Iq1ref_L, Id1ref_L) + atan2(Iq2ref_L, Id2ref_L);

  // Cont ..Calculate Ia_max , Ib_max, Ic_max 
  Ia_max = sqrt(MagIdq1*MagIdq1 + MagIdq2*MagIdq2 + 2*MagIdq1*MagIdq2*cos(AngIdq_12));
  Ib_max = sqrt(MagIdq1*MagIdq1 + MagIdq2*MagIdq2 + 2*MagIdq1*MagIdq2*cos(AngIdq_12+TWOPI3));
  Ic_max = sqrt(MagIdq1*MagIdq1 + MagIdq2*MagIdq2 + 2*MagIdq1*MagIdq2*cos(AngIdq_12-TWOPI3));
  Iph_max = fmax (Ia_max, fmax (Ib_max, Ic_max));
  IOL_flag = COMPARATOR(I1m_ref + I2m_ref, Ilim_pu);
  Ilim_phmax = SELECTOR(LIMITER((Ilim_pu / 0.877), 1, Ilim_pu / Iph_max), 1, IOL_flag); // TODO: where did 0.877 come from?

  // Generating Id1ref_L2, Iq1ref_L2, Idref_2_L2, Iq2ref_L2 
  scale_phmax = SELECTOR(Ilim_phmax, 1, 1 * IOL_flag);
  RECTANGULAR2POLAR(Id1ref_L, Iq1ref_L, &MagIdqref_1_L, &AngIdqref_1_L);
  POLAR2RECTANGULAR(MagIdqref_1_L * scale_phmax, AngIdqref_1_L, &Id1ref_L2, &Iq1ref_L2);
  RECTANGULAR2POLAR(Id2ref_L, Iq2ref_L, &MagIdqref_2_L, &AngIdqref_2_L);
  POLAR2RECTANGULAR(MagIdqref_2_L * scale_phmax, AngIdqref_2_L, &Id2ref_L2, &Iq2ref_L2);

  // Positive Sequence Current Limit Logic Block
  Id1ref_max = sqrt(LIMITER(999999, 0, Ilim_pu*Ilim_pu - Iq1ref*Iq1ref));
  Id1ref_L1 = LIMITER(Id1ref_max, 0, Id1ref);
  Iq1ref_L1 = LIMITER(Ilim_pu, -Ilim_pu, Iq1ref);

  // Input Currents to Current Controller 
  Idref_1 = SELECTOR(Id1ref_L2, Id1ref_L1, V2_flag);
  Iqref_1 = SELECTOR(Iq1ref_L2, Iq1ref_L1, V2_flag);
  Idref_2 = SELECTOR(Id2ref_L2, 0.0, V2_flag);
  Iqref_2 = SELECTOR(Iq2ref_L2, 0.0, V2_flag);

  // Current control loop 
  t_release = fmax((tstart_up - 1), 0.0);
  current_control = (currTIME > t_release);
  if (!current_control) { // Check if Current Control is disabled 
    Idref_1 = 0.0;
    Idref_2 = 0.0;
    Iqref_1 = 0.0;
    Iqref_2 = 0.0;
  }
  Iramp_up = SELECTOR(99, Ipramp_up, FRT_flag);
  Id1_ref = RATELIMITER(Idref_1, OldId1_ref, Iramp_up, 1000, delt);
  Id1_e = (Id1_ref - Id_1) * Idq_base;
  uctrld_1P = Id1_e * Kcc_p;
  uctrld_1Iin = Id1_e * AWCLAMP (Kcc_i, uctrld_1P + Olductrld_1I, Lim_upCC, Lim_lowCC, Id1_e, Olductrld_1I);
  uctrld_1I = INTEGRATORRESET(1, 0, 0, uctrld_1Iin, Olductrld_1Iin, Olductrld_1I, delt);
  uctrld_1 = LIMITER(Lim_upCC, Lim_lowCC, uctrld_1P + uctrld_1I);

  Iq1_ref = RATELIMITER(Iqref_1, OldIq1_ref, 99999, 99999, delt);
  Iq1_e = (Iq1_ref - Iq_1) * Idq_base;
  uctrlq_1P = Iq1_e * Kcc_p;
  uctrlq_1Iin = Iq1_e * AWCLAMP (Kcc_i, uctrlq_1P + Olductrlq_1I, Lim_upCC, Lim_lowCC, Iq1_e, Olductrlq_1I);
  uctrlq_1I = INTEGRATORRESET(1, 0, 0, uctrlq_1Iin, Olductrlq_1Iin, Olductrlq_1I, delt);
  uctrlq_1 = LIMITER(Lim_upCC, Lim_lowCC, uctrlq_1P + uctrlq_1I);

  Id2_ref = RATELIMITER(Idref_2, OldId2_ref, 99999, 99999, delt);
  Id2_e = (Id2_ref - Id_2) * Idq_base;
  uctrld_2P = Id2_e * Kcc_p;
  uctrld_2Iin = Id2_e * AWCLAMP (Kcc_i, uctrld_2P + Olductrld_2I, Lim_upCC, Lim_lowCC, Id2_e, Olductrld_2I);
  uctrld_2I = INTEGRATORRESET(1, 0, 0, uctrld_2Iin, Olductrld_2Iin, Olductrld_2I, delt);
  uctrld_2 = LIMITER(Lim_upCC, Lim_lowCC, uctrld_2P + uctrld_2I);

  Iq2_ref = RATELIMITER(Iqref_2, OldIq2_ref, 99999, 99999, delt);
  Iq2_e = (Iq2_ref - Iq_2) * Idq_base;
  uctrlq_2P = Iq2_e * Kcc_p;
  uctrlq_2Iin = Iq2_e * AWCLAMP (Kcc_i, uctrlq_2P + Olductrlq_2I, Lim_upCC, Lim_lowCC, Iq2_e, Olductrlq_2I);
  uctrlq_2I = INTEGRATORRESET(1, 0, 0, uctrlq_2Iin, Olductrlq_2Iin, Olductrlq_2I, delt);
  uctrlq_2 = LIMITER(Lim_upCC, Lim_lowCC, uctrlq_2P + uctrlq_2I);

  // Generate Ed_1, Eq_1, Ed_2, and Eq_2 // TODO: check the per-unit conversions of DQ voltage drops
  Vtd_1y = REALPOLE(1, Tau_Vff, Vtd_1, OldVtd_1, OldVtd_1y, -99999, 99999, delt);
  Ed_1 = SELECTOR(Vtd_1y, 0.0, Vff_flag) * Vdq_base + (-Iq_1*Lchoke*w_nom + Id_1*Rchoke) * Idq_base + uctrld_1;
  Vtq_1y = REALPOLE(1, Tau_Vff, Vtq_1, OldVtq_1, OldVtq_1y, -99999, 99999, delt);
  Eq_1 = SELECTOR(Vtq_1y, 0.0, Vff_flag) * Vdq_base + ( Id_1*Lchoke*w_nom + Iq_1*Rchoke) * Idq_base + uctrlq_1;
  Vtd_2y = REALPOLE(1, Tau_Vff, Vtd_2, OldVtd_2, OldVtd_2y, -99999, 99999, delt);
  Ed_2 = SELECTOR(Vtd_2y, 0.0, Vff_flag) * Vdq_base + ( Iq_2*Lchoke*w_nom + Id_2*Rchoke) * Idq_base + uctrld_2;
  Vtq_2y = REALPOLE(1, Tau_Vff, Vtq_2, OldVtq_2, OldVtq_2y, -99999, 99999, delt);
  Eq_2 = SELECTOR(Vtq_2y, 0.0, Vff_flag) * Vdq_base + (-Id_2*Lchoke*w_nom + Iq_2*Rchoke) * Idq_base + uctrlq_2;

  // Generate output Ea1, Eb1, Ec1 
  DQ2ABC(Ed_1, Eq_1, Theta_PLL, Eabc_1);

  // Generate output Ea2, Eb2, Ec2 
  DQ2ABC(Ed_2, Eq_2, -Theta_PLL, Eabc_2);

  // Check modulation index 
  Ea_m = Eabc_1[0] + Eabc_2[0];
  Eb_m = Eabc_1[1] + Eabc_2[1];
  Ec_m = Eabc_1[2] + Eabc_2[2];

  // Outputs 
  outputs->m_a = Ea_m * 2.0 / Vdc_nom;
  outputs->m_b = Eb_m * 2.0 / Vdc_nom;
  outputs->m_c = Ec_m * 2.0 / Vdc_nom;
  outputs->FreqPLL = f_PLL;
  outputs->ID1 = Id_1;
  outputs->IQ1 = Iq_1;
  outputs->ID2 = Id_2;
  outputs->IQ2 = Iq_2;
  outputs->VD1 = Vtd_1;
  outputs->VQ1 = Vtq_1;
  outputs->VD2 = Vtd_2;
  outputs->VQ2 = Vtq_2;
  outputs->FRT_flag = FRT_flag;
  outputs->Pout = Pelec_meas;
  outputs->Qout = Qelec_meas;
  // Added outputs for debugging 

  // save state variables 
  instance->DoubleStates[0]  = currTIME;  // not used
  instance->DoubleStates[1]  = Vta_pu;
  instance->DoubleStates[2]  = Vta_flt1;
  instance->DoubleStates[3]  = Vtb_pu;
  instance->DoubleStates[4]  = Vtb_flt1;
  instance->DoubleStates[5]  = Vtc_pu;
  instance->DoubleStates[6]  = Vtc_flt1;
  instance->DoubleStates[7]  = I1a_pu;
  instance->DoubleStates[8]  = I1a_flt1;
  instance->DoubleStates[9]  = I1b_pu;
  instance->DoubleStates[10] = I1b_flt1;
  instance->DoubleStates[11] = I1c_pu;
  instance->DoubleStates[12] = I1c_flt1;
  instance->DoubleStates[13] = I2a_pu;
  instance->DoubleStates[14] = I2a_flt1;
  instance->DoubleStates[15] = I2b_pu;
  instance->DoubleStates[16] = I2b_flt1;
  instance->DoubleStates[17] = I2c_pu;
  instance->DoubleStates[18] = I2c_flt1;
  instance->DoubleStates[19] = Omega_PLL;
  instance->DoubleStates[20] = Vt_alpha;
  instance->DoubleStates[21] = Vt_alpha_pr;
  instance->DoubleStates[22] = Vt_qalpha_pr;
  instance->DoubleStates[23] = Vt_beta;
  instance->DoubleStates[24] = Vt_beta_pr;
  instance->DoubleStates[25] = Vt_qbeta_pr;
  instance->DoubleStates[26] = Theta_PLL;
  instance->DoubleStates[27] = DelOmegaIin;
  instance->DoubleStates[28] = DelOmegaI;
  instance->DoubleStates[29] = Theta_DSOGIPLLcont;
  instance->DoubleStates[30] = Id1_ref;
  instance->DoubleStates[31] = OldId1_ref;
  instance->DoubleStates[32] = Id1r_flt;
  instance->DoubleStates[33] = Iq1_ref;
  instance->DoubleStates[34] = OldIq1_ref;
  instance->DoubleStates[35] = Iq1r_flt;
  instance->DoubleStates[36] = Id2_ref;
  instance->DoubleStates[37] = OldId2_ref;
  instance->DoubleStates[38] = Id2r_flt;
  instance->DoubleStates[39] = Iq2_ref;
  instance->DoubleStates[40] = OldIq2_ref;
  instance->DoubleStates[41] = Iq2r_flt;
  instance->DoubleStates[42] = Id1_FFin;
  instance->DoubleStates[43] = Id1_FFnolimit;
  instance->DoubleStates[44] = Id1_VdcIin; 
  instance->DoubleStates[45] = Id1_VdcI;
  instance->DoubleStates[46] = f_PLL;
  instance->DoubleStates[47] = fpu_flt;
  instance->DoubleStates[48] = Vtd_1_y;
  instance->DoubleStates[49] = Idref_droop_x;
  instance->DoubleStates[50] = Idref_droop;
  instance->DoubleStates[51] = Id1ref_hold;
  instance->DoubleStates[52] = Iq_VtdCLIin;
  instance->DoubleStates[53] = Iq_VtdCLI;
  instance->DoubleStates[54] = Iq_QCLIin;
  instance->DoubleStates[55] = Iq_QCLI;
  instance->DoubleStates[56] = Iq1_i;
  instance->DoubleStates[57] = Idref_1;
  instance->DoubleStates[58] = uctrld_1Iin;
  instance->DoubleStates[59] = uctrld_1I;
  instance->DoubleStates[60] = Iqref_1;
  instance->DoubleStates[61] = uctrlq_1Iin;
  instance->DoubleStates[62] = uctrlq_1I;
  instance->DoubleStates[63] = Idref_2;
  instance->DoubleStates[64] = uctrld_2Iin;
  instance->DoubleStates[65] = uctrld_2I;
  instance->DoubleStates[66] = Iqref_2;
  instance->DoubleStates[67] = uctrlq_2Iin;
  instance->DoubleStates[68] = uctrlq_2I;
  instance->DoubleStates[69] = Vtd_1;
  instance->DoubleStates[70] = Vtd_1y;
  instance->DoubleStates[71] = Vtq_1;
  instance->DoubleStates[72] = Vtq_1y;
  instance->DoubleStates[73] = Vtd_2;
  instance->DoubleStates[74] = Vtd_2y; 
  instance->DoubleStates[75] = Vtq_2;
  instance->DoubleStates[76] = Vtq_2y;
  instance->DoubleStates[77] = FRT_flag;
  instance->DoubleStates[78] = Id1ref_hold_SH[0]; // was [1]
  instance->DoubleStates[79] = Iq1_i_SH[0];       // was [1]
  instance->DoubleStates[80] = Pelec;
  instance->DoubleStates[81] = Pelec_meas;
  instance->DoubleStates[82] = Qelec;
  instance->DoubleStates[83] = Qelec_meas;
  instance->LastGeneralMessage = ErrorMessage;
  return IEEE_Cigre_DLLInterface_Return_OK;
};

//---------------------------------------------------------------- 

__declspec(dllexport) int32_T __cdecl Model_Terminate(IEEE_Cigre_DLLInterface_Instance* instance) { 
// Destroys any objects allocated by the model code- not used 
  return IEEE_Cigre_DLLInterface_Return_OK;
};

__declspec(dllexport) int32_T __cdecl Model_FirstCall(IEEE_Cigre_DLLInterface_Instance* instance) { 
// Destroys any objects allocated by the model code not used 
  return IEEE_Cigre_DLLInterface_Return_OK;

};

__declspec(dllexport) int32_T __cdecl Model_Iterate(IEEE_Cigre_DLLInterface_Instance* instance) { 
// Destroys any objects allocated by the model code not used 
  return IEEE_Cigre_DLLInterface_Return_OK;
};

__declspec(dllexport) int32_T __cdecl Model_PrintInfo () {
// Prints Model Information once 
  int Printed = 0;
  if (!Printed) { 
    printf("Cigre/IEEE DLL Standard\n");
    printf("Model name:             %s\n", Model_Info.ModelName);
    printf("Model version:          %s\n", Model_Info.ModelVersion);
    printf("Model description:      %s\n", Model_Info.ModelDescription);
    printf("Model general info:     %s\n", Model_Info.GeneralInformation);
    printf("Model created on:       %s\n", Model_Info.ModelCreated);
    printf("Model created by:       %s\n", Model_Info.ModelCreator);
    printf("Model last modified     %s\n", Model_Info.ModelLastModifiedDate);
    printf("Model last modified by: %s\n", Model_Info.ModelLastModifiedBy);

    printf("Model modified comment:  %s\n", Model_Info.ModelModifiedComment);
    printf("Model modified history: %s\n", Model_Info.ModelModifiedHistory);
    printf("Time Step Sampling Time (sec): %0.5g\n", Model_Info.FixedStepBaseSampleTime);
    switch (Model_Info.EMT_RMS_Mode) {
      case 1: 
        printf ("EMT/RMS mode: EMT\n");
        break;
      case 2: 
        printf ("EMT/RMS mode: RMS\n" );
        break;
      case 3: 
        printf ("EMT/RMS mode: EMT and RMS\n");
        break;
      default: 
        printf ("EMT/RMS mode : <not available>\n");
    }
    printf ("Number of inputs: %d\n", Model_Info.NumInputPorts);
    printf("Input description:\n");
    for (int k = 0;k < Model_Info.NumInputPorts;k++) { 
      printf(" %s\n", Model_Info.InputPortsInfo[k].Name);
    } 

    printf("Number of outputs: %d\n", Model_Info.NumOutputPorts);
    printf("Output description:\n");
    for (int k = 0;k < Model_Info.NumOutputPorts;k++) { 
      printf(" %s\n", Model_Info.OutputPortsInfo[k].Name);
    }

    printf("Number of parameters: %d\n", Model_Info.NumParameters);
    printf ("Parameter description:\n");
    for (int k = 0;k < Model_Info.NumParameters;k++) { 
      printf(" %s\n", Model_Info.ParametersInfo[k].Name);
    }
    printf("Number of int state variables: %d\n", Model_Info.NumIntStates);
    printf("Number of float state variables: %d\n", Model_Info.NumFloatStates);
    printf("Number of double state variables: %d\n", Model_Info.NumDoubleStates);
    printf ("\n");

    fflush ( stdout);
  }
  Printed = 1;
  return IEEE_Cigre_DLLInterface_Return_OK;
};

