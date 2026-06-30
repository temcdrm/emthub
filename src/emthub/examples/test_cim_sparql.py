# Copyright (C) 2025-2026 Meltran, Inc

import sys
import rdflib
import emthub.api as emthub

def main():
  """Use this for printing the results of a SPARQL query loaded into a Python dictionary.
  Edit the script to print the dictionaries of interest.

  Command-line Arguments:
    **index** (int): case number from 0 to 4
  """
  idx = 4
  if len(sys.argv) > 1:
    idx = int(sys.argv[1])
  case = emthub.CASES[idx]
  g = rdflib.Graph(store='Oxigraph')
  fname = case['name'] + '.ttl'
  #fname = case['name'] + '_merged.ttl'
  g.parse (fname)
  print ('read', len(g), 'statements from', fname)
  emthub.summarize_graph (g)

  d = emthub.load_emt_dict (g, case['id'], bTiming=True)

  for key in ['EMTIEEECigreDLLInfo', 'EMTIEEECigreDLLParameterInfos*', 'EMTIEEECigreDLLInputSignalInfos*', 'EMTIEEECigreDLLOutputSignalInfos*']:
#  for key in ['EMTIBRPlant*', 'EMTIBRPlantAttributes', 'EMTCountDLLInputs', 'EMTCountDLLOutputs', 'EMTCountDLLParameters',
#              'EMTIEEECigreDLL', 'EMTIEEECigreDLLInputs*', 'EMTIEEECigreDLLOutputs*', 'EMTIEEECigreDLLParameters*',
#              'EMTEquipmentContainer', 'EMTDCEquipmentContainer', 'EMTDCNode', 'EMTDCShunt', 'EMTDCEnergySource']:
    emthub.list_dict_table (d, key)
  quit()

  g = rdflib.Graph(store='Oxigraph')
  fname = case['name'] + '_ic.ttl'
  g.parse (fname)
  print ('read', len(g), 'statements from', fname)
  emthub.summarize_graph (g)

  d2 = emthub.load_ic_dict (g)
  for key in ['EMTBusVoltageIC', 'EMTBranchFlowIC', 'EMTXfmrFlowIC']:
    emthub.list_dict_table (d2, key)

if __name__ == '__main__':
  main()

