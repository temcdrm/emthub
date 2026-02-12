# Copyright (C) 2026 Meltran, Inc

import os
import sys
import pandas as pd
import cim_examples 
import io
import re
import math

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
        line = line.replace("'", "")
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
  return dyr

def row_length (row):
  for i in range(2, len(row)):
    if isinstance(row[i], float) and math.isnan(row[i]):
      return i
  return len(row)

if __name__ == '__main__':
  idx = 0
  if len(sys.argv) > 1:
    idx = int(sys.argv[1])
  case = cim_examples.CASES[idx]
  dyr = read_dyr_file (case)
  models = {}
  for row in dyr.itertuples(index=False):
    model_type = str(row[1])
    n = row_length (row)
    if model_type not in models:
      models[model_type] = {'count': 1, 'min_len': n, 'max_len': n}
    else:
      models[model_type]['count'] += 1
      if n < models[model_type]['min_len']:
        models[model_type]['min_len'] = n
      if n > models[model_type]['max_len']:
        models[model_type]['max_len'] = n

  print (case['name'])
  print ('Model   Count   Nmin   Nmax')
  for key in sorted (models):
    row = models[key]
    print ('{:6s} {:6d} {:6d} {:6d}'.format (key, row['count'], row['min_len'], row['max_len']))

