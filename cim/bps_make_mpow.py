# Copyright (C) 2023-2024 Battelle Memorial Institute
# Copyright (C) 2025-2026 Meltran, Inc

import sys
import os
import rdflib
import emthub.api as emthub
import cim_examples

if __name__ == '__main__':
  case_id = 3
  if len(sys.argv) > 1:
    case_id = int(sys.argv[1])
  case = cim_examples.CASES[case_id]
  sys_id = case['id']
  sys_name = case['name']

  g = rdflib.Graph()
  fname = sys_name + '.ttl'
  g.parse (fname)
  print ('read', len(g), 'statements from', fname)
  d = emthub.load_emt_dict (g, case['id'], bTiming=True)

  fp = open ('../matpower/' + sys_name + '.m', 'w')
  emthub.create_matpower (d, sys_name, fp, case['swingbus'], case['load'])
  fp.close()

