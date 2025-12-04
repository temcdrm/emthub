# Copyright (C) 2025 Meltran, Inc

import json
import csv
import rdflib
import os
import sys
import re
import uuid
import networkx
import math
from rdflib.namespace import XSD

CIM_NS = 'http://www.ucaiug.org/ns#'
EMT_NS = 'http://opensource.ieee.org/emtiop#'

CASES = [
  {'id': '1783D2A8-1204-4781-A0B4-7A73A2FA6038', 
   'name': 'IEEE118', 
   'rawfile':'raw/ieee-118-bus-v4.raw', 'cimfile':'ieee118.xml', 'locfile': 'raw/ieee118_network.json', 'mridfile':'raw/ieee118mrids.dat',
   'wind_units': ['132_W', '136_W', '138_W', '168_W', '180_W'],
   'solar_units': ['126_S', '128_S', '130_S', '140_S', '149_S', 
                   '151_S', '159_S', '165_S', '175_S', '179_S', 
                   '183_S', '185_S', '188_S', '191_S'],
   'hydro_units': [], 'nuclear_units': []},
  {'id': '2540AF5C-4F83-4C0F-9577-DEE8CC73BBB3', 
   'name': 'WECC240',
   'rawfile':'raw/240busWECC_2018_PSS.raw', 'cimfile':'wecc240.xml', 'locfile': 'raw/wecc240_network.json', 'mridfile':'raw/wecc240mrids.dat',
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
   'nuclear_units': ['1431_N', '4132_N']}
]

METAFILE = 'psseraw.json'
WFREQ = 2.0 * math.pi * 60.0
M_PER_MILE = 1609.344
SQRT3 = math.sqrt(3.0)
SQRT2 = math.sqrt(2.0)

XFMR_IMAG_PU = 0.01
XFMR_INLL_PU = 0.0025
XFMR_VSAT_PU = 1.1
XFMR_AIRCORE = 2.0

IBR_IFAULT = 1.2

DYNAMIC_SETTINGS_FILE = 'dynamics_defaults.json'

tables = {}
baseMVA = -1.0
bus_kvbases = {}
kvbases = {}

def load_bus_coordinates (fname):
  lp = open (fname).read()
  mdl = json.loads(lp)
  G = networkx.readwrite.json_graph.node_link_graph(mdl)
  xy = {}
  for n, data in G.nodes(data=True):
    ndata = data['ndata']
    if ('x' in ndata) and ('y' in ndata):
      xy[n] = [float(ndata['x']), float(ndata['y'])]
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

def append_wecc_dynamics (g, key, ID, pec, leaf_class, dyn_settings):
  leaf = rdflib.URIRef (ID)
  g.add ((leaf, rdflib.RDF.type, rdflib.URIRef (CIM_NS + leaf_class)))
  g.add ((leaf, rdflib.URIRef (CIM_NS + 'IdentifiedObject.name'), rdflib.Literal(key, datatype=CIM_NS+'String')))
  g.add ((leaf, rdflib.URIRef (CIM_NS + 'IdentifiedObject.mRID'), rdflib.Literal(ID, datatype=CIM_NS+'String')))
  g.add ((leaf, rdflib.URIRef (CIM_NS + 'WeccDynamics.PowerElectronicsConnection'), pec))
  for tag in dyn_settings['DynamicsFunctionBlock']:
    row = dyn_settings['DynamicsFunctionBlock'][tag]
    g.add ((leaf, rdflib.URIRef (CIM_NS + 'DynamicsFunctionBlock.{:s}'.format(tag)), rdflib.Literal(row[0], datatype=CIM_NS+row[1])))
  for tag in dyn_settings[leaf_class]:
    row = dyn_settings[leaf_class][tag]
    g.add ((leaf, rdflib.URIRef (CIM_NS + '{:s}.{:s}'.format(leaf_class, tag)), rdflib.Literal(row[0], datatype=CIM_NS+row[1])))

def create_machine_dynamics (g, leaf_class, key, uuids):
  ID = GetCIMID (leaf_class, key, uuids)
  leaf = rdflib.URIRef (ID)
  g.add ((leaf, rdflib.RDF.type, rdflib.URIRef (CIM_NS + leaf_class)))
  g.add ((leaf, rdflib.URIRef (CIM_NS + 'IdentifiedObject.name'), rdflib.Literal(key, datatype=CIM_NS+'String')))
  g.add ((leaf, rdflib.URIRef (CIM_NS + 'IdentifiedObject.mRID'), rdflib.Literal(ID, datatype=CIM_NS+'String')))
  return leaf

def append_dynamic_parameters (g, leaf, dyn_settings, sections):
  for sect in sections:
    for tag in dyn_settings[sect]:
      row = dyn_settings[sect][tag]
      if row[1].endswith('Kind'):
        g.add ((leaf, rdflib.URIRef (CIM_NS + '{:s}.{:s}'.format(sect, tag)), rdflib.URIRef (CIM_NS + '{:s}.{:s}'.format(row[1], row[0]))))
      else:
        g.add ((leaf, rdflib.URIRef (CIM_NS + '{:s}.{:s}'.format(sect, tag)), rdflib.Literal(row[0], datatype=CIM_NS+row[1])))

def create_cim_xml (tables, kvbases, bus_kvbases, baseMVA, case):
  g = rdflib.Graph()
  CIM = rdflib.Namespace (CIM_NS)
  g.bind('cim', CIM)
  EMT = rdflib.Namespace (EMT_NS)
  g.bind('emt', EMT)
#  g.bind('xsd', rdflib.namespace.XSD)
#  g.namespace_manager.bind('xsd', XSD)

  # hard-wire the prefixes for rdf:datatype
  if False: # but standard RDF doesn't allow prefixes in datatype
    CIM.ActivePower = 'cim:ActivePower'
    CIM.AngleDegrees = 'cim:AngleDegrees'
    CIM.ApparentPower = 'cim:ApparentPower'
    CIM.Boolean = 'cim:Boolean'
    CIM.Conductance = 'cim:Conductance'
    CIM.Float = 'cim:Float'
    CIM.Integer = 'cim:Integer'
    CIM.Length = 'cim:Length'
    CIM.PU = 'cim:PU'
    CIM.Reactance = 'cim:Reactance'
    CIM.ReactivePower = 'cim:ReactivePower'
    CIM.RealEnergy = 'cim:RealEnergy'
    CIM.Resistance = 'cim:Resistance'
    CIM.Seconds = 'cim:Seconds'
    CIM.String = 'cim:String'
    CIM.Susceptance = 'cim:Susceptance'
    CIM.Voltage = 'cim:Voltage'
  
  # read the existing mRID map for persistence
  uuids = {}
  fuidname = case['mridfile']
  if os.path.exists(fuidname):
    print ('reading instance mRIDs from ', fuidname)
    fuid = open (fuidname, 'r')
    for uuid_ln in fuid.readlines():
      uuid_toks = re.split('[,\s]+', uuid_ln)
      if len(uuid_toks) > 2 and not uuid_toks[0].startswith('//'):
        cls = uuid_toks[0]
        nm = uuid_toks[1]
        key = cls + ':' + nm
        val = uuid_toks[2]
        uuids[key] = val
    fuid.close()

  eq = rdflib.URIRef (case['id']) # no prefix with urn:uuid:

  g.add ((eq, rdflib.RDF.type, rdflib.URIRef (CIM_NS + 'EquipmentContainer')))
  g.add ((eq, rdflib.URIRef (CIM_NS + 'IdentifiedObject.name'), rdflib.Literal(case['name'], datatype=CIM.String)))
  g.add ((eq, rdflib.URIRef (CIM_NS + 'IdentifiedObject.mRID'), rdflib.Literal(case['id'], datatype=CIM.String)))

  # write the base voltages
  kvbase_ids = {}
  for kvname, kv in kvbases.items():
    print (kvname)
    ID = GetCIMID('BaseVoltage', kvname, uuids)
    bv = rdflib.URIRef (ID)
    g.add ((bv, rdflib.RDF.type, rdflib.URIRef (CIM_NS + 'BaseVoltage')))
    g.add ((bv, rdflib.URIRef (CIM_NS + 'IdentifiedObject.name'), rdflib.Literal(kvname, datatype=CIM.String)))
    g.add ((bv, rdflib.URIRef (CIM_NS + 'IdentifiedObject.mRID'), rdflib.Literal(ID, datatype=CIM.String)))
    g.add ((bv, rdflib.URIRef (CIM_NS + 'BaseVoltage.nominalVoltage'), rdflib.Literal(kv * 1000.0, datatype=CIM.Voltage)))
    kvbase_ids[str(kv)] = ID

  # write the connectivity nodes
  busids = {}
  for row in tables['BUS']['data']:
    busname = str(row[0])
    ID = GetCIMID('ConnectivityNode', busname, uuids)
    busids[busname] = ID
    cn = rdflib.URIRef (ID)
    g.add ((cn, rdflib.RDF.type, rdflib.URIRef (CIM_NS + 'ConnectivityNode')))
    g.add ((cn, rdflib.URIRef (CIM_NS + 'IdentifiedObject.name'), rdflib.Literal(busname, datatype=CIM.String)))
    g.add ((cn, rdflib.URIRef (CIM_NS + 'IdentifiedObject.mRID'), rdflib.Literal(ID, datatype=CIM.String)))
    g.add ((cn, rdflib.URIRef (CIM_NS + 'ConnectivityNode.ConnectivityNodeContainer'), eq))

  # write the diagram layout
  busxy = load_bus_coordinates (case['locfile'])
  for row in tables['BUS']['data']:
    key = str(row[0])
    busname = '{:d} {:s} {:.2f} kV'.format (row[0], row[1], row[2])
    xy = busxy[key]
    ID = GetCIMID('TextDiagramObject', key, uuids)
    td = rdflib.URIRef (ID)
    g.add ((td, rdflib.RDF.type, rdflib.URIRef (CIM_NS + 'TextDiagramObject')))
    g.add ((td, rdflib.URIRef (CIM_NS + 'IdentifiedObject.name'), rdflib.Literal(key, datatype=CIM.String)))
    g.add ((td, rdflib.URIRef (CIM_NS + 'IdentifiedObject.mRID'), rdflib.Literal(ID, datatype=CIM.String)))
    g.add ((td, rdflib.URIRef (CIM_NS + 'DiagramObject.IdentifiedObject'), rdflib.URIRef (busids[key])))
    g.add ((td, rdflib.URIRef (CIM_NS + 'DiagramObject.drawingOrder'), rdflib.Literal (1, datatype=CIM.Integer)))
    g.add ((td, rdflib.URIRef (CIM_NS + 'DiagramObject.isPolygon'), rdflib.Literal (False, datatype=CIM.Boolean)))
    g.add ((td, rdflib.URIRef (CIM_NS + 'TextDiagramObject.text'), rdflib.Literal(busname, datatype=CIM.String)))
    pt = rdflib.BNode()
    g.add ((pt, rdflib.RDF.type, rdflib.URIRef (CIM_NS + 'DiagramObjectPoint')))
    g.add ((pt, rdflib.URIRef (CIM_NS + 'DiagramObjectPoint.DiagramObject'), td))
    g.add ((pt, rdflib.URIRef (CIM_NS + 'DiagramObjectPoint.sequenceNumber'), rdflib.Literal(1, datatype=CIM.Integer)))
    g.add ((pt, rdflib.URIRef (CIM_NS + 'DiagramObjectPoint.xPosition'), rdflib.Literal(xy[0], datatype=CIM.Float)))
    g.add ((pt, rdflib.URIRef (CIM_NS + 'DiagramObjectPoint.yPosition'), rdflib.Literal(xy[1], datatype=CIM.Float)))

  # write the branches
  for row in tables['BRANCH']['data']:
    bus1 = rdflib.URIRef(busids[str(row[0])])
    bus2 = rdflib.URIRef(busids[str(row[1])])
    ckt = int(row[2])
    key = '{:d}_{:d}_{:d}'.format (row[0], row[1], ckt)
    kvbase = bus_kvbases[row[0]]
    zbase = kvbase * kvbase / baseMVA
    rpu = row[3]
    xpu = row[4]
    bpu = row[5]
    r1 = rpu * zbase
    x1 = xpu * zbase
    if x1 < 0.0:
      ID = GetCIMID('SeriesCompensator', key, uuids)
      ac = rdflib.URIRef (ID)
      bv = rdflib.URIRef (kvbase_ids[str(kvbase)])
      g.add ((ac, rdflib.RDF.type, rdflib.URIRef (CIM_NS + 'SeriesCompensator')))
      g.add ((ac, rdflib.URIRef (CIM_NS + 'IdentifiedObject.name'), rdflib.Literal(key, datatype=CIM.String)))
      g.add ((ac, rdflib.URIRef (CIM_NS + 'IdentifiedObject.mRID'), rdflib.Literal(ID, datatype=CIM.String)))
      g.add ((ac, rdflib.URIRef (CIM_NS + 'Equipment.EquipmentContainer'), eq))
      g.add ((ac, rdflib.URIRef (CIM_NS + 'Equipment.inService'), rdflib.Literal (True, datatype=CIM.Boolean)))
      g.add ((ac, rdflib.URIRef (EMT_NS + 'ConductingEquipment.FromConnectivityNode'), bus1))
      g.add ((ac, rdflib.URIRef (EMT_NS + 'ConductingEquipment.ToConnectivityNode'), bus2))
      g.add ((ac, rdflib.URIRef (CIM_NS + 'ConductingEquipment.BaseVoltage'), bv))
      g.add ((ac, rdflib.URIRef (CIM_NS + 'SeriesCompensator.r'), rdflib.Literal (r1, datatype=CIM.Resistance)))
      g.add ((ac, rdflib.URIRef (CIM_NS + 'SeriesCompensator.x'), rdflib.Literal (x1, datatype=CIM.Reactance)))
      g.add ((ac, rdflib.URIRef (CIM_NS + 'SeriesCompensator.r0'), rdflib.Literal (r1, datatype=CIM.Resistance)))
      g.add ((ac, rdflib.URIRef (CIM_NS + 'SeriesCompensator.x0'), rdflib.Literal (x1, datatype=CIM.Reactance)))
    else:
      ID = GetCIMID('ACLineSegment', key, uuids)
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
        x0 = 3.0 * x1
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
      ac = rdflib.URIRef (ID)
      bv = rdflib.URIRef (kvbase_ids[str(kvbase)])
      g.add ((ac, rdflib.RDF.type, rdflib.URIRef (CIM_NS + 'ACLineSegment')))
      g.add ((ac, rdflib.URIRef (CIM_NS + 'IdentifiedObject.name'), rdflib.Literal(key, datatype=CIM.String)))
      g.add ((ac, rdflib.URIRef (CIM_NS + 'IdentifiedObject.mRID'), rdflib.Literal(ID, datatype=CIM.String)))
      g.add ((ac, rdflib.URIRef (CIM_NS + 'Equipment.EquipmentContainer'), eq))
      g.add ((ac, rdflib.URIRef (CIM_NS + 'Equipment.inService'), rdflib.Literal (True, datatype=CIM.Boolean)))
      g.add ((ac, rdflib.URIRef (EMT_NS + 'ConductingEquipment.FromConnectivityNode'), bus1))
      g.add ((ac, rdflib.URIRef (EMT_NS + 'ConductingEquipment.ToConnectivityNode'), bus2))
      g.add ((ac, rdflib.URIRef (CIM_NS + 'ConductingEquipment.BaseVoltage'), bv))
      g.add ((ac, rdflib.URIRef (CIM_NS + 'Conductor.length'), rdflib.Literal (length, datatype=CIM.Length)))
      g.add ((ac, rdflib.URIRef (CIM_NS + 'ACLineSegment.r'), rdflib.Literal (r1, datatype=CIM.Resistance)))
      g.add ((ac, rdflib.URIRef (CIM_NS + 'ACLineSegment.x'), rdflib.Literal (x1, datatype=CIM.Reactance)))
      g.add ((ac, rdflib.URIRef (CIM_NS + 'ACLineSegment.bch'), rdflib.Literal (b1ch, datatype=CIM.Susceptance)))
      g.add ((ac, rdflib.URIRef (CIM_NS + 'ACLineSegment.r0'), rdflib.Literal (r0, datatype=CIM.Resistance)))
      g.add ((ac, rdflib.URIRef (CIM_NS + 'ACLineSegment.x0'), rdflib.Literal (x0, datatype=CIM.Reactance)))
      g.add ((ac, rdflib.URIRef (CIM_NS + 'ACLineSegment.b0ch'), rdflib.Literal (b0ch, datatype=CIM.Susceptance)))
      if vel1 >= 1.0:
        print ('check line data for {:s} kv={:2f} z1={:.2f} vel1={:.3f}c'.format (key, kvbase, z1, vel1))

  # write Load and load response characteristics
  LoadResponseCharacteristics = {}
  for row in tables['LOAD']['data']:
    if row[2] < 1:
      continue
    bus1 = rdflib.URIRef(busids[str(row[0])])
    kvbase = bus_kvbases[row[0]]
    ckt = int(row[1])
    scale = row[9] * 1.0e6
    # these are in W and var
    p = (row[3]+row[5]+row[7]) * scale
    q = (row[4]+row[6]+row[8]) * scale
    # create LoadResponseCharacteristics on the fly for ZIP coefficients
    # choosing the default percentages to match WECC 240
    Pp = 0.0
    Ip = 100.0
    Zp = 0.0
    Pq = 0.0
    Iq = 0.0
    Zq = 100.0
    # these are in MW and Mvar
    Pmag = abs(row[3]) +  abs(row[5]) +  abs(row[7])
    if Pmag > 0.0:
        Pp = 100.0 * abs(row[3]) / Pmag
        Ip = 100.0 * abs(row[5]) / Pmag
        Zp = 100.0 * abs(row[7]) / Pmag
    Qmag = abs(row[4]) +  abs(row[6]) +  abs(row[8])
    if Qmag > 0.0:
        Pq = 100.0 * abs(row[4]) / Qmag
        Iq = 100.0 * abs(row[6]) / Qmag
        Zq = 100.0 * abs(row[8]) / Qmag
    LRkey = 'LoadResp_Zp={:.3f}_Ip={:.3f}_Pp={:.3f}_Zq={:.3f}_Iq={:.3f}_Pq={:.3f}'.format(Zp, Ip, Pp, Zq, Iq, Pq)
    LRmRID = GetCIMID('LoadResponseCharacteristic', LRkey, uuids)
    if LRkey not in LoadResponseCharacteristics:
      LoadResponseCharacteristics[LRkey] = {'mRID': LRmRID, 'Zp': Zp, 'Ip': Ip, 'Pp': Pp, 'Zq': Zq, 'Iq': Iq, 'Pq': Pq}
    key = '{:d}_{:d}'.format (row[0], ckt)
    ID = GetCIMID('EnergyConsumer', key, uuids)
    ec = rdflib.URIRef (ID)
    bv = rdflib.URIRef (kvbase_ids[str(kvbase)])
    g.add ((ec, rdflib.RDF.type, rdflib.URIRef (CIM_NS + 'EnergyConsumer')))
    g.add ((ec, rdflib.URIRef (CIM_NS + 'IdentifiedObject.name'), rdflib.Literal(key, datatype=CIM.String)))
    g.add ((ec, rdflib.URIRef (CIM_NS + 'IdentifiedObject.mRID'), rdflib.Literal(ID, datatype=CIM.String)))
    g.add ((ec, rdflib.URIRef (CIM_NS + 'Equipment.EquipmentContainer'), eq))
    g.add ((ec, rdflib.URIRef (CIM_NS + 'Equipment.inService'), rdflib.Literal (True, datatype=CIM.Boolean)))
    g.add ((ec, rdflib.URIRef (EMT_NS + 'ConductingEquipment.FromConnectivityNode'), bus1))
    g.add ((ec, rdflib.URIRef (EMT_NS + 'ConductingEquipment.ToConnectivityNode'), bus1))
    g.add ((ec, rdflib.URIRef (CIM_NS + 'ConductingEquipment.BaseVoltage'), bv))
    g.add ((ec, rdflib.URIRef (CIM_NS + 'EnergyConsumer.LoadResponse'), rdflib.URIRef (LRmRID)))
    g.add ((ec, rdflib.URIRef (CIM_NS + 'EnergyConsumer.p'), rdflib.Literal (p, datatype=CIM.ActivePower)))
    g.add ((ec, rdflib.URIRef (CIM_NS + 'EnergyConsumer.q'), rdflib.Literal (q, datatype=CIM.ReactivePower)))

  print ('Writing', len(LoadResponseCharacteristics), 'load response characteristics')
  for key, row in LoadResponseCharacteristics.items():
    lr = rdflib.URIRef (row['mRID'])
    g.add ((lr, rdflib.RDF.type, rdflib.URIRef (CIM_NS + 'LoadResponseCharacteristic')))
    g.add ((lr, rdflib.URIRef (CIM_NS + 'IdentifiedObject.name'), rdflib.Literal(key, datatype=CIM.String)))
    g.add ((lr, rdflib.URIRef (CIM_NS + 'IdentifiedObject.mRID'), rdflib.Literal(row['mRID'], datatype=CIM.String)))
    g.add ((lr, rdflib.URIRef (CIM_NS + 'LoadResponseCharacteristic.exponentModel'), rdflib.Literal(False, datatype=CIM.Boolean)))
    g.add ((lr, rdflib.URIRef (CIM_NS + 'LoadResponseCharacteristic.pFrequencyExponent'), rdflib.Literal(0.0, datatype=CIM.Float)))
    g.add ((lr, rdflib.URIRef (CIM_NS + 'LoadResponseCharacteristic.qFrequencyExponent'), rdflib.Literal(0.0, datatype=CIM.Float)))
    g.add ((lr, rdflib.URIRef (CIM_NS + 'LoadResponseCharacteristic.pVoltageExponent'), rdflib.Literal(0.0, datatype=CIM.Float)))
    g.add ((lr, rdflib.URIRef (CIM_NS + 'LoadResponseCharacteristic.qVoltageExponent'), rdflib.Literal(0.0, datatype=CIM.Float)))
    g.add ((lr, rdflib.URIRef (CIM_NS + 'LoadResponseCharacteristic.pConstantImpedance'), rdflib.Literal(row['Zp'], datatype=CIM.Float)))
    g.add ((lr, rdflib.URIRef (CIM_NS + 'LoadResponseCharacteristic.pConstantCurrent'), rdflib.Literal(row['Ip'], datatype=CIM.Float)))
    g.add ((lr, rdflib.URIRef (CIM_NS + 'LoadResponseCharacteristic.pConstantPower'), rdflib.Literal(row['Pp'], datatype=CIM.Float)))
    g.add ((lr, rdflib.URIRef (CIM_NS + 'LoadResponseCharacteristic.qConstantImpedance'), rdflib.Literal(row['Zq'], datatype=CIM.Float)))
    g.add ((lr, rdflib.URIRef (CIM_NS + 'LoadResponseCharacteristic.qConstantCurrent'), rdflib.Literal(row['Iq'], datatype=CIM.Float)))
    g.add ((lr, rdflib.URIRef (CIM_NS + 'LoadResponseCharacteristic.qConstantPower'), rdflib.Literal(row['Pq'], datatype=CIM.Float)))

  # shunt compensators
  for row in tables['FIXED SHUNT']['data']:
    if row[2] < 1:
      continue
    bus1 = rdflib.URIRef(busids[str(row[0])])
    kvbase = bus_kvbases[row[0]]
    ckt = int(row[1])
    key = '{:d}_{:d}'.format (row[0], ckt)
    ID = GetCIMID('LinearShuntCompensator', key, uuids)
    sc = rdflib.URIRef (ID)
    bv = rdflib.URIRef (kvbase_ids[str(kvbase)])
    sectionMax = 1
    sectionCount = 1
    sectionG = row[3]/kvbase/kvbase
    sectionB = row[4]/kvbase/kvbase
    g.add ((sc, rdflib.RDF.type, rdflib.URIRef (CIM_NS + 'LinearShuntCompensator')))
    g.add ((sc, rdflib.URIRef (CIM_NS + 'IdentifiedObject.name'), rdflib.Literal(key, datatype=CIM.String)))
    g.add ((sc, rdflib.URIRef (CIM_NS + 'IdentifiedObject.mRID'), rdflib.Literal(ID, datatype=CIM.String)))
    g.add ((sc, rdflib.URIRef (CIM_NS + 'Equipment.EquipmentContainer'), eq))
    g.add ((sc, rdflib.URIRef (CIM_NS + 'Equipment.inService'), rdflib.Literal (True, datatype=CIM.Boolean)))
    g.add ((sc, rdflib.URIRef (EMT_NS + 'ConductingEquipment.FromConnectivityNode'), bus1))
    g.add ((sc, rdflib.URIRef (EMT_NS + 'ConductingEquipment.ToConnectivityNode'), bus1))
    g.add ((sc, rdflib.URIRef (CIM_NS + 'ConductingEquipment.BaseVoltage'), bv))
    g.add ((sc, rdflib.URIRef (CIM_NS + 'ShuntCompensator.nomU'), rdflib.Literal (kvbase * 1000.0, datatype=CIM.Voltage)))
    g.add ((sc, rdflib.URIRef (CIM_NS + 'ShuntCompensator.sections'), rdflib.Literal (sectionCount, datatype=CIM.Integer)))
    g.add ((sc, rdflib.URIRef (CIM_NS + 'ShuntCompensator.maximumSections'), rdflib.Literal (sectionMax, datatype=CIM.Integer)))
    g.add ((sc, rdflib.URIRef (CIM_NS + 'ShuntCompensator.grounded'), rdflib.Literal (True, datatype=CIM.Boolean)))
    g.add ((sc, rdflib.URIRef (CIM_NS + 'LinearShuntCompensator.bPerSection'), rdflib.Literal (sectionB, datatype=CIM.Susceptance)))
    g.add ((sc, rdflib.URIRef (CIM_NS + 'LinearShuntCompensator.gPerSection'), rdflib.Literal (sectionG, datatype=CIM.Conductance)))
  for row in tables['SWITCHED SHUNT']['data']:
    if row[1] < 1:
      continue
    bus1 = rdflib.URIRef(busids[str(row[0])])
    kvbase = bus_kvbases[row[0]]
    key = '{:d}'.format (row[0])
    ID = GetCIMID('LinearShuntCompensator', key, uuids)
    sc = rdflib.URIRef (ID)
    bv = rdflib.URIRef (kvbase_ids[str(kvbase)])
    sectionG = 0.0
    sectionMax = row[3]
    sectionB = row[4]/kvbase/kvbase
    sectionCount = int((row[2]+0.1*row[4])/row[4])
    g.add ((sc, rdflib.RDF.type, rdflib.URIRef (CIM_NS + 'LinearShuntCompensator')))
    g.add ((sc, rdflib.URIRef (CIM_NS + 'IdentifiedObject.name'), rdflib.Literal(key, datatype=CIM.String)))
    g.add ((sc, rdflib.URIRef (CIM_NS + 'IdentifiedObject.mRID'), rdflib.Literal(ID, datatype=CIM.String)))
    g.add ((sc, rdflib.URIRef (CIM_NS + 'Equipment.EquipmentContainer'), eq))
    g.add ((sc, rdflib.URIRef (CIM_NS + 'Equipment.inService'), rdflib.Literal (True, datatype=CIM.Boolean)))
    g.add ((sc, rdflib.URIRef (EMT_NS + 'ConductingEquipment.FromConnectivityNode'), bus1))
    g.add ((sc, rdflib.URIRef (EMT_NS + 'ConductingEquipment.ToConnectivityNode'), bus1))
    g.add ((sc, rdflib.URIRef (CIM_NS + 'ConductingEquipment.BaseVoltage'), bv))
    g.add ((sc, rdflib.URIRef (CIM_NS + 'ShuntCompensator.nomU'), rdflib.Literal (kvbase * 1000.0, datatype=CIM.Voltage)))
    g.add ((sc, rdflib.URIRef (CIM_NS + 'ShuntCompensator.sections'), rdflib.Literal (sectionCount, datatype=CIM.Integer)))
    g.add ((sc, rdflib.URIRef (CIM_NS + 'ShuntCompensator.maximumSections'), rdflib.Literal (sectionMax, datatype=CIM.Integer)))
    g.add ((sc, rdflib.URIRef (CIM_NS + 'ShuntCompensator.grounded'), rdflib.Literal (True, datatype=CIM.Boolean)))
    g.add ((sc, rdflib.URIRef (CIM_NS + 'LinearShuntCompensator.bPerSection'), rdflib.Literal (sectionB, datatype=CIM.Susceptance)))
    g.add ((sc, rdflib.URIRef (CIM_NS + 'LinearShuntCompensator.gPerSection'), rdflib.Literal (sectionG, datatype=CIM.Conductance)))

  # write the transformers, assumed to be 2-winding
  # TODO: 3-winding
  # TODO: handle the taps
  # TODO: sort windings in order of descending voltage
  # TODO: write inService False for equipment out of service
  for idx in range(len(tables['TRANSFORMER']['data'])):
    row = tables['TRANSFORMER']['data'][idx]
    if row[4] < 1:
      continue
    key = '{:d}_{:d}_{:d}_{:d}'.format (row[0], row[1], row[2], int(row[3]))
    wdg = tables['TRANSFORMER']['winding_data'][idx]
    mva = max(wdg['mvas'])
    if mva <= 0.0:
      mva = wdg['s12']
    for i in range(wdg['nwdgs']):
      if wdg['kvs'][i] <= 0.0:
        wdg['kvs'][i] = bus_kvbases[row[i]]
    #print (key, wdg['nwdgs'], wdg['r12'], wdg['x12'], wdg['s12'], wdg['taps'], wdg['kvs'], mva)
    ID = GetCIMID('PowerTransformer', key, uuids)
    pt = rdflib.URIRef (ID)
    g.add ((pt, rdflib.RDF.type, rdflib.URIRef (CIM_NS + 'PowerTransformer')))
    g.add ((pt, rdflib.URIRef (CIM_NS + 'IdentifiedObject.name'), rdflib.Literal(key, datatype=CIM.String)))
    g.add ((pt, rdflib.URIRef (CIM_NS + 'IdentifiedObject.mRID'), rdflib.Literal(ID, datatype=CIM.String)))
    g.add ((pt, rdflib.URIRef (CIM_NS + 'Equipment.EquipmentContainer'), eq))
    g.add ((pt, rdflib.URIRef (CIM_NS + 'Equipment.inService'), rdflib.Literal (True, datatype=CIM.Boolean)))
    if min(wdg['kvs']) > 20.0:
      bGSU = False
      vgrp = 'Yy'
      clocks = [0, 0]
    else:
      bGSU = True
      vgrp = 'Yd1'
      clocks = [0, 1]
    g.add ((pt, rdflib.URIRef (CIM_NS + 'PowerTransformer.vectorGroup'), rdflib.Literal (vgrp, datatype=CIM.String)))
    # write 2 ends, assuming they are in correct order by descending voltage
    ends = []
    for idx in range(2):
      endkey = '{:s}_End_{:d}'.format (key, idx+1)
      endID = GetCIMID('PowerTransformerEnd', endkey, uuids)
      end = rdflib.URIRef (endID)
      ends.append (end)
      g.add ((end, rdflib.RDF.type, rdflib.URIRef (CIM_NS + 'PowerTransformerEnd')))
      g.add ((end, rdflib.URIRef (CIM_NS + 'IdentifiedObject.name'), rdflib.Literal(endkey, datatype=CIM.String)))
      g.add ((end, rdflib.URIRef (CIM_NS + 'IdentifiedObject.mRID'), rdflib.Literal(endID, datatype=CIM.String)))
      g.add ((end, rdflib.URIRef (CIM_NS + 'PowerTransformerEnd.PowerTransformer'), pt))
      g.add ((end, rdflib.URIRef (CIM_NS + 'PowerTransformerEnd.ratedS'), rdflib.Literal(mva*1.0e6, datatype=CIM.ApparentPower)))
      g.add ((end, rdflib.URIRef (CIM_NS + 'PowerTransformerEnd.ratedU'), rdflib.Literal(wdg['kvs'][idx]*1.0e3, datatype=CIM.Voltage)))
      g.add ((end, rdflib.URIRef (CIM_NS + 'PowerTransformerEnd.phaseAngleClock'), rdflib.Literal(clocks[idx], datatype=CIM.Integer)))
      g.add ((end, rdflib.URIRef (CIM_NS + 'TransformerEnd.endNumber'), rdflib.Literal(idx+1, datatype=CIM.Integer)))
      if clocks[idx] != 0:
        g.add ((end, rdflib.URIRef (CIM_NS + 'PowerTransformerEnd.connectionKind'), rdflib.URIRef (CIM_NS + 'WindingConnection.D')))  # TODO: cim:WindingConnection.D?
        g.add ((end, rdflib.URIRef (CIM_NS + 'TransformerEnd.grounded'), rdflib.Literal(False, datatype=CIM.Boolean)))
      else:
        g.add ((end, rdflib.URIRef (CIM_NS + 'PowerTransformerEnd.connectionKind'), rdflib.URIRef (CIM_NS + 'WindingConnection.Y')))  # TODO: cim:WindingConnection.Y?
        g.add ((end, rdflib.URIRef (CIM_NS + 'TransformerEnd.grounded'), rdflib.Literal(True, datatype=CIM.Boolean)))
      g.add ((end, rdflib.URIRef (CIM_NS + 'TransformerEnd.rground'), rdflib.Literal(0.0, datatype=CIM.Resistance)))
      g.add ((end, rdflib.URIRef (CIM_NS + 'TransformerEnd.xground'), rdflib.Literal(0.0, datatype=CIM.Reactance)))
      bv = rdflib.URIRef (kvbase_ids[str(wdg['kvs'][idx])])
      g.add ((end, rdflib.URIRef (CIM_NS + 'TransformerEnd.BaseVoltage'), bv))
      bus1 = rdflib.URIRef(busids[str(row[0])])
      g.add ((end, rdflib.URIRef (EMT_NS + 'TransformerEnd.ConnectivityNode'), bus1))

    # write mesh impedance
    kvbase = wdg['kvs'][0]
    zbase = kvbase * kvbase / wdg['s12']
    rmesh = zbase * wdg['r12']
    xmesh = zbase * wdg['x12']
    meshname = '{:s}_Mesh'.format (key)
    ID = GetCIMID('TransformerMeshImpedance', meshname, uuids)
    mesh = rdflib.URIRef (ID)
    g.add ((mesh, rdflib.RDF.type, rdflib.URIRef (CIM_NS + 'TransformerMeshImpedance')))
    g.add ((mesh, rdflib.URIRef (CIM_NS + 'IdentifiedObject.name'), rdflib.Literal(meshname, datatype=CIM.String)))
    g.add ((mesh, rdflib.URIRef (CIM_NS + 'IdentifiedObject.mRID'), rdflib.Literal(ID, datatype=CIM.String)))
    g.add ((mesh, rdflib.URIRef (CIM_NS + 'TransformerMeshImpedance.FromTransformerEnd'), ends[0]))
    g.add ((mesh, rdflib.URIRef (CIM_NS + 'TransformerMeshImpedance.ToTransformerEnd'), ends[1]))
    g.add ((mesh, rdflib.URIRef (CIM_NS + 'TransformerMeshImpedance.r'), rdflib.Literal(rmesh, datatype=CIM.Resistance)))
    g.add ((mesh, rdflib.URIRef (CIM_NS + 'TransformerMeshImpedance.r0'), rdflib.Literal(rmesh, datatype=CIM.Resistance)))
    g.add ((mesh, rdflib.URIRef (CIM_NS + 'TransformerMeshImpedance.x'), rdflib.Literal(xmesh, datatype=CIM.Reactance)))
    g.add ((mesh, rdflib.URIRef (CIM_NS + 'TransformerMeshImpedance.x0'), rdflib.Literal(xmesh, datatype=CIM.Reactance)))

    # write default core branch
    kvbase = wdg['kvs'][1]
    ybase = mva / kvbase / kvbase  #TODO: the default core parameters are based on actual MVA rating, not the 100-MVA system base
    bcore = XFMR_IMAG_PU * ybase
    gcore = XFMR_INLL_PU * ybase
    corename = '{:s}_Core'.format (key)
    ID = GetCIMID('TransformerCoreAdmittance', corename, uuids)
    core = rdflib.URIRef (ID)
    g.add ((core, rdflib.RDF.type, rdflib.URIRef (CIM_NS + 'TransformerCoreAdmittance')))
    g.add ((core, rdflib.URIRef (CIM_NS + 'IdentifiedObject.name'), rdflib.Literal(corename, datatype=CIM.String)))
    g.add ((core, rdflib.URIRef (CIM_NS + 'IdentifiedObject.mRID'), rdflib.Literal(ID, datatype=CIM.String)))
    g.add ((core, rdflib.URIRef (CIM_NS + 'TransformerCoreAdmittance.TransformerEnd'), ends[1]))
    g.add ((core, rdflib.URIRef (CIM_NS + 'TransformerCoreAdmittance.g'), rdflib.Literal(gcore, datatype=CIM.Conductance)))
    g.add ((core, rdflib.URIRef (CIM_NS + 'TransformerCoreAdmittance.g0'), rdflib.Literal(gcore, datatype=CIM.Conductance)))
    g.add ((core, rdflib.URIRef (CIM_NS + 'TransformerCoreAdmittance.b'), rdflib.Literal(bcore, datatype=CIM.Susceptance)))
    g.add ((core, rdflib.URIRef (CIM_NS + 'TransformerCoreAdmittance.b0'), rdflib.Literal(bcore, datatype=CIM.Susceptance)))

    # write default saturation curve
    satname = '{:s}_Sat'.format (key)
    ID = GetCIMID('TransformerSaturation', satname, uuids)
    sat = rdflib.URIRef (ID)
    g.add ((sat, rdflib.RDF.type, rdflib.URIRef (EMT_NS + 'TransformerSaturation')))
    g.add ((sat, rdflib.URIRef (CIM_NS + 'IdentifiedObject.name'), rdflib.Literal(satname, datatype=CIM.String)))
    g.add ((sat, rdflib.URIRef (CIM_NS + 'IdentifiedObject.mRID'), rdflib.Literal(ID, datatype=CIM.String)))
    g.add ((sat, rdflib.URIRef (EMT_NS + 'TransformerSaturation.TransformerCoreAdmittance'), core))
    g.add ((sat, rdflib.URIRef (CIM_NS + 'Curve.curveStyle'), rdflib.URIRef (CIM_NS + 'CurveStyle.straightLineYValues')))
    g.add ((sat, rdflib.URIRef (CIM_NS + 'Curve.xUnit'), rdflib.URIRef (CIM_NS + 'UnitSymbol.A')))
    g.add ((sat, rdflib.URIRef (CIM_NS + 'Curve.y1Unit'), rdflib.URIRef (CIM_NS + 'UnitSymbol.Vs')))
    g.add ((sat, rdflib.URIRef (CIM_NS + 'Curve.xMultiplier'), rdflib.URIRef (CIM_NS + 'UnitMultiplier.none')))
    g.add ((sat, rdflib.URIRef (CIM_NS + 'Curve.y1Multiplier'), rdflib.URIRef (CIM_NS + 'UnitMultiplier.none')))
    ibase_peak = 1.0e3 * XFMR_IMAG_PU * SQRT2 * mva / kvbase / SQRT3
    fbase_peak = 1.0e3 * SQRT2 * kvbase / SQRT3 / WFREQ
    i1 = XFMR_VSAT_PU * ibase_peak
    f1 = XFMR_VSAT_PU * fbase_peak
    aircore = XFMR_AIRCORE * wdg['x12']* kvbase * kvbase / wdg['s12'] / WFREQ  # leakage inductance referred to this lower-voltage winding
    i2 = i1 + 100.0
    f2 = f1 + 100.0 * aircore
    #print ('SAT: Ib={:.6f} Fb={:.6f} Lac={:.6f} I1={:.6f} I2={:.6f} F1={:.6f} F2={:.6f}'.format (ibase_peak, fbase_peak, aircore, i1, i2, f1, f2))
    pt = rdflib.BNode()
    g.add ((pt, rdflib.RDF.type, rdflib.URIRef (CIM_NS + 'CurveData')))
    g.add ((pt, rdflib.URIRef (CIM_NS + 'CurveData.Curve'), sat))
    g.add ((pt, rdflib.URIRef (CIM_NS + 'CurveData.xvalue'), rdflib.Literal(i1, datatype=CIM.Float)))
    g.add ((pt, rdflib.URIRef (CIM_NS + 'CurveData.y1value'), rdflib.Literal(f1, datatype=CIM.Float)))
    pt = rdflib.BNode()
    g.add ((pt, rdflib.RDF.type, rdflib.URIRef (CIM_NS + 'CurveData')))
    g.add ((pt, rdflib.URIRef (CIM_NS + 'CurveData.Curve'), sat))
    g.add ((pt, rdflib.URIRef (CIM_NS + 'CurveData.xvalue'), rdflib.Literal(i2, datatype=CIM.Float)))
    g.add ((pt, rdflib.URIRef (CIM_NS + 'CurveData.y1value'), rdflib.Literal(f2, datatype=CIM.Float)))

  # write the generators: synchronous machine, generating unit, exciter, governor, stabilizer
  with open(DYNAMIC_SETTINGS_FILE, 'r') as file:
    dyn_settings = json.load (file)
  nsolar = 0
  nwind = 0
  nthermal = 0
  nhydro = 0
  nnuclear = 0
  for row in tables['GENERATOR']['data']:
    if row[7] < 1:
      continue
    bus1 = rdflib.URIRef(busids[str(row[0])])
    kvbase = bus_kvbases[row[0]]
    mvabase = row[6]
    bv = rdflib.URIRef (kvbase_ids[str(kvbase)])
    ckt = row[1].strip()
    key = '{:d}_{:s}'.format (row[0], ckt)
    ftype = 'ThermalGeneratingUnit'
    if key in case['wind_units']:
      ftype = 'PowerElectronicsWindUnit'
      nwind += 1
    elif key in case['solar_units']:
      ftype = 'PhotoVoltaicUnit'
      nsolar += 1
    elif key in case['hydro_units']:
      ftype = 'HydroGeneratingUnit'
      nhydro += 1
    elif key in case['nuclear_units']:
      ftype = 'NuclearGeneratingUnit'
      nnuclear += 1
    else:
      nthermal += 1

    if ftype in ['NuclearGeneratingUnit', 'ThermalGeneratingUnit', 'HydroGeneratingUnit']:
      unitID = GetCIMID(ftype, key, uuids)
      un = rdflib.URIRef (unitID)
      g.add ((un, rdflib.RDF.type, rdflib.URIRef (CIM_NS + ftype)))
      g.add ((un, rdflib.URIRef (CIM_NS + 'IdentifiedObject.name'), rdflib.Literal(key, datatype=CIM.String)))
      g.add ((un, rdflib.URIRef (CIM_NS + 'IdentifiedObject.mRID'), rdflib.Literal(unitID, datatype=CIM.String)))
      g.add ((un, rdflib.URIRef (CIM_NS + 'Equipment.EquipmentContainer'), eq))
      g.add ((un, rdflib.URIRef (CIM_NS + 'Equipment.inService'), rdflib.Literal (True, datatype=CIM.Boolean)))
      g.add ((un, rdflib.URIRef (CIM_NS + 'GeneratingUnit.minOperatingP'), rdflib.Literal (0.0, datatype=CIM.ActivePower)))
      g.add ((un, rdflib.URIRef (CIM_NS + 'GeneratingUnit.maxOperatingP'), rdflib.Literal (1.0e6 * mvabase, datatype=CIM.ActivePower)))
      ID = GetCIMID('SynchronousMachine', key, uuids)
      sm = rdflib.URIRef (ID)
      g.add ((sm, rdflib.RDF.type, rdflib.URIRef (CIM_NS + 'SynchronousMachine')))
      g.add ((sm, rdflib.URIRef (CIM_NS + 'IdentifiedObject.name'), rdflib.Literal(key, datatype=CIM.String)))
      g.add ((sm, rdflib.URIRef (CIM_NS + 'IdentifiedObject.mRID'), rdflib.Literal(ID, datatype=CIM.String)))
      g.add ((sm, rdflib.URIRef (CIM_NS + 'Equipment.EquipmentContainer'), eq))
      g.add ((sm, rdflib.URIRef (CIM_NS + 'Equipment.inService'), rdflib.Literal (True, datatype=CIM.Boolean)))
      g.add ((sm, rdflib.URIRef (EMT_NS + 'ConductingEquipment.FromConnectivityNode'), bus1))
      g.add ((sm, rdflib.URIRef (EMT_NS + 'ConductingEquipment.ToConnectivityNode'), bus1))
      g.add ((sm, rdflib.URIRef (CIM_NS + 'ConductingEquipment.BaseVoltage'), bv))
      g.add ((sm, rdflib.URIRef (CIM_NS + 'RotatingMachine.GeneratingUnit'), un))
      maxQ = row[4]
      if maxQ <= 0.0:
        maxQ = 0.3122 * mvabase # 0.95 pf
      minQ = row[5]
      if minQ >= 0.0:
        minQ = -0.3122 * mvabase
      g.add ((sm, rdflib.URIRef (CIM_NS + 'RotatingMachine.p'), rdflib.Literal (1.0e6*row[2], datatype=CIM.ActivePower)))
      g.add ((sm, rdflib.URIRef (CIM_NS + 'RotatingMachine.q'), rdflib.Literal (1.0e6*row[3], datatype=CIM.ReactivePower)))
      g.add ((sm, rdflib.URIRef (CIM_NS + 'RotatingMachine.ratedS'), rdflib.Literal (1.0e6*mvabase, datatype=CIM.ApparentPower)))
      g.add ((sm, rdflib.URIRef (CIM_NS + 'RotatingMachine.ratedU'), rdflib.Literal (1.0e3*kvbase, datatype=CIM.Voltage)))
      g.add ((sm, rdflib.URIRef (CIM_NS + 'SynchronousMachine.earthing'), rdflib.Literal (False, datatype=CIM.Boolean)))
      g.add ((sm, rdflib.URIRef (CIM_NS + 'SynchronousMachine.earthingStarPointR'), rdflib.Literal (0.0, datatype=CIM.Resistance)))
      g.add ((sm, rdflib.URIRef (CIM_NS + 'SynchronousMachine.earthingStarPointX'), rdflib.Literal (0.0, datatype=CIM.Reactance)))
      g.add ((sm, rdflib.URIRef (CIM_NS + 'SynchronousMachine.maxQ'), rdflib.Literal (1.0e6*maxQ, datatype=CIM.ReactivePower)))
      g.add ((sm, rdflib.URIRef (CIM_NS + 'SynchronousMachine.minQ'), rdflib.Literal (1.0e6*minQ, datatype=CIM.ReactivePower)))
      g.add ((sm, rdflib.URIRef (CIM_NS + 'SynchronousMachine.operatingMode'), rdflib.URIRef (CIM_NS + 'SynchronousMachineOperatingMode.generator')))
      g.add ((sm, rdflib.URIRef (CIM_NS + 'SynchronousMachine.type'), rdflib.URIRef (CIM_NS + 'SynchronousMachineKind.generator')))
      dynID = GetCIMID('SynchronousMachineTimeConstantReactance', key, uuids)
      dyn = create_machine_dynamics (g, 'SynchronousMachineTimeConstantReactance', key, uuids)
      exc = create_machine_dynamics (g, 'ExcST1A', key, uuids)
      pss = create_machine_dynamics (g, 'PssIEEE1A', key, uuids)
      gov = create_machine_dynamics (g, 'GovSteamSGO', key, uuids)
      append_dynamic_parameters (g, dyn, dyn_settings, ['SynchronousMachineTimeConstantReactance', 'SynchronousMachineDetailed', 
                                                        'RotatingMachineDynamics', 'DynamicsFunctionBlock'])
      append_dynamic_parameters (g, exc, dyn_settings, ['ExcST1A', 'DynamicsFunctionBlock'])
      append_dynamic_parameters (g, pss, dyn_settings, ['PssIEEE1A', 'DynamicsFunctionBlock'])
      append_dynamic_parameters (g, gov, dyn_settings, ['GovSteamSGO', 'DynamicsFunctionBlock'])
      g.add ((pss, rdflib.URIRef (CIM_NS + 'PowerSystemStabilizerDynamics.ExcitationSystemDynamics'), exc))
      g.add ((exc, rdflib.URIRef (CIM_NS + 'ExcitationSystemDynamics.SynchronousMachineDynamics'), dyn))
      g.add ((gov, rdflib.URIRef (CIM_NS + 'TurbineGovernorDynamics.SynchronousMachineDynamics'), dyn))
      g.add ((dyn, rdflib.URIRef (CIM_NS + 'SynchronousMachineDynamics.SynchronousMachine'), sm))
      g.add ((gov, rdflib.URIRef (CIM_NS + 'GovSteamSGO.mwbase'), rdflib.Literal (mvabase, datatype=CIM.ActivePower)))
    else:
      ID = GetCIMID('PowerElectronicsConnection', key, uuids)
      pec = rdflib.URIRef (ID)
      g.add ((pec, rdflib.RDF.type, rdflib.URIRef (CIM_NS + 'PowerElectronicsConnection')))
      g.add ((pec, rdflib.URIRef (CIM_NS + 'IdentifiedObject.name'), rdflib.Literal(key, datatype=CIM.String)))
      g.add ((pec, rdflib.URIRef (CIM_NS + 'IdentifiedObject.mRID'), rdflib.Literal(ID, datatype=CIM.String)))
      g.add ((pec, rdflib.URIRef (CIM_NS + 'Equipment.EquipmentContainer'), eq))
      g.add ((pec, rdflib.URIRef (CIM_NS + 'Equipment.inService'), rdflib.Literal (True, datatype=CIM.Boolean)))
      g.add ((pec, rdflib.URIRef (EMT_NS + 'ConductingEquipment.FromConnectivityNode'), bus1))
      g.add ((pec, rdflib.URIRef (EMT_NS + 'ConductingEquipment.ToConnectivityNode'), bus1))
      g.add ((pec, rdflib.URIRef (CIM_NS + 'ConductingEquipment.BaseVoltage'), bv))
      g.add ((pec, rdflib.URIRef (CIM_NS + 'PowerElectronicsConnection.maxIFault'), rdflib.Literal (IBR_IFAULT, datatype=CIM.PU)))
      maxQ = row[4]
      if maxQ <= 0.0:
        maxQ = mvabase
      minQ = row[5]
      if minQ >= 0.0:
        minQ = -mvabase
      g.add ((pec, rdflib.URIRef (CIM_NS + 'PowerElectronicsConnection.maxQ'), rdflib.Literal (1.0e6*maxQ, datatype=CIM.ReactivePower)))
      g.add ((pec, rdflib.URIRef (CIM_NS + 'PowerElectronicsConnection.minQ'), rdflib.Literal (1.0e6*minQ, datatype=CIM.ReactivePower)))
      g.add ((pec, rdflib.URIRef (CIM_NS + 'PowerElectronicsConnection.p'), rdflib.Literal (1.0e6*row[2], datatype=CIM.ActivePower)))
      g.add ((pec, rdflib.URIRef (CIM_NS + 'PowerElectronicsConnection.q'), rdflib.Literal (1.0e6*row[3], datatype=CIM.ReactivePower)))
      g.add ((pec, rdflib.URIRef (CIM_NS + 'PowerElectronicsConnection.ratedS'), rdflib.Literal (1.0e6*mvabase, datatype=CIM.ApparentPower)))
      g.add ((pec, rdflib.URIRef (CIM_NS + 'PowerElectronicsConnection.ratedU'), rdflib.Literal (1.0e3*kvbase, datatype=CIM.Voltage)))
      unitID = GetCIMID(ftype, key, uuids)
      un = rdflib.URIRef (unitID)
      g.add ((un, rdflib.RDF.type, rdflib.URIRef (CIM_NS + ftype)))
      g.add ((un, rdflib.URIRef (CIM_NS + 'IdentifiedObject.name'), rdflib.Literal(key, datatype=CIM.String)))
      g.add ((un, rdflib.URIRef (CIM_NS + 'IdentifiedObject.mRID'), rdflib.Literal(ID, datatype=CIM.String)))
      g.add ((un, rdflib.URIRef (CIM_NS + 'Equipment.EquipmentContainer'), eq))
      g.add ((un, rdflib.URIRef (CIM_NS + 'Equipment.inService'), rdflib.Literal (True, datatype=CIM.Boolean)))
      g.add ((un, rdflib.URIRef (CIM_NS + 'PowerElectronicsUnit.PowerElectronicsConnection'), pec))
      g.add ((un, rdflib.URIRef (CIM_NS + 'PowerElectronicsUnit.maxP'), rdflib.Literal (1.0e6*row[6], datatype=CIM.ActivePower)))
      g.add ((un, rdflib.URIRef (CIM_NS + 'PowerElectronicsUnit.minP'), rdflib.Literal (0.0, datatype=CIM.ActivePower)))  # TODO: parse PT and PB
      reecID = GetCIMID('WeccREECA', key, uuids)
      append_wecc_dynamics (g, key, reecID, pec, 'WeccREECA', dyn_settings)
      repcID = GetCIMID('WeccREPCA', key, uuids)
      append_wecc_dynamics (g, key, repcID, pec, 'WeccREPCA', dyn_settings)
      regcID = GetCIMID('WeccREGCA', key, uuids)
      append_wecc_dynamics (g, key, regcID, pec, 'WeccREGCA', dyn_settings)
      if ftype in ['PowerElectronicsWindUnit']:
        araID = GetCIMID('WeccWTGARA', key, uuids)
        append_wecc_dynamics (g, key, araID, pec, 'WeccWTGARA', dyn_settings)
        taID = GetCIMID('WeccWTGTA', key, uuids)
        append_wecc_dynamics (g, key, taID, pec, 'WeccWTGTA', dyn_settings)

  print ('{:d} thermal, {:d} hydro, {:d} nuclear, {:d} solar, {:d} wind generators'.format (nthermal, nhydro, nnuclear, nsolar, nwind))

  # save the XML with mRIDs for re-use
  g.serialize (destination=case['cimfile'], format='pretty-xml', max_depth=1)

  #print("Bound Namespaces:")
  #for prefix, namespace_uri in g.namespaces():
  #  print(f"  Prefix: {prefix}, URI: {namespace_uri}")

  print('saving instance mRIDs to ', fuidname)
  fuid = open(fuidname, 'w')
  for key, val in uuids.items():
      print('{:s},{:s}'.format(key.replace(':', ',', 1), val), file=fuid)
  fuid.close()

def print_table (table_name):
  table = tables[table_name]
  if table is None:
    print ('***', table_name, 'not found')
    return
  print (table_name, 'has', len(table['data']), 'rows of', table['col_names'])
  if table_name == 'TRANSFORMER':
    for i in range (len(table['data'])):
      print (table['data'][i], table['winding_data'][i])
  else:
    for row in table['data']:
      print (row)

def read_version_33_34(rdr,sections,bTwoTitles):
  for section in sections:
    sect = sections[section]
    columns = sect['columns']
    column_names = ','.join([columns[i]['Name'] for i in range(len(columns))])
    print ('Table "{:s}" has {:d} raw columns, using {:d}: {:s}'.format (section, sect['column_count'], len(columns), column_names))
  title = ','.join(next(reader))
  print('MVA base = {:.1f}, Title: {:s}'.format(baseMVA, title))
  if bTwoTitles:
    title = ','.join(next(reader))
    print ('Second Title: ', title)
  table = None
  bTransformer = False
  for row in reader:
    #print (row)
    if '@!' in row[0]:
      continue
    if len(row) > 1 and 'END OF' in row[0] and 'BEGIN' in row[1]: # start a new table
      i1 = row[1].find('BEGIN') + 6
      i2 = row[1].find(' DATA')
      table_name = row[1][i1:i2]
      if table_name in sections:
        sect = sections[table_name]
        n_columns = len(sect['columns'])
        total_columns = sect['column_count']
        column_names = [sect['columns'][i]['Name'] for i in range(n_columns)]
        column_indices = [sect['columns'][i]['Index'] for i in range(n_columns)]
        column_types = [sect['columns'][i]['Type'] for i in range(n_columns)]
        print ('found', table_name, 'data with', total_columns, 'columns, using', n_columns)
        print ('  column_names:', column_names)
        print ('  column_index:', column_indices)
        print ('  column_types:', column_types)
        # create a new table to hold the data of interest
        table = {'col_names': column_names, 'col_types': column_types, 'data': []}
        if table_name == 'TRANSFORMER':
          table['winding_data'] = [] # impedances, ratings, and taps on extra lines
          bTransformer = True
        else:
          bTransformer = False
        tables[table_name] = table
        print (table)
      else:
        print ('ignoring', table_name, 'raw file data')
        table = None
    elif table is not None:
      data = []
      ncol_read = len(row)
      for i in range(n_columns):
        idx = column_indices[i]
        if idx >= ncol_read:
          print ('** need column index {:d} but read only {:d} columns a'.format (idx, ncol_read))
          quit()
        val = row[idx]
        if column_types[i] == 'Float':
          data.append(float(val))
        elif column_types[i] == 'Integer':
          data.append(int(val))
        else:
          data.append(val.strip('\' '))
      if bTransformer: # impedance and winding data is provided on extra lines
        #print (data)
        row = next(reader)
        #print (row)
        ncol_read = len(row)
        if data[2] > 0.0:
          if ncol_read > 8:
            nwdgs = 3
            winding_data = {'nwdgs': nwdgs, 'r12':float(row[0]), 'x12':float(row[1]), 's12':float(row[2]),
                            'r23':float(row[3]), 'x23':float(row[4]), 's23':float(row[5]),
                            'r13':float(row[6]), 'x13':float(row[6]), 's13':float(row[7]), 
                            'taps':[], 'kvs':[], 'mvas':[]}
          else:
            print ('** need 9 impedance values for a 3-winding transformer, but read only {:d}'.format (ncol_read))
            quit()
        else:
          if ncol_read > 2:
            nwdgs = 2
            winding_data = {'nwdgs': nwdgs, 'r12':float(row[0]), 'x12':float(row[1]), 's12':float(row[2]), 'taps':[], 'kvs':[], 'mvas':[]}
          else:
            print ('** need 3 impedance values for a 2-winding transformer, but read only {:d}'.format (ncol_read))
            quit()
        for i in range(nwdgs):
          row = next(reader)
          ncol_read = len(row)
          winding_data['taps'].append(float(row[0]))
          winding_data['kvs'].append(float(row[1])) # this may be zero, in which case take from the bus nominal voltages
          if ncol_read > 5:
            winding_data['mvas'].append(float(row[5])) # this may still be zero in the rawfile
          else:
            winding_data['mvas'].append(0.0)
        table['winding_data'].append (winding_data)
      table['data'].append (data)

#  print_table ('BUS')
#  print_table ('LOAD')
#  print_table ('FIXED SHUNT')
#  print_table ('SWITCHED SHUNT')
#  print_table ('GENERATOR')
#  print_table ('BRANCH')
#  print_table ('TRANSFORMER')

if __name__ == '__main__':
  case_id = 0
  if len(sys.argv) > 1:
    case_id = int(sys.argv[1])

  with open(METAFILE, 'r') as file:
    meta = json.load (file)

  case = CASES[case_id]
  with open(case['rawfile'], 'r') as csvfile:
    reader = csv.reader(csvfile, quotechar="'") # don't use " because it causes problems for CSV reader in title lines
    row = next(reader)
    baseMVA = float(row[1])
    raw_version = int(row[2])
    if raw_version == 33:
      read_version_33_34 (reader, meta['version_sections']['33'], bTwoTitles=False)
    elif raw_version == 34:
      read_version_33_34 (reader, meta['version_sections']['34'], bTwoTitles=True)
    else:
      print ('Unknown RAW File Version = {:d} from {:s}'.format (raw_version, case['rawfile']))
      quit()

  for bus in tables['BUS']['data']:
    bus_kvbases[bus[0]] = bus[2]
    kvbases['BV_{:.2f}'.format(bus[2])] = bus[2]

  print ('All kV Bases =', kvbases)

  create_cim_xml (tables, kvbases, bus_kvbases, baseMVA, case)
#  print ('Bus kV Bases =', bus_kvbases)
  

