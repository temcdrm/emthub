# Copyright (C) 2025-2026 Meltran, Inc

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
from otsrdflib import OrderedTurtleSerializer

from .cim_support import load_dynamics_defaults
from .cim_support import load_psse_dyrfile 
from .cim_support import load_dynamics_mapping
from .cim_support import summarize_psse_dyrfile
from .cim_support import match_dyr_generators
from .cim_sparql import adhoc_sparql_dict

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

def append_xml_wecc_dynamics (g, key, ID, pec, leaf_class, dyn_defaults, attmap, dyr_row):
  #print (attmap)
  #print (dyr_row)
  leaf = rdflib.URIRef (ID)
  g.add ((leaf, rdflib.RDF.type, rdflib.URIRef (CIM_NS + leaf_class)))
  g.add ((leaf, rdflib.URIRef (CIM_NS + 'IdentifiedObject.name'), rdflib.Literal(key, datatype=CIM_NS+'String')))
  g.add ((leaf, rdflib.URIRef (CIM_NS + 'IdentifiedObject.mRID'), rdflib.Literal(ID, datatype=CIM_NS+'String')))
  g.add ((leaf, rdflib.URIRef (CIM_NS + 'WeccDynamics.PowerElectronicsConnection'), pec))
  for tag in dyn_defaults['DynamicsFunctionBlock']:
    row = dyn_defaults['DynamicsFunctionBlock'][tag]
    if row[0] is not None:
      g.add ((leaf, rdflib.URIRef (CIM_NS + 'DynamicsFunctionBlock.{:s}'.format(tag)), rdflib.Literal(row[0], datatype=CIM_NS+row[1])))
  if leaf_class == 'WeccWTGTA': # only dshaft comes directly from the dyr file
    h = dyr_row[0]
    ht = h * dyr_row[2]
    hg = h - ht
    freq = dyr_row[3]
    kshaft = 2*ht*hg*(2*math.pi*freq)**2 / h
    dshaft = dyr_row[4]
    g.add ((leaf, rdflib.URIRef (CIM_NS + 'WeccWTGTA.dshaft'), rdflib.Literal(dshaft, datatype=CIM_NS+'PU')))
    g.add ((leaf, rdflib.URIRef (CIM_NS + 'WeccWTGTA.kshaft'), rdflib.Literal(kshaft, datatype=CIM_NS+'PU')))
    g.add ((leaf, rdflib.URIRef (CIM_NS + 'WeccWTGTA.ht'), rdflib.Literal(ht, datatype=CIM_NS+'Seconds')))
    g.add ((leaf, rdflib.URIRef (CIM_NS + 'WeccWTGTA.hg'), rdflib.Literal(hg, datatype=CIM_NS+'Seconds')))
    return
  for tag in dyn_defaults[leaf_class]:
    row = dyn_defaults[leaf_class][tag]
    if row[0] is not None:
      att = '{:s}.{:s}'.format(leaf_class, tag)
      val = row[0]
      unit = row[1]
      if att in attmap:
        idx = attmap[att]
        if unit == 'Boolean':
          val = bool(dyr_row[idx])
        elif unit == 'Integer':
          val = int(dyr_row[idx])
        else:
          val = dyr_row[idx]
        #print ('Value supplied for', att, 'in column', idx, '=', dyr_row[idx])
      g.add ((leaf, rdflib.URIRef (CIM_NS + att), rdflib.Literal(val, datatype=CIM_NS+unit)))

def create_xml_machine_dynamics (g, leaf_class, key, uuids):
  ID = GetCIMID (leaf_class, key, uuids)
  leaf = rdflib.URIRef (ID)
  g.add ((leaf, rdflib.RDF.type, rdflib.URIRef (CIM_NS + leaf_class)))
  g.add ((leaf, rdflib.URIRef (CIM_NS + 'IdentifiedObject.name'), rdflib.Literal(key, datatype=CIM_NS+'String')))
  g.add ((leaf, rdflib.URIRef (CIM_NS + 'IdentifiedObject.mRID'), rdflib.Literal(ID, datatype=CIM_NS+'String')))
  return leaf

def append_xml_dynamic_parameters (g, leaf, dyn_defaults, sections, attmap, dyr_row):
  for sect in sections:
    for tag in dyn_defaults[sect]:
      row = dyn_defaults[sect][tag]
      if row[0] is not None:
        att = '{:s}.{:s}'.format(sect, tag)
        val = row[0]
        unit = row[1]
        if att in attmap:
          idx = attmap[att]
          if unit == 'Boolean':
            val = bool(dyr_row[idx])
          elif unit == 'Integer':
            val = int(dyr_row[idx])
          else:
            val = dyr_row[idx]
        if unit.endswith('Kind'):
          g.add ((leaf, rdflib.URIRef (CIM_NS + att), rdflib.URIRef (CIM_NS + '{:s}.{:s}'.format(unit, val))))
        else:
          g.add ((leaf, rdflib.URIRef (CIM_NS + att), rdflib.Literal(val, datatype=CIM_NS+unit)))

def create_cim_rdf (tables, kvbases, bus_kvbases, baseMVA, case):
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
    #print ('reading instance mRIDs from ', fuidname)
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

  eq = rdflib.URIRef (case['id']) # no prefix with urn:uuid:

  g.add ((eq, rdflib.RDF.type, rdflib.URIRef (CIM_NS + 'EquipmentContainer')))
  g.add ((eq, rdflib.URIRef (CIM_NS + 'IdentifiedObject.name'), rdflib.Literal(case['name'], datatype=CIM.String)))
  g.add ((eq, rdflib.URIRef (CIM_NS + 'IdentifiedObject.mRID'), rdflib.Literal(case['id'], datatype=CIM.String)))

  # write the OperationalLimitTypes to be shared
  olNormalID = GetCIMID('OperationalLimitType', 'Normal', uuids)
  olNormal = rdflib.URIRef (olNormalID)
  g.add ((olNormal, rdflib.RDF.type, rdflib.URIRef (CIM_NS + 'OperationalLimitType')))
  g.add ((olNormal, rdflib.URIRef (CIM_NS + 'IdentifiedObject.name'), rdflib.Literal('Normal', datatype=CIM.String)))
  g.add ((olNormal, rdflib.URIRef (CIM_NS + 'IdentifiedObject.mRID'), rdflib.Literal(olNormalID, datatype=CIM.String)))
  g.add ((olNormal, rdflib.URIRef (CIM_NS + 'OperationalLimitType.isInfiniteDuration'), rdflib.Literal(True, datatype=CIM.Boolean)))
  g.add ((olNormal, rdflib.URIRef (CIM_NS + 'OperationalLimitType.direction'), rdflib.URIRef (CIM_NS + 'OperationalLimitDirectionKind.absoluteValue')))

  olShortTermID = GetCIMID('OperationalLimitType', 'ShortTerm', uuids)
  olShortTerm = rdflib.URIRef (olShortTermID)
  g.add ((olShortTerm, rdflib.RDF.type, rdflib.URIRef (CIM_NS + 'OperationalLimitType')))
  g.add ((olShortTerm, rdflib.URIRef (CIM_NS + 'IdentifiedObject.name'), rdflib.Literal('ShortTerm', datatype=CIM.String)))
  g.add ((olShortTerm, rdflib.URIRef (CIM_NS + 'IdentifiedObject.mRID'), rdflib.Literal(olShortTermID, datatype=CIM.String)))
  g.add ((olShortTerm, rdflib.URIRef (CIM_NS + 'OperationalLimitType.isInfiniteDuration'), rdflib.Literal(False, datatype=CIM.Boolean)))
  g.add ((olShortTerm, rdflib.URIRef (CIM_NS + 'OperationalLimitType.acceptableDuration'), rdflib.Literal(SHORT_TERM_SECONDS, datatype=CIM.Seconds)))
  g.add ((olShortTerm, rdflib.URIRef (CIM_NS + 'OperationalLimitType.direction'), rdflib.URIRef (CIM_NS + 'OperationalLimitDirectionKind.absoluteValue')))

  # write the base voltages
  kvbase_ids = {}
  for kvname, kv in kvbases.items():
    #print (kvname)
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
  if 'locfile' in case:
    if os.path.exists(case['locfile']):
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
        pt = rdflib.URIRef (ID+'_pt1') # rdflib.BNode()
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
    rate1mva = row[6]
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
        x0 = 3.0 * x1 # was 2.0 * x1
        b0ch = 0.6 * b1ch
#        if kvbase >= 345.0:
#          length = M_PER_MILE * x1 / 0.6
#        else:
#          length = M_PER_MILE * x1 / 0.8
        tau1 = math.sqrt (x1 * b1ch) / WFREQ
        length = tau1 * 3.0e8 * PU_WAVE_SPEED
      else: # underground
        r0 = r1
        x0 = x1
        b0ch = b1ch
        length = M_PER_MILE * x1 / 0.2
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
    # operational limits on this branch
    olsID = GetCIMID('OperationalLimitSet', key, uuids)
    ols = rdflib.URIRef (olsID)
    g.add ((ols, rdflib.RDF.type, rdflib.URIRef (CIM_NS + 'OperationalLimitSet')))
    g.add ((ols, rdflib.URIRef (CIM_NS + 'IdentifiedObject.name'), rdflib.Literal(key, datatype=CIM.String)))
    g.add ((ols, rdflib.URIRef (CIM_NS + 'IdentifiedObject.mRID'), rdflib.Literal(olsID, datatype=CIM.String)))
    g.add ((ols, rdflib.URIRef (EMT_NS + 'OperationalLimitSet.ConductingEquipment'), ac))
    alkey = '{:s}_Normal'.format(key)
    alID = GetCIMID('ApparentPowerLimit', alkey, uuids)
    al = rdflib.URIRef (alID)
    g.add ((al, rdflib.RDF.type, rdflib.URIRef (CIM_NS + 'ApparentPowerLimit')))
    g.add ((al, rdflib.URIRef (CIM_NS + 'IdentifiedObject.name'), rdflib.Literal(alkey, datatype=CIM.String)))
    g.add ((al, rdflib.URIRef (CIM_NS + 'IdentifiedObject.mRID'), rdflib.Literal(alID, datatype=CIM.String)))
    g.add ((al, rdflib.URIRef (CIM_NS + 'OperationalLimit.OperationalLimitSet'), ols))
    g.add ((al, rdflib.URIRef (CIM_NS + 'OperationalLimit.OperationalLimitType'), olNormal))
    g.add ((al, rdflib.URIRef (CIM_NS + 'ApparentPowerLimit.value'), rdflib.Literal(rate1mva*1.0e6, datatype=CIM.ApparentPower)))
    if 'emergency_ratings' in case:
      if case['emergency_ratings'] == True:
        alkey = '{:s}_ShortTerm'.format(key)
        alID = GetCIMID('ApparentPowerLimit', alkey, uuids)
        al = rdflib.URIRef (alID)
        g.add ((al, rdflib.RDF.type, rdflib.URIRef (CIM_NS + 'ApparentPowerLimit')))
        g.add ((al, rdflib.URIRef (CIM_NS + 'IdentifiedObject.name'), rdflib.Literal(alkey, datatype=CIM.String)))
        g.add ((al, rdflib.URIRef (CIM_NS + 'IdentifiedObject.mRID'), rdflib.Literal(alID, datatype=CIM.String)))
        g.add ((al, rdflib.URIRef (CIM_NS + 'OperationalLimit.OperationalLimitSet'), ols))
        g.add ((al, rdflib.URIRef (CIM_NS + 'OperationalLimit.OperationalLimitType'), olShortTerm))
        g.add ((al, rdflib.URIRef (CIM_NS + 'ApparentPowerLimit.value'), rdflib.Literal(rate1mva*1.0e6*SHORT_TERM_SCALE, datatype=CIM.ApparentPower)))


  # write the switches (TODO: is this non-standard rawfile usage?)
  # write the branches
  if 'SYSTEM SWITCHING DEVICE' in tables:
    for row in tables['SYSTEM SWITCHING DEVICE']['data']:
      bus1 = rdflib.URIRef(busids[str(row[0])])
      bus2 = rdflib.URIRef(busids[str(row[1])])
      ckt = int(row[2])
      key = '{:d}_{:d}_{:d}'.format (row[0], row[1], ckt)
      ID = GetCIMID('DisconnectingCircuitBreaker', key, uuids)
      cb = rdflib.URIRef (ID)
      kvbase = bus_kvbases[row[0]]
      bv = rdflib.URIRef (kvbase_ids[str(kvbase)])
      g.add ((cb, rdflib.RDF.type, rdflib.URIRef (CIM_NS + 'DisconnectingCircuitBreaker')))
      g.add ((cb, rdflib.URIRef (CIM_NS + 'IdentifiedObject.name'), rdflib.Literal(key, datatype=CIM.String)))
      g.add ((cb, rdflib.URIRef (CIM_NS + 'IdentifiedObject.mRID'), rdflib.Literal(ID, datatype=CIM.String)))
      g.add ((cb, rdflib.URIRef (CIM_NS + 'Equipment.EquipmentContainer'), eq))
      g.add ((cb, rdflib.URIRef (CIM_NS + 'Equipment.inService'), rdflib.Literal (True, datatype=CIM.Boolean)))
      g.add ((cb, rdflib.URIRef (EMT_NS + 'ConductingEquipment.FromConnectivityNode'), bus1))
      g.add ((cb, rdflib.URIRef (EMT_NS + 'ConductingEquipment.ToConnectivityNode'), bus2))
      g.add ((cb, rdflib.URIRef (CIM_NS + 'ConductingEquipment.BaseVoltage'), bv))
      # operational limits on this branch
      rate1mva = row[4]
      olsID = GetCIMID('OperationalLimitSet', key, uuids)
      ols = rdflib.URIRef (olsID)
      g.add ((ols, rdflib.RDF.type, rdflib.URIRef (CIM_NS + 'OperationalLimitSet')))
      g.add ((ols, rdflib.URIRef (CIM_NS + 'IdentifiedObject.name'), rdflib.Literal(key, datatype=CIM.String)))
      g.add ((ols, rdflib.URIRef (CIM_NS + 'IdentifiedObject.mRID'), rdflib.Literal(olsID, datatype=CIM.String)))
      g.add ((ols, rdflib.URIRef (EMT_NS + 'OperationalLimitSet.ConductingEquipment'), cb))
      alkey = '{:s}_Normal'.format(key)
      alID = GetCIMID('ApparentPowerLimit', alkey, uuids)
      al = rdflib.URIRef (alID)
      g.add ((al, rdflib.RDF.type, rdflib.URIRef (CIM_NS + 'ApparentPowerLimit')))
      g.add ((al, rdflib.URIRef (CIM_NS + 'IdentifiedObject.name'), rdflib.Literal(alkey, datatype=CIM.String)))
      g.add ((al, rdflib.URIRef (CIM_NS + 'IdentifiedObject.mRID'), rdflib.Literal(alID, datatype=CIM.String)))
      g.add ((al, rdflib.URIRef (CIM_NS + 'OperationalLimit.OperationalLimitSet'), ols))
      g.add ((al, rdflib.URIRef (CIM_NS + 'OperationalLimit.OperationalLimitType'), olNormal))
      g.add ((al, rdflib.URIRef (CIM_NS + 'ApparentPowerLimit.value'), rdflib.Literal(rate1mva*1.0e6, datatype=CIM.ApparentPower)))

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

  print ('Creating', len(LoadResponseCharacteristics), 'load response characteristics')
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
    vgrp = 'Yy'
    clocks = [0, 0]
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
        g.add ((end, rdflib.URIRef (CIM_NS + 'PowerTransformerEnd.connectionKind'), rdflib.URIRef (CIM_NS + 'WindingConnection.D')))
        g.add ((end, rdflib.URIRef (CIM_NS + 'TransformerEnd.grounded'), rdflib.Literal(False, datatype=CIM.Boolean)))
      else:
        g.add ((end, rdflib.URIRef (CIM_NS + 'PowerTransformerEnd.connectionKind'), rdflib.URIRef (CIM_NS + 'WindingConnection.Y')))
        g.add ((end, rdflib.URIRef (CIM_NS + 'TransformerEnd.grounded'), rdflib.Literal(True, datatype=CIM.Boolean)))
      g.add ((end, rdflib.URIRef (CIM_NS + 'TransformerEnd.rground'), rdflib.Literal(0.0, datatype=CIM.Resistance)))
      g.add ((end, rdflib.URIRef (CIM_NS + 'TransformerEnd.xground'), rdflib.Literal(0.0, datatype=CIM.Reactance)))
      bv = rdflib.URIRef (kvbase_ids[str(wdg['kvs'][idx])])
      g.add ((end, rdflib.URIRef (CIM_NS + 'TransformerEnd.BaseVoltage'), bv))
      bus_wdg = rdflib.URIRef(busids[str(row[idx])])
      g.add ((end, rdflib.URIRef (EMT_NS + 'TransformerEnd.ConnectivityNode'), bus_wdg))
      tap = wdg['taps'][idx]
      if abs(1.0-tap) > 1.0e-8:
        rtcID = GetCIMID('RatioTapChanger', endkey, uuids)
        rtc = rdflib.URIRef (rtcID)
        step = (tap - 1.0) * 100.0 / STEP_VOLTAGE_INCREMENT
        if step > HIGH_STEP:
          step = HIGH_STEP
        elif step < LOW_STEP:
          step = LOW_STEP
        normalStep = round(step)
        g.add ((rtc, rdflib.RDF.type, rdflib.URIRef (CIM_NS + 'RatioTapChanger')))
        g.add ((rtc, rdflib.URIRef (CIM_NS + 'IdentifiedObject.name'), rdflib.Literal(endkey, datatype=CIM.String)))
        g.add ((rtc, rdflib.URIRef (CIM_NS + 'IdentifiedObject.mRID'), rdflib.Literal(rtcID, datatype=CIM.String)))
        g.add ((rtc, rdflib.URIRef (CIM_NS + 'TapChanger.highStep'), rdflib.Literal(HIGH_STEP, datatype=CIM.Integer)))
        g.add ((rtc, rdflib.URIRef (CIM_NS + 'TapChanger.lowStep'), rdflib.Literal(LOW_STEP, datatype=CIM.Integer)))
        g.add ((rtc, rdflib.URIRef (CIM_NS + 'TapChanger.neutralStep'), rdflib.Literal(0, datatype=CIM.Integer)))
        g.add ((rtc, rdflib.URIRef (CIM_NS + 'TapChanger.neutralU'), rdflib.Literal(wdg['kvs'][idx]*1.0e3, datatype=CIM.Voltage)))
        g.add ((rtc, rdflib.URIRef (CIM_NS + 'TapChanger.normalStep'), rdflib.Literal(normalStep, datatype=CIM.Integer)))
        g.add ((rtc, rdflib.URIRef (CIM_NS + 'TapChanger.step'), rdflib.Literal(step, datatype=CIM.Float)))
        g.add ((rtc, rdflib.URIRef (CIM_NS + 'RatioTapChanger.stepVoltageIncrement'), rdflib.Literal(STEP_VOLTAGE_INCREMENT, datatype=CIM.PerCent)))
        g.add ((rtc, rdflib.URIRef (CIM_NS + 'RatioTapChanger.TransformerEnd'), end))
      # operational limits on this transformer end
      olsID = GetCIMID('OperationalLimitSet', endkey, uuids)
      ols = rdflib.URIRef (olsID)
      g.add ((ols, rdflib.RDF.type, rdflib.URIRef (CIM_NS + 'OperationalLimitSet')))
      g.add ((ols, rdflib.URIRef (CIM_NS + 'IdentifiedObject.name'), rdflib.Literal(endkey, datatype=CIM.String)))
      g.add ((ols, rdflib.URIRef (CIM_NS + 'IdentifiedObject.mRID'), rdflib.Literal(olsID, datatype=CIM.String)))
      g.add ((ols, rdflib.URIRef (EMT_NS + 'OperationalLimitSet.TransformerEnd'), end))
      alkey = '{:s}_ONAN'.format(endkey)
      alID = GetCIMID('ApparentPowerLimit', alkey, uuids)
      al = rdflib.URIRef (alID)
      g.add ((al, rdflib.RDF.type, rdflib.URIRef (CIM_NS + 'ApparentPowerLimit')))
      g.add ((al, rdflib.URIRef (CIM_NS + 'IdentifiedObject.name'), rdflib.Literal(alkey, datatype=CIM.String)))
      g.add ((al, rdflib.URIRef (CIM_NS + 'IdentifiedObject.mRID'), rdflib.Literal(alID, datatype=CIM.String)))
      g.add ((al, rdflib.URIRef (CIM_NS + 'OperationalLimit.OperationalLimitSet'), ols))
      g.add ((al, rdflib.URIRef (CIM_NS + 'OperationalLimit.OperationalLimitType'), olNormal))
      g.add ((al, rdflib.URIRef (CIM_NS + 'ApparentPowerLimit.value'), rdflib.Literal(mva*1.0e6, datatype=CIM.ApparentPower)))
      if 'emergency_ratings' in case:
        if case['emergency_ratings'] == True:
          alkey = '{:s}_ONAN_ShortTerm'.format(endkey)
          alID = GetCIMID('ApparentPowerLimit', alkey, uuids)
          al = rdflib.URIRef (alID)
          g.add ((al, rdflib.RDF.type, rdflib.URIRef (CIM_NS + 'ApparentPowerLimit')))
          g.add ((al, rdflib.URIRef (CIM_NS + 'IdentifiedObject.name'), rdflib.Literal(alkey, datatype=CIM.String)))
          g.add ((al, rdflib.URIRef (CIM_NS + 'IdentifiedObject.mRID'), rdflib.Literal(alID, datatype=CIM.String)))
          g.add ((al, rdflib.URIRef (CIM_NS + 'OperationalLimit.OperationalLimitSet'), ols))
          g.add ((al, rdflib.URIRef (CIM_NS + 'OperationalLimit.OperationalLimitType'), olShortTerm))
          g.add ((al, rdflib.URIRef (CIM_NS + 'ApparentPowerLimit.value'), rdflib.Literal(mva*1.0e6*SHORT_TERM_SCALE, datatype=CIM.ApparentPower)))
          alkey = '{:s}_ONAF'.format(endkey)
          alID = GetCIMID('ApparentPowerLimit', alkey, uuids)
          al = rdflib.URIRef (alID)
          g.add ((al, rdflib.RDF.type, rdflib.URIRef (CIM_NS + 'ApparentPowerLimit')))
          g.add ((al, rdflib.URIRef (CIM_NS + 'IdentifiedObject.name'), rdflib.Literal(alkey, datatype=CIM.String)))
          g.add ((al, rdflib.URIRef (CIM_NS + 'IdentifiedObject.mRID'), rdflib.Literal(alID, datatype=CIM.String)))
          g.add ((al, rdflib.URIRef (CIM_NS + 'OperationalLimit.OperationalLimitSet'), ols))
          g.add ((al, rdflib.URIRef (CIM_NS + 'OperationalLimit.OperationalLimitType'), olNormal))
          g.add ((al, rdflib.URIRef (CIM_NS + 'ApparentPowerLimit.value'), rdflib.Literal(mva*1.0e6*ONAF_SCALE, datatype=CIM.ApparentPower)))
          alkey = '{:s}_ONAF_ShortTerm'.format(endkey)
          alID = GetCIMID('ApparentPowerLimit', alkey, uuids)
          al = rdflib.URIRef (alID)
          g.add ((al, rdflib.RDF.type, rdflib.URIRef (CIM_NS + 'ApparentPowerLimit')))
          g.add ((al, rdflib.URIRef (CIM_NS + 'IdentifiedObject.name'), rdflib.Literal(alkey, datatype=CIM.String)))
          g.add ((al, rdflib.URIRef (CIM_NS + 'IdentifiedObject.mRID'), rdflib.Literal(alID, datatype=CIM.String)))
          g.add ((al, rdflib.URIRef (CIM_NS + 'OperationalLimit.OperationalLimitSet'), ols))
          g.add ((al, rdflib.URIRef (CIM_NS + 'OperationalLimit.OperationalLimitType'), olShortTerm))
          g.add ((al, rdflib.URIRef (CIM_NS + 'ApparentPowerLimit.value'), rdflib.Literal(mva*1.0e6*ONAF_SCALE*SHORT_TERM_SCALE, datatype=CIM.ApparentPower)))
          alkey = '{:s}_OFAF'.format(endkey)
          alID = GetCIMID('ApparentPowerLimit', alkey, uuids)
          al = rdflib.URIRef (alID)
          g.add ((al, rdflib.RDF.type, rdflib.URIRef (CIM_NS + 'ApparentPowerLimit')))
          g.add ((al, rdflib.URIRef (CIM_NS + 'IdentifiedObject.name'), rdflib.Literal(alkey, datatype=CIM.String)))
          g.add ((al, rdflib.URIRef (CIM_NS + 'IdentifiedObject.mRID'), rdflib.Literal(alID, datatype=CIM.String)))
          g.add ((al, rdflib.URIRef (CIM_NS + 'OperationalLimit.OperationalLimitSet'), ols))
          g.add ((al, rdflib.URIRef (CIM_NS + 'OperationalLimit.OperationalLimitType'), olNormal))
          g.add ((al, rdflib.URIRef (CIM_NS + 'ApparentPowerLimit.value'), rdflib.Literal(mva*1.0e6*OFAF_SCALE, datatype=CIM.ApparentPower)))
          alkey = '{:s}_OFAF_ShortTerm'.format(endkey)
          alID = GetCIMID('ApparentPowerLimit', alkey, uuids)
          al = rdflib.URIRef (alID)
          g.add ((al, rdflib.RDF.type, rdflib.URIRef (CIM_NS + 'ApparentPowerLimit')))
          g.add ((al, rdflib.URIRef (CIM_NS + 'IdentifiedObject.name'), rdflib.Literal(alkey, datatype=CIM.String)))
          g.add ((al, rdflib.URIRef (CIM_NS + 'IdentifiedObject.mRID'), rdflib.Literal(alID, datatype=CIM.String)))
          g.add ((al, rdflib.URIRef (CIM_NS + 'OperationalLimit.OperationalLimitSet'), ols))
          g.add ((al, rdflib.URIRef (CIM_NS + 'OperationalLimit.OperationalLimitType'), olShortTerm))
          g.add ((al, rdflib.URIRef (CIM_NS + 'ApparentPowerLimit.value'), rdflib.Literal(mva*1.0e6*OFAF_SCALE*SHORT_TERM_SCALE, datatype=CIM.ApparentPower)))

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
    pt = rdflib.URIRef (ID+'_pt1') # rdflib.BNode()
    g.add ((pt, rdflib.RDF.type, rdflib.URIRef (CIM_NS + 'CurveData')))
    g.add ((pt, rdflib.URIRef (CIM_NS + 'CurveData.Curve'), sat))
    g.add ((pt, rdflib.URIRef (CIM_NS + 'CurveData.xvalue'), rdflib.Literal(i1, datatype=CIM.Float)))
    g.add ((pt, rdflib.URIRef (CIM_NS + 'CurveData.y1value'), rdflib.Literal(f1, datatype=CIM.Float)))
    pt = rdflib.URIRef (ID+'_pt2') # rdflib.BNode()
    g.add ((pt, rdflib.RDF.type, rdflib.URIRef (CIM_NS + 'CurveData')))
    g.add ((pt, rdflib.URIRef (CIM_NS + 'CurveData.Curve'), sat))
    g.add ((pt, rdflib.URIRef (CIM_NS + 'CurveData.xvalue'), rdflib.Literal(i2, datatype=CIM.Float)))
    g.add ((pt, rdflib.URIRef (CIM_NS + 'CurveData.y1value'), rdflib.Literal(f2, datatype=CIM.Float)))

  # write the generators: synchronous machine, generating unit, exciter, governor, stabilizer
  dyr_df = load_psse_dyrfile (case)
  if dyr_df is not None:
    dyr_summary = summarize_psse_dyrfile (dyr_df, case, bDetails=False)
    dyr = match_dyr_generators (dyr_df)
  dyn_defaults = load_dynamics_defaults ()
  dyn_mapping = load_dynamics_mapping ()
  dyr_used = {}
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
      if key in dyr:
        dyr_used[key] = True
        dyn = None
        exc = None
        pss = None
        gov = None
        used = []
        for mdl, row in dyr[key].items():
          cls = dyn_mapping[mdl]['CIMclass']
          used.append (cls)
          if cls.startswith ('SynchronousMachine'):
            dyn = create_xml_machine_dynamics (g, cls, key, uuids)
            append_xml_dynamic_parameters (g, dyn, dyn_defaults, [cls, 'SynchronousMachineDetailed', 'RotatingMachineDynamics', 'DynamicsFunctionBlock'], dyn_mapping[mdl]['AttMap'], row)
          elif cls.startswith ('Exc'):
            exc = create_xml_machine_dynamics (g, cls, key, uuids)
            append_xml_dynamic_parameters (g, exc, dyn_defaults, [cls, 'DynamicsFunctionBlock'], dyn_mapping[mdl]['AttMap'], row)
          elif cls.startswith ('Pss'):
            pss = create_xml_machine_dynamics (g, cls, key, uuids)
            append_xml_dynamic_parameters (g, pss, dyn_defaults, [cls, 'DynamicsFunctionBlock'], dyn_mapping[mdl]['AttMap'], row)
          elif cls.startswith ('Gov'):
            if 'Hydro' in cls and 'Hydro' not in ftype:
              print ('** non-hydro unit', key, 'has governor', cls, 'for', ftype)
            elif 'Hydro' not in cls and 'Hydro' in ftype:
              print ('** hydro unit', key, 'has governor', cls, 'for', ftype)
            gov = create_xml_machine_dynamics (g, cls, key, uuids)
            append_xml_dynamic_parameters (g, gov, dyn_defaults, [cls, 'DynamicsFunctionBlock'], dyn_mapping[mdl]['AttMap'], row)
            if 'mwbase' in dyn_defaults[cls]:
              att = '{:s}.mwbase'.format(cls)
              g.add ((gov, rdflib.URIRef (CIM_NS + att), rdflib.Literal (mvabase, datatype=CIM.ActivePower)))
          else:
            print ('** Unknown dynamics class', cls, 'for dyr model', mdl, 'generator', key)
        if dyn is not None:
          g.add ((dyn, rdflib.URIRef (CIM_NS + 'SynchronousMachineDynamics.SynchronousMachine'), sm))
          if gov is not None:
            g.add ((gov, rdflib.URIRef (CIM_NS + 'TurbineGovernorDynamics.SynchronousMachineDynamics'), dyn))
          if exc is not None:
            g.add ((exc, rdflib.URIRef (CIM_NS + 'ExcitationSystemDynamics.SynchronousMachineDynamics'), dyn))
            if pss is not None:
              g.add ((pss, rdflib.URIRef (CIM_NS + 'PowerSystemStabilizerDynamics.ExcitationSystemDynamics'), exc))
          #print ('machine dynamics for', key, used)
        else:
          print ('** missing machine dynamics for', key)
        if exc is None and pss is not None:
          print ('** power system stabilizer is missing excitation system for', key)
      else:
        print ('no machine dynamics found for', key, ftype)
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
      if key in dyr:
        dyr_used[key] = True
        used = []
        for mdl, row in dyr[key].items():
          cls = dyn_mapping[mdl]['CIMclass']
          used.append (cls)
          dynID = GetCIMID(cls, key, uuids)
          append_xml_wecc_dynamics (g, key, dynID, pec, cls, dyn_defaults, dyn_mapping[mdl]['AttMap'], row)
        #print ('wecc dynamics for', key, used)
      else:
        print ('no WECC dynamics found for', key, ftype)
  # warn of any unused dyr file entries
  if dyr_df is not None:
    dyr_unused = []
    for key in dyr:
      if key not in dyr_used:
        dyr_unused.append(key)
    if len(dyr_unused) > 0:
      print ('dyr entries for these generators were not used:') 
      print (' ', dyr_unused)
      print ('  (these units may have been flagged off-line in the raw file)')

  print ('{:d} thermal, {:d} hydro, {:d} nuclear, {:d} solar, {:d} wind generators'.format (nthermal, nhydro, nnuclear, nsolar, nwind))
  if nthermal+nhydro+nnuclear+nsolar+nwind < 1:
    if 'swingbus' in case:
      swingbus = int(case['swingbus'])
      print ('No Generators, need to write an EnergySource for swingbus', swingbus)
      bus1 = rdflib.URIRef(busids[case['swingbus']])
      kvbase = bus_kvbases[swingbus]
      bv = rdflib.URIRef (kvbase_ids[str(kvbase)])
      key = '{:d}_1'.format (swingbus)
      ID = GetCIMID('EnergySource', key, uuids)
      es = rdflib.URIRef (ID)
      g.add ((es, rdflib.RDF.type, rdflib.URIRef (CIM_NS + 'EnergySource')))
      g.add ((es, rdflib.URIRef (CIM_NS + 'IdentifiedObject.name'), rdflib.Literal(key, datatype=CIM.String)))
      g.add ((es, rdflib.URIRef (CIM_NS + 'IdentifiedObject.mRID'), rdflib.Literal(ID, datatype=CIM.String)))
      g.add ((es, rdflib.URIRef (CIM_NS + 'Equipment.EquipmentContainer'), eq))
      g.add ((es, rdflib.URIRef (CIM_NS + 'Equipment.inService'), rdflib.Literal (True, datatype=CIM.Boolean)))
      g.add ((es, rdflib.URIRef (EMT_NS + 'ConductingEquipment.FromConnectivityNode'), bus1))
      g.add ((es, rdflib.URIRef (EMT_NS + 'ConductingEquipment.ToConnectivityNode'), bus1))
      g.add ((es, rdflib.URIRef (CIM_NS + 'ConductingEquipment.BaseVoltage'), bv))
      g.add ((es, rdflib.URIRef (CIM_NS + 'EnergySource.nominalVoltage'), rdflib.Literal(1000.0 * kvbase, datatype=CIM.Voltage)))
      g.add ((es, rdflib.URIRef (CIM_NS + 'EnergySource.voltageMagnitude'), rdflib.Literal(1000.0 * kvbase, datatype=CIM.Voltage)))
      g.add ((es, rdflib.URIRef (CIM_NS + 'EnergySource.voltageAngle'), rdflib.Literal(0.0, datatype=CIM.AngleRadians)))
      g.add ((es, rdflib.URIRef (CIM_NS + 'EnergySource.r'), rdflib.Literal(0.0, datatype=CIM.Resistance)))
      g.add ((es, rdflib.URIRef (CIM_NS + 'EnergySource.x'), rdflib.Literal(0.001, datatype=CIM.Reactance)))
      g.add ((es, rdflib.URIRef (CIM_NS + 'EnergySource.r0'), rdflib.Literal(0.0, datatype=CIM.Resistance)))
      g.add ((es, rdflib.URIRef (CIM_NS + 'EnergySource.x0'), rdflib.Literal(0.001, datatype=CIM.Reactance)))

  # identify the generator plants with step-up transformers
  q = """SELECT DISTINCT ?name ?type ?bus ?rm_or_pec_id ?xfid ?vgroup ?enum ?endid WHERE {
   ?s c:IdentifiedObject.name ?name.
   ?s c:IdentifiedObject.mRID ?rm_or_pec_id.
   {?s c:RotatingMachine.GeneratingUnit ?unit.}
    UNION
   {?unit c:PowerElectronicsUnit.PowerElectronicsConnection ?s.}
   {?unit a ?rawtype.
    bind(strafter(str(?rawtype),"#") as ?type)}
   ?s e:ConductingEquipment.FromConnectivityNode ?cn.
   ?cn c:IdentifiedObject.mRID ?cn1id.
   ?cn c:IdentifiedObject.name ?bus.
   ?end e:TransformerEnd.ConnectivityNode ?cn.
   ?end c:IdentifiedObject.mRID ?endid.
   ?end c:PowerTransformerEnd.PowerTransformer ?pxf.
   ?end c:TransformerEnd.endNumber ?enum.
   ?pxf c:IdentifiedObject.mRID ?xfid.
   ?pxf c:PowerTransformer.vectorGroup ?vgroup
  }
  ORDER by ?name
  """
  d = adhoc_sparql_dict (g, q, 'rm_or_pec_id')
  #list_dict_table (d)
  for key, row in d['vals'].items():
    if row['type'] in ['PhotoVoltaicUnit', 'PowerElectronicsWindUnit']:  # leave the GSU as Yy
      plant_type = 'IBRPlant'
    else: # change the GSU to Yd1
      plant_type = 'RotatingMachinePlant'
      # change the transformer vectorGroup
      pt = rdflib.URIRef (row['xfid'])
      g.remove ((pt, rdflib.URIRef (CIM_NS + 'PowerTransformer.vectorGroup'), rdflib.Literal ('Yy', datatype=CIM.String)))
      g.add ((pt, rdflib.URIRef (CIM_NS + 'PowerTransformer.vectorGroup'), rdflib.Literal ('Yd1', datatype=CIM.String)))
      # find the transformer end that's connected to the generator
      end = rdflib.URIRef (row['endid'])
      # change end2 from wye grounded to delta
      g.remove ((end, rdflib.URIRef (CIM_NS + 'PowerTransformerEnd.phaseAngleClock'), rdflib.Literal(0, datatype=CIM.Integer)))
      g.remove ((end, rdflib.URIRef (CIM_NS + 'PowerTransformerEnd.connectionKind'), rdflib.URIRef (CIM_NS + 'WindingConnection.Y')))
      g.remove ((end, rdflib.URIRef (CIM_NS + 'TransformerEnd.grounded'), rdflib.Literal(True, datatype=CIM.Boolean)))
      g.add ((end, rdflib.URIRef (CIM_NS + 'PowerTransformerEnd.phaseAngleClock'), rdflib.Literal(1, datatype=CIM.Integer)))
      g.add ((end, rdflib.URIRef (CIM_NS + 'PowerTransformerEnd.connectionKind'), rdflib.URIRef (CIM_NS + 'WindingConnection.D')))
      g.add ((end, rdflib.URIRef (CIM_NS + 'TransformerEnd.grounded'), rdflib.Literal(False, datatype=CIM.Boolean)))
    ID = GetCIMID(plant_type, row['name'], uuids)
    plant = rdflib.URIRef (ID)
    g.add ((plant, rdflib.RDF.type, rdflib.URIRef (EMT_NS + plant_type)))
    g.add ((plant, rdflib.URIRef (CIM_NS + 'IdentifiedObject.name'), rdflib.Literal(row['name'], datatype=CIM.String)))
    g.add ((plant, rdflib.URIRef (CIM_NS + 'IdentifiedObject.mRID'), rdflib.Literal(ID, datatype=CIM.String)))
    g.add ((plant, rdflib.URIRef (EMT_NS + 'GeneratingPlant.Equipments'), rdflib.URIRef (key)))
    g.add ((plant, rdflib.URIRef (EMT_NS + 'GeneratingPlant.Equipments'), rdflib.URIRef (row['xfid'])))

  # save the XML with mRIDs for re-use
  g.serialize (destination=case['xmlfile'], format='pretty-xml', max_depth=1)

  #g.serialize (destination='test1.ttl', format='turtle')

  serializer = OrderedTurtleSerializer(g)
  serializer.class_order = [
    CIM.EquipmentContainer,
    CIM.BaseVoltage,
    CIM.ConnectivityNode,
    CIM.ACLineSegment,
    CIM.DisconnectingCircuitBreaker,
    CIM.LinearShuntCompensator,
    CIM.SeriesCompensator,
    CIM.EnergyConsumer,
    CIM.LoadResponseCharacteristic,
    CIM.EnergySource,
    CIM.SynchronousMachine,
    CIM.HydroGeneratingUnit,
    CIM.NuclearGeneratingUnit,
    CIM.ThermalGeneratingUnit,
    CIM.SynchronousMachineSimplified,
    CIM.SynchronousMachineTimeConstantReactance,
    CIM.GovGAST,
    CIM.GovHydro1,
    CIM.GovSteam0,
    CIM.GovSteamSGO,
    CIM.ExcIEEEDC1A,
    CIM.ExcSEXS,
    CIM.ExcST1A,
    CIM.PssIEEE1A,
    CIM.Pss1A,
    CIM.PowerElectronicsConnection,
    CIM.PhotoVoltaicUnit,
    CIM.PowerElectronicsWindUnit,
    CIM.WeccREECA,
    CIM.WeccREGCA,
    CIM.WeccREPCA,
    CIM.WeccWTGARA,
    CIM.WeccWTGTA,
    CIM.PowerTransformer,
    CIM.PowerTransformerEnd,
    CIM.RatioTapChanger,
    CIM.TransformerMeshImpedance,
    CIM.TransformerCoreAdmittance,
    EMT.TransformerSaturation,
    EMT.IBRPlant,
    EMT.RotatingMachinePlant,
    CIM.OperationalLimitType,
    CIM.OperationalLimitSet,
    CIM.ApparentPowerLimit,
    CIM.TextDiagramObject,
    CIM.DiagramObjectPoint,
    CIM.CurveData
  ]
  with open(case['ttlfile'], 'wb') as fp:
    serializer.serialize(fp)

  #print("Bound Namespaces:")
  #for prefix, namespace_uri in g.namespaces():
  #  print(f"  Prefix: {prefix}, URI: {namespace_uri}")

  #print('saving instance mRIDs to ', fuidname)
  fuid = open(fuidname, 'w')
  for key, val in uuids.items():
      print('{:s},{:s}'.format(key.replace(':', ',', 1), val), file=fuid)
  fuid.close()

