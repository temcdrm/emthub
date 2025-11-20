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
   'rawfile':'raw/ieee-118-bus-v4.raw', 'cimfile':'ieee118.xml', 'locfile': 'raw/ieee118_network.json', 'mridfile':'raw/ieee118mrids.dat'},
  {'id': '2540AF5C-4F83-4C0F-9577-DEE8CC73BBB3', 
   'name': 'WECC240',
   'rawfile':'raw/240busWECC_2018_PSS.raw', 'cimfile':'wecc240.xml', 'locfile': 'raw/wecc240_network.json', 'mridfile':'raw/wecc240mrids.dat'}
]

METAFILE = 'psseraw.json'
WFREQ = 2.0 * math.pi * 60.0
M_PER_MILE = 1609.344

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

def create_cim_xml (tables, kvbases, bus_kvbases, baseMVA, case):
  g = rdflib.Graph()
  CIM = rdflib.Namespace (CIM_NS)
  g.bind('cim', CIM)
  EMT = rdflib.Namespace (EMT_NS)
  g.bind('emt', EMT)
#  g.bind('xsd', rdflib.namespace.XSD)
#  g.namespace_manager.bind('xsd', XSD)
  
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

  eq = rdflib.URIRef (CASES[0]['id']) # no prefix with urn:uuid:

  g.add ((eq, rdflib.RDF.type, rdflib.URIRef (CIM_NS + 'EquipmentContainer')))
  g.add ((eq, rdflib.URIRef (CIM_NS + 'IdentifiedObject.name'), rdflib.Literal(CASES[0]['name'], datatype=CIM.String)))
  g.add ((eq, rdflib.URIRef (CIM_NS + 'IdentifiedObject.mRID'), rdflib.Literal(CASES[0]['id'], datatype=CIM.String)))

  # write the base voltages
  kvbase_ids = {}
  for kvname, kv in kvbases.items():
    print (kvname)
    ID = GetCIMID('BaseVoltage', kvname, uuids)
    bv = rdflib.URIRef (ID)
    g.add ((bv, rdflib.RDF.type, rdflib.URIRef (CIM_NS + 'BaseVoltage')))
    g.add ((bv, rdflib.URIRef (CIM_NS + 'IdentifiedObject.name'), rdflib.Literal(kvname, datatype=CIM.String)))
    g.add ((bv, rdflib.URIRef (CIM_NS + 'IdentifiedObject.mRID'), rdflib.Literal(ID, datatype=CIM.String)))
    g.add ((bv, rdflib.URIRef (CIM_NS + 'BaseVoltage.nominalVoltage'), rdflib.Literal(kv, datatype=CIM.Voltage)))
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
      g.add ((ac, rdflib.URIRef (CIM_NS + 'IdentifiedObject.name'), rdflib.Literal(key)))
      g.add ((ac, rdflib.URIRef (CIM_NS + 'IdentifiedObject.mRID'), rdflib.Literal(ID)))
      g.add ((ac, rdflib.URIRef (CIM_NS + 'Equipment.EquipmentContainer'), eq))
      g.add ((ac, rdflib.URIRef (CIM_NS + 'Equipment.inService'), rdflib.Literal (True, datatype='cim:Boolean')))
      g.add ((ac, rdflib.URIRef (CIM_NS + 'ConductingEquipment.FromConnectivityNode'), bus1))
      g.add ((ac, rdflib.URIRef (CIM_NS + 'ConductingEquipment.ToConnectivityNode'), bus2))
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
      g.add ((ac, rdflib.URIRef (CIM_NS + 'IdentifiedObject.name'), rdflib.Literal(key)))
      g.add ((ac, rdflib.URIRef (CIM_NS + 'IdentifiedObject.mRID'), rdflib.Literal(ID)))
      g.add ((ac, rdflib.URIRef (CIM_NS + 'Equipment.EquipmentContainer'), eq))
      g.add ((ac, rdflib.URIRef (CIM_NS + 'Equipment.inService'), rdflib.Literal (True, datatype='cim:Boolean')))
      g.add ((ac, rdflib.URIRef (CIM_NS + 'ConductingEquipment.FromConnectivityNode'), bus1))
      g.add ((ac, rdflib.URIRef (CIM_NS + 'ConductingEquipment.ToConnectivityNode'), bus2))
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
    g.add ((ec, rdflib.URIRef (CIM_NS + 'IdentifiedObject.name'), rdflib.Literal(key)))
    g.add ((ec, rdflib.URIRef (CIM_NS + 'IdentifiedObject.mRID'), rdflib.Literal(ID)))
    g.add ((ec, rdflib.URIRef (CIM_NS + 'Equipment.EquipmentContainer'), eq))
    g.add ((ec, rdflib.URIRef (CIM_NS + 'Equipment.inService'), rdflib.Literal (True, datatype='cim:Boolean')))
    g.add ((ec, rdflib.URIRef (CIM_NS + 'ConductingEquipment.FromConnectivityNode'), bus1))
    g.add ((ec, rdflib.URIRef (CIM_NS + 'ConductingEquipment.ToConnectivityNode'), bus1))
    g.add ((ec, rdflib.URIRef (CIM_NS + 'ConductingEquipment.BaseVoltage'), bv))
    g.add ((ec, rdflib.URIRef (CIM_NS + 'EnergyConsumer.LoadResponseCharacteristic'), rdflib.URIRef (LRmRID)))
    g.add ((ec, rdflib.URIRef (CIM_NS + 'EnergyConsumer.p'), rdflib.Literal (p, datatype=CIM.ActivePower)))
    g.add ((ec, rdflib.URIRef (CIM_NS + 'EnergyConsumer.q'), rdflib.Literal (q, datatype=CIM.ReactivePower)))

  print ('Writing', len(LoadResponseCharacteristics), 'load response characteristics')
  for key, row in LoadResponseCharacteristics.items():
    lr = rdflib.URIRef (row['mRID'])
    g.add ((lr, rdflib.RDF.type, rdflib.URIRef (CIM_NS + 'LoadResponseCharacteristic')))
    g.add ((lr, rdflib.URIRef (CIM_NS + 'IdentifiedObject.name'), rdflib.Literal(key)))
    g.add ((lr, rdflib.URIRef (CIM_NS + 'IdentifiedObject.mRID'), rdflib.Literal(row['mRID'])))
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
    print (row)
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
        print (data)
        row = next(reader)
        print (row)
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

# print_table ('BUS')
# print_table ('LOAD')
# print_table ('FIXED SHUNT')
# print_table ('GENERATOR')
# print_table ('BRANCH')
# print_table ('TRANSFORMER')

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
  

