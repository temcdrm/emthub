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

PLOT_CONFIGS = {
  'IEEE39': {
    'suptitle': 'IEEE 39-bus Case',
    'sm_start': 2,
    'sm_end': 10,
    'ibr_start': 1,
    'ibr_end': 2,
    'tmin': 0.0,
    'tmax': 20.0,
    'tpll': 0.05,
    'tticks': [0.0, 4.0, 8.0, 12.0, 16.0, 20.0],
    },
  'IEEE118': {
    },
  'WECC240': {
    },
  'XfmrSat': {
    },
  'SMIBDLL': {
    }
}

def df_table (df, sm_start, sm_end, ibr_start, ibr_end):
  print ('Column                 Min           Max')
  key = 'I:FAULTC:'
  data = df[key]
  print ('{:12s} {:13.5f} {:13.5f}'.format (key, data.min(), data.max()))
  print ('Machine           FREQ Min           Max       VPU Min           Max     PMECH Min           Max       EFD Min           Max')
  for i in range(sm_start, sm_end):
    mach = 'SM{:03d}'.format(i)
    line = '{:12s}'.format(mach)
    for sig in ['W', 'V', 'P', 'F']:
      key = 'T:{:s}{:s}'.format (mach, sig)
      if key in df:
        data = df[key]
        line += ' {:13.5f} {:13.5f}'.format (data.min(), data.max())
    print (line)
  print ('IBR               FREQ Min           Max       P   Min           Max     Q     Min           Max                            ')
  for i in range(ibr_start, ibr_end):
    ibr = 'IBR{:02d}'.format(i)
    line = '{:12s}'.format(ibr)
    for sig in ['F', 'P', 'Q']:
      key = 'T:{:s}{:s}'.format (ibr, sig)
      if key in df:
        data = df[key]
        line += ' {:13.5f} {:13.5f}'.format (data.min(), data.max())
    print (line)

def plot_case (atp_root, bPng):
  plt.rcParams['savefig.directory'] = os.getcwd()

  cfg = PLOT_CONFIGS[atp_root]
  sm_start = cfg['sm_start']
  sm_end = cfg['sm_end']
  ibr_start = cfg['ibr_start']
  ibr_end = cfg['ibr_end']
  tticks = cfg['tticks']
  tmin = cfg['tmin']
  tmax = cfg['tmax']
  tpll = cfg['tpll']

  df = pd.read_hdf(atp_root+'.hdf5')
  df_table (df, sm_start, sm_end, ibr_start, ibr_end)

  fig, ax = plt.subplots (2, 4, sharex = 'col', figsize=(21,9), constrained_layout=True)
  fig.suptitle (cfg['suptitle'])
  t = np.array(df.index)
  fmin = np.where(t>=tpll)
  amin = np.where(t==tmin)
  amax = np.where(t==tmax)
  ifmin = int(fmin[0][0])
  imin = int(amin[0][0])
  imax = int(amax[0][0])
  print ('Plotting from', tmin, imin, t[imin], 'to', tmax, imax, t[imax])
  tplot = t[imin:imax] - tmin
  tfreq = t[ifmin:imax] - tpll

  ax[0,0].set_title ('Machine Frequency [pu]')
  for i in range(sm_start, sm_end):
    key = 'T:SM{:03d}W'.format(i)
    if key in df:
      ax[0,0].plot (tplot, np.array(df[key])[imin:imax])

  ax[0,1].set_title ('Machine Voltage [pu]')
  for i in range(sm_start, sm_end):
    key = 'T:SM{:03d}V'.format(i)
    if key in df:
      ax[0,1].plot (tplot, np.array(df[key])[imin:imax])

  ax[0,2].set_title ('Fault Current [kA]')
  key = 'I:FAULTC:'
  ax[0,2].plot (tplot, 0.001 * np.array(df[key])[imin:imax], label=key)
  ax[0,2].legend()

  ax[1,0].set_title ('Machine Pmech [pu]')
  for i in range(sm_start, sm_end):
    key = 'T:SM{:03d}P'.format(i)
    if key in df:
      ax[1,0].plot (tplot, np.array(df[key])[imin:imax])

  ax[1,1].set_title ('Machine Efd [pu]')
  for i in range(sm_start, sm_end):
    key = 'T:SM{:03d}F'.format(i)
    if key in df:
      ax[1,1].plot (tplot, np.array(df[key])[imin:imax])

  ax[1,2].set_title ('IBR Frequency [pu]')
  for i in range(ibr_start, ibr_end):
    key = 'T:IBR{:02d}F'.format(i)
    if key in df:
      ax[1,2].plot (tfreq, np.array(df[key])[ifmin:imax] / 376.9911)

  ax[0,3].set_title ('IBR P [pu]')
  for i in range(ibr_start, ibr_end):
    key = 'T:IBR{:02d}P'.format(i)
    if key in df:
      ax[0,3].plot (tplot, np.array(df[key])[imin:imax], label=key)
#   ax[0,3].legend()

  ax[1,3].set_title ('IBR Q [pu]')
  for i in range(ibr_start, ibr_end):
    key = 'T:IBR{:02d}Q'.format(i)
    if key in df:
      ax[1,3].plot (tplot, np.array(df[key])[imin:imax])

  for i in range(2):
    for j in range(4):
      ax[i,j].grid()
      ax[i,j].set_xlim (tticks[0], tticks[-1])
      ax[i,j].set_xticks (tticks)

  if bPng:
    plt.savefig(atp_root+'.png')
  else:
    plt.show()
  plt.close()

def run_atp_case (atp_root):
  cmdline = 'c:\\atp\\atpmingw\\mytpbig ' + atp_root + '.atp >nul'
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
    plot_case (atp_root, bPng=False)
    print ('plot', idx)
  elif opt == 'png':
    plot_case (atp_root, bPng=True)
    print ('png', idx)
  else:
    print ('Unrecognized option:', opt)

