# Copyright (C) 2024-26 Meltran, Inc

import os
import sys
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['savefig.directory'] = os.getcwd()

data_path = 'scrx9.csv'

if __name__ == '__main__':
  if len(sys.argv) > 1:
    data_path = sys.argv[1]
  df = pd.read_csv (data_path, index_col='t')
  df.info()
  df.plot(subplots=True, title=data_path)
  plt.show()



