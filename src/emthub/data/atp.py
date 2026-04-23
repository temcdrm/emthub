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
import random
#import h5utils
import numpy

atp_roots = ['IEEE39', 'IEEE118', 'WECC240', 'XfmrSat', 'SMIBDLL']
atp_path = '.'

def run_atp_case(atp_root):
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
    print ('Usage: python atp.py idx [run|convert|plot]')
    quit()
  idx = int(sys.argv[1])
  opt = sys.argv[2]
  atp_root = atp_roots[idx]

  if opt == 'run':
    print ('run', idx)
    run_atp_case (atp_root)
  elif opt == 'convert':
    print ('convert', idx)
  elif opt == 'plot':
    print ('plot', idx)
  else:
    print ('Unrecognized option:', opt)

