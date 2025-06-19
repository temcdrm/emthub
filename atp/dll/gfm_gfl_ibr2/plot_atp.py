import sys
import matplotlib.pyplot as plt
import numpy as np
import h5py
import os

def plot_channel (ax, t, y, label, bLabelX = False):
  ax.plot (t, y)
  ax.set_ylabel (label)
  ax.set_xlim (t[0], t[-1])
  if bLabelX:
    ax.set_xlabel ('t [s]')
  else:
    ax.set_xticklabels ([])

lsize = 10
plt.rc('font', family='serif')
plt.rc('xtick', labelsize=lsize)
plt.rc('ytick', labelsize=lsize)
plt.rc('axes', labelsize=lsize)
plt.rc('legend', fontsize=lsize)
pWidth = 6.0
pHeight = pWidth / 1.618

f = h5py.File('base.hdf5', 'r')
grp = f['group0']
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

# data of interest
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

fig = plt.figure (figsize=(18,12), constrained_layout=True)
fig.suptitle ('Case Title', fontsize=lsize + 4)
subfigs = fig.subfigures (2, 2, wspace = 0.05, hspace = 0.05)

indices = np.where(t>=3.9)
i1 = indices[0][0]
indices = np.where(t>4.5)
i2 = indices[0][0]
print ('Window', i1, i2, t[i1], t[i2])
tplot = t[i1:i2]

ax = subfigs[0,0].subplots(3, 1)
plot_channel (ax[0], tplot, freq[i1:i2], 'Freq [Hz]')
plot_channel (ax[1], tplot, pout[i1:i2], 'Pout [pu]')
plot_channel (ax[2], tplot, qout[i1:i2], 'Qout [pu]', bLabelX = True)

ax = subfigs[0,1].subplots(4,2)
plot_channel (ax[0,0], tplot, vd1[i1:i2], 'Vd1 [pu]')
plot_channel (ax[1,0], tplot, vq1[i1:i2], 'Vq1 [pu]')
plot_channel (ax[2,0], tplot, id1[i1:i2], 'Id1 [pu]')
plot_channel (ax[3,0], tplot, iq1[i1:i2], 'Iq1 [pu]', bLabelX = True)
plot_channel (ax[0,1], tplot, vd2[i1:i2], 'Vd2 [pu]')
plot_channel (ax[1,1], tplot, vq2[i1:i2], 'Vq2 [pu]')
plot_channel (ax[2,1], tplot, id2[i1:i2], 'Id2 [pu]')
plot_channel (ax[3,1], tplot, iq2[i1:i2], 'Iq2 [pu]', bLabelX = True)

indices = np.where(t>=3.98)
i1 = indices[0][0]
indices = np.where(t>4.03)
i2 = indices[0][0]
print ('Window', i1, i2, t[i1], t[i2])
tplot = t[i1:i2]

ax = subfigs[1,0].subplots(2,2)
plot_channel (ax[0,0], tplot, id1[i1:i2], 'Id1 [pu]')
plot_channel (ax[1,0], tplot, iq1[i1:i2], 'Iq1 [pu]', bLabelX = True)
plot_channel (ax[0,1], tplot, id2[i1:i2], 'Id2 [pu]')
plot_channel (ax[1,1], tplot, iq2[i1:i2], 'Iq2 [pu]', bLabelX = True)

ax = subfigs[1,1].subplots(2,2)
plot_channel (ax[0,0], tplot, vd1[i1:i2], 'Vd1 [pu]')
plot_channel (ax[1,0], tplot, vq1[i1:i2], 'Vq1 [pu]', bLabelX = True)
plot_channel (ax[0,1], tplot, vd2[i1:i2], 'Vd2 [pu]')
plot_channel (ax[1,1], tplot, vq2[i1:i2], 'Vq2 [pu]', bLabelX = True)

plt.show()
quit()

plt.rcParams['savefig.directory'] = os.getcwd()
plt.savefig('atp0.pdf')
plt.show()
plt.close()


