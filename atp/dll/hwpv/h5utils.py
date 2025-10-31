# Copyright (C) 2025 Meltran, Inc
# file: h5utils.py
""" Loads ATP simulation results from COMTRADE files, saves to HDF.

Paragraph.

Public Functions:
    :main: does the work
"""

import sys
from comtrade import Comtrade
import numpy as np
import h5py
import math
#from scipy import signal

def load_atp_comtrade_channels (atp_base):
  rec = Comtrade ()
  rec.load (atp_base + '.cfg', atp_base + '.dat')
  t = np.array(rec.time)

  channels = {}
  channels['t'] = t
  for i in range(rec.analog_count):
    lbl = rec.analog_channel_ids[i]
    key = '**'
    if 'V-node' in lbl[16:22]:
      key = 'V:' + lbl[0:6].rstrip()
    elif 'I-branch' in lbl[14:22]:
      if 'MODELS' in lbl[0:6]:
        key = 'M:' + lbl[7:13].rstrip()
      elif 'TACS' in lbl[0:4]:
        key = 'T:' + lbl[7:13].rstrip()
      else:
        key = 'I:' + lbl[0:6].rstrip() + ':' + lbl[7:13].rstrip()
    print ('Channel', i, lbl, 'key', key)
    channels[key] = np.array (rec.analog[i])
  if 't' in channels: # since COMTRADE does not support sub-microsecond steps...
    channels['t'] = np.linspace (channels['t'][0], channels['t'][-1], len(channels['t']))
  return channels

def save_atp_channels (filename, groupname, channels, mode='w'):
  f = h5py.File (filename, mode)
  grp = f.create_group (groupname)
  for key, val in channels.items():
    if val is not None:
      grp.create_dataset (key, data=val, compression='gzip')
  f.close()

