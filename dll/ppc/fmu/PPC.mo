model PPC
  parameter OpenIPSL.Types.ApparentPower S_b = 100e6 "System base power";
  parameter OpenIPSL.Types.Frequency fn = 50 "System base frequency";

  parameter OpenIPSL.Types.ApparentPower M_b = 100e6 "Machine base power";
  parameter OpenIPSL.Types.Voltage V_b = 400e3 "Base voltage of the bus";
  parameter OpenIPSL.Types.PerUnit p_0 = 0.01
    "Initial plant active-power operating point in pu on machine base M_b for controller state initialization";
  parameter OpenIPSL.Types.PerUnit q_0 = 0
    "Initial plant reactive-power operating point in pu on machine base M_b for controller state initialization";

  parameter Boolean VcmpFlag = true
    "Reactive droop (false) or line drop compensation (true)";
  parameter Boolean RefFlag = true
    "Plant-level reactive power (false) or voltage control (true)";
  parameter Boolean FrqFlag = true
    "Governor response disable (false) or enable (true)";

  parameter Modelica.Units.SI.Time Tfltr = 0.02
    "Voltage or reactive power measurement filter time constant";
  parameter Real Kp = 18 "Reactive power PI control proportional gain";
  parameter Real Ki = 5 "Reactive power PI control integral gain";
  parameter Modelica.Units.SI.Time Tft = 0 "Lead time constant";
  parameter Modelica.Units.SI.Time Tfv = 0.075 "Lag time constant";
  parameter OpenIPSL.Types.PerUnit Vfrz = 0
    "Voltage below which State s2 is frozen";
  parameter OpenIPSL.Types.PerUnit Rc = 0.0025
    "Line drop compensation resistance";
  parameter OpenIPSL.Types.PerUnit Xc = 0.0025
    "Line drop compensation reactance";
  parameter Real Kc = 0.02 "Reactive current compensation gain";
  parameter OpenIPSL.Types.PerUnit emax = 0.1
    "Upper limit on deadband output";
  parameter OpenIPSL.Types.PerUnit emin = -0.1
    "Lower limit on deadband output";
  parameter OpenIPSL.Types.PerUnit dbd1 = 0
    "Lower threshold for reactive power control deadband (<=0)";
  parameter OpenIPSL.Types.PerUnit dbd2 = 0
    "Upper threshold for reactive power control deadband (>=0)";
  parameter OpenIPSL.Types.PerUnit Qmax = 0.4360
    "Upper limit on output of V/Q control";
  parameter OpenIPSL.Types.PerUnit Qmin = -0.4360
    "Lower limit on output of V/Q control";
  parameter Real Kpg = 0.1 "Proportional gain for power control";
  parameter Real Kig = 0.05 "Integral gain for power control";
  parameter Modelica.Units.SI.Time Tp = 0.25
    "Real power measurement filter time constant";
  parameter OpenIPSL.Types.PerUnit fdbd1 = 0
    "Deadband for frequency control, lower threshold (<=0)";
  parameter OpenIPSL.Types.PerUnit fdbd2 = 0
    "Deadband for frequency control, upper threshold (>=0)";
  parameter OpenIPSL.Types.PerUnit femax = 999
    "Frequency error upper limit";
  parameter OpenIPSL.Types.PerUnit femin = -999
    "Frequency error lower limit";
  parameter OpenIPSL.Types.PerUnit Pmax = 999
    "Upper limit on power reference";
  parameter OpenIPSL.Types.PerUnit Pmin = -999
    "Lower limit on power reference";
  parameter Modelica.Units.SI.Time Tg = 0.1 "Power controller lag time constant";
  parameter OpenIPSL.Types.PerUnit Ddn = 20
    "Reciprocal of droop for over-frequency conditions";
  parameter OpenIPSL.Types.PerUnit Dup = 0
    "Reciprocal of droop for under-frequency conditions";
  parameter Real Vref0 = v_0 "Regulated bus initial voltage";

  inner OpenIPSL.Electrical.SystemBase SysData(S_b = S_b, fn = fn);

  Modelica.Blocks.Interfaces.RealInput Qref
    "Reactive power reference in pu on machine base M_b";
  Modelica.Blocks.Interfaces.RealInput Plant_pref
    "Plant active-power reference in pu on machine base M_b";
  Modelica.Blocks.Interfaces.RealInput Freq
    "Measured frequency in pu on system frequency base fn";
  Modelica.Blocks.Interfaces.RealInput Freq_ref
    "Frequency reference in pu on system frequency base fn";
  Modelica.Blocks.Interfaces.RealInput Pmeas
    "Measured active power in pu on system base S_b";
  Modelica.Blocks.Interfaces.RealInput Qmeas
    "Measured reactive power in pu on system base S_b";
  Modelica.Blocks.Interfaces.RealInput Vmeas
    "Measured RMS voltage magnitude in pu on voltage base V_b";

  Modelica.Blocks.Interfaces.RealOutput Qext
    "Reactive power command in pu on machine base M_b";
  Modelica.Blocks.Interfaces.RealOutput Pref
    "Active power command in pu on machine base M_b";

protected
  parameter OpenIPSL.Types.PerUnit v_0 = 1
    "Legacy inherited initialization parameter; practically unused because Vref is set explicitly";
  parameter OpenIPSL.Types.Angle angle_0 = 0
    "Legacy inherited initialization parameter; practically unused in this wrapper";
  OpenIPSL.Electrical.Renewables.PSSE.PlantController.REPCA1 repca1(
    M_b = M_b,
    V_b = V_b,
    P_0 = p_0 * M_b,
    Q_0 = q_0 * M_b,
    v_0 = v_0,
    angle_0 = angle_0,
    vcflag = VcmpFlag,
    refflag = RefFlag,
    fflag = FrqFlag,
    Tfltr = Tfltr,
    Kp = Kp,
    Ki = Ki,
    Tft = Tft,
    Tfv = Tfv,
    Vfrz = Vfrz,
    Rc = Rc,
    Xc = Xc,
    Kc = Kc,
    emax = emax,
    emin = emin,
    dbd1 = dbd1,
    dbd2 = dbd2,
    Qmax = Qmax,
    Qmin = Qmin,
    Kpg = Kpg,
    Kig = Kig,
    Tp = Tp,
    fdbd1 = fdbd1,
    fdbd2 = fdbd2,
    femax = femax,
    femin = femin,
    Pmax = Pmax,
    Pmin = Pmin,
    Tg = Tg,
    Ddn = Ddn,
    Dup = Dup,
    Vref = Vref0);
  parameter Real vEps = 1e-6 "Minimum voltage magnitude in pu for current derivation";
  Real branch_ir;
  Real branch_ii;
  Real regulate_vr;
  Real regulate_vi;

equation
  regulate_vr = Vmeas;
  regulate_vi = 0;

  branch_ir = Pmeas / max(regulate_vr, vEps);
  branch_ii = -Qmeas / max(regulate_vr, vEps);

  connect(Qref, repca1.Qref);
  connect(Plant_pref, repca1.Plant_pref);
  connect(Freq, repca1.Freq);
  connect(Freq_ref, repca1.Freq_ref);
  repca1.p0 = p_0;
  repca1.q0 = q_0;
  repca1.v0 = v_0;
  repca1.branch_ir = branch_ir;
  repca1.branch_ii = branch_ii;
  repca1.regulate_vr = regulate_vr;
  repca1.regulate_vi = regulate_vi;

  connect(repca1.Qext, Qext);
  connect(repca1.Pref, Pref);
end PPC;
