MODEL mOPNIBR
INPUT
  v_ac,i_L,v_dc,P_request,Q_request,enable,P_lim_high,P_lim_low
DATA
OUTPUT
  v_bridge,pwm_enable,circuitControls_OUT.v_bridge[0],circuitControls_OUT.v_bridge[1],circuitControls_OUT.v_bridge[2],machineModel_OUT.i_ref[0],machineModel_OUT.i_ref[1],machineModel_OUT.i_ref[2],machineModel_OUT.fRotor,acMonitor_OUT.frequency,acMonitor_OUT.Vpve.real,acMonitor_OUT.Vpve.imag,acChecks_OUT.acOk
VAR
  v_bridge,pwm_enable,circuitControls_OUT.v_bridge[0],circuitControls_OUT.v_bridge[1],circuitControls_OUT.v_bridge[2],machineModel_OUT.i_ref[0],machineModel_OUT.i_ref[1],machineModel_OUT.i_ref[2],machineModel_OUT.fRotor,acMonitor_OUT.frequency,acMonitor_OUT.Vpve.real,acMonitor_OUT.Vpve.imag,acChecks_OUT.acOk
INIT
  v_bridge:=0.0
  pwm_enable:=0.0
  circuitControls_OUT.v_bridge[0]:=0.0
  circuitControls_OUT.v_bridge[1]:=0.0
  circuitControls_OUT.v_bridge[2]:=0.0
  machineModel_OUT.i_ref[0]:=0.0
  machineModel_OUT.i_ref[1]:=0.0
  machineModel_OUT.i_ref[2]:=0.0
  machineModel_OUT.fRotor:=0.0
  acMonitor_OUT.frequency:=0.0
  acMonitor_OUT.Vpve.real:=0.0
  acMonitor_OUT.Vpve.imag:=0.0
  acChecks_OUT.acOk:=0.0
ENDINIT
MODEL m1 FOREIGN GFM_BATTERY_OPENIBR {ixdata:0, ixin:10, ixout:13, ixvar:0}
EXEC
  USE m1 AS m1
    -- the DLL will convert inputs to kV, kA as needed
    INPUT xin[1] := v_ac         -- V
    INPUT xin[2] := i_L          -- A
    INPUT xin[3] := v_dc         -- V
    INPUT xin[4] := P_request    -- W
    INPUT xin[5] := Q_request    -- VAr
    INPUT xin[6] := enable       -- 
    INPUT xin[7] := P_lim_high   -- W
    INPUT xin[8] := P_lim_low    -- W
    INPUT xin[9] := t
    INPUT xin[10] := stoptime
    -- the DLL will convert inverter voltages from kV to V
    OUTPUT v_bridge     := xout[1] -- V
    OUTPUT pwm_enable   := xout[2] -- 
    OUTPUT circuitControls_OUT.v_bridge[0] := xout[3] -- 
    OUTPUT circuitControls_OUT.v_bridge[1] := xout[4] -- 
    OUTPUT circuitControls_OUT.v_bridge[2] := xout[5] -- 
    OUTPUT machineModel_OUT.i_ref[0] := xout[6] -- Amps
    OUTPUT machineModel_OUT.i_ref[1] := xout[7] -- Amps
    OUTPUT machineModel_OUT.i_ref[2] := xout[8] -- Amps
    OUTPUT machineModel_OUT.fRotor := xout[9] -- Hz
    OUTPUT acMonitor_OUT.frequency := xout[10] -- Hz
    OUTPUT acMonitor_OUT.Vpve.real := xout[11] -- Volts
    OUTPUT acMonitor_OUT.Vpve.imag := xout[12] -- Volts
    OUTPUT acChecks_OUT.acOk := xout[13] -- 
  ENDUSE
ENDEXEC
ENDMODEL
