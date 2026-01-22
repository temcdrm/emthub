# Copyright (C) 2023 Battelle Memorial Institute
# Copyright (C) 2025-2026 Meltran, Inc

import sys
import math
import networkx as nx
import json
import os
import rdflib
import cim_examples
import emthub.api as emthub

# global constants
SQRT3 = math.sqrt(3.0)
RAD_TO_DEG = 180.0 / math.pi
MVA_BASE = 100.0

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
    buses[data['cn1id']]['has_load'] = True
  for key, data in d['EMTSyncMachine']['vals'].items():
    buses[data['cn1id']]['has_gen'] = True
  for key, data in d['EMTSolar']['vals'].items():
    buses[data['cn1id']]['has_solar'] = True
  for key, data in d['EMTWind']['vals'].items():
    buses[data['cn1id']]['has_wind'] = True
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
    G.add_node (key, nclass=nclass, ndata={'kv':0.001*data['nomv'],'name':data['name']})
  # accumulate the transformer windings into transformers
  xfmrs = {}
  for key, data in d['EMTPowerXfmrWinding']['vals'].items():
    toks = key.split(':')
    pname = toks[0]
    busnum = 'cn{:s}id'.format(toks[1])
    if pname not in xfmrs:
      xfmrs[pname] = {busnum:data['cn1id']}
      xfmrs[pname]['name'] = data['pname']
    else:
      xfmrs[pname][busnum] = data['cn1id']

  # add line, transformer, series compensator, and circuit breaker branches
  for key, data in d['EMTLine']['vals'].items():
    km = round(0.001*data['len'],3)
    G.add_edge(data['cn1id'],data['cn2id'],eclass='line',eid=key,
               edata={'km':km, 'kv':0.001*data['basev'], 'name':data['name']}, weight=km)
  for key, data in xfmrs.items():
    G.add_edge(data['cn1id'],data['cn2id'],eclass='transformer',eid=key,
               edata={'km':1.0, 'name':data['name']}, weight=1.0)
  for key, data in d['EMTCompSeries']['vals'].items():
    G.add_edge(data['cn1id'],data['cn2id'],eclass='series',eid=key,
               edata={'km':1.0, 'kv':0.001*data['basev'], 'name':data['name']}, weight=1.0)
  for key, data in d['EMTDisconnectingCircuitBreaker']['vals'].items():
    G.add_edge(data['cn1id'],data['cn2id'],eclass='cb',eid=key,
               edata={'km':1.0, 'kv':0.001*data['basev'], 'name':data['name']}, weight=1.0)

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
  case_id = 2
  if len(sys.argv) > 1:
    case_id = int(sys.argv[1])
  case = cim_examples.CASES[case_id]
  sys_id = case['id']
  sys_name = case['name']

  g = rdflib.Graph()
  fname = sys_name + '.ttl'
  g.parse (fname)
  print ('read', len(g), 'statements from', fname)
  d = emthub.load_emt_dict (g, case['id'], bTiming=True)

  G = build_system_graph (d)
  save_system_graph (G, './raw/{:s}_Network.json'.format(sys_name))


