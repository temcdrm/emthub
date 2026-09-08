MODEL mSEXS
INPUT
  Vref,Vc,Vs
DATA
  TaTb         {dflt: 0.100000}
  Tb           {dflt: 10.000000}
  K            {dflt: 100.000000}
  Te           {dflt: 0.050000}
  Emin         {dflt: -5.000000}
  Emax         {dflt: 5.000000}
  Kc           {dflt: 0.080000}
  Tc           {dflt: 0.000000}
  EfdMin       {dflt: -5.000000}
  EfdMax       {dflt: 5.000000}
OUTPUT
  Efd
VAR
  Efd
INIT
  Efd:=0.0
ENDINIT
MODEL m1 FOREIGN SEXS {ixdata:10, ixin:5, ixout:1, ixvar:0}
EXEC
  USE m1 AS m1
    DATA xdata[1] := TaTb         -- sec
    DATA xdata[2] := Tb           -- sec
    DATA xdata[3] := K            -- pu
    DATA xdata[4] := Te           -- sec
    DATA xdata[5] := Emin         -- pu
    DATA xdata[6] := Emax         -- pu
    DATA xdata[7] := Kc           -- pu
    DATA xdata[8] := Tc           -- sec
    DATA xdata[9] := EfdMin       -- pu
    DATA xdata[10] := EfdMax       -- pu
    -- the DLL will convert inputs to kV, kA as needed
    INPUT xin[1] := Vref         -- pu
    INPUT xin[2] := Vc           -- pu
    INPUT xin[3] := Vs           -- pu
    INPUT xin[4] := t
    INPUT xin[5] := stoptime
    -- the DLL will convert inverter voltages from kV to V
    OUTPUT Efd          := xout[1] -- pu
  ENDUSE
ENDEXEC
ENDMODEL
