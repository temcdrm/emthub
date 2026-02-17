# Copyright (C) 2026 Meltran, Inc

import sys
import json

classes = ['SynchronousMachineSimplified', 'SynchronousMachineTimeConstantReactance',
           'RotatingMachineDynamics', 'DynamicsFunctionBlock', 'PowerSystemStabilizerDynamics',
           'WeccDynamics', 'TurbineGovernorDynamics', 'ExcitationSystemDynamics',
           'GovGAST', 'GovHydro1', 'Pss1A', 'ExcST1A', 'PssIEEE1A', 'OverexcLimX2', 
           'GovSteam0', 'ExcIEEEDC1A', 'ExcSEXS', 'GovSteamSGO', 'WeccREECA', 'WeccREECB',
           'WeccREGCA', 'WeccREPCA', 'WeccWTGTA', 'WeccWTGARA']

infile = 'profile_attributes.json'
outfile = '../src/emthub/queries/dynamics_defaults.json'

if __name__ == '__main__':
  with open (infile, 'r') as file:
    d1 = json.load (file)
  with open (outfile, 'r') as file:
    d2 = json.load (file)

  print ('\n{:40s} {:6s} {:6s}\n'.format ('Class to Merge Found in:', 'Atts', 'Dflts'))
  for cls in classes:
    bFound1 = cls in d1
    bFound2 = cls in d2
    print ('{:40s} {:6s} {:6s}'.format(cls, str(bFound1), str(bFound2)))
    if bFound1 and not bFound2:
      d2[cls] = {}
      bFound2 = True
      print ('** Added', cls)
    if bFound1 and bFound2:
      target = d2[cls]
      for key, val in d1[cls].items():
        if key not in target:
          #print ('  new data {:s}={:s}, {:s}'.format (key, str(val['default']), val['type']))
          d2[cls][key] = [val['default'], val['type']]

  jp = open (outfile, 'w')
  json.dump (d2, jp, indent=2)
  jp.close()

