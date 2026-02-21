# Copyright (C) 2026 Meltran, Inc

import cim_examples 
import emthub.api as emthub
import math

def lookup_cim_default (cls_att, defaults):
  val = 0
  if cls_att is None:
    return val
  toks = cls_att.split('.')
  cls = toks[0]
  att = toks[1]
  if cls in defaults:
    if att in defaults[cls]:
      cim_type = defaults[cls][att][1]
      val = defaults[cls][att][0]
      if cim_type == 'Boolean':
        val = int(val)
      elif val == 'rotorAngularFrequencyDeviation':
        val = 1
  return val

if __name__ == '__main__':
  case = cim_examples.CASES[1]
  fp = open (case['dyrfile'], 'w')

  tables, kvbases, bus_kvbases, baseMVA = emthub.load_psse_rawfile (case['rawfile'])
  dyn_map = emthub.load_dynamics_mapping (bReverseLookup=False)
  defaults = emthub.load_dynamics_defaults ()
  #print (defaults)
  #print (dyn_map)
  #emthub.print_psse_table (tables, 'GENERATOR')

  for dyn in ['GENROU', 'EXST1', 'IEEEST', 'IEESGO', 'HYGOV', 'REECA1', 'REGCA1', 'REPCA1', 'WTARA1', 'WTDTA1']:
    parms = ''
    for col in dyn_map[dyn]['parameters_after_ID']:
      parms += ' {:s}'.format(col['dyr'])
    print ('// Bus {:s} ID'.format (dyn), parms, file=fp)
  print ('//', file=fp)

  for row in tables['GENERATOR']['data']:
    if row[7] < 1:
      continue
    bus = str(row[0])
    gen_id = row[1].strip()
    mvabase = row[6]
    key = '{:s}_{:s}'.format(bus, gen_id)
    gen_fuel = 'Thermal'
    gen_type = 'SynchronousMachine'
    dynamics = ['GENROU', 'EXST1', 'IEEEST', 'IEESGO']
    if key in case['solar_units']:
      gen_fuel = 'Solar'
      gen_type = 'PowerElectronicsConnection'
      dynamics = ['REECA1', 'REGCA1', 'REPCA1']
    elif key in case['wind_units']:
      gen_fuel = 'Wind'
      gen_type = 'PowerElectronicsConnection'
      dynamics = ['REECA1', 'REGCA1', 'REPCA1', 'WTARA1', 'WTDTA1']
    elif key in case['hydro_units']:
      gen_fuel = 'Hydro'
      dynamics = ['GENROU', 'EXST1', 'IEEEST', 'HYGOV']
    elif key in case['nuclear_units']:
      gen_fuel = 'Nuclear'
      dynamics = ['GENROU', 'EXST1', 'IEEEST', 'IEESGO']

    for dyn in dynamics:
      cls = dyn_map[dyn]['CIMclass']
      if cls == 'WeccWTGTA': # an ugly special case
        ht = defaults[cls]['ht'][0]
        hg = defaults[cls]['hg'][0]
        kshaft = defaults[cls]['kshaft'][0]
        dshaft = defaults[cls]['dshaft'][0]
        damp = 0.0
        h = ht + hg
        htfrac = ht / h
        freq1 = math.sqrt(kshaft*h/2/ht/hg) / 2 / math.pi
        parms = '{:.6g} {:.1f} {:.6g} {:.6g} {:.6g}'.format (h, damp, htfrac, freq1, dshaft)
      else:
        parms = ''
        for col in dyn_map[dyn]['parameters_after_ID']:
          att = col['cim']
          val = lookup_cim_default (att, defaults)
          parms += ' {:s}'.format (str(val))
      print ('{:4s} {:6s} {:4s}'.format (bus, dyn, gen_id), parms, '/', file=fp)
    print ('//', file=fp)

    #print (key, gen_fuel, gen_type, dynamics, mvabase, 'MVA')
  fp.close()

