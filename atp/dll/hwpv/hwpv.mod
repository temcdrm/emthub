MODEL mHWPV
INPUT
  Tdeg, G, Fc, Ud, Uq, Vd, Vq, GVrms, Ctrl
OUTPUT
  Vdc, Idc, Id, Iq
VAR
  Vdc, Idc, Id, Iq
INIT
  Vdc:=0.0
  Idc:=0.0
  Id:=0.0
  Iq:=0.0
ENDINIT
MODEL m1 FOREIGN HWPV {ixdata:0, ixin:11, ixout:4, ixvar:0}
EXEC
  USE m1 AS m1
    INPUT xin[1]:=Tdeg
    INPUT xin[2]:=G
    INPUT xin[3]:=Fc
    INPUT xin[4]:=Ud
    INPUT xin[5]:=Uq
    INPUT xin[6]:=Vd
    INPUT xin[7]:=Vq
    INPUT xin[8]:=GVrms
    INPUT xin[9]:=Ctrl
    INPUT xin[10]:=t
    INPUT xin[11]:=stoptime
    OUTPUT Vdc:=xout[1]
    OUTPUT Idc:=xout[2]
    OUTPUT Id:=xout[3]
    OUTPUT Iq:=xout[4]
  ENDUSE
ENDEXEC
ENDMODEL
