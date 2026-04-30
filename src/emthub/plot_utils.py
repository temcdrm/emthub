# Copyright (C) 2023 Battelle Memorial Institute
# Copyright (C) 2025-2026 Meltran, Inc

"""
  Plotting and graph topology support functions. Use these to add missing *DiagramLayout* data to the CIM model. The sequence of steps for this is:

  1) Call *create_cim_rdf* using the *rawfile* and *dyrfile* data. It won't have *DiagramLayout* data in the serialized CIM RDF (unless the function finds an old JSON file from previously completing step 2).
  2) Call *build_system_graph*, using a dictionary obtained from the RDF data saved in step 1. This writes a JSON file with the layout.
  3) Call *plot_system_graph* to visually check the layout, including colors and labels.
  4) Call *create_cim_rdf* a second time. Now it will find the JSON file from step 2, and include *DiagramLayout* data in the serialized CIM RDF.
"""

import sys
import math
import networkx as nx
import json
import os
import matplotlib.pyplot as plt 
import matplotlib.lines as lines
import matplotlib.patches as patches

nodeTypes = {
  'load':  {'color':'green', 'tag':'Load',  'size':15},
  'gen':   {'color':'red',   'tag':'Gen',   'size':20},
  'solar': {'color':'orange','tag':'Solar', 'size':30},
  'wind':  {'color':'blue',  'tag':'Wind',  'size':30},
  'bus':   {'color':'black', 'tag':'Bus',   'size':10}
  }

edgeTypes = {
  'transformer': {'color':'gray',    'tag':'Xfmr'},
  'series':      {'color':'magenta', 'tag':'Cap'},
  'cb':          {'color':'purple',  'tag':'CB'},
  'lineEHV':     {'color':'red',     'tag':'EHV'},
  'lineHV':      {'color':'orange',  'tag':'HV'},
  'lineMV':      {'color':'blue',    'tag':'MV'}
  }

# global constants
SQRT3 = math.sqrt(3.0)
RAD_TO_DEG = 180.0 / math.pi
MVA_BASE = 100.0
lblDeltaY = 0.0 # 0.005

def reset_type_counts():
  for key, val in edgeTypes.items():
    val['count'] = 0
  for key, val in nodeTypes.items():
    val['count'] = 0

def filter_types_used(d):
  ret = {}
  for key, val in d.items():
    if val['count'] > 0:
      ret[key] = val
  return ret

def get_edge_highlights(data):
  weight = 1.0
  color = edgeTypes['lineMV']['color']
  if data['eclass'] == 'transformer':
    weight = 3.0
    color = edgeTypes['transformer']['color']
    edgeTypes['transformer']['count'] += 1
  elif data['eclass'] == 'series':
    weight = 20.0
    color = edgeTypes['series']['color']
    edgeTypes['series']['count'] += 1
  elif data['eclass'] == 'cb':
    weight = 3.0
    color = edgeTypes['cb']['color']
    edgeTypes['cb']['count'] += 1
  else: # 'line'
    kv = data['edata']['kv']
    weight = 1.5
    if kv > 344.0:
      color = edgeTypes['lineEHV']['color']
      edgeTypes['lineEHV']['count'] += 1
      if kv > 499.0:
        weight = 2.0
    elif kv >= 100.0:
      color = edgeTypes['lineHV']['color']
      edgeTypes['lineHV']['count'] += 1
      if kv > 229.0:
        weight = 2.0
    else:
      edgeTypes['lineMV']['count'] += 1
  return weight, color

def get_edge_color(eclass):
  if eclass in edgeTypes:
    edgeTypes[eclass]['count'] += 1
    return edgeTypes[eclass]['color']
  print ('unknown edge class', eclass)
  return 'black'

def get_edge_mnemonic(eclass):
  if eclass in edgeTypes:
    return edgeTypes[eclass]['tag']
  return 'Unknown'

def get_node_size(nclass):
  if nclass in nodeTypes:
    return nodeTypes[nclass]['size']
  return 3

def get_node_color(nclass):
  if nclass in nodeTypes:
    nodeTypes[nclass]['count'] += 1
    return nodeTypes[nclass]['color']
  return 'black'

def get_node_mnemonic(nclass):
  if nclass in nodeTypes:
    return nodeTypes[nclass]['tag']
  return 'Unknown'

def plot_system_graph (G, sys_name, plot_labels, loc):
  """Plot the transmission system topology from a networkx layout (graph).

  Uses *matplotlib* to make the plot from *G*. Optionally, use a button on the plot GUI
  to save it in the current working directory.

  Args:
    G(networkx.Graph): the node/edge system layout.
    sys_name (str): root name from the title, typically from *CASES[i]['name']*
    plot_labels (bool): plot node (bus) labels. Only recommended with a small number of nodes.
    loc (str): location of the legend for *matplotlib*,  typically from *CASES[i]['legend_loc']*. The examples use 'best', the default, or specify 'lower right'.
  """
  plt.rcParams['savefig.directory'] = os.getcwd()
  reset_type_counts()
  # assign node colors
  plotNodes = []
  nodeColors = []
  nodeSizes = []
  for n in G.nodes():
    if 'nclass' in G.nodes()[n]:
      nclass = G.nodes()[n]['nclass']
    else:
      nclass = 'bus'
    plotNodes.append(n)
    nodeColors.append (get_node_color (nclass))
    nodeSizes.append (get_node_size (nclass))

  # assign edge colors
  plotEdges = []
  edgeWidths = []
  edgeColors = []
  for n1, n2, data in G.edges(data=True):
    plotEdges.append ((n1, n2))
    width, color = get_edge_highlights (data)
    edgeWidths.append (width)
    edgeColors.append (color)

  # construct XY coordinates for plotting the network
  xy = {}
  xyLbl = {}
  lblNode = {}
  bMissing = False
  for n, data in G.nodes(data=True):
    ndata = data['ndata']
    if ('x' in ndata) and ('y' in ndata):
      busx = float(ndata['x'])
      busy = float(ndata['y'])
      xy[n] = [busx, busy]
      lblNode[n] = n.upper()
      xyLbl[n] = [busx, busy + lblDeltaY]
    else:
      bMissing = True
      break
  if bMissing:
    print ('Missing some node XY data, generating default coordinates')
    xy = nx.kamada_kawai_layout (G, weight='km')

  # create the plot
  fig, ax = plt.subplots(figsize=(10,8))

  nx.draw_networkx_nodes (G, xy, nodelist=plotNodes, node_color=nodeColors, node_size=nodeSizes, ax=ax)
  nx.draw_networkx_edges (G, xy, edgelist=plotEdges, edge_color=edgeColors, width=edgeWidths, alpha=0.8, ax=ax)
  if plot_labels:
    nx.draw_networkx_labels (G, xyLbl, lblNode, font_size=8, font_color='k', horizontalalignment='left', 
                             verticalalignment='baseline', ax=ax)

  plt.title ('{:s} Network'.format(sys_name))
  plt.xlabel ('X coordinate')
  plt.ylabel ('Y coordinate')
  ax.grid(linestyle='dotted')
  xdata = [0, 1]
  ydata = [1, 0]
  legendEdges = filter_types_used (edgeTypes)
  legendNodes = filter_types_used (nodeTypes)
  lns = [lines.Line2D(xdata, ydata, color=get_edge_color(e)) for e in legendEdges] + \
    [lines.Line2D(xdata, ydata, color=get_node_color(n), marker='o') for n in legendNodes]
  labs = [get_edge_mnemonic (e) for e in legendEdges] + [get_node_mnemonic (n) for n in legendNodes]
  ax.tick_params(left=True, bottom=True, labelleft=True, labelbottom=True)
  ax.legend(lns, labs, loc=loc)
  plt.show()

def load_system_graph (fname):
  """Load the networkx layout (graph) from a JSON file.

  Narrative.

  Args:
    fname (str): name of the JSON file containing networkx Graph data

  Returns:
    G(networkx.Graph): the node/edge system layout.
  """
  lp = open (fname).read()
  mdl = json.loads(lp)
  G = nx.readwrite.json_graph.node_link_graph(mdl)
  return G

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
  """Auto-layout a diagram of the CIM network, returning a networkx graph.

  This function assigns colors to buses (graph nodes) depending on the presence of load, wind, solar, or conventional generation.
  It assigns colors and weights to the mult-terminal components (graph edges) depending on the type of component and voltage class. *ACLineSegments*
  are weighed by an estimated physical length. Then the *networkx* package's *kamada_kawai_layout* option is used to create a plausible
  layout of the buses.

  Args:
    d (dict): CIM data from *load_emt_dict*

  Returns:
    G(networkx.Graph): the node/edge system layout.
  """
  # accumulate loads and generation onto the buses
  buses = d['EMTBus']['vals']
  for key, data in d['EMTLoad']['vals'].items():
    buses[data['FromConnectivityNode_mRID']]['has_load'] = True
  for key, data in d['EMTSyncMachine']['vals'].items():
    buses[data['FromConnectivityNode_mRID']]['has_gen'] = True
  for key, data in d['EMTSolar']['vals'].items():
    buses[data['FromConnectivityNode_mRID']]['has_solar'] = True
  for key, data in d['EMTWind']['vals'].items():
    buses[data['FromConnectivityNode_mRID']]['has_wind'] = True
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
    G.add_node (key, nclass=nclass, ndata={'kv':0.001*data['BaseVoltage_nominalVoltage'],'name':data['name']})
  # accumulate the transformer windings into transformers
  xfmrs = {}
  for key, data in d['EMTPowerXfmrWinding']['vals'].items():
    toks = key.split(':')
    pname = toks[0]
    busnum = 'cn{:s}id'.format(toks[1])
    if pname not in xfmrs:
      xfmrs[pname] = {busnum:data['FromConnectivityNode_mRID']}
      xfmrs[pname]['name'] = data['PowerTransformer_name']
    else:
      xfmrs[pname][busnum] = data['FromConnectivityNode_mRID']

  # add line, transformer, series compensator, and circuit breaker branches
  for key, data in d['EMTLine']['vals'].items():
    km = round(0.001*data['length'],3)
    G.add_edge(data['FromConnectivityNode_mRID'],data['ToConnectivityNode_mRID'],eclass='line',eid=key,
               edata={'km':km, 'kv':0.001*data['BaseVoltage_nominalVoltage'], 'name':data['name']}, weight=km)
  for key, data in xfmrs.items():  # connectivity nodes are numbered for transformers because there can be more than one, i.e., the windings associate to ConnectivityNode
    G.add_edge(data['cn1id'],data['cn2id'],eclass='transformer',eid=key,
               edata={'km':1.0, 'name':data['name']}, weight=1.0)
  for key, data in d['EMTCompSeries']['vals'].items():
    G.add_edge(data['FromConnectivityNode_mRID'],data['ToConnectivityNode_mRID'],eclass='series',eid=key,
               edata={'km':1.0, 'kv':0.001*data['BaseVoltage_nominalVoltage'], 'name':data['name']}, weight=1.0)
  for key, data in d['EMTDisconnectingCircuitBreaker']['vals'].items():
    G.add_edge(data['FromConnectivityNode_mRID'],data['ToConnectivityNode_mRID'],eclass='cb',eid=key,
               edata={'km':1.0, 'kv':0.001*data['BaseVoltage_nominalVoltage'], 'name':data['name']}, weight=1.0)

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
  """Save the networkx layout (graph) to a JSON file.

  Call this after *build_system_graph*.

  Args:
    G(networkx.Graph): the node/edge system layout.
    fname (str): name of the JSON file to save *G* in
  """
  fp = open (fname, 'w')
  data = nx.readwrite.json_graph.node_link_data(G)
  json.dump (data, fp, indent=2)
  fp.close()

