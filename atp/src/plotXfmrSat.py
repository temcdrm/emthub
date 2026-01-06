# Copyright (C) 2025-2026 Meltran, Inc

import sys
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import math
from scipy import signal

plt.rcParams['savefig.directory'] = os.getcwd()
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

def summarize_df (df, label):
  print ('Column                         Min           Max {:s}'.format (label))
  for lbl, data in df.items():
    print ('{:20s} {:13.5f} {:13.5f}'.format (lbl, data.min(), data.max()))

if __name__ == '__main__':
  df = pd.read_hdf('XfmrSat.hdf5')
  summarize_df (df, 'Transformer Saturation Case')

  fig, ax = plt.subplots (1, 3, sharex = 'col', figsize=(21,9), constrained_layout=True)
  # fig.suptitle ('Transformer Saturation Case', fontsize=lsize+4)
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

  plt.savefig('XfmrSat.png')
  plt.show()
  plt.close()

