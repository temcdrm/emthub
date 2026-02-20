# Copyright (C) 2023 Battelle Memorial Institute
# Copyright (C) 2025-2026 Meltran, Inc

import sys
import cim_examples
import emthub.api as emthub

if __name__ == '__main__':
  case_id = 0
  plot_labels = False
  if len(sys.argv) > 1:
    case_id = int(sys.argv[1])
    if len(sys.argv) > 2:
      if int(sys.argv[2]) > 0:
        plot_labels = True
  case = cim_examples.CASES[case_id]
  sys_name = case['name']
  loc = case['legend_loc']
  G = emthub.load_system_graph ('./raw/{:s}_Network.json'.format(sys_name))
  emthub.plot_system_graph (G, sys_name, plot_labels, loc)


