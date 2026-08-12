
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

#include "dll_autogen.c"

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

// Note - not yet implemented for OpenIBR 
  MyModelParameters* parameters = (MyModelParameters*)instance->Parameters;

  int bWarning = 0;
  int bError = 0;

  ErrorMessage[0] = '\0';

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

  double delt = Model_Info.FixedStepBaseSampleTime;
 
  MyModelInputs* inputs = (MyModelInputs*)instance->ExternalInputs;
  double Vta = inputs->Vta;

  // Working back from initial output 

  MyModelOutputs* outputs= (MyModelOutputs*) instance->ExternalOutputs;
  double m_a = outputs->m_a;

  ErrorMessage [0]= '\0';

  // save state variables 
  instance->DoubleStates[0]  = 0.0;

  instance->LastGeneralMessage = ErrorMessage;
  return IEEE_Cigre_DLLInterface_Return_OK;
};

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

  // load state variables
  double OldTIME = instance->DoubleStates[0];  // not used

  MyModelOutputs* outputs = (MyModelOutputs*)instance->ExternalOutputs;

  // Calculations

  // Outputs 
  outputs->m_a = Ea_m * 2.0 / Vdc_nom;

  // save state variables 
  instance->DoubleStates[0]  = currTIME;  // not used

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

