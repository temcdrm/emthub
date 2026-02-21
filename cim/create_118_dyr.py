# Copyright (C) 2026 Meltran, Inc

import cim_examples 
import emthub.api as emthub

if __name__ == '__main__':
  case = cim_examples.CASES[1]

  tables, kvbases, bus_kvbases, baseMVA = emthub.load_psse_rawfile (case['rawfile'])
  #emthub.print_psse_table (tables, 'GENERATOR')

  for row in tables['GENERATOR']['data']:
    if row[7] < 1:
      continue
    bus = str(row[0])
    gen_id = row[1].strip()
    mvabase = row[6]
    key = '{:s}_{:s}'.format(bus, gen_id)
    gen_fuel = 'Thermal'
    gen_type = 'SynchronousMachine'
    dynamics = ['SynchronousMachineTimeConstantReactance', 'ExcIEEEDC1A', 'PssIEEE1A', 'GovSteam0']
    if key in case['solar_units']:
      gen_fuel = 'Solar'
      gen_type = 'PowerElectronicsConnection'
      dynamics = ['WeccREECA', 'WeccREGCA', 'WeccREPCA']
    elif key in case['wind_units']:
      gen_fuel = 'Wind'
      gen_type = 'PowerElectronicsConnection'
      dynamics = ['WeccREECA', 'WeccREGCA', 'WeccREPCA', 'WeccWTGARA', 'WeccWTGTA']
    elif key in case['hydro_units']:
      gen_fuel = 'Hydro'
      dynamics = ['SynchronousMachineTimeConstantReactance', 'ExcIEEEDC1A', 'PssIEEE1A', 'GovHydro1']
    elif key in case['nuclear_units']:
      gen_fuel = 'Nuclear'
      dynamics = ['SynchronousMachineTimeConstantReactance', 'ExcIEEEDC1A', 'PssIEEE1A', 'GovSteam0']
    print (key, gen_fuel, gen_type, dynamics, mvabase, 'MVA')

