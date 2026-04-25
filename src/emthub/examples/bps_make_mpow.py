# Copyright (C) 2023-2024 Battelle Memorial Institute
# Copyright (C) 2025-2026 Meltran, Inc

import sys
import os
import rdflib
import emthub.api as emthub

if __name__ == '__main__':
  case_id = 0
  if len(sys.argv) > 1:
    case_id = int(sys.argv[1])
  case = emthub.CASES[case_id]
  sys_id = case['id']
  sys_name = case['name']
  if not case['UseMATPOWER']:
    print ('{:s} does not use MATPOWER'.format(sys_name))
    quit()

  g = rdflib.Graph()
  fname = sys_name + '.ttl'
  g.parse (fname)
  print ('read', len(g), 'statements from', fname)
  d = emthub.load_emt_dict (g, case['id'], bTiming=True)

  fp = open (sys_name + '.m', 'w')
  emthub.create_matpower (d, sys_name, fp, case['swingbus'], case['load'])
  fp.close()

