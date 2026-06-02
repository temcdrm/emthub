# Copyright (C) 2026 Meltran, Inc

import sys
import json
import uuid
import os

NERC_deprecated = ['GENROU']
NERC_prohibited = ['GENCLS', 'GENSAL', 'GAST', 'SEXS', 'IEESGO', 'REECB1']
WECC_names = ['REGCA1', 'REECA1', 'REECB1', 'REPCA1', 'WTDTA1', 'WTARA1']

infile = '../src/emthub/queries/dyr_mapping.json'
defaults = '../src/emthub/queries/dynamics_defaults.json'
outfile = '../src/emthub/queries/detailed_model_types.json'

def Get_CIM_Defaults (att, df):
  val = ''
  units = ''
  if att is not None:
    toks = att.split('.')
    if toks[0] in df:
      if toks[1] in df[toks[0]]:
        val = df[toks[0]][toks[1]][0]
        units = df[toks[0]][toks[1]][1]
  return val, units

def new_mRID ():
  return str(uuid.uuid4()).upper()

def Get_mRID (name, old):
  if name in old:
    if len(old[name]) > 35:
      return old[name]
  return new_mRID()

def get_status_kind (key):
  if key in NERC_deprecated:
    return 'deprecated'
  if key in NERC_prohibited:
    return 'prohibited'
  return 'allowed'

def get_name_kind (key):
  if key in WECC_names:
    return 'WECC'
  return 'PSSE'

def get_model_kind (key):
  if 'GOV' in key:
    return 'turbineGovernor'
  if key.startswith('GEN'):
    return 'machine'
  if key.startswith('WT') or key.startswith('RE'):
    return 'renewableEnergyResource'
  if 'EX' in key:
    return 'excitationSystem'
  return '** TBD **'

if __name__ == '__main__':
  with open (infile, 'r') as file:
    d1 = json.load (file)
  with open (defaults, 'r') as file:
    df = json.load (file)

  if os.path.exists(outfile):
    print ('reading from', outfile)
    with open (outfile, 'r') as file:
      d2 =json.load (file)
  else:
    print ('creating new', outfile)
    d2 = {}

  for key, row in d1.items():
    print (key, row['CIMclass'], len(row['parameters_after_ID']))
    if key not in d2:
      d2[key] = {'mRID': new_mRID(), 
                 'description': '', 
                 'modelKind': get_model_kind(key),
                 'parameterDescriptors': []}
    d2[key]['closestStandardModel'] = row['CIMclass']
    d2[key]['nameKind'] = get_name_kind(key)
    # modelKind is likely to have manual edits, so don't overwrite it
    # d2[key]['modelKind'] = get_model_kind(key)
    d2[key]['statusKind'] = get_status_kind(key)

    # add and update parameterDescriptors, attempting to preserve the mRIDs
    old_mRIDs = {}
    if 'parameterDescriptors' in d2[key]:
      pda = d2[key]['parameterDescriptors']
      for i in range(len(pda)):
        old_mRIDs[pda[i]['name']] = pda[i]['mRID']
    # start over with everything besides the mRIDs
    # first 3 parameters are the same for all dyr models
    d2[key]['parameterDescriptors'] = [
      {'name':'Bus', 'mRID':Get_mRID ('Bus', old_mRIDs), 'typicalValue':'', 'engineeringUnits':'Integer', 'sequenceNumber':1},
      {'name':'Model', 'mRID':Get_mRID ('Model', old_mRIDs), 'typicalValue':'', 'engineeringUnits':'String', 'sequenceNumber':2},
      {'name':'ID', 'mRID':Get_mRID ('ID', old_mRIDs), 'typicalValue':'1', 'engineeringUnits':'String', 'sequenceNumber':3}]
    pda = d2[key]['parameterDescriptors']
    for i in range(len(row['parameters_after_ID'])):
      prm = row['parameters_after_ID'][i]
      val, units = Get_CIM_Defaults (prm['cim'], df)
      pda.append({'name': prm['dyr'],
                  'mRID': Get_mRID (prm['dyr'], old_mRIDs), 
                  'typicalValue': val,
                  'engineeringUnits': units,
                  'sequenceNumber': i+4})

  jp = open (outfile, 'w')
  json.dump (d2, jp, indent=2)
  jp.close()

