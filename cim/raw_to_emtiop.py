# Copyright (C) 2025 Meltran, Inc

import json
import csv
import rdflib
import os
import re
import uuid
import networkx

CIM_NS = 'http://www.ucaiug.org/profile#'

CASES = [
  {'id': '1783D2A8-1204-4781-A0B4-7A73A2FA6038', 'name': 'IEEE118'},
  {'id': '2540AF5C-4F83-4C0F-9577-DEE8CC73BBB3', 'name': 'WECC240'},
]

RAWFILE = 'raw/ieee-118-bus-v4.raw'
METAFILE = 'psseraw.json'
CIMFILE = 'ieee118.xml'
LOCFILE = 'raw/ieee118_network.json'
MRIDFILE = 'raw/ieee118mrids.dat'

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

def create_cim_xml (tables, kvbases, bus_kvbases, location_file, cim_file):
  g = rdflib.Graph()
  CIM = rdflib.Namespace (CIM_NS)
  g.bind('cim', CIM)
  
  # read the existing mRID map for persistence
  uuids = {}
  fuidname = MRIDFILE
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
  g.add ((eq, rdflib.URIRef (CIM_NS + 'IdentifiedObject.name'), rdflib.Literal(CASES[0]['name'])))
  g.add ((eq, rdflib.URIRef (CIM_NS + 'IdentifiedObject.mRID'), rdflib.Literal(CASES[0]['id'])))

  # write the base voltages
  for kvname, kv in kvbases.items():
    print (kvname)
    ID = GetCIMID('BaseVoltage', kvname, uuids)
    bv = rdflib.URIRef (ID)
    g.add ((bv, rdflib.RDF.type, rdflib.URIRef (CIM_NS + 'BaseVoltage')))
    g.add ((bv, rdflib.URIRef (CIM_NS + 'IdentifiedObject.name'), rdflib.Literal(kvname)))
    g.add ((bv, rdflib.URIRef (CIM_NS + 'IdentifiedObject.mRID'), rdflib.Literal(ID)))
    g.add ((bv, rdflib.URIRef (CIM_NS + 'BaseVoltage.nominalVoltage'), rdflib.Literal(str(kv))))

  # write the connectivity nodes
  busids = {}
  for row in tables['BUS']['data']:
    busname = str(row[0])
    ID = GetCIMID('ConnectivityNode', busname, uuids)
    busids[busname] = ID
    cn = rdflib.URIRef (ID)
    g.add ((cn, rdflib.RDF.type, rdflib.URIRef (CIM_NS + 'ConnectivityNode')))
    g.add ((cn, rdflib.URIRef (CIM_NS + 'IdentifiedObject.name'), rdflib.Literal(busname)))
    g.add ((cn, rdflib.URIRef (CIM_NS + 'IdentifiedObject.mRID'), rdflib.Literal(ID)))
    g.add ((cn, rdflib.URIRef (CIM_NS + 'ConnectivityNode.ConnectivityNodeContainer'), eq))

  # write the diagram layout
  busxy = load_bus_coordinates (LOCFILE)
  for row in tables['BUS']['data']:
    key = str(row[0])
    busname = '{:d} {:s} {:.2f} kV'.format (row[0], row[1], row[2])
    xy = busxy[key]
    ID = GetCIMID('TextDiagramObject', key, uuids)
    td = rdflib.URIRef (ID)
    g.add ((td, rdflib.RDF.type, rdflib.URIRef (CIM_NS + 'TextDiagramObject')))
    g.add ((td, rdflib.URIRef (CIM_NS + 'IdentifiedObject.name'), rdflib.Literal(key)))
    g.add ((td, rdflib.URIRef (CIM_NS + 'IdentifiedObject.mRID'), rdflib.Literal(ID)))
    g.add ((td, rdflib.URIRef (CIM_NS + 'DiagramObject.IdentifiedObject'), rdflib.URIRef (busids[key])))
    g.add ((td, rdflib.URIRef (CIM_NS + 'TextDiagramObject.text'), rdflib.Literal(busname)))
    pt = rdflib.BNode()
    g.add ((pt, rdflib.RDF.type, rdflib.URIRef (CIM_NS + 'DiagramObjectPoint')))
    g.add ((pt, rdflib.URIRef (CIM_NS + 'DiagramObjectPoint.DiagramObject'), td))
    g.add ((pt, rdflib.URIRef (CIM_NS + 'DiagramObjectPoint.sequenceNumber'), rdflib.Literal('1')))
    g.add ((pt, rdflib.URIRef (CIM_NS + 'DiagramObjectPoint.xPosition'), rdflib.Literal(str(xy[0]))))
    g.add ((pt, rdflib.URIRef (CIM_NS + 'DiagramObjectPoint.yPosition'), rdflib.Literal(str(xy[1]))))

  # save the XML with mRIDs for re-use
  g.serialize (destination=cim_file, format='pretty-xml', max_depth=1)

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
  for row in table['data']:
    print (row)

if __name__ == '__main__':
  with open(METAFILE, 'r') as file:
    meta = json.load (file)
  for section in meta['sections']:
    sect = meta['sections'][section]
    columns = sect['columns']
    column_names = ','.join([columns[i]['Name'] for i in range(len(columns))])
    print ('Table "{:s}" has {:d} raw columns, using {:d}: {:s}'.format (section, sect['column_count'], len(columns), column_names))

  table = None
  with open(RAWFILE, 'r') as csvfile:
    reader = csv.reader(csvfile)
    row = next(reader)
    baseMVA = float(row[1])
    title = next(reader)[0]
    print('MVA base = {:.1f}, Title = {:s}'.format(baseMVA, title))
    for row in reader:
      if len(row) > 1 and 'END OF' in row[0] and 'BEGIN' in row[1]: # start a new table
        i1 = row[1].find('BEGIN') + 6
        i2 = row[1].find(' DATA')
        table_name = row[1][i1:i2]
        if table_name in meta['sections']:
          sect = meta['sections'][table_name]
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
          tables[table_name] = table
          print (table)
        else:
          print ('ignoring', table_name, 'raw file data')
          table = None
      elif table is not None:
        data = []
        while len(row) < total_columns:
          row = row + next(reader)
          if len(row) > total_columns:
            print ('*** read', len(row), table_name, 'columns from the raw file. Need to match', total_columns)
        for i in range(n_columns):
          val = row[column_indices[i]]
          if column_types[i] == 'Float':
            data.append(float(val))
          elif column_types[i] == 'Integer':
            data.append(int(val))
          else:
            data.append(val.strip('\' '))
        table['data'].append (data)

#  print_table ('BUS')
#  print_table ('LOAD')
#  print_table ('FIXED SHUNT')
#  print_table ('GENERATOR')
#  print_table ('BRANCH')
#  print_table ('TRANSFORMER')

  for bus in tables['BUS']['data']:
    bus_kvbases[bus[0]] = bus[2]
    kvbases['BV_{:.2f}'.format(bus[2])] = bus[2]

  print ('All kV Bases =', kvbases)

  create_cim_xml (tables, kvbases, bus_kvbases, LOCFILE, CIMFILE)
#  print ('Bus kV Bases =', bus_kvbases)
  

