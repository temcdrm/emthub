# Copyright (C) 2023 Battelle Memorial Institute
# Copyright (C) 2025-2026 Meltran, Inc

import sys
import rdflib
import emthub.api as emthub

if __name__ == '__main__':
  case_id = 2
  if len(sys.argv) > 1:
    case_id = int(sys.argv[1])
  case = emthub.CASES[case_id]
  sys_id = case['id']
  sys_name = case['name']

  g = rdflib.Graph()
  fname = sys_name + '.ttl'
  g.parse ('../test/' + fname)
  print ('read', len(g), 'statements from', fname)
  d = emthub.load_emt_dict (g, case['id'], bTiming=True)

  G = emthub.build_system_graph (d)
  emthub.save_system_graph (G, './{:s}_Network.json'.format(sys_name))


