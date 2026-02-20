# Copyright (C) 2023 Battelle Memorial Institute
# Copyright (C) 2025-2026 Meltran, Inc

import sys
#import math
#import networkx as nx
#import json
#import os
import rdflib
import cim_examples
import emthub.api as emthub

if __name__ == '__main__':
  case_id = 2
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

  G = emthub.build_system_graph (d)
  emthub.save_system_graph (G, './raw/{:s}_Network.json'.format(sys_name))


