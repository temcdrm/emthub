# Copyright (C) 2025-2026 Meltran, Inc

import rdflib
import sys
import math
import cmath
import os
import numpy as np
import json
import cim_examples
import emthub.api as emthub

GEN_TYPE_ST = 0
GEN_TYPE_PV = 1
GEN_TYPE_WT = 2

USE_TYPE_14_MACHINES = False
USE_FIELD_SATURATION = False
USE_TYPE_14_WIND = False
USE_TYPE_14_SOLAR = False
MIN_BERGERON_TAU = 200.0e-6

DUM_NODES = 0
PV3_DUM_NODES = 49
MACHINE_DUM_NODES = 31
SOLAR_DUM_NODES = 114
WIND_DUM_NODES = 114
DUM_NODE_LIMIT = 9999

DELIM = ':'
SQRT3 = math.sqrt(3.0)
SQRT2 = math.sqrt(2.0)
RAD_TO_DEG = 180.0 / math.pi
OMEGA = 2.0 * 60.0 * math.pi
MIN_IMAG = 0.00015
MIN_PNLL = 0.00010
TOPEN = 9990.0

MACHINE_NPOLES = 2.0
MACHINE_H = 3.0
MACHINE_J = 2.0*MACHINE_H*math.pow(0.5*MACHINE_NPOLES/OMEGA, 2.0) # multiply by RMVA for HICO in million kg-m2
MACHINE_DSD = 1e-5 * 1e6 * 0.5 * MACHINE_NPOLES / OMEGA # multiply by RMVA for DSD in N-m

# these can be reset for each model conversion
LOAD_MULT = 1.0
LOAD_TOTAL = 0.0
DR_COUNT = 0
DR_TOTAL = 0.0
PV_COUNT = 0
PV_TOTAL = 0.0
SM_COUNT = 0
SM_TOTAL = 0.0
WND_COUNT = 0
WND_TOTAL = 0.0
NEXT_BUSNUM = 0

def reset_globals(case):
  """Reset counters and limits for the next ATP netlist export.

  Args:
    case (dict): one of the CASES
  """
  global LOAD_MULT, DUM_NODES, LOAD_TOTAL, PV_COUNT, PV_TOTAL, SM_COUNT, SM_TOTAL, WND_COUNT, WND_TOTAL
  global NEXT_BUSNUM, DR_COUNT, DR_TOTAL
  if 'load' in case:
    LOAD_MULT = case['load']
  else:
    LOAD_MULT = 1.0
  LOAD_TOTAL = 0.0
  DUM_NODES = 0
  DR_COUNT = 0
  DR_TOTAL = 0.0
  PV_COUNT = 0
  PV_TOTAL = 0.0
  SM_COUNT = 0
  SM_TOTAL = 0.0
  WND_COUNT = 0
  WND_TOTAL = 0.0
  NEXT_BUSNUM = 0

def AtpNode(bus, phs):
  if bus[0].isdigit():
    return 'B{:4s}{:1s}'.format(bus, phs).replace(' ', '_')
  return '{:5s}{:1s}'.format(bus, phs).replace(' ', '_')

def AtpBus(bus):
  if bus[0].isdigit():
    return 'B{:4s}'.format(bus).replace(' ', '_')
  return '{:5s}'.format(bus).replace(' ', '_')

def GetNextScratchBus ():
  global NEXT_BUSNUM
  NEXT_BUSNUM += 1
  return '_{:4s}'.format(str(NEXT_BUSNUM)).replace(' ', '_')

# should preserve order
def GetAtpPhaseList(abc):
  if len(abc) < 1:
    return ['A', 'B', 'C']
  retval = []
  if '1' in abc:
    retval.append('1')
  if '2' in abc:
    retval.append('2')
  if 'A' in abc:
    retval.append('A')
  if 'B' in abc:
    retval.append('B')
  if 'C' in abc:
    retval.append('C')
  return retval

def GetAtpPhaseSequence (seqs):
  seqphs = sorted(seqs.split(':'))
  retval = []
  for e in seqphs:
    phs = e[1:]
    if phs == 's1':
      retval.append('1')
    elif phs == 's2':
      retval.append('2')
    elif phs != 'N':
      retval.append(phs)
  return retval

# look up the lower triangle, i.e., i >= j and both >= 0
# return ohms, ohms, uF
def PhaseMatrixElement (tbl, lname, i, j, llen):
  tok = '{:s}{:s}{:d}{:s}{:d}'.format (lname, DELIM, i, DELIM, j)
  row = tbl[tok]
  r = row['r'] * llen
  xl = row['x'] * llen
  uc = row['b'] * 1.0e6 * llen / OMEGA
  return r, xl, uc

def AtpLoadTo(bus, phs, bDelta):
  if bDelta == True:
    if phs == 'A':
      return AtpNode (bus, 'B')
    if phs == 'B':
      return AtpNode (bus, 'C')
    if phs == 'C':
      return AtpNode (bus, 'A')
  return '      '

def AtpDeltaLaggingNode(bus, phs):
  nd = 'B'
  if phs == 'B':
    nd = 'C'
  elif phs == 'C':
    nd = 'A'
  return AtpNode(bus, nd)

def AtpDeltaLeadingNode(bus, phs):
  nd = 'C'
  if phs == 'B':
    nd = 'A'
  elif phs == 'C':
    nd = 'B'
  return AtpNode(bus, nd)

def AtpXfmrNeutralNode(xfbus, wdgrow):
  if wdgrow['conn'] == 'Y':
    if wdgrow['grounded']:
      if wdgrow['rground'] > 0.0 or wdgrow['xground'] > 0.0:
        return AtpNode (xfbus, 'N')
      else:
        return '      '
  return ''

def PadBlanks(nb):
  retval = ''
  for i in range(nb):
    retval += ' '
  return retval

def AtpRXC(r, x, c):
  return '{:16e}{:16e}{:16e}'.format(r, x, c)

def AtpRZTL(r, z, t, l):
  return '{:12e}{:12e}{:12e}{:12e}'.format(r, z, t, l)

def AtpFit6(x):
  if x == 0.0:
    return '0.0000'
  elif x >= 10000:
    exp = 0
    while x >= 999.0:
      x /= 10.0
      exp += 1
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

def AtpFit10(x):
  if x == 0.0:
    return '0.0'
  elif x < 0.0:
    return '{:9.3e}'.format(x)
  return '{:10.4e}'.format(x)

def AtpXfmrNeutralNode(xfbus, enum, wdgrow):
  if wdgrow['conn'] == 'Y':
    if wdgrow['grounded']:
      if wdgrow['rground'] > 0.0 or wdgrow['xground'] > 0.0:
        return AtpNode (xfbus, chr(ord('M')+enum))
      else:
        return '      '
    else:
      return AtpNode (xfbus, chr(ord('M')+enum))
  return ''

def AtpXfmrNeutralImpedance(xfbus, enum, wdgrow):
  if wdgrow['conn'] == 'Y' and wdgrow['grounded'] and (len(wdgrow['rground']) > 0) and (len(wdgrow['rground']) > 0):
    if wdgrow['rground'] > 0.0 or wdgrow['xground'] > 0.0:
      return '  {:s}                  {:s}{:s}'.format (AtpNode (xfbus, chr(ord('M')+enum)), 
                                                        AtpFit6(wdgrow['rground']), 
                                                        AtpFit6(wdgrow['xground']))
  return ''

# this is for balanced PowerTransformer; ph can be A, B, C for Y or D
def AtpXfmrNodes(xfbus, enum, wdgrow, bEnd1Delta, ph, atp_buses=None):
  bus = wdgrow['cn1id']
  if atp_buses:
    bus = atp_buses[bus]
  if wdgrow['conn'] == 'Y':
    return '{:2d}{:s}{:s}'.format(enum, AtpNode(bus, ph), AtpXfmrNeutralNode(xfbus, enum, wdgrow))
  else:
    if enum == 1 or bEnd1Delta: # leading Delta
      if ph == 'A':
        ph2 = 'C'
      elif ph == 'B':
        ph2 = 'A'
      elif ph == 'C':
        ph2 = 'B'
    else: # lagging Delta
      if ph == 'A':
        ph2 = 'B'
      elif ph == 'B':
        ph2 = 'C'
      elif ph == 'C':
        ph2 = 'A'
    return '{:2d}{:s}{:s}'.format(enum, AtpNode(bus, ph), AtpNode(bus, ph2))

def AtpXfmr(r, x, v, tap=1.0):
  return AtpFit6(r) + AtpFit6(x) + AtpFit6(v*tap)

def AtpStarEquivalent(wdgs, meshes, taps):
  nwdgs = len(wdgs)
  r = []
  x = []
  v = []
  for i in range(nwdgs):
    if wdgs[i]['conn'] == 'D':
      v.append(wdgs[i]['ratedU']*0.001)
    else:
      v.append(wdgs[i]['ratedU']*0.001/SQRT3)
    r.append(0.0001) # this should at least run for nwdgs > 3
    x.append(0.0001)
  if nwdgs == 2:
    # input impedances are wye equivalent on 3-phase base
    zbase1 = wdgs[0]['ratedU'] * wdgs[0]['ratedU'] / wdgs[0]['ratedS']
    zbase2 = wdgs[1]['ratedU'] * wdgs[1]['ratedU'] / wdgs[1]['ratedS']
    rpu = meshes[0]['r'] / zbase1
    xpu = meshes[0]['x'] / zbase1
    r[0] = 0.5 * rpu * zbase1
    r[1] = 0.5 * rpu * zbase2
    x[0] = 0.5 * xpu * zbase1
    x[1] = 0.5 * xpu * zbase2
  elif nwdgs == 3:
    zbase1 = wdgs[0]['ratedU'] * wdgs[0]['ratedU'] / wdgs[0]['ratedS'] # work on winding 1 Sbase
    zbase2 = wdgs[1]['ratedU'] * wdgs[1]['ratedU'] / wdgs[0]['ratedS']
    zbase3 = wdgs[2]['ratedU'] * wdgs[2]['ratedU'] / wdgs[0]['ratedS']
    r12pu = meshes[0]['r'] / zbase1
    x12pu = meshes[0]['x'] / zbase1
    r13pu = meshes[1]['r'] / zbase1
    x13pu = meshes[1]['x'] / zbase1
    r23pu = meshes[2]['r'] / zbase2
    x23pu = meshes[2]['x'] / zbase2
    r[0] = 0.5 * (r12pu + r13pu - r23pu) * zbase1
    r[1] = 0.5 * (r12pu + r23pu - r13pu) * zbase2
    r[2] = 0.5 * (r13pu + r23pu - r12pu) * zbase3
    x[0] = 0.5 * (x12pu + x13pu - x23pu) * zbase1
    x[1] = 0.5 * (x12pu + x23pu - x13pu) * zbase2
    x[2] = 0.5 * (x13pu + x23pu - x12pu) * zbase3
  # TODO: account for DY connections? account for effect of taps on impedance?
  for i in range(nwdgs):
    v[i] *= taps[i]
  # multiply any delta-connected impedances by 3
  for i in range(nwdgs):
    if wdgs[i]['conn'] == 'D':
      r[i] *= 3.0
      x[i] *= 3.0
  return r, x, v

def AtpStarCore(wdgs, dict, pid, bUseSaturation):
  # determine steady-state exciting branch from the core admittance attributes
  # TODO: account fo effect of taps on core admittance and saturation?
  core = dict['EMTPowerXfmrCore']['vals'][pid]
  cim_b = core['b']
  cim_g = core['g']
  cim_e = core['enum'] - 1  # This may not be 0 in the CIM. For ATP, transform this to end 0
  cim_v = wdgs[cim_e]['ratedU']
  core_e = 0 # ATP saturation branch always goes with first winding
  core_v = wdgs[core_e]['ratedU']
  core_s = wdgs[core_e]['ratedS']
  core_c = wdgs[core_e]['conn']
  core_s /= 3.0
  ratio = core_v * core_v / cim_v / cim_v
  #print ('ratio', ratio, core_v, cim_v)
  core_b = cim_b / ratio
  core_g = cim_g / ratio
  if core_c == 'Y':
    cim_v /= SQRT3
    core_v /= SQRT3
  if core_b > 0.0:
    Iss = SQRT2 * core_b * core_v
  else:
    Iss = MIN_IMAG * SQRT2 * core_s / core_v
  Fss = core_v / OMEGA * SQRT2
  # this represents the core losses, TODO: check validity for a delta connection
  if core_g > 0.0:
    Rmag = 1.0 / core_g
  else:
    Rmag = core_v * core_v / MIN_PNLL / core_s

  # create a saturable current-flux curve if available, or use the steady-state parameters if not
  Imag = []
  Fmag = []
  if bUseSaturation:
    sat = dict['EMTXfmrSaturation']
    for key in sat['vals']:
      toks = key.split(':')
      if toks[0] == pid:
        ival = float(toks[1]) * cim_v / core_v
        fval = sat['vals'][key]['vs'] * core_v / cim_v
        #print (toks[0], ival, fval)
        Imag.append (ival)
        Fmag.append (fval)
  if len(Imag) < 1:
    Imag.append (Iss)
    Fmag.append (Fss)

  return Imag, Fmag, Rmag

def AtpLoadXfmr(zb, v):
  if zb < 0.001:
    return '{:6.5f}{:6.5f}{:6.2f}'.format(0.01*zb, 0.02*zb, v)
  elif zb < 0.1:
    return '{:6.4f}{:6.4f}{:6.2f}'.format(0.01*zb, 0.02*zb, v)
  elif zb < 1.0:
    return '{:6.3f}{:6.3f}{:6.2f}'.format(0.01*zb, 0.02*zb, v)
  elif zb < 1000.0:
    return '{:6.2f}{:6.2f}{:6.2f}'.format(0.01*zb, 0.02*zb, v)
  elif zb < 100000.0:
    return '{:6.1f}{:6.1f}{:6.2f}'.format(0.01*zb, 0.02*zb, v)
  else:
    return ' 1.0E5 2.0E5{:6.2f}'.format(v)

def TheveninVoltage (vpu, deg, rpu, xpu, ppu, qpu):
  s = complex(ppu, qpu)
  z = complex(rpu, xpu)
  rad = deg / RAD_TO_DEG
  vt = complex(vpu*math.cos(rad), vpu*math.sin(rad))
  i = (s/vt).conjugate()
  vs = vt + z*i
# print ('TheveninVoltage')
# print (' ', s)
# print (' ', z)
# print (' ', deg, rad)
# print (' ', vt)
# print (' ', i)
# print (' ', vs)
  return abs(vs), cmath.phase(vs) * RAD_TO_DEG

solar_template = """$INCLUDE,IBR.PCH,{sbus},{sname} $$
  ,{vbase},{sbase},{ibase},{ppu},{qpu},{vpu},{theta}"""

def AppendSolar (bus, vbase, sbase, ibase, ppu, qpu, vpu, ap, ibr_count):
  sbus = AtpBus (bus)
  sname = 'IBR{:02d}'.format (ibr_count)
  print (solar_template.format(sbus=sbus, sname=sname,
                               vbase = AtpFit10 (vbase),
                               sbase = AtpFit10 (sbase),
                               ibase = AtpFit10 (ibase),
                               ppu = AtpFit10 (ppu),
                               qpu = AtpFit10 (qpu),
                               vpu = AtpFit10 (vpu),
                               theta = AtpFit10 (1.8)), 
         file=ap)

def AppendType14Generator (cn1id, bus, vbase, rmva, Xdp, Ra, icd, mw, mvar, ap, gsu_ang):
  vpu = 1.0
  vdeg = 0.0
  if icd is not None and cn1id in icd['EMTBusVoltageIC']['vals']:
    ic = icd['EMTBusVoltageIC']['vals'][cn1id]
    vpu = ic['vmag'] / vbase
    vdeg = ic['vdeg']
  vpu, deg = TheveninVoltage (vpu, deg, Ra, Xdp, mw/rmva, mvar/rmva)
  kv = vbase * 0.001
  zbase = kv * kv / rmva
  X1 = Xdp * zbase
  R1 = Ra * zbase
  X0 = X1
  R0 = R1
  vmag = vpu * kv * 1000.0 * SQRT2 / SQRT3
  vang = deg + gsu_ang

  genbus = GetNextScratchBus()
  bus = AtpBus(bus)

  print ('/SOURCE', file=ap)
  print ('C < n 1><>< Ampl.  >< Freq.  ><Phase/T0><   A1   ><   T1   >< TSTART >< TSTOP  >', file=ap)
  for ph in ['A', 'B', 'C']:
    print ('14{:s}  {:10.3f}{:10.3f}{:10.3f}{:s}{:10.3f}{:10.3f}'.format (AtpNode (genbus, ph), 
                                                                          vmag, 60.0, vang, 
                                                                          PadBlanks(20), -1.0, 9999.0), file=ap)
    vang -= 120.0
  print ('/BRANCH', file=ap)
  print ('C < n1 >< n2 ><ref1><ref2>< R  >< X  >< C  >', file=ap)
  print ('51{:5s}A{:5s}A            {:s}{:s}'.format (bus, genbus, AtpFit6 (R0), AtpFit6 (X0)), file=ap)
  print ('52{:5s}B{:5s}B            {:s}{:s}'.format (bus, genbus, AtpFit6 (R1), AtpFit6 (X1)), file=ap)
  print ('53{:5s}C{:5s}C'.format (bus, genbus), file=ap)
  return genbus

def AppendIBRInitializer (cn1id, bus, vbase, rmva, xpu, rpu, icd, mw, mvar, ap, gsu_ang):
  vpu = 1.0
  vdeg = 0.0
  if icd is not None and cn1id in icd['EMTBusVoltageIC']['vals']:
    ic = icd['EMTBusVoltageIC']['vals'][cn1id]
    vpu = ic['vmag'] / vbase
    vdeg = ic['vdeg']
  ppu = mw/rmva
  qpu = mvar/rmva
  vpu, vdeg = TheveninVoltage (vpu, vdeg, rpu, xpu, ppu, qpu)
  kv = vbase * 0.001
  zbase = kv * kv / rmva
  X1 = xpu * zbase
  R1 = rpu * zbase
  X0 = X1
  R0 = R1
  vmag = vpu * kv * 1000.0 * SQRT2 / SQRT3
  vang = vdeg + gsu_ang

  genbus = GetNextScratchBus()
  swtbus = GetNextScratchBus()
  bus = AtpBus(bus)

  print ('/SOURCE', file=ap)
  print ('C < n 1><>< Ampl.  >< Freq.  ><Phase/T0><   A1   ><   T1   >< TSTART >< TSTOP  >', file=ap)
  for ph in ['A', 'B', 'C']:
    print ('14{:s}  {:10.3f}{:10.3f}{:10.3f}{:s}{:10.3f}{:10.3f}'.format (AtpNode (genbus, ph), 
                                                                          vmag, 60.0, vang, 
                                                                          PadBlanks(20), -1.0, 9999.0), file=ap)
    vang -= 120.0
  print ('/SWITCH', file=ap)
  print ('C < n 1>< n 2>< Tclose ><Top/Tde ><   Ie   ><Vf/CLOP ><  type  >               1', file=ap)
  for ph in ['A', 'B', 'C']:
    print ('  {:6s}{:6s}{:10.3f}{:10.3f}'.format (AtpNode (swtbus, ph), AtpNode (bus, ph), -1.0, 0.020), file=ap)
  print ('/BRANCH', file=ap)
  print ('C < n1 >< n2 ><ref1><ref2>< R  >< X  >< C  >', file=ap)
  print ('51{:5s}A{:5s}A            {:s}{:s}'.format (genbus, swtbus, AtpFit6 (R0), AtpFit6 (X0)), file=ap)
  print ('52{:5s}B{:5s}B            {:s}{:s}'.format (genbus, swtbus, AtpFit6 (R1), AtpFit6 (X1)), file=ap)
  print ('53{:5s}C{:5s}C'.format (genbus, swtbus), file=ap)
  return genbus

def GetMachineDynamic (d, mach_id):
  for key, row in d.items():
    if mach_id == row['eqid']:
      return row
  return None

machine_dynamic_template = """$INCLUDE,SYNCMACH.PCH,{sbus},{sname} $$
  ,{rmva},{rkv},{agline},{s1d},{s2d},{vpk} $$
  ,{ang0},{ra},{xl},{xd},{xq},{xdp} $$
  ,{xqp},{xdpp},{xqpp},{tdop},{tqop},{tdopp} $$
  ,{tqopp},{x0},{rn},{xn},{xcan},{hico} $$
  ,{dsd} $$
  ,{ikv0},{kvini},{ifini},{ifnom} $$
  ,{kgov},{t2},{t1pt3},{t1t3},{pmax} $$
  ,{kc},{ilr},{klr},{vrmin},{vrmax} $$
  ,{v0pu},{ka},{ta},{tb},{tc},{tled} $$
  ,{tlag},{kfbk},{tfbk} $$
  ,{psk5},{psa1},{psa2},{pst3},{pst4},{pst5} $$
  ,{pst6},{vstmn},{vstmx}"""

def AppendMachineDynamics (bus, vpu, deg, mach, gov, exc, pss, ap, gsu_ang):
  global SM_COUNT
  sbus = AtpBus (bus)
  sname = 'SM{:03d}'.format (SM_COUNT)
  rmva = 1e-6 * mach['ratedS']
  rkv = 1e-3 * mach['ratedU']
  if USE_FIELD_SATURATION:
    agline = -1000.0
  else:
    agline = 1000.0
  ifini = 1.76 # 1.44673 # 1.76 # 0.0
  ifnom = abs(agline)
  s1d = 1.073 * abs(agline)
  s2d = 1.760 * abs(agline)
  vpk = 1000.0 * vpu * rkv * SQRT2 / SQRT3
  ang0 = deg + gsu_ang
  ra = mach['Ra']
  xl = mach['Xl']
  xd = mach['Xd']
  xq = mach['Xq']
  xdp = mach['Xdp']
  xqp = mach['Xqp']
  xdpp = mach['Xdpp']
  xqpp = mach['Xqpp']
  tdop = mach['Tdop']
  tqop = mach['Tqop']
  tdopp = mach['Tdopp']
  tqopp = mach['Tqopp']
  x0 = mach['Xl']  # REVISIT
  rn = 900.0 # 0.0
  xn = 65.0 # 0.0
  xcan = xl
  hico = rmva * MACHINE_J
  dsd = rmva * MACHINE_DSD
  ikv0 = 1.0 / vpu / rkv
  kvini = vpu * rkv
  kgov = gov['k1']
  t2 = gov['t2']
  t1t3 = gov['t1'] * gov['t3']
  t1pt3 = gov['t1'] + gov['t3']
  pmax = max (1.2, gov['pmax']) # pmin not used from CIM?
  kc = exc['kc'] # not using CIM kf, tb1, tc1, tf, vamax, vamin, vimax, vimin
  ilr = exc['ilr']
  klr = exc['klr']
  vrmin = abs(exc['vrmin'])
  vrmax = exc['vrmax']
  ka = exc['ka']
  v0pu = vpu + 1.0 / ka
  ta = max(exc['ta'],1e-9)
  tb = exc['tb']
  tc = exc['tc']
  tled = max(0.0,0.4)
  tlag = max(0.0,0.025)
  kfbk = 0.0
  tfbk = max(0.0,1.0)
  psk5 = pss['ks'] # t1 and t2 from CIM not used?
  psa1 = max(pss['a1'],2e-9)
  psa2 = max(pss['a2'],1e-18)
  pst3 = pss['t3']
  pst4 = pss['t4']
  pst5 = pss['t5']
  pst6 = max(pss['t6'],1e-9)
  vstmn = pss['vrmin']
  vstmx = pss['vrmax']
#  print ('58 at {:s}, V={:.2f} at {:.2f}, gov={:s}, exc={:s}, pss={:s}'.format(bus, vpu, deg+gsu_ang, gov['id'], exc['id'], pss['id']), file=ap)
  print (machine_dynamic_template.format(sbus=sbus,
                                         sname=sname,
                                         rmva = AtpFit10 (rmva),
                                         rkv = AtpFit10(rkv),
                                         agline = AtpFit10(agline),
                                         s1d = AtpFit10(s1d),
                                         s2d = AtpFit10(s2d),
                                         vpk = AtpFit10(vpk),
                                         ang0 = AtpFit10(ang0),
                                         ra = AtpFit10(ra),
                                         xl = AtpFit10(xl),
                                         xd = AtpFit10(xd),
                                         xq = AtpFit10(xq),
                                         xdp = AtpFit10(xdp),
                                         xqp = AtpFit10(xqp),
                                         xdpp = AtpFit10(xdpp),
                                         xqpp = AtpFit10(xqpp),
                                         tdop = AtpFit10(tdop),
                                         tqop = AtpFit10(tqop),
                                         tdopp = AtpFit10(tdopp),
                                         tqopp = AtpFit10(tqopp),
                                         x0 = AtpFit10(x0),
                                         rn = AtpFit10(rn),
                                         xn = AtpFit10(xn),
                                         xcan = AtpFit10(xcan),
                                         hico = AtpFit10(hico),
                                         dsd = AtpFit10(dsd),
                                         ikv0 = AtpFit6(ikv0),
                                         kvini = AtpFit10(kvini),
                                         ifini = AtpFit10(ifini),
                                         ifnom = AtpFit10(ifnom),
                                         kgov = AtpFit6(kgov),
                                         t2 = AtpFit10(t2),
                                         t1t3 = AtpFit10(t1t3),
                                         t1pt3 = AtpFit10(t1pt3),
                                         pmax = AtpFit6(pmax),
                                         kc = AtpFit6(kc),
                                         ilr = AtpFit10(ilr),
                                         klr = AtpFit10(klr),
                                         vrmin = AtpFit6(vrmin),
                                         vrmax = AtpFit6(vrmax),
                                         v0pu = AtpFit10(v0pu),
                                         ka = AtpFit6(ka),
                                         ta = AtpFit10(ta),
                                         tb = AtpFit10(tb),
                                         tc = AtpFit10(tc),
                                         tled = AtpFit10(tled),
                                         tlag = AtpFit10(tlag),
                                         kfbk = AtpFit10(kfbk),
                                         tfbk = AtpFit10(tfbk),
                                         psk5 = AtpFit6(psk5),
                                         psa1 = AtpFit10(psa1),
                                         psa2 = AtpFit10(psa2),
                                         pst3 = AtpFit10(pst3),
                                         pst4 = AtpFit10(pst4),
                                         pst5 = AtpFit10(pst5),
                                         pst6 = AtpFit10(pst6),
                                         vstmn = AtpFit6(vstmn),
                                         vstmx = AtpFit6(vstmx)), file=ap)

# parallel all machines at a bus, since they have identical controls and electrical parameters
# (this avoids need for FINISH and FINISH PART input of the individual machines in parallel)
# at the same time, assign initial conditions of P, Q, and voltage
def ParallelMachines (d, icd, atp_buses):
  par = {}
  bus_generators = {}
  for key, row in d.items():
    vbase = row['ratedU']
    bus = row['cn1id']
    ic = icd['EMTBranchFlowIC']['vals'][key]
    row['p'] = -ic['p'] # account for load convention of shunt power flows
    row['q'] = -ic['q']
    ic = icd['EMTBusVoltageIC']['vals'][bus]
    row['vpu'] = ic['vmag'] / vbase
    row['deg'] = ic['vdeg']
    if bus not in bus_generators:
      bus_generators[bus] = [key]
    else:
      bus_generators[bus].append(key)
  for bus, machines in bus_generators.items():
    if len(machines) < 2:
      key = machines[0]
      par[key] = d[key]
    else:
      parkey = '{:s}_{:d}EQG'.format(bus, len(machines))
      par[parkey] = d[machines[0]]
      for i in range(1, len(machines)):
        key = machines[i]
        row = d[key]
        for tag in ['ratedS', 'p', 'q', 'minP', 'maxP', 'minQ', 'maxQ']:
          par[parkey][tag] += row[tag]
  print ('Generator  Bus           MVA          P      Vpu     Vdeg')
  for key, row in par.items():
    print ('{:10s} {:6s} {:10.2f} {:10.2f} {:8.4f} {:8.4f}'.format (row['name'], 
                                                                    row['bus'], 
                                                                    row['ratedS']*1e-6, 
                                                                    row['p']*1e-6,
                                                                    row['vpu'], row['deg']))
  return par

# over-write the CIM power with initial conditions
def InitializeIBR (key, row, icd):
  if icd is not None and key in icd['EMTBranchFlowIC']['vals']:
    ic = icd['EMTBranchFlowIC']['vals'][key]
    row['p'] = -ic['p'] # accounting for the load convention of shunt power flow
    row['q'] = -ic['q']
    bus = row['cn1id']
    vbase = row['ratedU']
    ic = icd['EMTBusVoltageIC']['vals'][bus]
    row['vpu'] = ic['vmag'] / vbase
    row['deg'] = ic['vdeg']

def GetGSUPhaseShift (d, key, dxf):
  for plant, ary in d.items():
    for row in ary:
      if row['eqid'] == key:
        for eqs in d[plant]:
          if eqs['eqtype'] == 'PowerTransformer':
            winding_key = eqs['eqid'] + ':1'
            vgrp = dxf[winding_key]['vgrp']
            if vgrp == 'Yd1':
              return -30.0
            else:
              return 0.0
  return 0.0

def convert_one_atp_model (d, icd, fpath, case):
  """Export one BES network model to ATP.

  Writes a file ending in *_net.atp*, which references support files for machines,
  IBR, controls, and other components. An ATP user license is required for the
  support files, and to run a simulation on the *_net.atp* file. Also writes an
  *atpmap* file that maps CIM bus (ConnectivityNode) names to ATP bus numbers.

  Args:
    d (dict): loaded from rdflib
    icd (dict): power flow solution for initial conditions
    fpath (str): relative path for ATP netlist files
    case (dict): one of the CASES
  """
  global LOAD_MULT, DUM_NODES, LOAD_TOTAL, PV_COUNT, PV_TOTAL, SM_COUNT, SM_TOTAL, WND_COUNT, WND_TOTAL
  global DELIM, DR_COUNT, DR_TOTAL

  sys_id=case['id']
  fname=case['name']
  swingbus=case['swingbus']

  atp_buses = {}  # find the ATP bus number (as a string) from the CIM ConnectivityNode id
  cim_bus_ids = {}  # find the CIM ConnectivityNode id from the ATP bus number
  cim_bus_names = {} # find the CIM ConnectivityNode name from the ATP bus number
  bus_kv = {}     # nominal voltage (line-to-line kV) from the CIM ConnectivityNode id
  ordered_buses, atp_buses = emthub.build_bus_lists(d)
  idx = 1
  for key, data in ordered_buses.items():
    bus = str(idx)
    atp_buses[key] = bus
    cim_bus_ids[bus] = key
    cim_bus_names[key] = data['name']
    bus_kv[key] = 0.001 * data['nomv']
    idx += 1
  print ('Mapping {:d} buses to {:s}.atpmap'.format (idx-1, fname))
  fp = open (fpath + fname + '.atpmap', mode='w')
  print ('ATP Bus CIM Bus               CIM ID                                Bus kV', file=fp)
  for key in cim_bus_ids:
    cnid = cim_bus_ids[key]
    print ('{:6s}  {:20s}  {:36s} {:7.3f}'.format (key, cim_bus_names[cnid], cnid, bus_kv[cnid]), file=fp)
  print ('\nCIM Bus              ATP Bus  CIM ID                                Bus kV', file=fp)
  for key in atp_buses:
    print ('{:20s} {:6s}   {:36s} {:7.3f}'.format (cim_bus_names[key], atp_buses[key], key, bus_kv[key]), file=fp)
  fp.close()

  machines = ParallelMachines (d['EMTSyncMachine']['vals'], icd, atp_buses)

  ap = open (fpath + fname + '_net.atp', mode='w')
  print ('C file: {:s}, Load Mult={:.3f}'.format (fname, LOAD_MULT), file=ap)
  print ('$VINTAGE,0', file=ap)

  swing_id = emthub.get_swingbus_id (ordered_buses, swingbus)
  bus = atp_buses[swing_id]
  kv = bus_kv[swing_id]
  # define an "infinite bus" for the case with no machines
  x1pu_swing = 0.010
  r1pu_swing = 0.001
  mva_swing = 1000.0
  p_swing = 0.0
  q_swing = 0.0
  vmag = 1.0
  vang = 0.0
  gsu_ang = 0.0
  if len(machines) > 0: # find the swing bus
    for key, row in machines.items():
      if bus == atp_buses[row['cn1id']]:
        mva_swing = 1.0e-6 * row['ratedS']
        x1pu_swing = row['Xdp']
        r1pu_swing = row['Ra']
        vmag = row['vpu']
        vang = row['deg']
        p_swing = 1.0e-6*row['p']
        q_swing = 1.0e-6*row['q']
        gsu_ang = GetGSUPhaseShift (d['EMTRotatingMachinePlant*']['vals'], key, d['EMTPowerXfmrWinding']['vals']) 
        print ('Swing Generator {:.2f} MVA, {:.2f} MW, {:.2f} MVAR, X1={:.6f} pu, R1={:.6f} pu'.format(mva_swing, 
                                                                                                       p_swing, 
                                                                                                       q_swing, 
                                                                                                       x1pu_swing, 
                                                                                                       r1pu_swing))
        print ('   Swing bus V={:.4f} pu @ {:.3f} deg, GSU {:.3f} deg'.format (vmag, vang, gsu_ang))
        break

  zbase = kv * kv / mva_swing
  X1 = x1pu_swing * zbase
  R1 = r1pu_swing * zbase
  X0 = X1
  R0 = R1
  vmag, vang = TheveninVoltage (vmag, vang, r1pu_swing, x1pu_swing, p_swing/mva_swing, q_swing/mva_swing)
  vmag = vmag * kv * 1000.0 * SQRT2 / SQRT3
  vang = vang + gsu_ang
  print ('C =============================================================================', file=ap)
  print ('C Swing Bus {:s} at {:s}'.format (swingbus, bus), file=ap)
  print ('/SOURCE', file=ap)
  print ('C < n 1><>< Ampl.  >< Freq.  ><Phase/T0><   A1   ><   T1   >< TSTART >< TSTOP  >', file=ap)
  for ph in ['A', 'B', 'C']:
    print ('14{:s}  {:10.3f}{:10.3f}{:10.3f}{:s}{:10.3f}{:10.3f}'.format (AtpNode ('THEV', ph), 
                                                                          vmag, 60.0, vang, 
                                                                          PadBlanks(20), -1.0, 9999.0), file=ap)
    vang -= 120.0
  print ('/BRANCH', file=ap)
  print ('C < n1 >< n2 ><ref1><ref2>< R  >< X  >< C  >', file=ap)
  print ('51THEV_ASBUS_A            {:s}{:s}'.format (AtpFit6 (R0), AtpFit6 (X0)), file=ap)
  print ('52THEV_BSBUS_B            {:s}{:s}'.format (AtpFit6 (R1), AtpFit6 (X1)), file=ap)
  print ('53THEV_CSBUS_C', file=ap)
  print ('/SWITCH', file=ap)
  print ('C < n 1>< n 2>< Tclose ><Top/Tde ><   Ie   ><Vf/CLOP ><  type  >               1', file=ap)
  for ph in ['A', 'B', 'C']:
    print ('  {:6s}{:6s}{:10.3f}{:10.3f}                    MEASURING                1'.format (AtpNode ('SBUS', ph), 
      AtpNode (bus, ph), -1.0, TOPEN), file=ap)
  print ('/BRANCH', file=ap)

  # organize the balanced PowerTransformers, including fixed off-nominal taps
  PowerXfmrs = {}
  xfbusnum = 1
  for key, row in d['EMTPowerXfmrWinding']['vals'].items():
    pid = key.split(DELIM)[0]
    if pid in PowerXfmrs:
      PowerXfmrs[pid]['nwdg'] += 1
    else:
      PowerXfmrs[pid] = {'nwdg':1, 'taps': [], 'ends': []}
    PowerXfmrs[pid]['ends'].append (row['id'])
  #print (PowerXfmrs)
  for pid, row in PowerXfmrs.items():
    nwdg = row['nwdg']
    taps = row['taps']
    wdgs = []
    meshes = []
    for i in range(nwdg):
      # look for an off-nominal tap, which may not be present
      tap = 1.0
      key = row['ends'][i]
      if key in d['EMTXfmrTap']['vals']:
        tap = 1.0 + (d['EMTXfmrTap']['vals'][key]['svi']*d['EMTXfmrTap']['vals'][key]['step']) / 100.0
      taps.append (tap)
      # look for the mesh impedances, which must always be present
      wdgs.append (d['EMTPowerXfmrWinding']['vals']['{:s}{:s}{:d}'.format(pid, DELIM, i+1)])
      for j in range(i+1, nwdg):
        meshes.append (d['EMTPowerXfmrMesh']['vals']['{:s}{:s}{:s}'.format(row['ends'][i], DELIM, row['ends'][j])])
    print ('C =============================================================================', file=ap)
    print ('C transformer {:s}, {:d} windings from {:s}'.format (wdgs[0]['pname'], nwdg, wdgs[0]['bus']), file=ap)
    if nwdg > 3:
      print ('C *** too many windings for saturable transformer component', file=ap)
      print ('*** Transformer {:s} has {:d} windings, but only 2 or 3 supported'.format(pname, nwdg))
      continue
    Imag, Fmag, Rmag = AtpStarCore (wdgs, d, pid, case['UseXfmrSaturation'])
    xfbus = 'X' + str(xfbusnum)
    if wdgs[0]['conn'] == 'D':
      bEnd1Delta = True
    else:
      bEnd1Delta = False
    r, x, v = AtpStarEquivalent (wdgs, meshes, taps)
    for ph in ['A', 'B', 'C']:
      if ph == 'A':
        print ('C TRANSFORMER             <Imag><Fmag><BusT><Rmag>', file=ap)
        print ('  TRANSFORMER             {:s}{:s}{:s}{:s}'.format (AtpFit6 (Imag[0]), AtpFit6 (Fmag[0]), 
                                                                    AtpNode (xfbus, 'X'),
                                                                    AtpFit6 (Rmag)), file=ap)
        for idx in range(len(Imag)):
          print ('{:>16s}{:>16s}'.format (AtpFit6 (Imag[idx]), AtpFit6 (Fmag[idx])), file=ap)
        print ('            9999', file=ap)
        print ('C < n 1>< n 2><ref1><ref2><   R><   X><  KV>', file=ap)
        for i in range(nwdg):
          print ('{:s}{:s}{:s}'.format (AtpXfmrNodes(xfbus, i+1, wdgs[i], bEnd1Delta, ph, atp_buses), 
                                        PadBlanks(12), AtpXfmr (r[i], x[i], v[i])), file=ap)
      else:
        print ('  TRANSFORMER {:s}{:s}{:s}'.format (AtpNode (xfbus, 'X'), PadBlanks(18), 
                                                    AtpNode (xfbus, chr(ord(ph)+23))), file=ap)
        for i in range(nwdg):
          print ('{:s}'.format (AtpXfmrNodes(xfbus, i+1, wdgs[i], bEnd1Delta, ph, atp_buses)), file=ap)
    for i in range(nwdg):
      if wdgs[i]['conn'] == 'D':
        for ph in ['A', 'B', 'C']:
          print ('  {:s}                  1000.0         1.0'.format (AtpNode (atp_buses[wdgs[i]['cn1id']], ph)), file=ap)

    xfbusnum += 1

  for key, row in d['EMTLine']['vals'].items():
    bus1 = AtpBus(atp_buses[row['cn1id']])
    bus2 = AtpBus(atp_buses[row['cn2id']])
    rs = (row['r0']+2.0*row['r']) / 3.0
    rm = (row['r0']-row['r']) / 3.0
    xs = (row['x0']+2.0*row['x']) / 3.0
    xm = (row['x0']-row['x']) / 3.0
    cs = 1.0e6 * (row['b0']+2.0*row['b']) / 3.0 / OMEGA
    cm = 1.0e6 * (row['b0']-row['b']) / 3.0 / OMEGA
    if rs < 0.0 or rm < 0.0:
      print ('** Line', key, 'has negative resistance')
    # calculate the positive and negative Bergeron parameters
    bergeron = False
    km = 0.001*row['len']
    if cs > 0.0:
      r0p = (rs + 2*rm) / km
      l0 = (xs + 2*xm) / OMEGA
      c0 = 1.0e-6 * (cs + 2*cm)
      r1p = (rs - rm) / km
      l1 = (xs - xm) / OMEGA
      c1 = 1.0e-6 * (cs - cm)
      tau1 = math.sqrt(l1 * c1)
      tau0 = math.sqrt(l0 * c0)
      z1 = math.sqrt(l1/c1)
      z0 = math.sqrt(l0/c0)
      if min(tau0, tau1) >= MIN_BERGERON_TAU:
        bergeron = True
    print ('C =============================================================================', file=ap)
    print ('C line {:s} from {:s} to {:s}'.format (row['name'], row['bus1'], row['bus2']), file=ap)
    print ('C   per-instance sequence parameters for {:.2f}km'.format(km), file=ap)
    if bergeron:
      print ('$VINTAGE,1', file=ap)
      print ('C < n 1>< n 2>            <   R/LEN  ><     Z    ><   TAU    ><   LEN    > 2 0 0', file=ap)
      print ('-1{:5s}A{:5s}A            {:s} 2 0 0'.format (bus1, bus2, AtpRZTL(r0p, z0, tau0, km)), file=ap)
      print ('-2{:5s}B{:5s}B            {:s} 2 0 0'.format (bus1, bus2, AtpRZTL(r1p, z1, tau1, km)), file=ap)
      print ('-3{:5s}C{:5s}C'.format (bus1, bus2), file=ap)
      print ('$VINTAGE,0', file=ap)
    else:
      print ('$VINTAGE,1', file=ap)
      print ('C < n 1>< n 2><ref1><ref2><       R      ><      X       ><      C       ><   >', file=ap)
      print ('1 {:5s}A{:5s}A'.format (bus1, bus2) + PadBlanks(12) + AtpRXC(rs, xs, cs), file=ap)
      print ('2 {:5s}B{:5s}B'.format (bus1, bus2) + PadBlanks(12) + AtpRXC(rm, xm, cm), file=ap)
      print (PadBlanks(26) + AtpRXC(rs, xs, cs), file=ap)
      print ('3 {:5s}C{:5s}C'.format (bus1, bus2) + PadBlanks(12) + AtpRXC(rm, xm, cm), file=ap)
      print (PadBlanks(26) + AtpRXC(rm, xm, cm), file=ap)
      print (PadBlanks(26) + AtpRXC(rs, xs, cs), file=ap)
      print ('$VINTAGE,0', file=ap)

  if len(d['EMTDisconnectingCircuitBreaker']['vals']) > 0:
    nbrkr = 0
    print ('/SWITCH', file=ap)
    for key, row in d['EMTDisconnectingCircuitBreaker']['vals'].items():
      bus1 = AtpBus(atp_buses[row['cn1id']])
      bus2 = AtpBus(atp_buses[row['cn2id']])
      sClose = '_TCLOSE{:d}'.format (nbrkr).ljust (10, '_')
      sOpen = '_TOPEN{:d}'.format (nbrkr).ljust (10, '_')
      print ('C =============================================================================', file=ap)
      print ('C Breaker {:s} from {:s} to {:s} numbered {:d} for timing'.format (row['name'], row['bus1'], row['bus2'], nbrkr), file=ap)
      print ('C < n 1>< n 2>< Tclose ><Top/Tde ><   Ie   ><Vf/CLOP ><  type  >               1', file=ap)
      for ph in ['A', 'B', 'C']:
        print ('  {:6s}{:6s}{:10s}{:10s}                                             1'.format (AtpNode (bus1, ph), 
          AtpNode (bus2, ph), sClose, sOpen), file=ap)
#        print ('  {:6s}{:6s}{:10.3f}{:10.3f}                                             0'.format (AtpNode (bus1, ph), 
#          AtpNode (bus2, ph), -1.0, TOPEN), file=ap)
      nbrkr += 1
    print ('/BRANCH', file=ap)

  for key, row in d['EMTCompSeries']['vals'].items():
    bus1 = AtpBus(atp_buses[row['cn1id']])
    bus2 = AtpBus(atp_buses[row['cn2id']])
    if row['x'] > 0.0:
      print ('C =============================================================================', file=ap)
      print ('C series reactor {:s} from {:s} to {:s}'.format (row['name'], row['bus1'], row['bus2']), file=ap)
      print ('C < n1 >< n2 ><ref1><ref2>< R  >< X  >< C  >', file=ap)
      print ('51{:5s}A{:5s}A            {:s}{:s}'.format (bus1, bus2, AtpFit6 (row['r0']), AtpFit6 (row['x0'])), file=ap)
      print ('52{:5s}B{:5s}B            {:s}{:s}'.format (bus1, bus2, AtpFit6 (row['r']), AtpFit6 (row['x'])), file=ap)
      print ('53{:5s}C{:5s}C'.format(bus1, bus2), file=ap)
    else:
      cuf = -1.0e6 / row['x'] / OMEGA
      print ('C =============================================================================', file=ap)
      print ('C series capacitor {:s} from {:s} to {:s}'.format (row['name'], row['bus1'], row['bus2']), file=ap)
      print ('C < n1 >< n2 ><ref1><ref2>< R  >< X  >< C  >', file=ap)
      print ('  {:5s}A{:5s}A                        {:s}'.format (bus1, bus2, AtpFit6 (cuf)), file=ap)
      print ('  {:5s}B{:5s}B                        {:s}'.format (bus1, bus2, AtpFit6 (cuf)), file=ap)
      print ('  {:5s}C{:5s}C                        {:s}'.format (bus1, bus2, AtpFit6 (cuf)), file=ap)

  for key, row in d['EMTCompShunt']['vals'].items():
    kv = 0.001 * row['nomu']
    kvar = 1000.0 * row['bsection'] * row['sections'] * kv * kv
    if kvar > 0.0:
      cuf = 1000.0 * kvar / kv / kv / OMEGA
      bus = atp_buses[row['cn1id']]
      print ('C =============================================================================', file=ap)
      print ('C capacitor {:s} at {:s} is {:.2f} kVAR'.format (row['name'], row['bus'], kvar), file=ap)
      print ('C < n 1>< n 2><ref1><ref2><       R      ><      X       ><      C       ><   >', file=ap)
      print ('$VINTAGE,1', file=ap)
      for ph in GetAtpPhaseList ('ABC'):
        print ('  ' + AtpNode (bus, ph) + PadBlanks(50) + '{:16e}'.format(cuf), file=ap)
      print ('$VINTAGE,0', file=ap)
    elif kvar < 0.0:
      xshunt = -1000.0 * kv * kv / kvar
      bus = atp_buses[row['cn1id']]
      print ('C =============================================================================', file=ap)
      print ('C reactor {:s} at {:s} is {:.2f} kVAR'.format (row['name'], row['bus'], -kvar), file=ap)
      print ('C < n 1>< n 2><ref1><ref2><       R      ><      X       ><      C       ><   >', file=ap)
      print ('$VINTAGE,1', file=ap)
      for ph in GetAtpPhaseList ('ABC'):
        print ('  ' + AtpNode (bus, ph) + PadBlanks(34) + '{:16e}'.format(xshunt), file=ap)
      print ('$VINTAGE,0', file=ap)

  for key, row in d['EMTLoad']['vals'].items():
    bus = atp_buses[row['cn1id']]
    phases = GetAtpPhaseList ('ABC')
    nph = len(phases)
    kv = 0.001 * row['basev']
    kw = 0.001 * row['p'] * LOAD_MULT
    kvar = 0.001 * row['q'] * LOAD_MULT
    LOAD_TOTAL += 0.001 * kw
    if False: # row['conn'] == 'D':
      bDelta = True
      kvld = kv
    else:
      bDelta = False
      kvld = kv / SQRT3
    rload = nph * 1000.0 * kvld * kvld / kw
    if kvar != 0.0:
      xload = nph * 1000.0 * kvld * kvld / kvar
    else:
      xload = 0.0
    if rload < 0.0:
      print ('** Load', key, 'has negative resistance, write as DER')
      DR_COUNT += 1
      DUM_NODES += PV3_DUM_NODES
      vbase = row['basev']
      sbase = abs(row['p'])
      wtotal = sbase
      DR_TOTAL += 1e-6 * wtotal
      irmsmx = 1.1 * sbase / vbase / SQRT3
      vtrip = 0.5 * vbase / SQRT3
      pfang = 0.0
      sBus = AtpBus(bus) # '{:5s}'.format(bus).replace(' ', '#')
      sName = 'DR{:03d}'.format (DR_COUNT)
      sW = AtpFit6 (wtotal)
      sImax = AtpFit6 (irmsmx)
      sUV = AtpFit6 (vtrip)
      sUT = AtpFit6 (0.16)
      sV0 = AtpFit6 (vbase)
      sV02 = AtpFit6 (vbase*vbase)
      sVWc = AtpFit6 (vbase/376.9911)
      sPF = AtpFit6 (pfang)
      print ('C =============================================================================', file=ap)
      print ('C DER {:s} at {:s} is {:.2f} MVA producing {:.2f} MW'.format (row['name'], row['bus'], 1e-6*sbase, 1e-6*wtotal), file=ap)
      print ('$INCLUDE,TACSPV3.PCH,{:s},{:s},{:s},{:s},{:s},{:s},{:s} $$'.format(sBus, sName, sW, sImax, sUV, sUT, sPF), file=ap)
      print ('  ,{:s},{:s},{:s}'.format(sV0, sV02, sVWc), file=ap)
      print ('/BRANCH', file=ap)
    else:
      print ('C =============================================================================', file=ap)
      print ('C load {:s} at {:s} is {:.3f} + j{:.3f} kVA'.format (row['name'], row['bus'], kw, kvar), file=ap)
      print ('C < n 1>< n 2><ref1><ref2><       R      ><      X       ><      C       ><   >', file=ap)
      print ('$VINTAGE,1', file=ap)
      for ph in phases:
        bus_from = AtpNode (bus, ph)
        bus_to = AtpLoadTo (bus, ph, bDelta)
        print ('  ' + bus_from + bus_to + PadBlanks(12) + '{:16e}'.format(rload), file=ap)
        if xload > 0.0:
          print ('  ' + bus_from + bus_to + PadBlanks(28) + '{:16e}'.format(xload), file=ap)
        elif xload < 0.0:
          cuf = -1.0e6 / xload / OMEGA
          print ('  ' + bus_from + bus_to + PadBlanks(44) + '{:16e}'.format(cuf), file=ap)
      print ('$VINTAGE,0', file=ap)

  # dictionary of generators to track ratings and initial conditions
  dgens = {}

  for key, row in d['EMTSolar']['vals'].items():
    gsu_ang = GetGSUPhaseShift (d['EMTIBRPlant*']['vals'], key, d['EMTPowerXfmrWinding']['vals'])
    bus = atp_buses[row['cn1id']]
    phases = GetAtpPhaseList ('ABC')
    nph = len(phases)
    vbase = row['ratedU']
    sbase = row['ratedS']
    InitializeIBR (key, row, icd)
    wtotal = row['p'] * 1.0 # PV_MULT
    PV_TOTAL += 1e-6 * wtotal
    PV_COUNT += 1
    pfang = 0.0
    if row['q'] != 0.0:
      if wtotal != 0.0:
        pfang = math.atan2(row['q'], wtotal) * RAD_TO_DEG
    vtrip = 0.5 * vbase / SQRT3
    if nph == 1:
      vbase /= SQRT3
      irmsmx = row['ipu'] * sbase / vbase
    elif nph == 2:
      vtrip = 0.5 * vbase
      irmsmx = row['ipu'] * sbase / vbase
    else:
      irmsmx = row['ipu'] * sbase / vbase / SQRT3
    sBus1 = AtpNode (bus, phases[0]).replace(' ', '#')
    sName = 'PV{:03d}'.format (PV_COUNT)
    sW = AtpFit6 (wtotal)
    sImax = AtpFit6 (irmsmx)
    sUV = AtpFit6 (vtrip)
    sUT = AtpFit6 (0.16)
    if (abs(pfang) < 0.001) or (abs(pfang) > 100.0) or (pfang < 0.0):  # TODO: verify
      pfang = 0.0
    sPF = AtpFit6 (pfang)
    rmva = sbase*1e-6
    mw = wtotal*1e-6
    mvar = row['q']*1e-6
    print ('C =============================================================================', file=ap)
    print ('C solar {:s} at {:s} is {:.3f} MVA producing {:.3f} MW and {:.3f} Mvar'.format (row['name'], row['bus'], rmva, mw, mvar), file=ap)
    AppendSolar (bus, vbase, sbase, ibase=sbase/vbase, ppu=wtotal/sbase, qpu=row['q']/sbase, vpu=1.0, ap=ap, ibr_count=PV_COUNT+WND_COUNT)
    AppendIBRInitializer (row['cn1id'], bus, vbase, rmva, 0.2, 0.0, icd, mw, mvar, ap, gsu_ang)
    dgens[key] = {'Type':'Solar', 'Source':None, 'Name':row['name'], 'Bus':AtpBus(bus), 'kV': vbase*0.001, 'S': sbase*1e-6, 'P':0.0, 'Q':0.0, 'Vmag':0.0, 'Vang':0.0}
    DUM_NODES += SOLAR_DUM_NODES

  for key, row in d['EMTWind']['vals'].items():
    gsu_ang = GetGSUPhaseShift (d['EMTIBRPlant*']['vals'], key, d['EMTPowerXfmrWinding']['vals'])
    bus = atp_buses[row['cn1id']]
    phases = GetAtpPhaseList ('ABC')
    nph = len(phases)
    vbase = row['ratedU']
    sbase = row['ratedS']
    InitializeIBR (key, row, icd)
    wtotal = row['p'] * 1.0 # PV_MULT
    rmva = sbase*1e-6
    mw = wtotal*1e-6
    mvar = row['q']*1e-6
    WND_TOTAL += 1e-6 * wtotal
    WND_COUNT += 1
    print ('C =============================================================================', file=ap)
    print ('C wind {:s} at {:s} is {:.3f} MVA producing {:.3f} MW and {:.3f} Mvar'.format (row['name'], row['bus'], rmva, mw, mvar), file=ap)
    AppendSolar (bus, vbase, sbase, ibase=sbase/vbase, ppu=wtotal/sbase, qpu=row['q']/sbase, vpu=1.0, ap=ap, ibr_count=PV_COUNT+WND_COUNT)
    AppendIBRInitializer (row['cn1id'], bus, vbase, rmva, 0.2, 0.0, icd, mw, mvar, ap, gsu_ang)
    dgens[key] = {'Type':'Wind', 'Source':None, 'Name':row['name'], 'Bus':AtpBus(bus), 'kV': vbase*0.001, 'S': sbase*1e-6, 'P':0.0, 'Q':0.0, 'Vmag':0.0, 'Vang':0.0}
    DUM_NODES += WIND_DUM_NODES

  ic_idx = 0
  if len(machines) > 0: # ATP requires these come after all other sources
    lastKey = list(machines.keys())[-1]
    for key, row in machines.items():
      gsu_ang = GetGSUPhaseShift (d['EMTRotatingMachinePlant*']['vals'], key, d['EMTPowerXfmrWinding']['vals'])
      bus = atp_buses[row['cn1id']]
      phases = GetAtpPhaseList ('ABC')
      nph = len(phases)
      vbase = row['ratedU']
      sbase = row['ratedS']
      rmva = 1e-6 * sbase
      mw = 1.0e-6 * row['p']
      mvar = 1.0e-6 * row['q']
      SM_TOTAL += mw
      SM_COUNT += 1
      if row['Ra'] < 0.0:
        print ('** Machine', key, 'has negative resistance')
      if row['bus'] == swingbus:
        print ('C =============================================================================', file=ap)
        print ('C SyncMachine {:s} at {:s} is {:.2f} MVA, part of Swing Bus'.format (row['name'], row['bus'], rmva), file=ap)
      else:
        print ('C =============================================================================', file=ap)
        print ('C SyncMachine {:s} at {:s} is {:.2f} MVA, {:.2f} MW, {:.2f} MVAR'.format (row['name'], row['bus'], rmva, mw, mvar), file=ap)
        if USE_TYPE_14_MACHINES: #  or (key != lastKey):
          genbus = AppendType14Generator (row['cn1id'], bus, vbase, rmva, row['Xdp'], row['Ra'], icd, mw, mvar, ap, gsu_ang)
          dgens[key] = {'Type':'SyncMach', 'Source':'14', 'Name':row['name'], 'Bus':genbus, 'kV': vbase*0.001, 'S': sbase*1e-6, 'P':0.0, 'Q':0.0, 'Vmag':0.0, 'Vang':0.0}
        else:
          gov = GetMachineDynamic (d['EMTGovSteamSGO']['vals'], key)
          exc = GetMachineDynamic (d['EMTExcST1A']['vals'], key)
          pss = GetMachineDynamic (d['EMTPssIEEE1A']['vals'], key)
          AppendMachineDynamics (bus=bus, vpu=row['vpu'], deg=row['deg'], mach=row, gov=gov, exc=exc, pss=pss, ap=ap, gsu_ang=gsu_ang)
          DUM_NODES += MACHINE_DUM_NODES
          dgens[key] = {'Type':'SyncMach', 'Source':'59', 'Name':row['name'], 'Bus':AtpBus(bus), 'kV': vbase*0.001, 'S': sbase*1e-6, 'P':0.0, 'Q':0.0, 'Vmag':0.0, 'Vang':0.0}
    print ('/BRANCH', file=ap)

  ap.close()
  with open('{:s}{:s}_dgen.json'.format(fpath, fname), 'w') as jp: 
    json.dump(dgens, jp)

  print ('Wrote {:s}_net.atp to {:s}'.format(fname, fpath))
  print ('  Total Load = {:.2f} MW, PV = {:.2f} MW, Wind = {:.2f} MW, SyncMach={:.2f} MVA, DER={:.2f} MW'.format (LOAD_TOTAL, PV_TOTAL, WND_TOTAL, SM_TOTAL, DR_TOTAL))
  print ('  Wrote {:d} transformers; limit of X bus numbers is 9999'.format(xfbusnum-1))
  print ('  Wrote {:d} PV, {:d} Wind, {:d} Equiv SyncMach, {:d} DER'.format (PV_COUNT, WND_COUNT, SM_COUNT, DR_COUNT))
  print ('  Estimated {:d} TACS dummy nodes, limit is {:d}'.format (DUM_NODES, DUM_NODE_LIMIT))

if __name__ == '__main__':
  idx = 0
  if len(sys.argv) > 1:
    idx = int(sys.argv[1])
  case = cim_examples.CASES[idx]

  g = rdflib.Graph()
  fname = case['ttlfile']
  g.parse (fname)
  print ('read', len(g), 'statements from', fname)
  d = emthub.load_emt_dict (g, case['id'], bTiming=True)
  for key in ['EMTBaseVoltage']: #, 'EMTIBRPlant*', 'EMTRotatingMachinePlant*']:
    emthub.list_dict_table (d, key)

  icd = None
  if 'ttl_ic' in case and os.path.exists(case['ttl_ic']):
    g = rdflib.Graph()
    fname = case['ttl_ic']
    g.parse (fname)
    print ('read', len(g), 'initial condition statements from', fname)
    icd = emthub.load_ic_dict (g)
    #emthub.list_dict_table (icd, 'EMTBusVoltageIC')

  reset_globals (case)
  convert_one_atp_model (d, icd, fpath = '../atp/data/', case=case)

