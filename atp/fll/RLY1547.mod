MODEL RLY1547
DATA
  vbase -- base line-to-line rms voltage
  vl1  {dflt: 0.50} -- voltage trip thresholds
  vl2  {dflt: 0.88} 
  vh1  {dflt: 1.20} 
  vh2  {dflt: 1.10} 
  dvl1 {dflt: 0.16} -- voltage trip delays 
  dvl2 {dflt: 2.00}
  dvh1 {dflt: 0.16}
  dvh2 {dflt: 1.00}
  fl1  {dflt: 57.0} -- frequency trip thresholds
  fl2  {dflt: 59.8}
  fh1  {dflt: 60.5}
  dfl1 {dflt: 0.16} -- frequency trip delays
  dfl2 {dflt: 1.00}
  dfh1 {dflt: 0.16}
INPUT 
  va
  vb
  vc
OUTPUT 
  stat  -- relay close status
VAR 
  vab   -- smoothed per-unit line-to-line rms voltage
  vbc
  vca
  stat  -- relay close status
  freq  -- frequency of vca

  tfl1  -- frequency pickup times
  tfl2
  tfh1
  tvl1ab -- voltage pickup times
  tvl2ab
  tvh1ab
  tvh2ab
  tvl1bc
  tvl2bc
  tvh1bc
  tvh2bc
  tvl1ca
  tvl2ca
  tvh1ca
  tvh2ca

  -- temp variables for vrms calculation
  vllab, vllbc, vllca, x2ab, x2bc, x2ca 
  ix2ab, ix2bc, ix2ca 
  per

  -- temp variables for frequency calculation
  a, amin, volt, tf

DELAY CELLS (ix2ab): 1/60/timestep+1
DELAY CELLS (ix2bc): 1/60/timestep+1
DELAY CELLS (ix2ca): 1/60/timestep+1
HISTORY volt {dflt:0}

INIT
  vab:=1
  vbc:=1
  vca:=1
  freq:=60
  stat:=1

  per:=1/60
  histdef(ix2ab):=0
  histdef(ix2bc):=0
  histdef(ix2ca):=0
  integral(x2ab):=0
  integral(x2bc):=0
  integral(x2ca):=0
  tf:=1/60

  tfl1:=-1
  tfl2:=-1
  tfh1:=-1
  tvl1ab:=-1
  tvl2ab:=-1
  tvh1ab:=-1
  tvh2ab:=-1
  tvl1bc:=-1
  tvl2bc:=-1
  tvh1bc:=-1
  tvh2bc:=-1
  tvl1ca:=-1
  tvl2ca:=-1
  tvh1ca:=-1
  tvh2ca:=-1
ENDINIT

EXEC
-- calculate the rms line-to-line voltages
  vllab:=(va-vb)/vbase
  x2ab:=vllab*vllab
  ix2ab:=integral(x2ab)
  vllbc:=(vb-vc)/vbase
  x2bc:=vllbc*vllbc
  ix2bc:=integral(x2bc)
  vllca:=(vc-va)/vbase
  x2ca:=vllca*vllca
  ix2ca:=integral(x2ca)
  if t > per then
    vab:=sqrt((ix2ab - delay(ix2ab,per))/per)
    vbc:=sqrt((ix2bc - delay(ix2bc,per))/per)
    vca:=sqrt((ix2ca - delay(ix2ca,per))/per)
  endif
-- calculate the frequency of Vca
  volt:=vllca
  a:=AND((stat),(volt),(-prevval(volt)))
  if a then
    amin:=max((fl1-0.1),(1/(tf+timestep)))
    if t > 2*per then
      freq:=min((amin),(fh1+0.1))
    endif
    tf:=0
  else
    tf:=tf+timestep
  endif

-- enable relay trip after one full cycle of simulation time
  if t>per then
-- frequency trip check
    if freq < fl1 then
      if tfl1 < 0 then
        tfl1:=t
      elsif (t-tfl1) > dfl1 then
        stat:=0
      endif
    else
      tfl1:=-1
    endif
    if freq < fl2 then
      if tfl2 < 0 then
        tfl2:=t
      elsif (t-tfl2) > dfl2 then
        stat:=0
      endif
    else
      tfl2:=-1
    endif
    if freq > fh1 then
      if tfh1 < 0 then
        tfh1:=t
      elsif (t-tfh1) > dfh1 then
        stat:=0
      endif
    else
      tfh1:=-1
    endif
-- voltage trip check on AB
    if vab < vl1 then
      if tvl1ab < 0 then
        tvl1ab:=t
      elsif (t-tvl1ab) > dvl1 then
        stat:=0
      endif
    else
      tvl1ab:=-1
    endif
    if vab < vl2 then
      if tvl2ab < 0 then
        tvl2ab:=t
      elsif (t-tvl2ab) > dvl2 then
        stat:=0
      endif
    else
      tvl2ab:=-1
    endif
    if vab > vh1 then
      if tvh1ab < 0 then
        tvh1ab:=t
      elsif (t-tvh1ab) > dvh1 then
        stat:=0
      endif
    else
      tvh1ab:=-1
    endif
    if vab > vh2 then
      if tvh2ab < 0 then
        tvh2ab:=t
      elsif (t-tvh2ab) > dvh2 then
        stat:=0
      endif
    else
      tvh2ab:=-1
    endif
-- voltage trip check on BC
    if vbc < vl1 then
      if tvl1bc < 0 then
        tvl1bc:=t
      elsif (t-tvl1bc) > dvl1 then
        stat:=0
      endif
    else
      tvl1bc:=-1
    endif
    if vbc < vl2 then
      if tvl2bc < 0 then
        tvl2bc:=t
      elsif (t-tvl2bc) > dvl2 then
        stat:=0
      endif
    else
      tvl2bc:=-1
    endif
    if vbc > vh1 then
      if tvh1bc < 0 then
        tvh1bc:=t
      elsif (t-tvh1bc) > dvh1 then
        stat:=0
      endif
    else
      tvh1bc:=-1
    endif
    if vbc > vh2 then
      if tvh2bc < 0 then
        tvh2bc:=t
      elsif (t-tvh2bc) > dvh2 then
        stat:=0
      endif
    else
      tvh2bc:=-1
    endif
-- voltage trip check on CA
    if vca < vl1 then
      if tvl1ca < 0 then
        tvl1ca:=t
      elsif (t-tvl1ca) > dvl1 then
        stat:=0
      endif
    else
      tvl1ca:=-1
    endif
    if vca < vl2 then
      if tvl2ca < 0 then
        tvl2ca:=t
      elsif (t-tvl2ca) > dvl2 then
        stat:=0
      endif
    else
      tvl2ca:=-1
    endif
    if vca > vh1 then
      if tvh1ca < 0 then
        tvh1ca:=t
      elsif (t-tvh1ca) > dvh1 then
        stat:=0
      endif
    else
      tvh1ca:=-1
    endif
    if vca > vh2 then
      if tvh2ca < 0 then
        tvh2ca:=t
      elsif (t-tvh2ca) > dvh2 then
        stat:=0
      endif
    else
      tvh2ca:=-1
    endif
  endif

ENDEXEC
ENDMODEL

