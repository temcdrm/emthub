# Copyright (C) 2025 Meltran, Inc

def AtpFit6(x):
  if x == 0.0:
    return '0.0000'
  elif x >= 10000:
    exp = 0
    while x >= 999.0:
      x /= 10.0
      exp += 1
      print ('reduced', x, exp)
    xstr = '{:3d}.E{:d}'.format(int(round(x, 3)), exp)
  elif x >= 1000:
    xstr = '{:6.1f}'.format(x)
  elif x >= 100:
    xstr = '{:6.2f}'.format(x)
  elif x >= 10:
    xstr = '{:6.3f}'.format(x)
  elif x <= -100.0:
    xstr = '{:6.1f}'.format(x)
  elif x <= -10.0:
    xstr = '{:6.2f}'.format(x)
  elif x <= -1.0:
    xstr = '{:6.3f}'.format(x)
  elif x < 0.0:
    xstr = '{:6.3f}'.format(x)
  elif x <= 0.001:
    exp = 0
    while x < 10.0:
      x *= 10.0
      exp += 1
    xstr = '{:2d}.E-{:d}'.format(int(round(x)), exp)
  else:
    xstr = '{:6.4f}'.format(x)
  return xstr

if __name__ == '__main__':
  for x in [999999.9999999999]: # [1000.0, 1e6, 999999.9999999999]:
    s = AtpFit6(x)
    print ('#{:s}#{:d}'.format (s, len(s)))
