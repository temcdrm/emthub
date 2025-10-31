import json
import sys
import math

VPK_TO_KVRMS = math.sqrt(3.0) / math.sqrt(2.0) / 1000.0

def AssignInitialConditions (d, bus, p, q, vmag, vang):
  for key, row in d.items():
    if bus == row['Bus'] and row['Source'] is not None:
      row['P'] = p
      row['Q'] = q
      row['Vmag'] = vmag
      row['Vang'] = vang
      return

if __name__ == '__main__':
  fname = 'IEEE118'
  if len(sys.argv) > 1:
    fname = sys.argv[1]

  jp = open('{:s}_dgen.json'.format (fname), 'r')
  d = json.load(jp)
  jp.close()

#  B177_A  10570.177955925           11268.      4613.0516336008  4982.6115463341      .280560072144E8   .28072033452E8
#          -3903.736925061      -20.2700000      -1883.128367211      -22.2061417      948430.97798532        0.9994291

  bInSources = False
  bNeedNextLine = False
  fp = open ('{:s}.lis'.format (fname), 'r')
  bus = ''
  p = 0.0
  q = 0.0
  vmag = 0.0
  vang = 0.0
  for ln in fp:
    if 'Solution at nodes with known voltage.' in ln:
      print ('Found sources')
      bInSources = True
    elif 'Data parameters and initial conditions of next machine follow.' in ln:
      print ('Done with sources')
      bInSources = False
      break
    elif 'Zero-frequency (dc) steady-state solution for TACS follows.' in ln:
      print ('Done with sources')
      bInSources = False
      break
    elif bNeedNextLine:
      toks = ln.split()
      bNeedNextLine = False
      vang = float(toks[1])
      q = float(toks[4]) * 3.0e-6
      AssignInitialConditions (d, bus, p, q, vmag, vang)
    elif bInSources:
      toks = ln.split()
      if len(toks) == 7:
        if '_A' in toks[0]:
          bus = toks[0][0:5] # drop the phase designator in position 5
          vmag = float(toks[2]) * VPK_TO_KVRMS
          p = float(toks[5]) * 3.0e-6
          bNeedNextLine = True

  fp.close()

  print ('Name       Type     Source Bus         kV      MVA        P        Q    Vpu    Vang')
  for key, row in d.items():
    kvbase = row['kV']
    print ('{:10s} {:8s} {:6s} {:6s} {:7.2f} {:8.2f} {:8.2f} {:8.2f} {:6.4f} {:7.4f}'.format (key,
      row['Type'], str(row['Source']), row['Bus'], kvbase, row['S'], row['P'], row['Q'], 
      row['Vmag'] / kvbase, row['Vang']))
