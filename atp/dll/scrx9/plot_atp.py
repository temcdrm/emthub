import sys
import matplotlib.pyplot as plt
import numpy as np
import h5py
import os
import json

LSIZE = 10

def plot_channel (ax, t, y, label, bLabelX = False):
  ax.plot (t, y)
  ax.set_ylabel (label)
  ax.set_xlim (t[0], t[-1])
  ax.grid()
  if bLabelX:
    ax.set_xlabel ('t [s]')
  else:
    ax.set_xticklabels ([])

if __name__ == '__main__':
  plt.rcParams['savefig.directory'] = os.getcwd()
  plt.rc('font', family='serif')
  plt.rc('xtick', labelsize=LSIZE)
  plt.rc('ytick', labelsize=LSIZE)
  plt.rc('axes', labelsize=LSIZE)
  plt.rc('legend', fontsize=LSIZE)
  #pWidth = 6.0
  #pHeight = pWidth / 1.618
  f = h5py.File('scrx9.hdf5', 'r')
  grp = f['base_case']
  dlen = grp['t'].len()
  t = np.zeros(dlen)
  y = np.zeros(dlen)
  grp['t'].read_direct (t)
  dt = t[1] - t[0]

  print (' {:d} time points from {:.7f} to {:.7f} at step={:.7f}'.format(dlen, t[0], t[-1], dt)) 
  print ('Column                         Min           Max')
  for key in grp:
    grp[key].read_direct (y)
    print ('{:20s} {:13.5f} {:13.5f}'.format (key, y.min(), y.max()))

  grp['M:EFD'].read_direct(y)
  # fig = plt.figure (figsize=(6.5,2.5), constrained_layout=True)
  fig, ax = plt.subplots (1, 1, sharex = 'col', figsize=(6.5,2.5), constrained_layout=True)
  plot_channel (ax, t, y, 'Efd [pu]', True)
  plt.show()
  plt.close()

  grp['T:VTPU'].read_direct(y)
  fig, ax = plt.subplots (1, 1, sharex = 'col', figsize=(6.5,2.5), constrained_layout=True)
  plot_channel (ax, t, y, 'Vt [pu]', True)
  plt.show()
  plt.close()

