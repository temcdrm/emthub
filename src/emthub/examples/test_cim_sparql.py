# Copyright (C) 2025-2026 Meltran, Inc

import sys
import rdflib
import emthub.api as emthub

if __name__ == '__main__':
  idx = 4
  if len(sys.argv) > 1:
    idx = int(sys.argv[1])
  case = emthub.CASES[idx]
  g = rdflib.Graph()
  fname = case['name'] + '.ttl'
  #fname = case['name'] + '_merged.ttl'
  g.parse (fname)
  print ('read', len(g), 'statements from', fname)
  emthub.summarize_graph (g)

  d = emthub.load_emt_dict (g, case['id'], bTiming=True)

  for key in ['EMTIEEECigreDLLInputs*', 'EMTIEEECigreDLLOutputs*']:
    emthub.list_dict_table (d, key)
  quit()

  g = rdflib.Graph()
  fname = case['name'] + '_ic.ttl'
  g.parse (fname)
  print ('read', len(g), 'statements from', fname)
  emthub.summarize_graph (g)

  d2 = emthub.load_ic_dict (g)
  for key in ['EMTBusVoltageIC', 'EMTBranchFlowIC', 'EMTXfmrFlowIC']:
    emthub.list_dict_table (d2, key)

