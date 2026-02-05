# Copyright (C) 2025-2026 Meltran, Inc
 
import sys
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import sys

plt.rcParams['savefig.directory'] = os.getcwd()

tticks = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0]

def summarize_df (df, label):
  print ('\nSummary of ', label)
  print ('Column                         Min           Max')
  for lbl, data in df.items():
    print ('{:20s} {:13.5f} {:13.5f}'.format (lbl, data.min(), data.max()))

if __name__ == '__main__':
  root = 'WECC240'
  swing_bus = 'B120'
  swing_bus = 'B31'
  if len(sys.argv) > 1:
    root = sys.argv[1]
  df1 = pd.read_hdf('{:}.hdf5'.format(root))
  summarize_df (df1, root)

  fig, ax = plt.subplots (1, 3, sharex = 'col', figsize=(10,4), constrained_layout=True)
  fig.suptitle (' {:s} Swing Bus {:s}'.format(root, swing_bus))
  t = np.array(df1.index)
  tmin = tticks[0]
  tmax = tticks[-1]
  amin = np.where(t==tmin)
  amax = np.where(t==tmax)
  imin = int(amin[0][0])
  imax = int(amax[0][0])
  print ('Plotting from', tmin, imin, t[imin], 'to', tmax, imax, t[imax])

  tplot = np.array(t[imin:imax])
  va = 1.0e-3 * np.array(df1['V:SBUSA'])[imin:imax]
  vb = 1.0e-3 * np.array(df1['V:SBUSB'])[imin:imax]
  vc = 1.0e-3 * np.array(df1['V:SBUSC'])[imin:imax]
  ia = 1.0e-3 * np.array(df1['I:SBUSA:{:s}A'.format(swing_bus)])[imin:imax]
  ib = 1.0e-3 * np.array(df1['I:SBUSB:{:s}B'.format(swing_bus)])[imin:imax]
  ic = 1.0e-3 * np.array(df1['I:SBUSC:{:s}C'.format(swing_bus)])[imin:imax]
  p = va*ia + vb*ib +vc*ic

  ax[0].set_title ('Voltages [kV]')
  for v in [va, vb, vc]:
    ax[0].plot (tplot, v)

  ax[1].set_title ('Currents [kA]')
  for i in [ia, ib, ic]:
    ax[1].plot (tplot, i)

  ax[2].set_title ('Power [MW]')
  ax[2].plot (tplot, p)

  for i in range(3):
    ax[i].grid()
    ax[i].set_xlim (tticks[0], tticks[-1])
    ax[i].set_xticks (tticks)
#    ax[i].legend()

  plt.show()
  plt.close()

