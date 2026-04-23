# Copyright (C) 2025-2026 Meltran, Inc

import rdflib
import sys
import os
import emthub.api as emthub

if __name__ == '__main__':
  idx = 0
  if len(sys.argv) > 1:
    idx = int(sys.argv[1])
  case = emthub.CASES[idx]

  g = rdflib.Graph()
  fname = case['name']+'.ttl'
  g.parse (fname)
  print ('read', len(g), 'statements from', fname)
  d = emthub.load_emt_dict (g, case['id'], bTiming=False)
  for key in ['EMTBaseVoltage']: # , 'EMTIBRPlantAttributes', 'EMTIEEECigreDLL', 'EMTIEEECigreDLLInputs*', 'EMTIEEECigreDLLOutputs*']:
    emthub.list_dict_table (d, key)

  icd = None
  fname = case['name']+'_ic.ttl'
  if os.path.exists(fname):
    g = rdflib.Graph()
    g.parse (fname)
    print ('read', len(g), 'initial condition statements from', fname)
    icd = emthub.load_ic_dict (g)
    #emthub.list_dict_table (icd, 'EMTBusVoltageIC')

  emthub.create_atp (d, icd, fpath = '', case=case)

