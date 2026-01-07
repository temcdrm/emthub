# Copyright (C) 2026 Meltran, Inc

import math

DEGRAD = 180.0 / math.pi
POS120 = 120.0 / DEGRAD
NEG120 = -POS120
SQRTSIXTH = math.sqrt (1.0 / 6.0)
SQRTHALF = math.sqrt (1.0 / 2.0)

# ATP Type 14 sources use the cosine function
def pcc_voltages (Vmag, Vang, we, t):
  Va = Vmag * math.cos (we*t + Vang)
  Vb = Vmag * math.cos (we*t + Vang + NEG120)
  Vc = Vmag * math.cos (we*t + Vang + POS120)
  return Va, Vb, Vc

def transform_alpha (Va, Vb, Vc, Vbase):
  Valpha = SQRTSIXTH * (2*Va - Vb - Vc) / Vbase
  Vbeta = SQRTHALF * (Vb - Vc) / Vbase
  return Valpha, Vbeta

def transform_dq (Valpha, Vbeta, th):
  costh = math.cos(th)
  sinth = math.sin(th)
  print ('costh={:.3f}, sinth={:.3f}'.format (costh, sinth))
  Vd = Valpha*costh + Vbeta*sinth
  Vq = -Valpha*sinth + Vbeta*sinth
  return Vd, Vq

if __name__ == '__main__':
  Vbase = 2.2e4
  Vmag = 18412.0
  Vang = -5.0 / DEGRAD
  we = 376.9911
  th0 = 3.1416 # 3.12 # 2.36
  t = 0.0

  Va, Vb, Vc = pcc_voltages (Vmag, Vang, we, t)
  Valpha, Vbeta = transform_alpha (Va, Vb, Vc, Vbase)
  Vd, Vq = transform_dq (Valpha, Vbeta, th0)

  print ('Vang={:.3f}, th0={:.2f}, Va={:.1f}, Vb={:.1f}, Vc={:.1f}, Valpha={:.3f}, Vbeta={:.3f}, Vd={:.3f}, Vq={:.3f}'.format (Vang, th0, Va, Vb, Vc, Valpha, Vbeta, Vd, Vq))

  # predict the initial angle
  theta_ic = Vang + 90.0 / DEGRAD
  print ('Predicted IC for Vang={:.3f} is {:.3f}'.format (Vang, theta_ic))
