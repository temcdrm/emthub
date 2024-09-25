MODEL PV1FLL -- NB! 6 character name limit 

-- Start header. Do not modify the type-94 header. 
comment---------------------------------------------------------------
 | First, declarations required for any type 94 Norton non-TR model    |
 | - these data and input values are provided to the model by ATP      |
 | - these output values are used by ATP                               |
 | - these names can be changed, except 'n', but not their order       |
 -------------------------------------------------------------endcomment

DATA  n                      -- number of phases
      ng {dflt: n*(n+1)/2}   -- number of conductances on each side

INPUT v[1..n]   -- voltage(t) at each left node
      v0[1..n]  -- voltage(t=0) at each left node
      i0[1..n]  -- current(t=0) into each left node

VAR   i[1..n]   -- current(t) into each left node (for plotting)
      is[1..n]  -- Norton source(t+timestep) at each left node
      g[1..ng]  -- conductance(t+timestep) at each left node
                -- sequence is 1-gr, 1-2, 1-3..1-n,2-gr,2-3..2-n,...n-gr
      flag      -- set to 1 whenever conductance value is modified

OUTPUT i[1..n],is[1..n],g[1..ng],flag

 comment---------------------------------------------------------------
 | Next, declarations of user-defined data for this particular model   |
 | - their value is defined at the time of using the type-94 component |
 -------------------------------------------------------------endcomment
-- End header.  

-- This uses the single-phase second-order generalized integrator (SOGI)
-- frequency-locked-loop (FLL) with gain normalization from
-- Teodorescu, Liserre and Rodriguez, "Grid Converters for Photovoltaic
-- and Wind Power Systems", Wiley, 2011, pp. 80-89. 
DATA  WC {dflt: 377.0}
      K  {dflt: 1.414}
      GAMMA {dflt: 46}
      VBASE {dflt: 2400}
      WTOTAL {dflt: 166667.0}
      PFANG {dflt: 0}
      IRMSMX {dflt: 80.0}
      ANG0 {dflt: 0}
      UV2SET {dflt: 0.45}
      UT2SET {dflt: 0.16}

VAR   deria
      theta
      wdvlim
      irmsa
      vrmsa
      per
      ang
      mag
      epsv
      kepsv
      epsf
      qvp
      wp
      gepsf
      x2
      x3
      vp
      vp1
      vp2
      scale
      den
      va
      vpk
      -- to guard against loss of frequency lock
      WPMIN
      WPMAX
      wpgood
      -- mimic the UV2 function from IEEE 1547-2018
      uv2s
      uv2v
      uv2t

INIT
  -- UV trip settings
  uv2s := 1
  uv2v := VBASE * UV2SET
  uv2t := -1
  -- bounds on frequency lock
  WPMIN := 0.8 * WC
  WPMAX := 1.2 * WC
  wpgood := 1
  wdvlim := 69.6
  irmsa := 0.0
  g[1] := 0.001
  deria := 0.0
  per:=1/60
  vrmsa := VBASE
  vpk := sqrt(2) * VBASE
  va := vpk * cos(ANG0*PI/360)
  histdef(irmsa):=0
  integral(gepsf):=0
  integral(vp):=(vpk/WC) * cos(ANG0*PI/360 - PI/2)
  integral(vp2):=va
  histdef(epsv):=0
  histdef(epsf):=0
  histdef(kepsv):=0
  histdef(qvp):=vpk * cos(ANG0*PI/360 - PI/2)
  histdef(wp):=WC
  histdef(vp2):=WC * vpk * cos(ANG0*PI/360 - PI/2)
  histdef(gepsf):=0
  histdef(vp1):=vpk * cos(ANG0*PI/360 + PI/2)
  histdef(x2):=(vpk/WC) * cos(ANG0*PI/360 - PI/2)
  histdef(x3):=0
  histdef(vp):=va
  histdef(scale):=2*K*WC/VBASE/VBASE
  histdef(den):=2*VBASE*VBASE
ENDINIT

EXEC
  if t=0 then
    flag:=1
  else
    flag:=0
  endif
-- FLL
  combine iterate as fll_sogi
    epsv := v[1] - vp
    kepsv := K * epsv
    epsf := epsv * qvp
    qvp := x2 * wp
    wp := WC + x3
    gepsf := -GAMMA * epsf * scale
    vp1 := kepsv - qvp
    vp2 := vp1 * wp
    x3 := integral(gepsf)
    x2 := integral(vp)
    vp := integral(vp2)
    den := qvp * qvp + vp * vp + 0.001
    scale := K * wp / den
  endcombine
-- calculate the current output
  if (qvp <> 0) or (vp <> 0) then
    ang:=atan2(qvp,vp)
    mag:=sqrt(vp*vp + qvp*qvp)
  else
    ang:=0
    mag:=0.001 -- was 1
  endif
  wdvlim := sqrt(2) * WTOTAL / mag
  IF wdvlim > IRMSMX THEN
    wdvlim := IRMSMX
  ENDIF
  laplace(irmsa/wdvlim) := (1|s0)/(1|s0 + 0.002|s1)
  -- frequency lock bounds
  if wp < WPMIN then
    wp := WPMIN
    wpgood := 0
  endif
  if wp > WPMAX then
    wp := WPMAX
    wpgood := 0
  endif
  if wpgood < 1 then
    irmsa := 0.1
    mag := 0.0001
  endif
  -- uvtrip
  if t > 0.01 then
    if mag < uv2v then
      if uv2t < 0 then
        uv2t:=t
      elsif (t-uv2t) > UT2SET then
        uv2s:=0
        irmsa:=0
      endif
    else
      uv2t:=-1
    endif
  endif
  theta := ang + (PI/2) + (PI*PFANG/180.0)
  deria := 1.414 * irmsa * SIN(theta)
  i[1] := deria
  is[1] := deria
ENDEXEC
ENDMODEL
