# Copyright (C) 2024-26 Meltran, Inc

import os
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

# CERTS inverter is 100 kW, 480 V
hwpv_vbase = 480.0 * math.sqrt(2.0) / math.sqrt(3.0)
hwpv_ibase = math.sqrt(2.0) * 100.0e3 / 480.0 / math.sqrt(3.0)
hwpv_vdcbase = 1.0 / 0.00260668
hwpv_idcbase = 100.0e3 / hwpv_vdcbase

plots = {
  "ibr.csv": {"tmin": 0.0, "tmax": 0.5, "ttick": 0.1, "title": "IBR v1 Test",
                "ytitles": ["Voltage [kV]", "Current [kA]", "Control [pu]", "dq [pu]"],
                "signals": [{"name": "Ea", "base": 1.0, "axis": 0},
                            {"name": "Eb", "base": 1.0, "axis": 0},
                            {"name": "Ec", "base": 1.0, "axis": 0},
                            {"name": "Ia", "base": 1.0, "axis": 1},
                            {"name": "Ib", "base": 1.0, "axis": 1},
                            {"name": "Ic", "base": 1.0, "axis": 1},
                            {"name": "Freq_pll", "base": 60.0, "axis": 2},
                            {"name": "Pref", "base": 1.0, "axis": 2},
                            {"name": "Qref", "base": 1.0, "axis": 2},
                            {"name": "Vref", "base": 1.0, "axis": 2},
                            {"name": "Pout", "base": 1.0, "axis": 2},
                            {"name": "Qout", "base": 1.0, "axis": 2},
                            {"name": "Id", "base": 1.0, "axis": 3},
                            {"name": "Iq", "base": 1.0, "axis": 3},
                            {"name": "Vd", "base": 1.0, "axis": 3},
                            {"name": "Vq", "base": 1.0, "axis": 3}]},
  "grid.csv": {"tmin": 0.0, "tmax": 0.2, "ttick": 0.04, "title": "SMIB Impedance Test",
                "ytitles": ["Voltage [V]", "Iinv [kA]", "Power [MW]"],
                "signals": [{"name": "Vsa", "base": 1.0, "axis": 0},
                            {"name": "Vsb", "base": 1.0, "axis": 0},
                            {"name": "Vsc", "base": 1.0, "axis": 0},
                            {"name": "Vta", "base": 1.0, "axis": 0},
                            {"name": "Vtb", "base": 1.0, "axis": 0},
                            {"name": "Vtc", "base": 1.0, "axis": 0},
                            {"name": "Ia", "base": 1000.0, "axis": 1},
                            {"name": "Ib", "base": 1000.0, "axis": 1},
                            {"name": "Ic", "base": 1000.0, "axis": 1},
                            {"name": "P", "base": 1.0e6, "axis": 2}]},
  "hwpv.csv": {"tmin": 0.5, "tmax": 5.5, "ttick": 0.5, "title": "HWPV Generalized Block Diagram Test",
                "ytitles": ["Inputs [pu]", "Outputs [pu]"],
                "signals": [{"name": "G", "base": 1000.0, "axis": 0},
                            {"name": "Ctl", "base": 1.0, "axis": 0},
                            {"name": "GVrms", "base": 1000.0, "axis": 0},
                            {"name": "Vd", "base": hwpv_vbase, "axis": 0},
                            {"name": "Vq", "base": hwpv_vbase, "axis": 0},
                            {"name": "Id", "base": hwpv_ibase, "axis": 1},
                            {"name": "Iq", "base": hwpv_ibase, "axis": 1},
                            {"name": "Idc", "base": hwpv_idcbase, "axis": 1},
                            {"name": "Vdc", "base": hwpv_vdcbase, "axis": 1}]},
  "scrx9.csv": {"tmin": 1.0, "tmax": 3.0, "ttick": 0.2, "title": "SCRX9 Excitation System Test",
                "ytitles": ["Inputs [pu]", "Outputs [pu]"],
                "signals": [{"name": "VRef", "base": 1.0, "axis": 0},
                            {"name": "VT", "base": 1.0, "axis": 0},
                            {"name": "VUEL", "base": 1.0, "axis": 1},
                            {"name": "VOEL", "base": 1.0, "axis": 1},
                            {"name": "EFD", "base": 1.0, "axis": 1}]},
  "ppc_voltage_step.csv": {"tmin": 0.0, "tmax": 5.0, "ttick": 1.0, "title": "PPC Voltage Step Test",
                        "ytitles": ["Inputs [pu]", "Outputs [pu]"],
                        "signals": [{"name": "Vmeas", "base": 1.0, "axis": 0},
                                    {"name": "Plant_pref", "base": 1.0, "axis": 0},
                                    {"name": "Qext", "base": 1.0, "axis": 0},
                                    {"name": "Pref", "base": 1.0, "axis": 1}]},
  "ppc_qmeas_step.csv": {"tmin": 0.0, "tmax": 5.0, "ttick": 1.0, "title": "PPC Reactive Power Step Test",
                        "ytitles": ["Inputs [pu]", "Outputs [pu]"],
                        "signals": [{"name": "Qmeas", "base": 1.0, "axis": 0},
                                    {"name": "Plant_pref", "base": 1.0, "axis": 0},
                                    {"name": "Qext", "base": 1.0, "axis": 0},
                                    {"name": "Pref", "base": 1.0, "axis": 1}]},
  "ppc_freq_step.csv": {"tmin": 0.0, "tmax": 10.0, "ttick": 1.0, "title": "PPC Frequency Step Test",
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
      lbl = '{:s} / {:s}'.format (key, str(round(base, 2)))
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
  if data_path.lower() in plots and all_channels == False:
    plot_page (df, plots[data_path])
  else:
    df.plot(subplots=True, title=data_path.lower())
    plt.show()
    plt.close()



