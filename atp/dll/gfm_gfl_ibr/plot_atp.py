import sys
import matplotlib.pyplot as plt
import numpy as np
import h5py
import os
import json

LSIZE = 10
FIGWIDTH = 6.5
FIGHEIGHT = 2.5

def finish_plot (ax, t, ylabel=None, bLegend=False, legend_loc='best'):
  ax.set_xlim (t[0], t[-1])
  ax.grid()
  if bLegend:
    ax.legend(loc=legend_loc)
  ax.set_xlabel ('t [s]')
  if ylabel is not None:
    ax.set_ylabel (ylabel)

if __name__ == '__main__':
  plt.rcParams['savefig.directory'] = os.getcwd()
  plt.rc('font', family='serif')
  plt.rc('xtick', labelsize=LSIZE)
  plt.rc('ytick', labelsize=LSIZE)
  plt.rc('axes', labelsize=LSIZE)
  plt.rc('legend', fontsize=LSIZE)
  #pWidth = 6.0
  #pHeight = pWidth / 1.618
  f = h5py.File('ibr.hdf5', 'r')
  grp = f['base_case']
  dlen = grp['t'].len()
  t = np.zeros(dlen)
  y = np.zeros(dlen)
  y2 = np.zeros(dlen)
  y3 = np.zeros(dlen)
  y4 = np.zeros(dlen)
  grp['t'].read_direct (t)
  dt = t[1] - t[0]

  print (' {:d} time points from {:.7f} to {:.7f} at step={:.7f}'.format(dlen, t[0], t[-1], dt)) 
  print ('Column                         Min           Max')
  for key in grp:
    grp[key].read_direct (y)
    print ('{:20s} {:13.5f} {:13.5f}'.format (key, y.min(), y.max()))

  indices = np.where(t>=1.95)
  i1 = indices[0][0]
  indices = np.where(t>2.05)
  i2 = indices[0][0]
  print ('Zoom Window', i1, i2, t[i1], t[i2])
  tplot = t[i1:i2]

# grp['M:POUT'].read_direct(y)
# grp['M:QOUT'].read_direct(y2)
# fig, ax = plt.subplots (1, 1, sharex = 'col', figsize=(FIGWIDTH,FIGHEIGHT), constrained_layout=True)
# ax.plot (t, y, label='P')
# ax.plot (t, y2, label='Q')
# finish_plot (ax, t, bLegend=True, legend_loc='lower right', ylabel='[MW, Mvar]')
# plt.show()
# plt.close()
#
# grp['M:FPLL'].read_direct(y)
# fig, ax = plt.subplots (1, 1, sharex = 'col', figsize=(FIGWIDTH,FIGHEIGHT), constrained_layout=True)
# ax.plot (t, y)
# finish_plot (ax, t, ylabel='PLL Freq [Hz]')
# plt.show()
# plt.close()
#
# grp['M:VD'].read_direct(y)
# grp['M:VQ'].read_direct(y2)
# fig, ax = plt.subplots (1, 1, sharex = 'col', figsize=(FIGWIDTH,FIGHEIGHT), constrained_layout=True)
# ax.plot (t, y, label='Vd')
# ax.plot (t, y2, label='Vq')
# finish_plot (ax, t, ylabel='[pu]', bLegend=True)
# plt.show()
# plt.close()
#
# grp['M:ID'].read_direct(y)
# grp['M:IQ'].read_direct(y2)
# grp['M:IDREF'].read_direct(y3)
# grp['M:IQREF'].read_direct(y4)
# fig, ax = plt.subplots (1, 1, sharex = 'col', figsize=(FIGWIDTH,FIGHEIGHT), constrained_layout=True)
# ax.plot (t, y, label='Id')
# ax.plot (t, y2, label='Iq')
# ax.plot (t, y3, label='Idref')
# ax.plot (t, y4, label='Iqref')
# finish_plot (ax, t, ylabel='[pu]', bLegend=True, legend_loc='upper right')
# plt.show()
# plt.close()

  grp['V:VSCA'].read_direct(y)
  grp['V:INFA'].read_direct(y2)
  fig, ax = plt.subplots (1, 1, sharex = 'col', figsize=(FIGWIDTH,FIGHEIGHT), constrained_layout=True)
  ax.plot (tplot, y[i1:i2], label='Vvsc A')
  ax.plot (tplot, y2[i1:i2], label='Vinf A')
  ax.set_xlim (1.95, 2.05)
  ax.set_xticks ([1.95, 1.97, 1.99, 2.01, 2.03, 2.05])
  ax.grid()
  ax.legend()
  ax.set_xlabel ('t [s]')
  ax.set_ylabel ('[V]')
  plt.show()
  plt.close()

  grp['I:VSCA:CHOKEA'].read_direct(y)
  grp['I:FILTA:POCA'].read_direct(y2)
  fig, ax = plt.subplots (1, 1, sharex = 'col', figsize=(FIGWIDTH,FIGHEIGHT), constrained_layout=True)
  ax.plot (tplot, y[i1:i2], label='Ivsc A')
  ax.plot (tplot, y2[i1:i2], label='Iout A')
  ax.set_xlim (1.95, 2.05)
  ax.set_xticks ([1.95, 1.97, 1.99, 2.01, 2.03, 2.05])
  ax.grid()
  ax.legend()
  ax.set_xlabel ('t [s]')
  ax.set_ylabel ('[A]')
  plt.show()
  plt.close()

