# Copyright (C) 2025-2026 Meltran, Inc

import time
import sys
import sqlite3
import cim_examples

PREFIX = None
DELIM = ':'

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
  dict['ACLineSegment'] = load_one_dict (cur, ['name', 'from', 'to', 'bv', 'r1', 'x1', 'b1ch', 'r0', 'x0', 'b0ch', 'length'], 
    'SELECT io.mRID, io.name, eq.FromConnectivityNode, eq.ToConnectivityNode, eq.BaseVoltage, ac.r, ac.x, ac.bch, ac.r0, ac.x0, ac.b0ch, cd.length from ACLineSegment as ac INNER JOIN IdentifiedObject as io ON ac.mRID = io.mRID INNER JOIN Conductor as cd on ac.mRID = cd.mRID INNER JOIN ConductingEquipment as eq on ac.mRID = eq.mRID')
  dict['SeriesCompensator'] = load_one_dict (cur, ['name', 'from', 'to', 'bv', 'r1', 'x1', 'r0', 'x0'], 
    'SELECT io.mRID, io.name, eq.FromConnectivityNode, eq.ToConnectivityNode, eq.BaseVoltage, sc.r, sc.x, sc.r0, sc.x0 from SeriesCompensator as sc INNER JOIN IdentifiedObject as io ON sc.mRID = io.mRID INNER JOIN ConductingEquipment as eq on sc.mRID = eq.mRID')

  con.close()
  return dict

if __name__ == '__main__':
  idx = 0
  if len(sys.argv) > 1:
    idx = int(sys.argv[1])
  case = cim_examples.CASES[idx]

  start_time = time.time()
  d = load_sql_emt_dict ('emtiop.db', case['id'])
  print ('Total query time {:6.3f} s'.format (time.time() - start_time))

  list_dict_table (d, 'EquipmentContainer')
  list_dict_table (d, 'BaseVoltage')
  list_dict_table (d, 'ConnectivityNode')
  list_dict_table (d, 'ACLineSegment')
  list_dict_table (d, 'SeriesCompensator')

