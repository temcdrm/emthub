# Copyright (C) 2023 Battelle Memorial Institute
# Copyright (C) 2025 Meltran, Inc

import sys
import math
import networkx as nx
import json
import os
import rdflib
import time
import xml.etree.ElementTree as ET

PREFIX = None
DELIM = ':'

CASES = [
  {'id': '1783D2A8-1204-4781-A0B4-7A73A2FA6038', 'name': 'IEEE118'},
  {'id': '2540AF5C-4F83-4C0F-9577-DEE8CC73BBB3', 'name': 'WECC240'},
]

# global constants
SQRT3 = math.sqrt(3.0)
RAD_TO_DEG = 180.0 / math.pi
MVA_BASE = 100.0

def list_dict_table(dict, tag):
  tbl = dict[tag]
  print ('\n{:s}: key,{:s}'.format(tag, str(tbl['columns'])))
  for key, row in tbl['vals'].items():
    print ('{:s},{:s}'.format (key, ','.join(str(row[c]) for c in tbl['columns'])))

def build_query (prefix, base, sysid):
  if sysid is not None:
    idx = base.find('WHERE {') + 8
    return prefix + '\n' + base[:idx] + """ VALUES ?sysid {{"{:s}"^^c:String}}\n""".format (sysid) + base[idx:]
  return prefix + '\n' + base

def query_for_values (g, tbl, sysid):
  keyflds = tbl['keyfld'].split(':')
  q = build_query (PREFIX, tbl['sparql'], sysid)
 # print ('===================')
 # print (q)
  result = g.query(q)
  vars = [str(item) for item in result.vars]
  for akey in keyflds:
    vars.remove (akey)
  tbl['columns'] = vars
  for b in result:
    row = {}
    key = str(b[keyflds[0]])
    for i in range(1, len(keyflds)):
      key = key + DELIM + str(b[keyflds[i]])
    for fld in vars:
      if fld in ['name', 'conn', 'sysid', 'bus', 'bus1', 'bus2', 'id', 'eqid']:
        row[fld] = str(b[fld])
      else:
        try:
          row[fld] = int(b[fld])
        except ValueError:
          try:
            row[fld] = float(b[fld])
          except ValueError:
            row[fld] = str(b[fld])
    tbl['vals'][key] = row

def load_emt_dict (g, xml_file, sysid):
  global PREFIX
  # read the queries into dict
  tree = ET.parse(xml_file)
  root = tree.getroot()
  nsCIM = root.find('nsCIM').text.strip()
  nsRDF = root.find('nsRDF').text.strip()
  nsEMT = root.find('nsEMT').text.strip()
  PREFIX = """PREFIX r: <{:s}>\nPREFIX c: <{:s}>\nPREFIX e: <{:s}>""".format (nsRDF, nsCIM, nsEMT)
  #print (PREFIX)
  dict = {}
  for query in root.findall('query'):
    qid = query.find('id').text.strip()
    dict[qid] = {}
    dict[qid]['keyfld'] = query.find('keyfld').text
    dict[qid]['sparql'] = query.find('value').text.strip()
    dict[qid]['columns'] = []
    dict[qid]['vals'] = {}
    #print (' ', qid, dict[qid]['keyfld'])

  for key in ['EMTContainer', 'EMTBus', 'EMTBusXY', 'EMTBaseVoltage', 'EMTLine', 'EMTLoad',
              'EMTCountPowerXfmrWindings', 'EMTPowerXfmrWinding', 'EMTPowerXfmrCore',
              'EMTPowerXfmrMesh', 'EMTXfmrSaturation', 'EMTCompShunt', 'EMTCompSeries',
              'EMTSyncMachine', 'EMTSolar', 'EMTWind', 'EMTGovSteamSGO', 'EMTExcST1A',
              'EMTPssIEEE1A', 'EMTWeccREGCA', 'EMTWeccREECA', 'EMTWeccREPCA',
              'EMTWeccWTGTA', 'EMTWeccWTGARA', 'EMTEnergySource', 'EMTDisconnectingCircuitBreaker']:
    start_time = time.time()
    query_for_values (g, dict[key], sysid)
    print ('  Running {:40s} took {:6.3f} s for {:5d} rows'.format (key, time.time() - start_time, len(dict[key]['vals'])))
 #   list_dict_table (dict, key)
  return dict

def km_distance (G, n1, n2):
#  seq = nx.dijkstra_path(G, n1, n2)
  seq = nx.shortest_path(G, n1, n2)
#  print (seq)
  edges = zip(seq[0:], seq[1:])
  km = 0.0
  for u, v in edges:
#    print(G[u][v])
    km += G[u][v]['edata']['km']
  return km

def build_system_graph (d):
  # accumulate loads and generation onto the buses
  buses = d['EMTBus']['vals']
  for key, data in d['EMTLoad']['vals'].items():
    buses[data['bus']]['has_load'] = True
  for key, data in d['EMTSyncMachine']['vals'].items():
    buses[data['bus']]['has_gen'] = True
  for key, data in d['EMTSolar']['vals'].items():
    buses[data['bus']]['has_solar'] = True
  for key, data in d['EMTWind']['vals'].items():
    buses[data['bus']]['has_wind'] = True
  G = nx.Graph()
  for key, data in buses.items():
    if 'has_solar' in data:
      nclass='solar'
    elif 'has_wind' in data:
      nclass='wind'
    elif 'has_gen' in data:
      nclass='gen'
    elif 'has_load' in data:
      nclass='load'
    else:
      nclass='bus'
    G.add_node (key, nclass=nclass, ndata={'kv':0.001*data['nomv']})
  # accumulate the transformer windings into transformers
  xfmrs = {}
  for key, data in d['EMTPowerXfmrWinding']['vals'].items():
    toks = key.split(':')
    pname = toks[0]
    busnum = 'bus{:s}'.format(toks[1])
    if pname not in xfmrs:
      xfmrs[pname] = {busnum:data['bus']}
    else:
      xfmrs[pname][busnum] = data['bus']

  # add line, transformer, series compensator branches
  for key, data in d['EMTLine']['vals'].items():
    km = round(0.001*data['len'],3)
    G.add_edge(data['bus1'],data['bus2'],eclass='line',ename=key,
               edata={'km':km, 'kv':0.001*data['basev']}, weight=km)
  for key, data in xfmrs.items():
    G.add_edge(data['bus1'],data['bus2'],eclass='transformer',ename=key,
               edata={'km':1.0}, weight=1.0)
  for key, data in d['EMTCompSeries']['vals'].items():
    G.add_edge(data['bus1'],data['bus2'],eclass='series',ename=key,
               edata={'km':1.0, 'kv':0.001*data['basev']}, weight=1.0)

  # create XY coordinates for the buses
  dist = {}
  for n1 in G.nodes():
    if n1 not in dist:
      dist[n1] = {}
    for n2 in G.nodes():
      dist[n1][n2] = km_distance(G, n1, n2)
#  dist = dict(nx.shortest_path_length(G))
#  print (dist['99']['119'], dist['99']['99'], km_distance (G, '99', '119'))

  xy = nx.kamada_kawai_layout (G, dist=dist)
  for bus, row in xy.items():
    G.nodes()[bus]['ndata']['x'] = row[0]
    G.nodes()[bus]['ndata']['y'] = row[1]

  return G

def save_system_graph (G, fname):
  fp = open (fname, 'w')
  data = nx.readwrite.json_graph.node_link_data(G)
  json.dump (data, fp, indent=2)
  fp.close()

if __name__ == '__main__':
  case_id = 0
  if len(sys.argv) > 1:
    case_id = int(sys.argv[1])
  case = CASES[case_id]
  sys_id = case['id']
  sys_name = case['name']

  g = rdflib.Graph()
  fname = sys_name + '.ttl'
  g.parse (fname)
  print ('read', len(g), 'statements from', fname)
  #summarize_graph (g)

  start_time = time.time()
  d = load_emt_dict (g, 'sparql_queries.xml', case['id'])
  print ('Total query time {:6.3f} s'.format (time.time() - start_time))
  #list_dict_table (d, 'EMTBus')
  #quit()

  G = build_system_graph (d)
  save_system_graph (G, './raw/{:s}_Network.json'.format(sys_name))


