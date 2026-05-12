# Copyright (C) 2025-2026 Meltran, Inc

import sys
import emthub.api as emthub
 
def main():
  """Creates CIM RDF from *rawfile* and *dyrfile* data. Three output formats are produced, namely TTL, XML, and JSON.

  Command-line Arguments:
    **index** (int): case number from 0 to **3**. Case 4 uses *create_smib_dll.py* instead.
  """
  case_id = 0
  if len(sys.argv) > 1:
    case_id = int(sys.argv[1])
  case = emthub.CASES[case_id]

  tables, kvbases, bus_kvbases, baseMVA = emthub.load_psse_rawfile (case['name']+'.raw')
#  emthub.print_psse_table (tables, 'GENERATOR')

  print ('All kV Bases =', kvbases)

  emthub.create_cim_rdf (tables, kvbases, bus_kvbases, baseMVA, case)
  
if __name__ == '__main__':
  main()

