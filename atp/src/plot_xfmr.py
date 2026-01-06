# Copyright (C) 2025-2026 Meltran, Inc
 
import sys
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

plt.rcParams['savefig.directory'] = os.getcwd()

tticks = [0.0, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30]

def summarize_df (df, label):
  print ('\nSummary of ', label)
  print ('Column                         Min           Max')
  for lbl, data in df.items():
    print ('{:20s} {:13.5f} {:13.5f}'.format (lbl, data.min(), data.max()))

if __name__ == '__main__':
  df1 = pd.read_hdf('Saturated.hdf5')
#  summarize_df (df1, 'Saturated')
  df2 = pd.read_hdf('Linear.hdf5')
#  summarize_df (df2, 'Linear')

  fig, ax = plt.subplots (1, 2, sharex = 'col', figsize=(10,4), constrained_layout=True)
  fig.suptitle ('Transformer Load Rejection')
  t = np.array(df1.index)
  tmin = tticks[0]
  tmax = tticks[-1]
  amin = np.where(t==tmin)
  amax = np.where(t==tmax)
  imin = int(amin[0][0])
  imax = int(amax[0][0])
  print ('Plotting from', tmin, imin, t[imin], 'to', tmax, imax, t[imax])

  ax[0].set_title ('Reactive Power [Mvar]')
  key = 'M:Q'
  ax[0].plot (t[imin:imax], 1.0e-6 * np.array(df1[key])[imin:imax], label='Saturated')
  ax[0].plot (t[imin:imax], 1.0e-6 * np.array(df2[key])[imin:imax], label='Linear')

  ax[1].set_title ('Transformer Current [kA]')
  key = 'I:X0002A:HIGHA'
  ax[1].plot (t[imin:imax], 1.0e-3 * np.array(df1[key])[imin:imax], label='Saturated')
  ax[1].plot (t[imin:imax], 1.0e-3 * np.array(df2[key])[imin:imax], label='Linear')

  for i in range(2):
    ax[i].grid()
    ax[i].set_xlim (tticks[0], tticks[-1])
    ax[i].set_xticks (tticks)
    ax[i].legend()

  plt.show()
  plt.close()

