# Copyright (C) 2026 Meltran, Inc
# calculating ACLineSegment power flow at the "to" end, for Annex C.4

import math
import cmath
LONGLINE = True

if __name__ == '__main__':
  # ACLineSegment attributes for the total length
  Z = complex(20.0, 188.5)
  Y = complex(0.0, 0.002092)
  # known variables at the "from" bus, port 2 in the ABCD network
  s2 = complex(341453311.0, 7543467.0)
  v2 = complex(345000.0, 0.0)
  i2 = (-s2/v2).conjugate() # i2 defined to flow out of port 2
  # known voltage and power at the "to" bus
  v1solved = cmath.rect (309915.22500000003, math.radians(-35.25937))
  s1solved = complex(-318932949.0, -20252242.0)

  print ('v2=', cmath.polar(v2))
  print ('i2=', cmath.polar(i2))

  # line parameters
  gammaL = cmath.sqrt(Z*Y)
  Zc = cmath.sqrt(Z/Y)
  if LONGLINE:
    A = cmath.cosh(gammaL)
    D = A
    B = Zc * cmath.sinh(gammaL)
    C = (1.0/Zc) * cmath.sinh(gammaL)
    print (' (using long-line correction)')
  else:
    A = 1 + 0.5*Y*Z
    D = A
    B = Z * (1.0 + Y*Z/6.0)
    C = Y * (1.0 + Y*Z/6.0)
    print (' (using nominal pi section)')

  # calculate the port 1 parameters
  v1 = A*v2 + B*i2
  i1 = C*v2 + D*i2
  s1 = v1*i1.conjugate()

  print ('gammaL=', gammaL)
  print ('Zc=', Zc)
  print ('A=', A)
  print ('B=', B)
  print ('C=', C)
  print ('D=', D)
  print ('AD-BC=', A*D - B*C)
  print ('v1=', cmath.polar(v1),'compared to', cmath.polar(v1solved))
  print ('i1=', cmath.polar(i1))
  print ('s1=', s1, 'compared to', s1solved)

  # find currents and losses in the pi branches
  Iseries = (v2 - v1) / Z
  Ishunt2 = v2 * Y / 2.0
  Ishunt1 = v1 * Y / 2.0
  Ploss = abs(Iseries)**2 * Z.real
  print ('Pi P loss=', Ploss*1.0e-6, 'compared to ABCD', (s2.real + s1.real)*1.0e-6, 'or MATPOWER', (s2.real + s1solved.real)*1.0e-6)
  Qloss = abs(Iseries)**2 * Z.imag - 0.5 * abs(v1)**2 * Y.imag - 0.5 * abs(v2)**2 * Y.imag
  print ('Pi Q loss=', Qloss*1.0e-6, 'compared to ABCD', (s2.imag + s1.imag)*1.0e-6, 'or MATPOWER', (s2.imag + s1solved.imag)*1.0e-6)

  # final answer
  print ('** S1 = Sto = ', s1.real*1.0e-6, 'MW,', s1.imag*1.0e-6, 'Mvar')

