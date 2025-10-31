import sys
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

plt.rcParams['savefig.directory'] = os.getcwd()

if __name__ == '__main__':
  fname = 'SyncMachCall.hdf5'
  if len(sys.argv) > 1:
    fname = sys.argv[1]

  df = pd.read_hdf(fname)
  #df.info()
  #print (df.describe(include='all'))

  print ('Column                         Min           Max')
  for lbl, data in df.items():
    print ('{:20s} {:13.5f} {:13.5f}'.format (lbl, data.min(), data.max()))

  ax = df.plot (title=fname, subplots=True, figsize=(15,12))
  plt.show()

