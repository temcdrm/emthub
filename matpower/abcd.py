# Copyright (C) 2026 Meltran, Inc
# calculating ACLineSegment power flow at the "to" end, for Annex C.4

import math
import cmath
LONGLINE = False
USE_ATP_SOLN = False
SQRT3 = math.sqrt(3.0)

if __name__ == '__main__':
  # ACLineSegment nominal attributes for the total length
  Z = complex(20.0, 188.5)
  Y = complex(0.0, 0.002092)
  gammaL = cmath.sqrt(Z*Y)
  Zc = cmath.sqrt(Z/Y)

  # find the long-line adjusted pi parameters
  print ('Nominal Z=', Z)
  print ('Nominal Y=', Y)
  Zpi = Z * cmath.sinh(gammaL) / gammaL
  Ypi = Y * 2.0 * cmath.tanh(0.5*gammaL) / gammaL
  print ('Long-line Z=', Zpi)
  print ('Long-line Y=', Ypi)

  # adjusted for long-line effects
  Z = complex(17.4476, 176.4845)
  Y = complex(0.0, 0.00216353) # NOTE: Y.real has a noticeable impact, compared with true long-line equations

  if USE_ATP_SOLN:
    s2 = complex(353330000.0,-3590000.0)
    v2ln = complex(344888.3/SQRT3, math.radians(-0.202722)) # this is now line-to-neutral
    i2 = (-s2/v2ln/3.0).conjugate() # i2 defined to flow out of port 2
    # known voltage and power at the "to" bus
    v1solved = cmath.rect (315781.75, math.radians(-33.69307))
    s1solved = complex(-331880000.0, -25220000.0)
    print ('** Using ATP Phasor Solution')
  else:
    # known variables at the "from" bus, port 2 in the ABCD network
    #s2 = complex(341453311.0, 7543467.0) # from nominal pi MATPOWER
    s2 = complex(355950166.0, -6724663.0)
    v2ln = complex(345000.0/SQRT3, 0.0) # this is now line-to-neutral
    i2 = (-s2/v2ln/3.0).conjugate() # i2 defined to flow out of port 2
    # known voltage and power at the "to" bus
    #v1solved = cmath.rect (309915.22500000003, math.radians(-35.25937)) # from nominal pi MATPOWER
    #s1solved = complex(-318932949.0, -20252242.0) # from nominal pi MATPOWER
    v1solved = cmath.rect (317717.745, math.radians(-33.619911))
    s1solved = complex(-335194123.0, -21284827.0)
    print ('** Using MATPOWER Solution')

  print ('v2ln=', cmath.polar(v2ln))
  print ('i2=', cmath.polar(i2))

  # ABCD parameters
  if LONGLINE:
    A = cmath.cosh(gammaL)
    D = A
    B = Zc * cmath.sinh(gammaL)
    C = (1.0/Zc) * cmath.sinh(gammaL)
    print (' (using long-line correction)')
  else:
    A = 1 + 0.5*Y*Z
    D = A
    B = Z
    C = Y * (1.0 + Y*Z/4.0)
    print (' (using nominal pi section)')

  # calculate the port 1 parameters
  v1ln = A*v2ln + B*i2
  i1 = C*v2ln + D*i2
  s1 = 3.0*v1ln*i1.conjugate()
  v1 = SQRT3*v1ln

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

  print ('ERROR Summary:')
  print ('  v1mag = {:.4f} [%]'.format (100.0*(abs(v1) - abs(v1solved))/abs(v1solved)))
  print ('     P1 = {:.4f} [%]'.format (100.0*(abs(s1.real) - abs(s1solved.real))/abs(s1solved.real)))
  print ('     Q1 = {:.4f} [%]'.format (100.0*(abs(s1.imag) - abs(s1solved.imag))/abs(s1solved.imag)))

  # find currents and losses in the pi branches
  Iseries = (v2ln - v1ln) / Z
  Ishunt2 = v2ln * Y / 2.0
  Ishunt1 = v1ln * Y / 2.0
  Ploss = 3*(abs(Iseries)**2 * Z.real)
  print ('Pi P loss=', Ploss*1.0e-6, 'compared to ABCD', (s2.real + s1.real)*1.0e-6, 'or MATPOWER', (s2.real + s1solved.real)*1.0e-6)
  Qloss = 3*(abs(Iseries)**2 * Z.imag - 0.5 * abs(v1ln)**2 * Y.imag - 0.5 * abs(v2ln)**2 * Y.imag)
  print ('Pi Q loss=', Qloss*1.0e-6, 'compared to ABCD', (s2.imag + s1.imag)*1.0e-6, 'or MATPOWER', (s2.imag + s1solved.imag)*1.0e-6)

  # final answer
  print ('** S1 = Sto = ', s1.real*1.0e-6, 'MW,', s1.imag*1.0e-6, 'Mvar')

