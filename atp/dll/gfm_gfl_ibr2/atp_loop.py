# Copyright (C) 2025 Meltran, Inc
# file: atp_loop.py
""" Run all ATP test cases for EPRI IBR2 model report.

Called from ATP_Loop.bat, driven by coded  parameter arrays.

Public Functions:
    :main: does the work
"""

import math
import sys
import operator
import subprocess
import os
import shutil
import random
import h5utils
import numpy

atp_path = '.'

parmcopy = """DDN_____=DDN
DFSRC_____=DFSRC
DPHI______=DPHI
DPREF_____=DPREF
DQREF_____=DQREF
DUP_____=DUP
DVAMP_____=DVAMP
DVREF_____=DVREF
FFLAG___=FFLAG
FSRC0_____=FSRC0
KQ_I____=KQ_I
KQ_P____=KQ_P
KQV1____=KQV1
KQV2____=KQV2
KV_I____=KV_I
KV_P____=KV_P
LCHOK_=LCHOK
MGAIN_=MGAIN
PHI0______=PHI0
PREF0_____=PREF0
QCFLG___=QCFLG
QREF0_____=QREF0
RCHOK_=RCHOK
TAB1______=TAB1
TAB2______=TAB2
TAC1______=TAC1
TAC2______=TAC2
TAG1______=TAG1
TAG2______=TAG2
TBC1______=TBC1
TBC2______=TBC2
TBG1______=TBG1
TBG2______=TBG2
TCG1______=TCG1
TCG2______=TCG2
TFSRC_____=TFSRC
TPHI______=TPHI
TPREF_____=TPREF
TQREF_____=TQREF
TVAMP_____=TVAMP
TVREF_____=TVREF
V2FLG___=V2FLG
VAMP0_____=VAMP0
VREF0_____=VREF0
VTFLG___=VTFLG"""

baseparms = {
  'CFILT': 776.0,   
  'DDN': 20.0,      
  'DFSRC': 0.05,    
  'DPHI': 0.1,      
  'DPREF': -0.2,    
  'DQREF': 0.25,    
  'DUP': 0.0,       
  'DVAMP': 1000.0,  
  'DVREF': 0.02,    
  'FFLAG': 0.0,     
  'FSRC0': 60.0,    
  'KQ_I': 40.0,     
  'KQ_P': 0.0,      
  'KQV1': 2.0,      
  'KQV2': 2.0,      
  'KV_I': 100.0,    
  'KV_P': 0.0,      
  'LCHOK': 3.6E-5,  
  'MGAIN': 600.0,   
  'PHI0': 1.0E-6,   
  'PREF0': 0.9,     
  'QCFLG': 0.0,     
  'QREF0': 0.05,    
  'RCHOK': 1.0E-8,  
  'RDAMP': 0.05,    
  'TAB1': 999.0,    
  'TAB2': 1000.0,   
  'TAC1': 994.0,    
  'TAC2': 994.2,    
  'TAG1': 994.0,    
  'TAG2': 994.2,    
  'TBC1': 994.0,    
  'TBC2': 994.2,    
  'TBG1': 999.0,    
  'TBG2': 1000.0,   
  'TCG1': 999.0,    
  'TCG2': 1000.0,   
  'TFSRC': 994.0,   
  'TPHI': 994.0,    
  'TPREF': 994.0,   
  'TQREF': 994.0,   
  'TVAMP': 994.0,   
  'TVREF': 4.0,     
  'V2FLG': 1.0,     
  'VAMP0': 28169.13,
  'VREF0': 1.01,    
  'VTFLG': 1.0}

def AtpFit10(x):
  if x == 0.0:
    return '0.0'
  elif x < 0.0:
    return '{:9.3e}'.format(x)
  return '{:10.4e}'.format(x)

def AtpFit6(x):
  if x == 0.0:
    return '0.0000'
  elif x >= 20000:  # special handling of VAMP0
    xstr = '{:6.2f}'.format(x)
  elif x >= 10000:
    exp = 0
    while x >= 1000:
      x /= 10.0
      exp += 1
    xstr = '{:3d}.E{:d}'.format(int(round(x, 3)), exp)
  elif x >= 1000:
    xstr = '{:6.1f}'.format(x)
  elif x >= 100:
    xstr = '{:6.2f}'.format(x)
  elif x >= 10:
    xstr = '{:6.3f}'.format(x)
  elif x <= -100.0:
    xstr = '{:6.1f}'.format(x)
  elif x <= -10.0:
    xstr = '{:6.2f}'.format(x)
  elif x <= -1.0:
    xstr = '{:6.3f}'.format(x)
  elif x < 0.0:
    xstr = '{:6.3f}'.format(x)
  elif x <= 0.001:
    exp = 0
    while x < 10.0:
      x *= 10.0
      exp += 1
    xstr = '{:2d}.E-{:d}'.format(int(round(x)), exp)
  else:
    xstr = '{:6.4f}'.format(x)
  return xstr

def run_atp_case(atp_root, pl4_dest, parms, Tstep=1.0e-5, Tmax=5.0):
  atp_file = '{:s}.atp'.format (atp_root)
  prm_file = '{:s}.prm'.format (atp_root)
  lis_file = '{:s}.lis'.format (atp_root)
  pl4_file = '{:s}.pl4'.format (atp_root)
  fp = open (prm_file, mode='w')
  print ('$PARAMETER', file=fp)
  print ('__DELTAT   ={:s}'.format (AtpFit6 (Tstep)), file=fp)
  print ('____TMAX   ={:s}'.format (AtpFit6 (Tmax)), file=fp)
  for key, val in parms.items():
    print ('{:s}={:s} $$'.format (key, AtpFit6 (val)), file=fp)
  print (parmcopy, file=fp)
  print ('BLANK END PARAMETER', file=fp)
  fp.close()
  cmdline = 'mytpbig ' + atp_file + ' >nul'
  pw0 = subprocess.Popen (cmdline, cwd=atp_path, shell=True)
  pw0.wait()

  # move the pl4 file
  cmdline = 'c:\\atp\\gtppl32\\gtppl32 @@commands.script > nul'
  fp = open ('commands.script', mode='w')
  print ('file', atp_root, file=fp)
  print ('comtrade all', file=fp)
  print ('', file=fp)
  print ('stop', file=fp)
  fp.close()
  pw0 = subprocess.Popen (cmdline, cwd=atp_path, shell=True)
  pw0.wait()

def add_training_set (idx, atp_root, pl4_file, hdf5_file, parms):
  print ('Running', idx, parms)

  grp_name = 'group{:d}'.format(idx)
  if idx < 1:
    print ('writing', grp_name)
    mode = 'w'
  else:
    print ('appending', grp_name)
    mode = 'a'

  run_atp_case (atp_root, pl4_file,  parms)
  channels = h5utils.load_atp_comtrade_channels (atp_root)
  h5utils.save_atp_channels (hdf5_file, grp_name, channels, mode=mode)

  return idx+1

if __name__ == '__main__':
  atp_root = sys.argv[1]
  pl4_path = sys.argv[2]
  hdf5_file = sys.argv[3]
  pl4_file = '{:s}/{:s}.pl4'.format (pl4_path, atp_root)
  print ('running {:s}, PL4 output to {:s}, hdf5 archive to {:s}'.format (atp_root, pl4_file, hdf5_file))
  idx = 0
  add_training_set (idx, atp_root, pl4_file, hdf5_file, baseparms)

