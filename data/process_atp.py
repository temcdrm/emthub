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
  if bLabelX:
    ax.set_xlabel ('t [s]')
  else:
    ax.set_xticklabels ([])

def plot_page (grp, title, savename=None, start_time = 3.5, end_time = 5.0):
  dlen = grp['t'].len()
  t = np.zeros(dlen)
  y = np.zeros(dlen)
  grp['t'].read_direct (t)
  dt = t[1] - t[0]
  
  istart = np.where(t>=start_time)[0][0]
  iend = np.where(t>=end_time)[0][0]
  print (' {:d} time points from {:.7f} to {:.7f} at step={:.7f}'.format(dlen, t[0], t[-1], dt)) 
  print ('Analysis window from {:.5f} to {:.5f} s'.format (start_time, end_time))
  print ('Column         Min           Max         Start         Final')
  for key in grp:
    if key != 't':
      grp[key].read_direct (y)
      print ('{:4s} {:13.5f} {:13.5f} {:13.5f} {:13.5f}'.format (key, y.min(), y.max(), y[istart], y[iend]))

  # data of interest
  v1 = np.zeros(dlen)
  grp['V1'].read_direct(v1)
  v2 = np.zeros(dlen)
  grp['V2'].read_direct(v2)
  f = np.zeros(dlen)
  grp['F'].read_direct(f)
  p = np.zeros(dlen)
  grp['P'].read_direct(p)
  q = np.zeros(dlen)
  grp['Q'].read_direct(q)

  fig, ax = plt.subplots (5, 1, figsize=(18,12), constrained_layout=True)
  fig.suptitle (title, fontsize=LSIZE + 4)

# indices = np.where(t>=3.9)
# i1 = indices[0][0]
# indices = np.where(t>4.5)
# i2 = indices[0][0]
# print ('Window', i1, i2, t[i1], t[i2])
# tplot = t[i1:i2]

  plot_channel (ax[0], t[istart:iend], v1[istart:iend], 'V1 [pu]')
  plot_channel (ax[1], t[istart:iend], v2[istart:iend], 'V2 [pu]')
  plot_channel (ax[2], t[istart:iend], f[istart:iend], 'Freq [Hz]')
  plot_channel (ax[3], t[istart:iend], p[istart:iend], 'Pout [pu]')
  plot_channel (ax[4], t[istart:iend], q[istart:iend], 'Qout [pu]', bLabelX = True)

# ax = subfigs[0,1].subplots(4,2)
# plot_channel (ax[0,0], tplot, vd1[i1:i2], 'Vd1 [pu]')

# indices = np.where(t>=3.98)
# i1 = indices[0][0]
# indices = np.where(t>4.03)
# i2 = indices[0][0]
# print ('Window', i1, i2, t[i1], t[i2])
# tplot = t[i1:i2]

  if savename is not None:
    plt.savefig(savename)
#    plt.show()
  else:
    plt.show()
  plt.close()

if __name__ == '__main__':
  fignum = 1
  if len(sys.argv) > 1:
    fignum = int(sys.argv[1])
  idx = fignum - 1
  plt.rcParams['savefig.directory'] = os.getcwd()
  plt.rc('font', family='serif')
  plt.rc('xtick', labelsize=LSIZE)
  plt.rc('ytick', labelsize=LSIZE)
  plt.rc('axes', labelsize=LSIZE)
  plt.rc('legend', fontsize=LSIZE)
  #pWidth = 6.0
  #pHeight = pWidth / 1.618
  with open('cases.json', 'r') as f:
    cases = json.load(f)
  f = h5py.File('prepped.hdf5', 'r')
  grp = f['fig{:d}'.format(fignum)]
  title = 'Figure A-{:d}: {:s}'.format (fignum, cases[idx]['Title'])
  savename = 'fig{:d}.png'.format(fignum)

  plot_page (grp, title, savename=None)

