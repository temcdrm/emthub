# Copyright (C) 2025 Meltran, Inc

import json
import textwrap

if __name__ == '__main__':
  with open('dynamics_defaults.json', 'r') as file:
    dyn_settings = json.load (file)

  # to add manually, because they are not included in default settings:
  #   GovSteamSGO.mwbase
  for key in ['ExcST1A', 'GovSteamSGO', 'PssIEEE1A', 'WeccREECA', 'WeccREPCA', 'WeccREGCA', 'WeccWTGARA', 'WeccWTGTA']:
    tab = dyn_settings[key]
    fields = list(tab.keys())
    print ('\n# EMT{:s}'.format (key))
    field_str = ' ?'.join (fields)
    select_str = 'SELECT ?name ?{:s} ?id ?eqid ?sysid WHERE {{'.format (field_str)
#    print (key, fields)
    print (textwrap.fill (select_str, width=80))
    print ('# VALUES ?sysid {"1783D2A8-1204-4781-A0B4-7A73A2FA6038"^^c:String}')
    print (' VALUES ?sysid {"2540AF5C-4F83-4C0F-9577-DEE8CC73BBB3"^^c:String}')
    print (' ?sys c:IdentifiedObject.mRID ?sysid.')
    print (' ?s r:type c:{:s}.'.format (key))
    # find the connected ConductingEquipment, based on the class of dynamics
    if key.startswith ('Exc'):
      print (' ?s c:ExcitationSystemDynamics.SynchronousMachineDynamics ?dyn.')
      print (' ?dyn c:SynchronousMachineDynamics.SynchronousMachine ?eq.')
    elif key.startswith ('Gov'):
      print (' ?s c:TurbineGovernorDynamics.SynchronousMachineDynamics ?dyn.')
      print (' ?dyn c:SynchronousMachineDynamics.SynchronousMachine ?eq.')
    elif key.startswith ('Pss'):
      print (' ?s c:PowerSystemStabilizerDynamics.ExcitationSystemDynamics ?exc.')
      print (' ?exc c:ExcitationSystemDynamics.SynchronousMachineDynamics ?dyn.')
      print (' ?dyn c:SynchronousMachineDynamics.SynchronousMachine ?eq.')
    elif key.startswith ('Wecc'):
      print (' ?s c:WeccDynamics.PowerElectronicsConnection ?eq.')
    else:
      print ('**** UNKNOWN class of connection')
    print (' ?eq c:Equipment.EquipmentContainer ?sys.')
    print (' ?eq c:IdentifiedObject.mRID ?eqid.')
    print (' ?s r:type c:{:s}.'.format (key))
    print (' ?s c:IdentifiedObject.name ?name.')
    print (' ?s c:IdentifiedObject.mRID ?id.')
    for fld in fields:
      print (' ?s c:{:s}.{:s} ?{:s}.'.format (key, fld, fld))
    print ('} ORDER BY ?name')


