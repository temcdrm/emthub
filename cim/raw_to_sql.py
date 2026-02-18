# Copyright (C) 2025-2026 Meltran, Inc

import json
import csv
import os
import sys
import re
import uuid
import networkx
import math
import sqlite3
import cim_examples
import emthub.api as emthub
 
CIM_NS = 'http://www.ucaiug.org/ns#'
EMT_NS = 'http://opensource.ieee.org/emtiop#'

WFREQ = 2.0 * math.pi * 60.0
M_PER_MILE = 1609.344
SQRT3 = math.sqrt(3.0)
SQRT2 = math.sqrt(2.0)

XFMR_IMAG_PU = 0.0100 # was 0.00015
XFMR_INLL_PU = 0.0025 # was 0.00010
XFMR_VSAT_PU = 1.1
XFMR_AIRCORE = 2.0

PU_WAVE_SPEED = 0.965

IBR_IFAULT = 1.2

STEP_VOLTAGE_INCREMENT = 0.625
HIGH_STEP = 16
LOW_STEP = -16

SHORT_TERM_SECONDS = 4*3600.0
SHORT_TERM_SCALE = 1.2
ONAF_SCALE = 4.0 / 3.0
OFAF_SCALE = 5.0 / 3.0

def load_bus_coordinates (fname):
  lp = open (fname).read()
  mdl = json.loads(lp)
  G = networkx.readwrite.json_graph.node_link_graph(mdl)
  xy = {}
  for n, data in G.nodes(data=True):
    ndata = data['ndata']
    if ('x' in ndata) and ('y' in ndata):
      xy[ndata['name']] = [float(ndata['x']), float(ndata['y'])]
  return xy

def GetCIMID(cls, nm, uuids, identify=False):
    if nm is not None:
        key = cls + ':' + nm
        if key not in uuids:
            uuids[key] = str(uuid.uuid4()).upper()
        elif identify:
            print('Found existing ID for ', key)
        return uuids[key]
    return str(uuid.uuid4()).upper() # for unidentified CIM instances

def create_cim_sql (tables, kvbases, bus_kvbases, baseMVA, case):
  # read the existing mRID map for persistence
  # TODO: consolidate this step with XML export
  uuids = {}
  fuidname = case['mridfile']
  if os.path.exists(fuidname):
    print ('reading instance mRIDs from ', fuidname)
    fuid = open (fuidname, 'r')
    for uuid_ln in fuid.readlines():
      uuid_toks = re.split(r'[,\s]+', uuid_ln)
      if len(uuid_toks) > 2 and not uuid_toks[0].startswith('//'):
        cls = uuid_toks[0]
        nm = uuid_toks[1]
        key = cls + ':' + nm
        val = uuid_toks[2]
        uuids[key] = val
    fuid.close()

  con = sqlite3.connect ('emtiop.db')
  cur = con.cursor()
  # clean out existing tables, in an order that should maintain referential integrity
  # TODO: see if deleting from IdentifiedObject is enough, i.e., cascading deletes will clean out the other tables
  for table_name in ['WeccWTGTA', 'WeccWTGARA', 'WeccREPCA', 'WeccREGCA', 'WeccREECA', 'WeccREEC', 'WeccDynamics',
                     'GovSteamSGO', 'TurbineGovernorDynamics', 'PssIEEE1A', 'PowerSystemStabilizerDynamics',
                     'ExcST1A', 'ExcitationSystemDynamics', 'TransformerSaturation', 'TransformerMeshImpedance',
                     'TransformerCoreAdmittance', 'ThermalGeneratingUnit', 'TextDiagramObject', 'SynchronousMachineTimeConstantReactance',
                     'SynchronousMachineDetailed', 'SynchronousMachineDynamics', 'SeriesCompensator', 'RotatingMachineDynamics',
                     'PowerTransformerEnd', 'PowerTransformer', 'PowerElectronicsWindUnit', 'PhotoVoltaicUnit',
                     'PSRType', 'NuclearGeneratingUnit', 'LinearShuntCompensator', 'HydroGeneratingUnit', 'EnergyConsumer',
                     'DynamicsFunctionBlock', 'DiagramObjectPoint', 'DiagramObject', 'CurveData', 'Curve', 'BatteryUnit',
                     'AsynchronousMachine', 'RotatingMachine', 'ShuntCompensator', 'PowerElectronicsUnit', 'PowerElectronicsConnection',
                     'RegulatingCondEq', 'ACLineSegment', 'Conductor', 'LoadResponseCharacteristic', 'EnergyConnection',
                     'ConductingEquipment', 'GeneratingUnit', 'TransformerEnd', 'Equipment', 'EquipmentContainer',
                     'ConnectivityNode', 'ConnectivityNodeContainer', 'PowerSystemResource', 'BaseVoltage', 'IdentifiedObject']:
    cur.execute ('DELETE from {:s}'.format (table_name))
    con.commit()

  # write the EquipmentContainer->ConnectivityNodeContainer->PowerSystemResource->IdentifiedObject
  eq_id = case['id']
  cur.execute ("INSERT into IdentifiedObject (mRID, name) VALUES ('{:s}', '{:s}')".format (eq_id, case['name']))
  cur.execute ("INSERT into PowerSystemResource (mRID) VALUES ('{:s}')".format (eq_id))
  cur.execute ("INSERT into ConnectivityNodeContainer (mRID) VALUES ('{:s}')".format (eq_id))
  cur.execute ("INSERT into EquipmentContainer (mRID) VALUES ('{:s}')".format (eq_id))
  con.commit()
  # BaseVoltage(s)->IdentifiedObject
  kvbase_ids = {}
  for kvname, kv in kvbases.items():
    print (kvname)
    ID = GetCIMID('BaseVoltage', kvname, uuids)
    cur.execute ("INSERT into IdentifiedObject (mRID, name) VALUES ('{:s}', '{:s}')".format (ID, kvname))
    cur.execute ("INSERT into BaseVoltage (mRID, nominalVoltage) VALUES ('{:s}', {:.3f})".format (ID, kv * 1000.0))
    kvbase_ids[str(kv)] = ID
    con.commit()
  # ConnectivityNode(s)->IdentifiedObject
  busids = {}
  for row in tables['BUS']['data']:
    busname = str(row[0])
    ID = GetCIMID('ConnectivityNode', busname, uuids)
    busids[busname] = ID
    cur.execute ("INSERT into IdentifiedObject (mRID, name) VALUES ('{:s}', '{:s}')".format (ID, busname))
    cur.execute ("INSERT into ConnectivityNode (mRID, ConnectivityNodeContainer) VALUES ('{:s}', '{:s}')".format (ID, eq_id))
    con.commit()
  # ACLineSegment(s)->Conductor->ConductingEquipment->Equipment->PowerSystemResource->IdentifiedObject
  # SeriesCompensator(s)->ConductingEquipment->Equipment->PowerSystemResource->IdentifiedObject
  for row in tables['BRANCH']['data']:
    bus1 = busids[str(row[0])]
    bus2 = busids[str(row[1])]
    ckt = int(row[2])
    key = '{:d}_{:d}_{:d}'.format (row[0], row[1], ckt)
    kvbase = bus_kvbases[row[0]]
    bv = kvbase_ids[str(kvbase)]
    zbase = kvbase * kvbase / baseMVA
    rpu = row[3]
    xpu = row[4]
    bpu = row[5]
    r1 = rpu * zbase
    x1 = xpu * zbase
    if x1 < 0.0:
      ID = GetCIMID('SeriesCompensator', key, uuids)
      cur.execute ("INSERT into IdentifiedObject (mRID, name) VALUES ('{:s}', '{:s}')".format (ID, key))
      cur.execute ("INSERT into PowerSystemResource (mRID) VALUES ('{:s}')".format (ID))
      cur.execute ("INSERT into Equipment (mRID, inService, EquipmentContainer) VALUES ('{:s}',{:d},'{:s}')".format (ID, 1, eq_id))
      cur.execute ("INSERT into ConductingEquipment (mRID, BaseVoltage, FromConnectivityNode, ToConnectivityNode) VALUES ('{:s}','{:s}','{:s}','{:s}')".format (ID, bv, bus1, bus2))
      cur.execute ("INSERT into SeriesCompensator (mRID, r, x, r0, x0) VALUES ('{:s}',{:.6f},{:.6f},{:.6f},{:.6f})".format (ID, r1, x1, r1, x1))
    else:
      ID = GetCIMID('ACLineSegment', key, uuids)
      cur.execute ("INSERT into IdentifiedObject (mRID, name) VALUES ('{:s}', '{:s}')".format (ID, key))
      cur.execute ("INSERT into PowerSystemResource (mRID) VALUES ('{:s}')".format (ID))
      cur.execute ("INSERT into Equipment (mRID, inService, EquipmentContainer) VALUES ('{:s}',{:d},'{:s}')".format (ID, 1, eq_id))
      cur.execute ("INSERT into ConductingEquipment (mRID, BaseVoltage, FromConnectivityNode, ToConnectivityNode) VALUES ('{:s}','{:s}','{:s}','{:s}')".format (ID, bv, bus1, bus2))
      l1 = x1 / WFREQ
      if bpu > 0.0:
        c1 = bpu / WFREQ / zbase
        z1 = math.sqrt (l1/c1)
      else:
        z1 = 400.0
        c1 = l1 / z1 / z1
      b1ch = c1 * WFREQ
      if z1 >= 100.0 : # overhead
        r0 = 2.0 * r1
        x0 = 3.0 * x1 # was 2.0 * x1
        b0ch = 0.6 * b1ch
        if kvbase >= 345.0:
          length = x1 / 0.6
        else:
          length = x1 / 0.8
      else: # underground
        r0 = r1
        x0 = x1
        b0ch = b1ch
        length = x1 / 0.2
      length *= M_PER_MILE
      vel1 = length / math.sqrt(l1*c1) / 3.0e8 # wave velocity normalized to speed of light
      cur.execute ("INSERT into Conductor (mRID, length) VALUES ('{:s}',{:.6f})".format (ID, length))
      cur.execute ("INSERT into ACLineSegment (mRID, r, x, bch, r0, x0, b0ch) VALUES ('{:s}',{:f},{:f},{:f},{:f},{:f},{:f})".format (ID, r1, x1, b1ch, r0, x0, b0ch))
      if vel1 >= 1.0:
        print ('check line data for {:s} kv={:2f} z1={:.2f} vel1={:.3f}c'.format (key, kvbase, z1, vel1))
    con.commit()

  con.close()
  # TODO: consolidate this step with XML export
  print('saving instance mRIDs to ', fuidname)
  fuid = open(fuidname, 'w')
  for key, val in uuids.items():
      print('{:s},{:s}'.format(key.replace(':', ',', 1), val), file=fuid)
  fuid.close()

if __name__ == '__main__':
  case_id = 0
  if len(sys.argv) > 1:
    case_id = int(sys.argv[1])
  case = cim_examples.CASES[case_id]

  tables, kvbases, bus_kvbases, baseMVA = emthub.load_psse_rawfile (case['rawfile'])
  emthub.print_psse_table (tables, 'SYSTEM SWITCHING DEVICE')

  print ('All kV Bases =', kvbases)

  create_cim_sql (tables, kvbases, bus_kvbases, baseMVA, case)
  

