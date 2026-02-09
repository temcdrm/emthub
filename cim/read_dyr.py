# Copyright (C) 2026 Meltran, Inc

import os
import sys
import pandas as pd
import cim_examples 
import io
import re

# the PSSE DYR file does not conform to CSV standards:
#  1) A line beginning with / or // is a comment to be ignored
#  2) Rows span lines. Each row ends with a single /
#  3) Field delimiters are comma (,) or any number of blanks
#  4) Each row generally begins with bus number (int), model name (str), and ID (str) but the ID is not always quoted
def read_dyr_file (case):
  if 'dyrfile' in case and case['dyrfile'] is not None and os.path.exists(case['dyrfile']):
    buf = io.StringIO()
    maxcols = 0
    ncols = 0
    with open (case['dyrfile'], 'r') as file:
      for line in file:
        line = line.strip()
        if len(line) == 0 or line.startswith ('/'):
          continue
        s = re.sub ('[ ,\t]+', ',', line)
        if s.endswith('/'):
          s = s.replace(',/','\n')
          s = s.replace('/','\n')
          ncols += s.count(',')
          if ncols > maxcols:
            maxcols = ncols
          ncols = 0
        else:
          s = s + ','
          ncols += s.count(',')
        buf.write(s)
#    buf.seek(0)
#    print (buf.read())
    maxcols += 1
    print ('maxcols', maxcols)
    buf.seek(0)
    dyr = pd.read_csv (buf, names=range(maxcols))
    print ('Dynamics data from', case['dyrfile'], 'includes', dyr.shape)
    print (dyr)
    buf.close()

if __name__ == '__main__':
  idx = 0
  if len(sys.argv) > 1:
    idx = int(sys.argv[1])
  case = cim_examples.CASES[idx]
  read_dyr_file (case)

