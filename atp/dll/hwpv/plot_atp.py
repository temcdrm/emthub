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
  f = h5py.File('hwpv.hdf5', 'r')
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

  grp['T:VD'].read_direct(y)
  grp['T:VQ'].read_direct(y2)
  grp['T:VRMS'].read_direct(y3)
  grp['V:G'].read_direct(y4)
  fig, ax = plt.subplots (1, 1, sharex = 'col', figsize=(FIGWIDTH,FIGHEIGHT), constrained_layout=True)
  ax.plot (t, y, label='Vd [V]')
  ax.plot (t, y2, label='Vq [V]')
  ax.plot (t, y3, label='Vrms [V]')
  ax.plot (t, y4, label='G [W/m2]')
  finish_plot (ax, t, bLegend=True, legend_loc='upper center')
  plt.show()
  plt.close()

  grp['V:TEMP'].read_direct(y)
  fig, ax = plt.subplots (1, 1, sharex = 'col', figsize=(FIGWIDTH,FIGHEIGHT), constrained_layout=True)
  ax.plot (t, y)
  finish_plot (ax, t, ylabel='Temp [deg C]')
  plt.show()
  plt.close()

  grp['T:PDQ0'].read_direct(y)
  grp['T:QDQ0'].read_direct(y2)
  fig, ax = plt.subplots (1, 1, sharex = 'col', figsize=(FIGWIDTH,FIGHEIGHT), constrained_layout=True)
  ax.plot (t, 0.001*y, label='P')
  ax.plot (t, 0.001*y2, label='Q')
  finish_plot (ax, t, ylabel='[kW, kVAR]', bLegend=True)
  plt.show()
  plt.close()

  grp['T:ID'].read_direct(y)
  grp['T:IQ'].read_direct(y2)
  fig, ax = plt.subplots (1, 1, sharex = 'col', figsize=(FIGWIDTH,FIGHEIGHT), constrained_layout=True)
  ax.plot (t, y, label='Id')
  ax.plot (t, y2, label='Iq')
  finish_plot (ax, t, ylabel='[A]', bLegend=True)
  plt.show()
  plt.close()

  grp['V:FCTRL'].read_direct(y)
  fig, ax = plt.subplots (1, 1, sharex = 'col', figsize=(FIGWIDTH,FIGHEIGHT), constrained_layout=True)
  ax.plot (t, y)
  ax.set_ylim (50.0, 70.0)
  finish_plot (ax, t, ylabel='Fctrl [Hz]')
  plt.show()
  plt.close()

  grp['V:MD'].read_direct(y)
  grp['V:MQ'].read_direct(y2)
  grp['V:CTRL'].read_direct(y3)
  fig, ax = plt.subplots (1, 1, sharex = 'col', figsize=(FIGWIDTH,FIGHEIGHT), constrained_layout=True)
  ax.plot (t, y, label='Md')
  ax.plot (t, y2, label='Mq')
  ax.plot (t, y3, label='Ctrl')
  finish_plot (ax, t, ylabel='[pu]', bLegend=True)
  plt.show()
  plt.close()


