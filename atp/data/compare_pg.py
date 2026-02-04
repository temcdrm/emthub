# Copyright (C) 2026 Meltran, Inc

import re
import sys

if __name__ == '__main__':
  root = 'WECC240'
  if len(sys.argv) > 1:
    root = sys.argv[1]

  print ('Summarizing', root)
  total_pibr = 0.0
  total_sibr = 0.0

  total_pmpow = 0.0
  total_patp = 0.0

  pthev = 0.0
  swing_mva = 0.0
  swing_bus = ''
  gens = {}
  with open ('{:s}_net.atp'.format(root), 'r') as fp:
    for line in fp:
      if 'SyncMachine' in line:
        toks = line.split(' ')
        if toks[8] == 'part':
          swing_bus = toks[4]
          swing_mva = float(toks[6])
        else:
          data = {'RawBus':toks[4], 'Rating': float(toks[6]), 'Pmpow': float(toks[8]), 'Patp':0.0}
      elif '$INCLUDE,SYNCMACH.PCH,' in line:
        toks = line.split(',')
        key = toks[2]
        gens[key] = data
      elif 'C solar' in line or 'C wind' in line:
        toks = line.split(' ')
        total_pibr += float(toks[9])
        total_sibr += float(toks[6])
  with open ('{:s}.lis'.format(root), 'r') as fp:
    bLooking = False
    for line in fp:
      if 'Solution at nodes with known voltage.' in line:
        bLooking = True
      elif 'Data parameters and initial conditions of next machine follow.' in line:
        bLooking = False
      elif bLooking:
        if 'THEV_A' in line:
          toks = re.split('[ ]+', line.lstrip(' '))
          pa = float(toks[5])
          pthev = 3.0e-6*pa
        elif '_A' in line:
          toks = re.split('[ ]+', line.lstrip(' '))
          pgen = 3.0e-6*float(toks[5])
          key = toks[0][0:5]
          gens[key]['Patp'] = pgen

  print ('ATPbus RawBus      MVA      Ppf     Patp Error[%]')
  for key, row in gens.items():
    pmpow = row['Pmpow']
    patp = row['Patp']
    total_pmpow += pmpow
    total_patp += patp
    if pmpow > 0.0:
      error = 100.0*(patp-pmpow)/pmpow
    else:
      error = 0.0
    print ('{:5s}: {:6s} {:8.2f} {:8.2f} {:8.2f} {:8.2f}'.format (key, row['RawBus'], row['Rating'], pmpow, patp, error))
  print ('Thevenin injection = {:.2f} MW at {:s}, rating {:.2f} MVA'.format (pthev, swing_bus, swing_mva))
  print ('IBR dispatch  = {:.2f} MW, total rating {:.2f} MVA'.format (total_pibr, total_sibr))
  print ('SM dispatch  = {:.2f} MW, ATP total is {:.2f} MW'.format (total_pmpow, total_patp))


