MODEL PV3FLL -- NB! 6 character name limit 

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

-- This uses the three-phase double second-order generalized integrator (DSOGI)
-- frequency-locked-loop (FLL) with gain normalization from
-- Teodorescu, Liserre and Rodriguez, "Grid Converters for Photovoltaic
-- and Wind Power Systems", Wiley, 2011, pp. 194-202. 
DATA  WC {dflt: 377.0}
      K  {dflt: 1.414}
      GAMMA {dflt: 46}
      VBASE {dflt: 4160}
      ANG0 {dflt: 0}
      WTOTAL {dflt: 500000.0}
      PFANG {dflt: 0}
      IRMSMX {dflt: 80.0}
      UV2SET {dflt: 0.50}
      UT2SET {dflt: 2.00}

VAR   deria
      derib
      deric
      theta
      wdvlim
      irms1
      valpha
      vbeta
      ang
      mag
      gepsf
      scale
      den
      wp
      epsval
      zalpha
      erralp
      vpalph
      qvpalp
      epsvbe
      zbeta
      errbet
      vpbeta
      qvpbet
      vpap
      vpbp
      vpan
      vpbn
      efalph
      efbeta
      intalp
      intbet
      inteps
      magalp
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
  g[1] := 0.0001
  g[2] := 0.0
  g[3] := 0.0
  g[4] := 0.0001
  g[5] := 0.0
  g[6] := 0.0001
  magalp := VBASE
  valpha := magalp * cos(ANG0*PI/360)
  vbeta := magalp * cos(ANG0*PI/360 + PI/2)
  qvpalp := vbeta
  qvpbet := -valpha
  wdvlim := 69.6
  irms1 := 0.0
  histdef(irms1):=0
  histdef(efalph):=0
  histdef(efbeta):=0
  histdef(gepsf):=0
  histdef(scale):=K*WC/VBASE/VBASE
  histdef(vpalph):=valpha
  histdef(vpbeta):=vbeta
  histdef(epsval):=0
  histdef(epsvbe):=0
  histdef(zalpha):=0
  histdef(zbeta):=0
  histdef(erralp):=0
  histdef(errbet):=0
  histdef(qvpalp):=qvpalp
  histdef(qvpbet):=qvpbet
  histdef(vpap):=valpha
  histdef(vpbp):=vbeta
  histdef(vpan):=0
  histdef(vpbn):=0
  histdef(den):=VBASE*VBASE
  histdef(wp):=WC
  histdef(intalp):=0
  histdef(intbet):=0
  histdef(inteps):=0
  integral(vpalph):=qvpalp/WC
  integral(vpbeta):=qvpbet/WC
  integral(erralp):=valpha
  integral(errbet):=vbeta
  integral(gepsf):=0
ENDINIT
EXEC
  if t=0 then
    flag:=1
  else
    flag:=0
  endif
-- FLL
  valpha := sqrt(2/3)*(v[1] - 0.5*v[2] - 0.5*v[3])
  vbeta := sqrt(2)*0.5*(v[2]-v[3])
  combine iterate as fll_norm
-- SOGI-QSG alpha
    epsval := valpha - vpalph
    zalpha := K * epsval - qvpalp
    erralp := wp * zalpha
    vpalph := integral(erralp)
    intalp := integral(vpalph)
    qvpalp := wp * intalp
-- SOGI-QSG beta
    epsvbe := vbeta - vpbeta
    zbeta  := K * epsvbe - qvpbet
    errbet := wp * zbeta
    vpbeta := integral(errbet)
    intbet := integral(vpbeta)
    qvpbet := wp * intbet
-- Positive-Negative Sequence
    vpap := 0.5 * (vpalph - qvpbet)
    vpbp := 0.5 * (qvpalp + vpbeta)
    vpan := 0.5 * (vpalph + qvpbet)
    vpbn := 0.5 * (vpbeta - qvpalp)
-- FLL normalization
    efalph := epsval * qvpalp
    efbeta := epsvbe * qvpbet
    den := vpap * vpap + vpbp * vpbp
    scale := K * wp / (10 + den)
    gepsf := -GAMMA * 0.5 * (efalph + efbeta) * scale
    inteps := integral(gepsf)
    wp := WC + inteps
  endcombine
-- RMS magnitude calculations, originally lock to vpalph, vpbeta
  if (vpap <> 0) or (vpbp <> 0) then -- lock to positive sequence
    ang:=atan2(vpbp,vpap)
    mag:=sqrt(vpap*vpap + vpbp*vpbp)  -- LL RMS
  else
    ang:=0
    mag:=0.001
  endif
  wdvlim := WTOTAL / mag / sqrt(3)
  IF wdvlim > IRMSMX THEN
    wdvlim := IRMSMX
  ENDIF
  laplace(irms1/wdvlim) := (1|s0)/(1|s0 + 0.002|s1)
  if wp < WPMIN then
    wp := WPMIN
    wpgood := 0
  endif
  if wp > WPMAX then
    wp := WPMAX
    wpgood := 0
  endif
  if wpgood < 1 then
    irms1 := 0.1
    mag := 0.0001
  endif
  -- uvtrip
  if t > 0.01 then
    if mag < uv2v then
      if uv2t < 0 then
        uv2t:=t
      elsif (t-uv2t) > UT2SET then
        uv2s:=0
        irms1:=0
      endif
    else
      uv2t:=-1
    endif
  endif
-- calculate the current outputs
  theta := ang + (PI/2) + (PI*PFANG/180.0)
  deria := 1.414 * irms1 * sin(theta)
  derib := 1.414 * irms1 * sin(theta - 2 * PI / 3)
  deric := 1.414 * irms1 * sin(theta + 2 * PI / 3)
  i[1] := deria
  is[1] := deria
  i[2] := derib
  is[2] := derib
  i[3] := deric
  is[3] := deric
ENDEXEC
ENDMODEL
