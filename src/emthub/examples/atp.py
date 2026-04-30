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
    'der_start': None,
    'der_end': None,
    'ncols': 4,
    'tmin': 0.0,
    'tmax': 20.0,
    'tpll': 0.05,
    'tticks': [0.0, 4.0, 8.0, 12.0, 16.0, 20.0]
    },
  'IEEE118': {
    'suptitle': 'IEEE 118-bus Case',
    'sm_start': 0,
    'sm_end': 56,
    'ibr_start': 0,
    'ibr_end': 19,
    'der_start': None,
    'der_end': None,
    'ncols': 4,
    'tmin': 0.0,
    'tmax': 20.0,
    'tpll': 0.05,
    'tticks': [0.0, 4.0, 8.0, 12.0, 16.0, 20.0]
    },
  'WECC240': {
    'suptitle': 'WECC 240-bus Case',
    'sm_start': 0,
    'sm_end': 105,
    'ibr_start': 0,
    'ibr_end': 35,
    'der_start': 0,
    'der_end': 2,
    'ncols': 5,
    'tmin': 0.0,
    'tmax': 20.0,
    'tpll': 0.05,
    'tticks': [0.0, 4.0, 8.0, 12.0, 16.0, 20.0]
    },
  'XfmrSat': {
    'suptitle': 'Transformer Saturation Case'
    },
  'SMIBDLL': {
    'suptitle': 'SMIB DLL Test Case'
    }
}

def df_table (df, sm_start, sm_end, ibr_start, ibr_end, der_start=None, der_end=None):
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
  if der_end is not None:
    print ('DER               FREQ Min           Max      VRMS Min           Max      IRMS Min           Max')
    for i in range(der_start, der_end):
      der = 'DR{:03d}'.format(i+1)
      line = '{:12s}'.format(der)
      for sig in ['W', 'V', 'I']:
        key = 'T:{:s}{:s}'.format (der, sig)
        if key in df:
          data = df[key]
          line += ' {:13.5f} {:13.5f}'.format (data.min(), data.max())
      print (line)

def plot_xfmr_sat (atp_root, bPng):
  cfg = PLOT_CONFIGS[atp_root]

  lsize = 22
  plt.rc('font', family='serif')
  plt.rc('xtick', labelsize=lsize)
  plt.rc('ytick', labelsize=lsize)
  plt.rc('axes', labelsize=lsize)
  plt.rc('legend', fontsize=lsize)

  tticks = [0.0, 0.1, 0.2, 0.3]
  vbase = 345000.0 * math.sqrt(2.0/3.0)
  SQRT3H = math.sqrt(3.0) / 2.0
  TWOTHIRDS = 2.0 / 3.0
  SQRT23 = math.sqrt(TWOTHIRDS)

  b, a = signal.butter (2, 1.0 / 2048.0, btype='low', analog=False)
  df = pd.read_hdf(atp_root + '.hdf5')
  summarize_df (df, cfg['suptitle'])

  fig, ax = plt.subplots (1, 3, sharex = 'col', figsize=(21,9), constrained_layout=True)
  # fig.suptitle (cfg['suptitle'], fontsize=lsize+4)
  t = np.array(df.index)
  va = df['V:B3A']
  vb = df['V:B3B']
  vc = df['V:B3C']
  ia = df['I:B2A:B3A']
  ib = df['I:B2B:B3B']
  ic = df['I:B2C:B3C']
  p = va*ia+vb*ib+vc*ic

  # use power-invariant alpha-beta transformations
  valpha = (va - 0.5*vb - 0.5*vc) * SQRT23 # TWOTHIRDS
  ialpha = (ia - 0.5*ib - 0.5*ic) * SQRT23 # TWOTHIRDS
  vbeta = (vb*SQRT3H - vc*SQRT3H) * SQRT23 # TWOTHIRDS
  ibeta = (ib*SQRT3H - ic*SQRT3H) * SQRT23 # TWOTHIRDS
  p_alphabeta = valpha*ialpha + vbeta*ibeta
  q_alphabeta = -valpha*ibeta + vbeta*ialpha

  # filter the P and Q signals
  p = signal.lfilter (b, a, p_alphabeta)
  q = signal.lfilter (b, a, q_alphabeta)

  ax[0].set_title ('Xfmr Voltages [pu]', fontsize=lsize+4)
  ax[0].plot (t, va/vbase, label='Va')
  ax[0].plot (t, vb/vbase, label='Vb')
  ax[0].plot (t, vc/vbase, label='Vc')

  ax[1].set_title ('Xfmr Currents [kA]', fontsize=lsize+4)
  ax[1].plot (t, 0.001*ia, label='Ia')
  ax[1].plot (t, 0.001*ib, label='Ib')
  ax[1].plot (t, 0.001*ic, label='Ic')

  ax[2].set_title ('Xfmr Powers [MVA]', fontsize=lsize+4)
  ax[2].plot (t, p/1.0e6, label='Active')
  ax[2].plot (t, q/1.0e6, label='Reactive')

  for i in range(3):
    ax[i].grid()
    ax[i].set_xlim (tticks[0], tticks[-1])
    ax[i].set_xticks (tticks)
    ax[i].set_xlabel ('Time [s]')
    ax[i].legend()

  if bPng:
    plt.savefig('XfmrSat.png')
  else:
    plt.show()
  plt.close()

def plot_channel (ax, t, y, label, bLabelX = False):
  ax.plot (t, y)
  ax.set_ylabel (label)
  ax.set_xlim (t[0], t[-1])
  if bLabelX:
    ax.set_xlabel ('t [s]')
  else:
    ax.set_xticklabels ([])

def plot_smibdll (atp_root, bPng):
  cfg = PLOT_CONFIGS[atp_root]

  LSIZE = 14
  TZOOM1 = 3.9
  TZOOM2 = 4.2

  plt.rc('font', family='serif')
  plt.rc('xtick', labelsize=LSIZE)
  plt.rc('ytick', labelsize=LSIZE)
  plt.rc('axes', labelsize=LSIZE)
  plt.rc('legend', fontsize=LSIZE)
  #pWidth = 6.0
  #pHeight = pWidth / 1.618
  df = pd.read_hdf(atp_root+'.hdf5')
  summarize_df (df, cfg['suptitle'])
  t = np.array(df.index)
  dt = t[1] - t[0]
  dlen = len(t)

  print (' {:d} time points from {:.7f} to {:.7f} at step={:.7f}'.format(dlen, t[0], t[-1], dt)) 

  # data of interest
  id1 = np.array (df['M:ID1'])
  iq1 = np.array (df['M:IQ1'])
  id2 = np.array (df['M:ID2'])
  iq2 = np.array (df['M:IQ2'])
  vd1 = np.array (df['M:VTD1'])
  vq1 = np.array (df['M:VTQ1'])
  vd2 = np.array (df['M:VTD2'])
  vq2 = np.array (df['M:VTQ2'])
  freq = np.array (df['M:FREQP']) / 60.0
  pout = np.array (df['M:POUT'])
  qout = np.array (df['M:QOUT'])
  ia = np.array (df['I:B1D:B1A'])
  ib = np.array (df['I:B1E:B1B'])
  ic = np.array (df['I:B1F:B1C'])
  va = np.array (df['T:B1A'])
  vb = np.array (df['T:B1B'])
  vc = np.array (df['T:B1C'])

  fig = plt.figure (figsize=(18,12), constrained_layout=True)
  fig.suptitle (cfg['suptitle'], fontsize=LSIZE + 4)
  subfigs = fig.subfigures (2, 2, wspace = 0.05, hspace = 0.05)

# indices = np.where(t>=3.9)
# i1 = indices[0][0]
# indices = np.where(t>4.5)
# i2 = indices[0][0]
# print ('Window', i1, i2, t[i1], t[i2])
# tplot = t[i1:i2]
  i1 = 0
  i2 = -1
  tplot = t[i1:i2]

  ax = subfigs[0,0].subplots(3, 1)
  plot_channel (ax[0], tplot, freq[i1:i2], 'Freq [Hz]')
  plot_channel (ax[1], tplot, pout[i1:i2], 'Pout [pu]')
  plot_channel (ax[2], tplot, qout[i1:i2], 'Qout [pu]', bLabelX = True)

  ax = subfigs[0,1].subplots(4,2)
  plot_channel (ax[0,0], tplot, vd1[i1:i2], 'Vd1 [pu]')
  plot_channel (ax[1,0], tplot, vq1[i1:i2], 'Vq1 [pu]')
  plot_channel (ax[2,0], tplot, id1[i1:i2], 'Id1 [pu]')
  plot_channel (ax[3,0], tplot, iq1[i1:i2], 'Iq1 [pu]', bLabelX = True)
  plot_channel (ax[0,1], tplot, vd2[i1:i2], 'Vd2 [pu]')
  plot_channel (ax[1,1], tplot, vq2[i1:i2], 'Vq2 [pu]')
  plot_channel (ax[2,1], tplot, id2[i1:i2], 'Id2 [pu]')
  plot_channel (ax[3,1], tplot, iq2[i1:i2], 'Iq2 [pu]', bLabelX = True)

  indices = np.where(t>=TZOOM1)
  i1 = indices[0][0]
  indices = np.where(t>TZOOM2)
  i2 = indices[0][0]
  print ('Window', i1, i2, t[i1], t[i2])
  tplot = t[i1:i2]

  ax = subfigs[1,0].subplots(1,1)
  ax.plot (tplot, va[i1:i2])
  ax.plot (tplot, vb[i1:i2])
  ax.plot (tplot, vc[i1:i2])
  ax.set_ylabel ('Vout [V]')
  ax.set_xlim (tplot[0], tplot[-1])
  ax.set_xlabel ('t [s]')

  ax = subfigs[1,1].subplots(1,1)
  ax.plot (tplot, ia[i1:i2])
  ax.plot (tplot, ib[i1:i2])
  ax.plot (tplot, ic[i1:i2])
  ax.set_ylabel ('Iout [A]')
  ax.set_xlim (tplot[0], tplot[-1])
  ax.set_xlabel ('t [s]')

# ax = subfigs[1,0].subplots(2,2)
# plot_channel (ax[0,0], tplot, id1[i1:i2], 'Id1 [pu]')
# plot_channel (ax[1,0], tplot, iq1[i1:i2], 'Iq1 [pu]', bLabelX = True)
# plot_channel (ax[0,1], tplot, id2[i1:i2], 'Id2 [pu]')
# plot_channel (ax[1,1], tplot, iq2[i1:i2], 'Iq2 [pu]', bLabelX = True)
#
# ax = subfigs[1,1].subplots(2,2)
# plot_channel (ax[0,0], tplot, vd1[i1:i2], 'Vtd1 [pu]')
# plot_channel (ax[1,0], tplot, vq1[i1:i2], 'Vtq1 [pu]', bLabelX = True)
# plot_channel (ax[0,1], tplot, vd2[i1:i2], 'Vtd2 [pu]')
# plot_channel (ax[1,1], tplot, vq2[i1:i2], 'Vtq2 [pu]', bLabelX = True)

  if bPng:
    plt.savefig('SMIBDLL.png')
  else:
    plt.show()
  plt.close()

def plot_case (atp_root, bPng):
  plt.rcParams['savefig.directory'] = os.getcwd()

  if atp_root == 'XfmrSat':
    plot_xfmr_sat (atp_root, bPng)
    return
  elif atp_root == 'SMIBDLL':
    plot_smibdll (atp_root, bPng)
    return

  cfg = PLOT_CONFIGS[atp_root]
  sm_start = cfg['sm_start']
  sm_end = cfg['sm_end']
  ibr_start = cfg['ibr_start']
  ibr_end = cfg['ibr_end']
  der_start = cfg['der_start']
  der_end = cfg['der_end']
  tticks = cfg['tticks']
  tmin = cfg['tmin']
  tmax = cfg['tmax']
  tpll = cfg['tpll']

  df = pd.read_hdf(atp_root+'.hdf5')
  df_table (df, sm_start, sm_end, ibr_start, ibr_end, der_start, der_end)

  fig, ax = plt.subplots (2, cfg['ncols'], sharex = 'col', figsize=(21,9), constrained_layout=True)
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

  if der_end is not None:
    ax[0,4].set_title ('DER Voltage [kV]')
    for i in range(der_start, der_end):
      key = 'T:DR{:03d}V'.format(i+1)
      if key in df:
        ax[0,4].plot (t, df[key] / 1000.0)

    ax[1,4].set_title ('DER Current [kA]')
    for i in range(der_start, der_end):
      key = 'T:DR{:03d}I'.format(i+1)
      if key in df:
        ax[1,4].plot (t, df[key] / 1000.0)

  for i in range(2):
    for j in range(cfg['ncols']):
      ax[i,j].grid()
      ax[i,j].set_xlim (tticks[0], tticks[-1])
      ax[i,j].set_xticks (tticks)

  if bPng:
    plt.savefig(atp_root+'.png')
  else:
    plt.show()
  plt.close()

def run_atp_case (atp_root):
  if atp_root == 'SMIBDLL':
    cmdline = 'c:\\atp\\atpmingw\\mytpbig ' + atp_root + '.atp >nul'
  else:
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
    plot_case (atp_root, bPng=False)
    print ('plot', idx)
  elif opt == 'png':
    plot_case (atp_root, bPng=True)
    print ('png', idx)
  else:
    print ('Unrecognized option:', opt)

