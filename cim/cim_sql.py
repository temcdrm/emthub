# Copyright (C) 2025 Meltran, Inc

import time
import sys
import sqlite3

PREFIX = None
DELIM = ':'

CASES = [
  {'id': '1783D2A8-1204-4781-A0B4-7A73A2FA6038', 
   'name': 'IEEE118', 
   'rawfile':'raw/ieee-118-bus-v4.raw', 'xmlfile':'ieee118.xml', 'locfile': 'raw/ieee118_network.json', 'mridfile':'raw/ieee118mrids.dat', 'ttlfile': 'ieee118.ttl',
   'wind_units': ['132_W', '136_W', '138_W', '168_W', '180_W'],
   'solar_units': ['126_S', '128_S', '130_S', '140_S', '149_S', 
                   '151_S', '159_S', '165_S', '175_S', '179_S', 
                   '183_S', '185_S', '188_S', '191_S'],
   'hydro_units': [], 'nuclear_units': [],   
   'bus_ic': 'c:/src/cimhub/bes/ieee118mb.txt',
   'gen_ic': 'c:/src/cimhub/bes/ieee118mg.txt',
   'swingbus':'131', 
   'load': 0.6748},
  {'id': '2540AF5C-4F83-4C0F-9577-DEE8CC73BBB3', 
   'name': 'WECC240',
   'rawfile':'raw/240busWECC_2018_PSS.raw', 'xmlfile':'wecc240.xml', 'locfile': 'raw/wecc240_network.json', 'mridfile':'raw/wecc240mrids.dat', 'ttlfile': 'wecc240.ttl',
   'wind_units': ['1032_S', '1034_W', '1333_S', '2130_G', '2332_S', 
                  '2431_S', '2434_S', '2438_RG', '2438_SW', '2439_S'],
   'solar_units': ['2533_S', '2631_S', '3234_NW', '3433_S', '3835_NG', 
                   '3932_S', '3933_CG', '3933_NB', '4031_H', '4031_S', 
                   '4035_C', '4039_W', '4131_W', '4232_H', '5032_C', 
                   '5032_W', '6132_H', '6132_W', '6235_H', '6333_W', 
                   '6433_W', '6533_C', '6533_G', '7031_P', '7032_G'],
   'hydro_units': ['1232_H', '1331_H', '2130_H', '2637_H', '2638_H', 
                   '4035_H', '4039_H', '4131_H', '4132_H', '4231_H', 
                   '5031_H', '6335_H', '6533_H', '7032_H', '8033_H', 
                   '8034_H'],
   'nuclear_units': ['1431_N', '4132_N'],
   'bus_ic': 'c:/src/cimhub/bes/wecc240mb.txt',
   'gen_ic': 'c:/src/cimhub/bes/wecc240mg.txt',
   'swingbus':'2438', 
   'load': 1.0425}
]

def list_dict_table(dict, tag):
  tbl = dict[tag]
  print ('\n{:s}: key,{:s}'.format(tag, str(tbl['columns'])))
  for key, row in tbl['vals'].items():
    print ('  {:s},{:s}'.format (key, ','.join(str(row[c]) for c in tbl['columns'])))

def load_one_dict (cur, cols, sql):
  d = {}
  d['columns'] = cols
  d['vals'] = {}
  vals = d['vals']
  for row in cur.execute (sql):
    vals[row[0]] = {}
    rvals = vals[row[0]]
    for i in range(len(cols)):
      rvals[cols[i]] = row[i+1]
  return d

def load_sql_emt_dict (db_file, sysid):  # TODO: filter on sysid
  dict = {}

  con = sqlite3.connect (db_file)
  cur = con.cursor()

  dict['EquipmentContainer'] = load_one_dict (cur, ['name'], 
    'SELECT eq.mRID, io.name from EquipmentContainer as eq INNER JOIN IdentifiedObject as io ON eq.mRID = io.mRID')
  dict['BaseVoltage'] = load_one_dict (cur, ['name', 'nominalVoltage'], 
    'SELECT io.mRID, io.name, bv.nominalVoltage from BaseVoltage as bv INNER JOIN IdentifiedObject as io ON bv.mRID = io.mRID')
  dict['ConnectivityNode'] = load_one_dict (cur, ['name', 'container'], 
    'SELECT io.mRID, io.name, cn.ConnectivityNodeContainer from ConnectivityNode as cn INNER JOIN IdentifiedObject as io ON cn.mRID = io.mRID')
  dict['ACLineSegment'] = load_one_dict (cur, ['name', 'from', 'to', 'r1', 'x1', 'b1ch', 'r0', 'x0', 'b0ch', 'length'], 
    'SELECT io.mRID, io.name, eq.FromConnectivityNode, eq.ToConnectivityNode, ac.r, ac.x, ac.bch, ac.r0, ac.x0, ac.b0ch, cd.length from ACLineSegment as ac INNER JOIN IdentifiedObject as io ON ac.mRID = io.mRID INNER JOIN Conductor as cd on ac.mRID = cd.mRID INNER JOIN ConductingEquipment as eq on ac.mRID = eq.mRID')
  dict['SeriesCompensator'] = load_one_dict (cur, ['name', 'from', 'to', 'r1', 'x1', 'r0', 'x0'], 
    'SELECT io.mRID, io.name, eq.FromConnectivityNode, eq.ToConnectivityNode, sc.r, sc.x, sc.r0, sc.x0 from SeriesCompensator as sc INNER JOIN IdentifiedObject as io ON sc.mRID = io.mRID INNER JOIN ConductingEquipment as eq on sc.mRID = eq.mRID')

# print ('ACLineSegment:')
# for row in cur.execute ('SELECT io.mRID, io.name, eq.FromConnectivityNode, eq.ToConnectivityNode, ac.r, ac.x, ac.bch, ac.r0, ac.x0, ac.b0ch, cd.length from ACLineSegment as ac INNER JOIN IdentifiedObject as io ON ac.mRID = io.mRID INNER JOIN Conductor as cd on ac.mRID = cd.mRID INNER JOIN ConductingEquipment as eq on ac.mRID = eq.mRID'):
#   print ('  ', row)
#
# print ('SeriesCompensator:')
# for row in cur.execute ('SELECT io.mRID, io.name, eq.FromConnectivityNode, eq.ToConnectivityNode, sc.r, sc.x, sc.r0, sc.x0 from SeriesCompensator as sc INNER JOIN IdentifiedObject as io ON sc.mRID = io.mRID INNER JOIN ConductingEquipment as eq on sc.mRID = eq.mRID'):
#   print ('  ', row)

  con.close()
  return dict

if __name__ == '__main__':
  idx = 0
  if len(sys.argv) > 1:
    idx = int(sys.argv[1])
  case = CASES[idx]

  start_time = time.time()
  d = load_sql_emt_dict ('emtiop.db', case['id'])
  print ('Total query time {:6.3f} s'.format (time.time() - start_time))

  list_dict_table (d, 'EquipmentContainer')
  list_dict_table (d, 'BaseVoltage')
  list_dict_table (d, 'ConnectivityNode')
  list_dict_table (d, 'ACLineSegment')
  list_dict_table (d, 'SeriesCompensator')

