# Copyright (C) 2025-2026 Meltran, Inc

import rdflib
import sys
import os
import cim_examples
import emthub.api as emthub

if __name__ == '__main__':
  idx = 4
  if len(sys.argv) > 1:
    idx = int(sys.argv[1])
  case = cim_examples.CASES[idx]

  g = rdflib.Graph()
  fname = case['ttlfile']
  g.parse (fname)
  print ('read', len(g), 'statements from', fname)
  d = emthub.load_emt_dict (g, case['id'], bTiming=False)
  for key in ['EMTBaseVoltage']:# , 'EMTIBRPlantAttributes', 'EMTIEEECigreDLL', 'EMTCountDLLParameters']: #, 'EMTIEEECigreDLLParameters*']:
    emthub.list_dict_table (d, key)

  icd = None
  if 'ttl_ic' in case and os.path.exists(case['ttl_ic']):
    g = rdflib.Graph()
    fname = case['ttl_ic']
    g.parse (fname)
    print ('read', len(g), 'initial condition statements from', fname)
    icd = emthub.load_ic_dict (g)
    #emthub.list_dict_table (icd, 'EMTBusVoltageIC')

  emthub.create_atp (d, icd, fpath = '../atp/data/', case=case)

