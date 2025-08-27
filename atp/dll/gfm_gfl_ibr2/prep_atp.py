import sys
import numpy as np
import h5py
import os
from scipy import signal

# for decimation
b, a = signal.butter (2, 1.0 / 4096.0, btype='lowpass', analog=False)

def my_decimate(x, q, method):
  if method == 'fir':
    return signal.decimate (x, q, ftype='fir', n=None)
  elif method == 'butter':
    return signal.lfilter (b, a, x)[::q]
  elif method == 'slice':
    return x[::q]
  elif q == 65:  # downsampling 1 MHz signals to 256 samples per 60-Hz cycle
    return signal.decimate (signal.decimate(x, 5), 13)
  elif q <= 13:
    return signal.decimate (x, q)
  elif q == 800:
    return signal.decimate (signal.decimate (signal.decimate(x, 10), 10), 8)
  elif q == 1000:
    return signal.decimate (signal.decimate (signal.decimate(x, 10), 10), 10)
  return x[::q] # default will be slice

def decimate_channels(channels, k=1000, method='iir', filtered=[]): # can choose iir, fir, slice
  for key in channels:
    if key == 't':
      channels['t'] = channels['t'][::k]
    elif channels[key] is not None:
      if key in filtered:
        channels[key] = my_decimate (channels[key], k, method)
      else:
        channels[key] = channels[key][::k]

def process_group (grp):
  dlen = grp['t'].len()
  t = np.zeros(dlen)
  y = np.zeros(dlen)
  grp['t'].read_direct (t)
  dt = t[1] - t[0]
   
  # input data of interest
  id1 = np.zeros(dlen)
  grp['M:ID1'].read_direct(id1)
  iq1 = np.zeros(dlen)
  grp['M:IQ1'].read_direct(iq1)
  id2 = np.zeros(dlen)
  grp['M:ID2'].read_direct(id2)
  iq2 = np.zeros(dlen)
  grp['M:IQ2'].read_direct(iq2)
  vd1 = np.zeros(dlen)
  grp['M:VTD1'].read_direct(vd1)
  vq1 = np.zeros(dlen)
  grp['M:VTQ1'].read_direct(vq1)
  vd2 = np.zeros(dlen)
  grp['M:VTD2'].read_direct(vd2)
  vq2 = np.zeros(dlen)
  grp['M:VTQ2'].read_direct(vq2)
  freq = np.zeros(dlen)
  grp['M:FREQ'].read_direct(freq)
  pout = np.zeros(dlen)
  grp['M:POUT'].read_direct(pout)
  qout = np.zeros(dlen)
  grp['M:QOUT'].read_direct(qout)

  V1 = np.sqrt (vd1*vd1 + vq1*vq1)
  V2 = np.sqrt (vd2*vd2 + vq2*vq2)

  tnew = my_decimate (t, 10, 'slice')
  v1new = my_decimate (V1, 10, 'slice')
  v2new = my_decimate (V2, 10, 'slice')
  fnew = my_decimate (freq, 10, 'slice')
  pnew = my_decimate (pout, 10, 'slice')
  qnew = my_decimate (qout, 10, 'slice')

  return tnew, v1new, v2new, fnew, pnew, qnew

if __name__ == '__main__':
  f1 = h5py.File('base.hdf5', 'r')
  f2 = h5py.File('prepped.hdf5', 'w')
  f3 = h5py.File('downsample.hdf5', 'w')
  ncases = len(f1.items())
  print ('Processing', ncases, 'cases')
  for grp_name, grp in f1.items():
    print (' ', grp_name)
    grp2 = f2.create_group (grp_name)
    t, v1, v2, f, p, q = process_group (grp)
    grp2.create_dataset ('t', data=t, compression='gzip')
    grp2.create_dataset ('V1', data=v1, compression='gzip')
    grp2.create_dataset ('V2', data=v2, compression='gzip')
    grp2.create_dataset ('F', data=f, compression='gzip')
    grp2.create_dataset ('P', data=p, compression='gzip')
    grp2.create_dataset ('Q', data=q, compression='gzip')

    # downsample all signals
    grp3 = f3.create_group (grp_name)
    dlen = grp['t'].len()
    y = np.zeros(dlen)
    for key in grp: # picks up t, too
      grp[key].read_direct(y)
      ynew = my_decimate (y, 10, 'slice')
      grp3.create_dataset (key, data=ynew, compression='gzip')
      

