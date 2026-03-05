import sys
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

LSIZE = 14
TZOOM1 = 3.9
TZOOM2 = 4.2

def summarize_df (df, label):
  print ('Column                         Min           Max {:s}'.format (label))
  for lbl, data in df.items():
    print ('{:20s} {:13.5f} {:13.5f}'.format (lbl, data.min(), data.max()))

def plot_channel (ax, t, y, label, bLabelX = False):
  ax.plot (t, y)
  ax.set_ylabel (label)
  ax.set_xlim (t[0], t[-1])
  if bLabelX:
    ax.set_xlabel ('t [s]')
  else:
    ax.set_xticklabels ([])

def plot_page (df, title, savename=None):
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
  fig.suptitle (title, fontsize=LSIZE + 4)
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

  if savename is not None:
    plt.savefig(savename)
    plt.show()
  else:
    plt.show()
  plt.close()

if __name__ == '__main__':
  plt.rcParams['savefig.directory'] = os.getcwd()
  plt.rc('font', family='serif')
  plt.rc('xtick', labelsize=LSIZE)
  plt.rc('ytick', labelsize=LSIZE)
  plt.rc('axes', labelsize=LSIZE)
  plt.rc('legend', fontsize=LSIZE)
  #pWidth = 6.0
  #pHeight = pWidth / 1.618
  df = pd.read_hdf('smib.hdf5')
  summarize_df (df, 'SMIB DLL Test Case')
  plot_page (df, 'SMIB DLL Test Case', savename='smib.png')

