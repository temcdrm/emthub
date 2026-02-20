# Copyright (C) 2025-2026 Meltran, Inc

import sys
import cim_examples
import emthub.api as emthub
 
if __name__ == '__main__':
  case_id = 0
  if len(sys.argv) > 1:
    case_id = int(sys.argv[1])
  case = cim_examples.CASES[case_id]

  tables, kvbases, bus_kvbases, baseMVA = emthub.load_psse_rawfile (case['rawfile'])
  emthub.print_psse_table (tables, 'SYSTEM SWITCHING DEVICE')

  print ('All kV Bases =', kvbases)

  emthub.create_cim_sql (tables, kvbases, bus_kvbases, baseMVA, case)
  

