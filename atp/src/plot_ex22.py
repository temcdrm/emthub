# Copyright (C) 2025-2026 Meltran, Inc

import sys
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

plt.rcParams['savefig.directory'] = os.getcwd()

def summarize_df (df, label):
  print ('Column                         Min           Max {:s}'.format (label))
  for lbl, data in df.items():
    print ('{:20s} {:13.5f} {:13.5f}'.format (lbl, data.min(), data.max()))

if __name__ == '__main__':
  dfm = pd.read_hdf('Exa_22a_Models.hdf5')
#  summarize_df (dfm, 'Example 22a MODELS')
  dft = pd.read_hdf('Exa_22a_Tacs.hdf5')
#  summarize_df (dft, 'Example 22a TACS')
  dfc = pd.read_hdf('Exa_22a_CIM.hdf5')
  summarize_df (dfc, 'Example 22a CIM')

  fig, ax = plt.subplots (2, 3, sharex = 'col', figsize=(18,9), constrained_layout=True)
  fig.suptitle ('Example 22a Test')
  t = dfm.index
  tmin = t[0]
  tmax = t[-1]

  ax[0,0].set_title ('Vrms [pu]')
  ax[0,0].plot (dfm.index, dfm['M:UG']/22.55, color='red', label='MODELS')
  ax[0,0].plot (dft.index, dft['T:VRMSPU'], color='blue', label='TACS')
  ax[0,0].plot (dfc.index, dfc['T:VRMSPU'], color='green', label='CIM')

  ax[0,1].set_title ('Pgen [pu]')
  ax[0,1].plot (dfm.index, dfm['M:PG']/500.0e6, color='red', label='MODELS')
  ax[0,1].plot (dft.index, dft['T:PGENPU'], color='blue', label='TACS')

  ax[0,2].set_title ('Freq [pu]')
  ax[0,2].plot (dfm.index, dfm['M:RPMG']/3600.0, color='red', label='MODELS')
  ax[0,2].plot (dft.index, dft['T:WGPU'], color='blue', label='TACS')
  ax[0,2].plot (dfc.index, dfc['T:WGPU'], color='green', label='CIM')

  ax[1,0].set_title ('LP Torque [pu]')
  ax[1,0].plot (dfm.index, dfm['M:TORQC'], color='red', label='MODELS')
  ax[1,0].plot (dft.index, dft['T:TORQC'], color='blue', label='TACS')
  ax[1,0].plot (dfc.index, dfc['T:TORQC'], color='green', label='CIM')

  ax[1,1].set_title ('HP Torque [pu]')
  ax[1,1].plot (dfm.index, dfm['M:TORQD'], color='red', label='MODELS')
  ax[1,1].plot (dft.index, dft['T:TORQD'], color='blue', label='TACS')
  ax[1,1].plot (dfc.index, dfc['T:TORQD'], color='green', label='CIM')

  ax[1,2].set_title ('Efd [pu]')
  ax[1,2].plot (dfm.index, dfm['M:EFD'], color='red', label='MODELS')
  ax[1,2].plot (dft.index, dft['T:EFD'], color='blue', label='TACS')
  ax[1,2].plot (dfc.index, dfc['T:EFD'], color='green', label='CIM')

# ax[2,0].set_title ('DPWG [pu]')
# ax[2,0].plot (dfm.index, dfm['M:DPWG'], color='red', label='MODELS')
# ax[2,0].plot (dft.index, dft['T:DPWG'], color='blue', label='TACS')
#
# ax[2,1].set_title ('DPPG [pu]')
# ax[2,1].plot (dfm.index, dfm['M:DPPG'], color='red', label='MODELS')
# ax[2,1].plot (dft.index, dft['T:DPPG'], color='blue', label='TACS')
#
# ax[2,2].set_title ('DPGN [pu]')
# ax[2,2].plot (dfm.index, dfm['M:DPGN'], color='red', label='MODELS')
# ax[2,2].plot (dft.index, -dft['T:PGENPU']+1.0, color='blue', label='TACS')

  for i in range(2):
    for j in range(3):
      ax[i,j].legend()
      ax[i,j].grid()
      ax[i,j].set_xlim (tmin, tmax)

# plt.savefig('ex22a.png')
  plt.show()
  plt.close()

