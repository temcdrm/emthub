MODEL mSCRX9
INPUT
  Vref, Ec, Vs, IFD, VT, VUEL, VOEL
DATA
  TAdTB          {dflt: 0.1 }
  TB             {dflt: 10.0 }
  K              {dflt: 100.0 }
  TE             {dflt: 0.05 }
  Emin           {dflt: -5.0 }
  Emax           {dflt: 5.0 }
  Cswitch        {dflt: 1.0 }
  RCdRFD         {dflt: 10.0 }
OUTPUT
  EFD
VAR
  EFD
INIT
  EFD:=1.0
ENDINIT
MODEL m1 FOREIGN SCRX9 {ixdata:8, ixin:9, ixout:1, ixvar:0}
EXEC
  USE m1 AS m1
    DATA xdata[1]:=TAdTB
    DATA xdata[2]:=TB
    DATA xdata[3]:=K
    DATA xdata[4]:=TE
    DATA xdata[5]:=Emin
    DATA xdata[6]:=Emax
    DATA xdata[7]:=Cswitch
    DATA xdata[8]:=RCdRFD
    INPUT xin[1]:=Vref
    INPUT xin[2]:=Ec  
    INPUT xin[3]:=Vs  
    INPUT xin[4]:=Ifd 
    INPUT xin[5]:=VT  
    INPUT xin[6]:=VUEL
    INPUT xin[7]:=VOEL
    INPUT xin[8]:=t
    INPUT xin[9]:=stoptime
    OUTPUT EFD:=xout[1]
  ENDUSE
ENDEXEC
ENDMODEL
