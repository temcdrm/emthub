# Copyright (C) 2024-26 Meltran, Inc

import os
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plots = {
  "PPC_voltage_step.csv": {"tmin": 0.0, "tmax": 5.0, "ttick": 1.0, "title": "PPC Voltage Step Test",
                        "ytitles": ["Inputs [pu]", "Outputs [pu]"],
                        "signals": [{"name": "Vmeas", "base": 1.0, "axis": 0},
                                    {"name": "Plant_pref", "base": 1.0, "axis": 0},
                                    {"name": "Qext", "base": 1.0, "axis": 0},
                                    {"name": "Pref", "base": 1.0, "axis": 1}]},
  "PPC_qmeas_step.csv": {"tmin": 0.0, "tmax": 5.0, "ttick": 1.0, "title": "PPC Reactive Power Step Test",
                        "ytitles": ["Inputs [pu]", "Outputs [pu]"],
                        "signals": [{"name": "Qmeas", "base": 1.0, "axis": 0},
                                    {"name": "Plant_pref", "base": 1.0, "axis": 0},
                                    {"name": "Qext", "base": 1.0, "axis": 0},
                                    {"name": "Pref", "base": 1.0, "axis": 1}]},
  "PPC_freq_step.csv": {"tmin": 0.0, "tmax": 10.0, "ttick": 1.0, "title": "PPC Frequency Step Test",
                        "ytitles": ["Inputs [pu]", "Outputs [pu]"],
                        "signals": [{"name": "Freq", "base": 1.0, "axis": 0},
                                    {"name": "Plant_pref", "base": 1.0, "axis": 0},
                                    {"name": "Qext", "base": 1.0, "axis": 0},
                                    {"name": "Pref", "base": 1.0, "axis": 1}]}
    }

plt.rcParams['savefig.directory'] = os.getcwd()
lsize = 18

def plot_page (df, cfg):
  plt.rc('font', family='serif')
  plt.rc('xtick', labelsize=lsize)
  plt.rc('ytick', labelsize=lsize)
  plt.rc('axes', labelsize=lsize)
  plt.rc('legend', fontsize=lsize)

  t = np.array(df.index)
  tmin = cfg['tmin']
  tmax = cfg['tmax']
  amin = np.where(t==tmin)
  amax = np.where(t==tmax)
  imin = int(amin[0][0])
  imax = int(amax[0][0])
  nticks = int((tmax-tmin)/cfg['ttick']) + 1
  tticks = np.linspace (tmin, tmax, num=nticks, endpoint=True)
  nrows = len(cfg['ytitles'])
  ncols = 1
  fig, ax = plt.subplots (nrows, ncols, sharex = 'col', figsize=(18,12), constrained_layout=True)
  fig.suptitle (cfg['title'], fontsize=lsize+4)
  for sig in cfg['signals']:
    key = sig['name']
    base = sig['base']
    axis = sig['axis']
    if base != 1.0:
      lbl = '{:s} / {:s}'.format (key, str(base))
    else:
      lbl = key
    ax[axis].plot (t[imin:imax], np.array(df[key])[imin:imax]/base, label=lbl)
  for axis in range(nrows):
    ax[axis].grid()
    ax[axis].set_xlim (tticks[0], tticks[-1])
    ax[axis].set_xticks (tticks)
    ax[axis].set_ylabel (cfg['ytitles'][axis])
    ax[axis].legend()
  ax[nrows-1].set_xlabel ('Time [s]')

  plt.show()
  plt.close()

data_path = 'scrx9.csv'
all_channels = False

if __name__ == '__main__':
  if len(sys.argv) > 1:
    data_path = sys.argv[1]
  if len(sys.argv) > 2 and int(sys.argv[2]) > 0:
    all_channels = True
  df = pd.read_csv (data_path, index_col='t')
  df.info()
  if data_path in plots and all_channels == False:
    plot_page (df, plots[data_path])
  else:
    df.plot(subplots=True, title=data_path)
    plt.show()
    plt.close()



