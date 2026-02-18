# Copyright (C) 2026 Meltran, Inc

import os
import sys
import cim_examples 
import emthub.api as emthub

if __name__ == '__main__':
  idx = 0
  if len(sys.argv) > 1:
    idx = int(sys.argv[1])
  case = cim_examples.CASES[idx]
  dyrdf = emthub.load_psse_dyrfile (case)
  if dyrdf is None:
    print (case['name'], 'has no associated dyr file')
    quit()
  emthub.summarize_psse_dyrfile (dyrdf, case, bDetails=True)

