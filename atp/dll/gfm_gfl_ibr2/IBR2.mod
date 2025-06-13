MODEL mIBR2
INPUT
  Vta,Vtb,Vtc,I1a,I1b,I1c,I2a,I2b,I2c,Idc,VdcMPPT,Pref,Qref,Vdc_meas
DATA
  VLLbase      {dflt: 600.000000}
  Sbase        {dflt: 1000000.000000}
  Tflt_v       {dflt: 0.000010}
  Vflt_flag    {dflt: 1.000000}
  Tflt_i       {dflt: 0.000010}
  Iflt_flag    {dflt: 1.000000}
  Cur1_flag    {dflt: 1.000000}
  k_PLL        {dflt: 1.000000}
  KpPLL        {dflt: 25.400000}
  KiPLL        {dflt: 324.000000}
  Lim_PLL      {dflt: 70.000000}
  w_nom        {dflt: 376.991118}
  tstart_up    {dflt: 1.900000}
  Vdc_nom      {dflt: 1200.000000}
  VI_flag      {dflt: 0.000000}
  MPPT_flag    {dflt: 0.000000}
  b_Vdc        {dflt: 0.560000}
  Kp_Vdc       {dflt: 5.180000}
  Ki_Vdc       {dflt: 52.910000}
  T_frq        {dflt: 0.100000}
  fdbd1        {dflt: -0.000600}
  fdbd2        {dflt: 0.000600}
  Ddn          {dflt: 20.000000}
  Dup          {dflt: 0.000000}
  Tp_droop     {dflt: 0.001000}
  Vdc_flag     {dflt: 0.000000}
  f_flag       {dflt: 0.000000}
  Id_frz_flag  {dflt: 0.000000}
  Ilim_pu      {dflt: 1.100000}
  Vt_ref       {dflt: 1.010000}
  Kv_p         {dflt: 0.000000}
  Kv_i         {dflt: 100.000000}
  Qmin         {dflt: -0.400000}
  Qmax         {dflt: 0.400000}
  Kq_p         {dflt: 0.000000}
  Kq_i         {dflt: 40.000000}
  dbhv_frt     {dflt: -0.100000}
  dblv_frt     {dflt: 0.100000}
  Kqv1         {dflt: 2.000000}
  Qctl_CL_flag {dflt: 1.000000}
  Vt_flag      {dflt: 1.000000}
  dbl_2        {dflt: -0.100000}
  dbh_2        {dflt: 0.100000}
  Kqv2         {dflt: 2.000000}
  V2_flag      {dflt: 1.000000}
  Ipramp_up    {dflt: 1.000000}
  Kcc_p        {dflt: 0.323250}
  Kcc_i        {dflt: 324.000000}
  Lim_upCC     {dflt: 99999.000000}
  Lim_lowCC    {dflt: -99999.000000}
  Tau_Vff      {dflt: 0.000100}
  Vff_flag     {dflt: 0.000000}
  Lchoke       {dflt: 0.000100}
  IR_flag      {dflt: 1.000000}
OUTPUT
  m_a,m_b,m_c,FreqPLL,Id1,Iq1,Id2,Iq2,Vtd1,Vtq1,Vtd2,Vtq2,FRT_Flag,Pout,Qout
VAR
  m_a,m_b,m_c,FreqPLL,Id1,Iq1,Id2,Iq2,Vtd1,Vtq1,Vtd2,Vtq2,FRT_Flag,Pout,Qout
INIT
  m_a:=0.0
  m_b:=0.0
  m_c:=0.0
  FreqPLL:=0.0
  Id1:=0.0
  Iq1:=0.0
  Id2:=0.0
  Iq2:=0.0
  Vtd1:=0.0
  Vtq1:=0.0
  Vtd2:=0.0
  Vtq2:=0.0
  FRT_Flag:=0.0
  Pout:=0.0
  Qout:=0.0
ENDINIT
MODEL m1 FOREIGN GFM_GFL_IBR2 {ixdata:54, ixin:16, ixout:15, ixvar:0}
EXEC
  USE m1 AS m1
    DATA xdata[1] := VLLbase      -- V
    DATA xdata[2] := Sbase        -- VA
    DATA xdata[3] := Tflt_v       -- s
    DATA xdata[4] := Vflt_flag    -- N/A
    DATA xdata[5] := Tflt_i       -- s
    DATA xdata[6] := Iflt_flag    -- N/A
    DATA xdata[7] := Cur1_flag    -- N/A
    DATA xdata[8] := k_PLL        -- N/A
    DATA xdata[9] := KpPLL        -- pu/pu
    DATA xdata[10] := KiPLL        -- pu/pu
    DATA xdata[11] := Lim_PLL      -- pu/pu
    DATA xdata[12] := w_nom        -- rad/s
    DATA xdata[13] := tstart_up    -- s
    DATA xdata[14] := Vdc_nom      -- kV
    DATA xdata[15] := VI_flag      -- N/A
    DATA xdata[16] := MPPT_flag    -- pu/pu
    DATA xdata[17] := b_Vdc        -- N/A
    DATA xdata[18] := Kp_Vdc       -- pu/pu
    DATA xdata[19] := Ki_Vdc       -- pu/pu
    DATA xdata[20] := T_frq        -- s
    DATA xdata[21] := fdbd1        -- N/A
    DATA xdata[22] := fdbd2        -- N/A
    DATA xdata[23] := Ddn          -- ******
    DATA xdata[24] := Dup          -- ******
    DATA xdata[25] := Tp_droop     -- s
    DATA xdata[26] := Vdc_flag     -- N/A
    DATA xdata[27] := f_flag       -- N/A
    DATA xdata[28] := Id_frz_flag  -- N/A
    DATA xdata[29] := Ilim_pu      -- pu
    DATA xdata[30] := Vt_ref       -- pu
    DATA xdata[31] := Kv_p         -- pu
    DATA xdata[32] := Kv_i         -- pu
    DATA xdata[33] := Qmin         -- pu
    DATA xdata[34] := Qmax         -- pu
    DATA xdata[35] := Kq_p         -- pu
    DATA xdata[36] := Kq_i         -- pu
    DATA xdata[37] := dbhv_frt     -- pu
    DATA xdata[38] := dblv_frt     -- pu
    DATA xdata[39] := Kqv1         -- pu
    DATA xdata[40] := Qctl_CL_flag -- N/A
    DATA xdata[41] := Vt_flag      -- N/A
    DATA xdata[42] := dbl_2        -- N/A
    DATA xdata[43] := dbh_2        -- N/A
    DATA xdata[44] := Kqv2         -- pu
    DATA xdata[45] := V2_flag      -- pu
    DATA xdata[46] := Ipramp_up    -- pu
    DATA xdata[47] := Kcc_p        -- pu
    DATA xdata[48] := Kcc_i        -- pu
    DATA xdata[49] := Lim_upCC     -- pu
    DATA xdata[50] := Lim_lowCC    -- pu
    DATA xdata[51] := Tau_Vff      -- s
    DATA xdata[52] := Vff_flag     -- N/A
    DATA xdata[53] := Lchoke       -- pu
    DATA xdata[54] := IR_flag      -- N/A
    -- the DLL will convert inputs to kV, kA as needed
    INPUT xin[1] := Vta          -- kV
    INPUT xin[2] := Vtb          -- kV
    INPUT xin[3] := Vtc          -- kV
    INPUT xin[4] := I1a          -- kA
    INPUT xin[5] := I1b          -- kA
    INPUT xin[6] := I1c          -- kA
    INPUT xin[7] := I2a          -- kA
    INPUT xin[8] := I2b          -- kA
    INPUT xin[9] := I2c          -- kA
    INPUT xin[10] := Idc          -- kA
    INPUT xin[11] := VdcMPPT      -- kV
    INPUT xin[12] := Pref         -- pu
    INPUT xin[13] := Qref         -- pu
    INPUT xin[14] := Vdc_meas     -- kV
    INPUT xin[15] := t
    INPUT xin[16] := stoptime
    -- the DLL will convert inverter voltages from kV to V
    OUTPUT m_a          := xout[1] -- N/A
    OUTPUT m_b          := xout[2] -- N/A
    OUTPUT m_c          := xout[3] -- N/A
    OUTPUT FreqPLL      := xout[4] -- Hz
    OUTPUT Id1          := xout[5] -- pu
    OUTPUT Iq1          := xout[6] -- pu
    OUTPUT Id2          := xout[7] -- pu
    OUTPUT Iq2          := xout[8] -- pu
    OUTPUT Vtd1         := xout[9] -- pu
    OUTPUT Vtq1         := xout[10] -- pu
    OUTPUT Vtd2         := xout[11] -- pu
    OUTPUT Vtq2         := xout[12] -- pu
    OUTPUT FRT_Flag     := xout[13] -- N/A
    OUTPUT Pout         := xout[14] -- pu
    OUTPUT Qout         := xout[15] -- pu
  ENDUSE
ENDEXEC
ENDMODEL
