MODEL mIBR
INPUT
  Va, Vb, Vc, Ia, Ib, Ic, IaL1, IbL1, IcL1, Pref, Qref, Vref
DATA
  Vbase          {dflt: 0.65  }
  Sbase          {dflt: 1000  }
  Vdcbase        {dflt: 1.3   }
  KpI            {dflt: 0.5   }
  KiI            {dflt: 1     }
  Wtype          {dflt: 0     }
  KpPLL          {dflt: 20    }
  KiPLL          {dflt: 200   }
  del_f_limit    {dflt: 12    }
  KpP            {dflt: 0.5   }
  KiP            {dflt: 10    }
  Qflag          {dflt: 1     }
  KpQ            {dflt: 0.5   }
  KiQ            {dflt: 20    }
  KpV            {dflt: 0.5   }
  KiV            {dflt: 150   }
  KpVq           {dflt: 0     }
  KiVq           {dflt: 0     }
  Imax           {dflt: 1.2   }
  Pmax           {dflt: 1     }
  Pmin           {dflt: 0     }
  Qmax           {dflt: 1     }
  Qmin           {dflt: -1    }
  PQflag         {dflt: 1     }
  KfDroop        {dflt: 30    }
  KvDroop        {dflt: 22.22 }
  K_POD          {dflt: 0     }
  T_POD          {dflt: 0.01  }
  T1_POD         {dflt: 0.01  }
  T2_POD         {dflt: 0.001 }
  POD_min        {dflt: -0.5  }
  POD_max        {dflt: 0.5   }
  Vdip           {dflt: 0.8   }
  Vup            {dflt: 1.2   }
  KpVdq          {dflt: 3     }
  KiVdq          {dflt: 10    }
  Tr             {dflt: 0.001 }
  Rchoke         {dflt: 0     }
  Lchoke         {dflt: 0.15  }
  Cfilt          {dflt: 0.01666}
  Rdamp          {dflt: 9.4868}
OUTPUT
  Ea, Eb, Ec, Idref, Id, Iqref, Iq, Vd, Vq, Fpll, Pout, Qout
VAR
  Ea, Eb, Ec, Idref, Id, Iqref, Iq, Vd, Vq, Fpll, Pout, Qout
INIT
  Ea:=0.0
  Eb:=0.0
  Ec:=0.0
  Idref:=0.0
  Id:=0.0
  Iqref:=0.0
  Iq:=0.0
  Vd:=0.0
  Vq:=0.0
  Fpll:=0.0
  Pout:=0.0
  Qout:=0.0
ENDINIT
MODEL m1 FOREIGN GFM_GFL_IBR {ixdata:41, ixin:14, ixout:12, ixvar:0}
EXEC
  USE m1 AS m1
    DATA   xdata[1]:=Vbase        
    DATA   xdata[2]:=Sbase        
    DATA   xdata[3]:=Vdcbase      
    DATA   xdata[4]:=KpI          
    DATA   xdata[5]:=KiI          
    DATA   xdata[6]:=Wtype        
    DATA   xdata[7]:=KpPLL        
    DATA   xdata[8]:=KiPLL        
    DATA   xdata[9]:=del_f_limit  
    DATA  xdata[10]:=KpP          
    DATA  xdata[11]:=KiP          
    DATA  xdata[12]:=Qflag        
    DATA  xdata[13]:=KpQ          
    DATA  xdata[14]:=KiQ          
    DATA  xdata[15]:=KpV          
    DATA  xdata[16]:=KiV          
    DATA  xdata[17]:=KpVq         
    DATA  xdata[18]:=KiVq         
    DATA  xdata[19]:=Imax         
    DATA  xdata[20]:=Pmax         
    DATA  xdata[21]:=Pmin         
    DATA  xdata[22]:=Qmax         
    DATA  xdata[23]:=Qmin         
    DATA  xdata[24]:=PQflag       
    DATA  xdata[25]:=KfDroop      
    DATA  xdata[26]:=KvDroop      
    DATA  xdata[27]:=K_POD        
    DATA  xdata[28]:=T_POD        
    DATA  xdata[29]:=T1_POD       
    DATA  xdata[30]:=T2_POD       
    DATA  xdata[31]:=POD_min      
    DATA  xdata[32]:=POD_max      
    DATA  xdata[33]:=Vdip         
    DATA  xdata[34]:=Vup          
    DATA  xdata[35]:=KpVdq        
    DATA  xdata[36]:=KiVdq        
    DATA  xdata[37]:=Tr           
    DATA  xdata[38]:=Rchoke       
    DATA  xdata[39]:=Lchoke       
    DATA  xdata[40]:=Cfilt        
    DATA  xdata[41]:=Rdamp
    -- the DLL will convert inputs to kV, kA as needed
    INPUT  xin[1]:=Va
    INPUT  xin[2]:=Vb
    INPUT  xin[3]:=Vc
    INPUT  xin[4]:=Ia
    INPUT  xin[5]:=Ib
    INPUT  xin[6]:=Ic
    INPUT  xin[7]:=IaL1
    INPUT  xin[8]:=IbL1
    INPUT  xin[9]:=IcL1
    INPUT xin[10]:=Pref
    INPUT xin[11]:=Qref
    INPUT xin[12]:=Vref
    INPUT xin[13]:=t
    INPUT xin[14]:=stoptime
    -- the DLL will convert inverter voltages from kV to V
    OUTPUT Ea:=xout[1]
    OUTPUT Eb:=xout[2]
    OUTPUT Ec:=xout[3]
    OUTPUT Idref:=xout[4] -- pu
    OUTPUT Id:=xout[5]    -- pu
    OUTPUT Iqref:=xout[6] -- pu
    OUTPUT Iq:=xout[7]    -- pu
    OUTPUT Vd:=xout[8]    -- pu
    OUTPUT Vq:=xout[9]    -- pu
    OUTPUT Fpll:=xout[10] -- Hz
    OUTPUT Pout:=xout[11] -- MW
    OUTPUT Qout:=xout[12] -- Mvar
  ENDUSE
ENDEXEC
ENDMODEL
