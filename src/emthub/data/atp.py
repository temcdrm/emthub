# Copyright (C) 2018-2022 Battelle Memorial Institute
# Copyright (C) 2026 Meltran, Inc
# file: Atp.py
""" Run ATP cases, convert outputs, plot hdf5 files.
"""

import math
import sys
import operator
import subprocess
import os
import shutil
import pandas as pd
import numpy as np
from comtrade import Comtrade
import matplotlib.pyplot as plt
from scipy import signal

atp_roots = ['IEEE39', 'IEEE118', 'WECC240', 'XfmrSat', 'SMIBDLL']
atp_path = '.'

def summarize_df (df, label):
  print ('Column                         Min           Max {:s}'.format (label))
  for lbl, data in df.items():
    print ('{:20s} {:13.5f} {:13.5f}'.format (lbl, data.min(), data.max()))

def make_pd_key (prefix, tok1, tok2 = None):
  key = '{:s}:{:s}'.format (prefix, tok1.lstrip().rstrip().replace('_', ''))
  if tok2 is not None:
    key = '{:s}:{:s}'.format (key, tok2.lstrip().rstrip().replace('_', ''))
  return key

def comtrade_to_pd5 (atp_root):
  chan = {}
  rec = Comtrade ()
  rec.load (atp_root + '.cfg', atp_root + '.dat')
  t = np.array(rec.time)
  t = np.linspace (t[0], t[-1], len(t)) # COMTRADE does not have sub-microsecond time steps
  for i in range(rec.analog_count):
    lbl = rec.analog_channel_ids[i]
    tok1 = lbl[0:6]
    tok2 = lbl[7:13]
    tok3 = lbl[14:]
#    print ('"{:s}" "{:s}" "{:s}" "{:s}"'.format (lbl, tok1, tok2, tok3))
    key = None
    if tok1 == 'TACS  ':
      key = make_pd_key ('T', tok2)
    elif tok1 == 'MODELS':
      key = make_pd_key ('M', tok2)
    elif tok3 == 'V-branch':
      key = make_pd_key ('V', tok1, tok2)
    elif tok3 == '  V-node':
      key = make_pd_key ('V', tok1)
    elif tok3 == 'I-branch':
      key = make_pd_key ('I', tok1, tok2)
    else:
      print ('Unrecognized COMTRADE Channel {:d} "{:s}"'.format (i, lbl))
    if key is not None:
      chan[key] = np.array (rec.analog[i])

  df = pd.DataFrame(data=chan, index=t)
  df.info()
  df.to_hdf(atp_root + '.hdf5', key='Base', mode='w', complevel=4)

def run_atp_case (atp_root):
  cmdline = 'c:\\atp\\atpgnu\\runtpgig ' + atp_root + '.atp >nul'
  print (cmdline)
  pw0 = subprocess.Popen (cmdline, cwd=atp_path, shell=True)
  pw0.wait()

  cmdline = 'c:\\atp\\gtppl32\\gtppl32 @@commands.script > nul'
  fp = open ('commands.script', mode='w')
  print ('file', atp_root, file=fp)
  print ('comtrade all', file=fp)
  print ('', file=fp)
  print ('stop', file=fp)
  fp.close()
  pw0 = subprocess.Popen (cmdline, cwd=atp_path, shell=True)
  pw0.wait()

if __name__ == '__main__':
  if len(sys.argv) != 3:
    print ('Usage: python atp.py idx [run|convert|plot|png]')
    quit()
  idx = int(sys.argv[1])
  opt = sys.argv[2]
  atp_root = atp_roots[idx]

  if opt == 'run':
    print ('run', idx)
    run_atp_case (atp_root)
  elif opt == 'convert':
    print ('convert', idx)
    comtrade_to_pd5 (atp_root)
  elif opt == 'plot':
    print ('plot', idx)
  elif opt == 'png':
    print ('png', idx)
  else:
    print ('Unrecognized option:', opt)

