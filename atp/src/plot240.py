# Copyright (C) 2025-2026 Meltran, Inc

import sys
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import math

NMACH = 105
NDER = 2
NIBR = 35
OMEGA = 2.0 * 60.0 * math.pi

plt.rcParams['savefig.directory'] = os.getcwd()

def summarize_df (df, label):
  print ('Column                         Min           Max {:s}'.format (label))
  for lbl, data in df.iteritems():
    print ('{:20s} {:13.5f} {:13.5f}'.format (lbl, data.min(), data.max()))

if __name__ == '__main__':
  df = pd.read_hdf('WECC240.hdf5')
#  summarize_df (df, 'WECC 240-bus Case')
  print ('Column                 Min           Max')
  key = 'I:FAULTC:'
  data = df[key]
  print ('{:12s} {:13.5f} {:13.5f}'.format (key, data.min(), data.max()))
  print ('Machine           FREQ Min           Max       VPU Min           Max     PMECH Min           Max       EFD Min           Max')
  for i in range(NMACH):
    mach = 'SM{:03d}'.format(i+1)
    line = '{:12s}'.format(mach)
    for sig in ['W', 'V', 'P', 'F']:
      key = 'T:{:s}{:s}'.format (mach, sig)
      if key in df:
        data = df[key]
        line += ' {:13.5f} {:13.5f}'.format (data.min(), data.max())
    print (line)

  print ('DER               FREQ Min           Max      VRMS Min           Max      IRMS Min           Max')
  for i in range(NDER):
    der = 'DR{:03d}'.format(i+1)
    line = '{:12s}'.format(der)
    for sig in ['W', 'V', 'I']:
      key = 'T:{:s}{:s}'.format (der, sig)
      if key in df:
        data = df[key]
        line += ' {:13.5f} {:13.5f}'.format (data.min(), data.max())
    print (line)

  print ('IBR               FREQ Min           Max       P   Min           Max     Q     Min           Max                            ')
  for i in range(NIBR):
    ibr = 'IBR{:02d}'.format(i+1)
    line = '{:12s}'.format(ibr)
    for sig in ['F', 'P', 'Q']:
      key = 'T:{:s}{:s}'.format (ibr, sig)
      if key in df:
        data = df[key]
        line += ' {:13.5f} {:13.5f}'.format (data.min(), data.max())
    print (line)

  fig, ax = plt.subplots (2, 5, sharex = 'col', figsize=(21,9), constrained_layout=True)
  fig.suptitle ('WECC 240-bus Case')
  t = df.index
  tmin = t[0]
  tmax = t[-1]

  ax[0,0].set_title ('Machine Frequency [pu]')
  for i in range(NMACH):
    key = 'T:SM{:03d}W'.format(i+1)
    if key in df:
      ax[0,0].plot (t, df[key])

  ax[0,1].set_title ('Machine Voltage [pu]')
  for i in range(NMACH):
    key = 'T:SM{:03d}V'.format(i+1)
    if key in df:
      ax[0,1].plot (t, df[key])

  ax[0,2].set_title ('Fault Current [kA]')
  key = 'I:FAULTC:'
  ax[0,2].plot (t, df[key], label=key)
  ax[0,2].legend()

  ax[0,3].set_title ('IBR P [pu]')
  for i in range(NIBR):
    key = 'T:IBR{:02d}P'.format(i+1)
    if key in df:
      ax[0,3].plot (t, df[key], label=key)

  ax[1,0].set_title ('Machine Pmech [pu]')
  for i in range(NMACH):
    key = 'T:SM{:03d}P'.format(i+1)
    if key in df:
      ax[1,0].plot (t, df[key])

  ax[1,1].set_title ('Machine Efd [pu]')
  for i in range(NMACH):
    key = 'T:SM{:03d}F'.format(i+1)
    if key in df:
      ax[1,1].plot (t, df[key])

  ax[1,2].set_title ('IBR Frequency [pu]')
  for i in range(NIBR):
    key = 'T:IBR{:02d}F'.format(i+1)
    if key in df:
      ax[1,2].plot (t, df[key] / 376.9911)

  ax[1,3].set_title ('IBR Q [pu]')
  for i in range(NIBR):
    key = 'T:IBR{:02d}Q'.format(i+1)
    if key in df:
      ax[1,3].plot (t, df[key])

  ax[0,4].set_title ('DER Voltage [kV]')
  for i in range(NDER):
    key = 'T:DR{:03d}V'.format(i+1)
    if key in df:
      ax[0,4].plot (t, df[key] / 1000.0)
 
  ax[1,4].set_title ('DER Current [kA]')
  for i in range(NDER):
    key = 'T:DR{:03d}I'.format(i+1)
    if key in df:
      ax[1,4].plot (t, df[key] / 1000.0)

# ax[0,2].set_title ('DER Frequency [pu]')
# for i in range(NMACH):
#   key = 'T:DR{:03d}W'.format(i+1)
#   if key in df:
#     ax[0,2].plot (t, df[key] / OMEGA)

  for i in range(2):
    for j in range(5):
#      ax[i,j].legend()
      ax[i,j].grid()
      ax[i,j].set_xlim (tmin, tmax)

  plt.savefig('WECC240.png')
  plt.show()
  plt.close()

