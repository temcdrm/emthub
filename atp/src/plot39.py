import sys
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

plt.rcParams['savefig.directory'] = os.getcwd()

tmin = 40.0
tmax = 50.0
#tmin = 0.0
#tmax = 10.0
#tticks = [40.0, 42.0, 44.0, 46.0, 48.0, 50.0]
#tticks = [20.0, 22.0, 24.0, 26.0, 28.0, 30.0]
tticks = [0.0, 2.0, 4.0, 6.0, 8.0, 10.0]

def summarize_df (df, label):
  print ('Column                         Min           Max {:s}'.format (label))
  for lbl, data in df.items():
    print ('{:20s} {:13.5f} {:13.5f}'.format (lbl, data.min(), data.max()))

if __name__ == '__main__':
  sm_start = 2
  sm_end = 10
  ibr_start = 1
  ibr_end = 2

  df = pd.read_hdf('IEEE39.hdf5')
# summarize_df (df, 'IEEE 118-bus Case')
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

  fig, ax = plt.subplots (2, 4, sharex = 'col', figsize=(21,9), constrained_layout=True)
  fig.suptitle ('IEEE 39-bus Case')
  t = np.array(df.index)
  amin = np.where(t==tmin)
  amax = np.where(t==tmax)
  imin = int(amin[0][0])
  imax = int(amax[0][0])
  print ('Plotting from', tmin, imin, t[imin], 'to', tmax, imax, t[imax])
  tplot = t[imin:imax] - tmin

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
      ax[1,2].plot (tplot, np.array(df[key])[imin:imax] / 376.9911)

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

  plt.savefig('IEEE39.png')
  plt.show()
  plt.close()

