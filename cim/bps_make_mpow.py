# Copyright (C) 2023-2024 Battelle Memorial Institute
# Copyright (C) 2025-2026 Meltran, Inc

import sys
import os
import rdflib
import time
import xml.etree.ElementTree as ET

PREFIX = None
DELIM = ':'

CASES = [
  {'id': '6477751A-0472-4FD6-B3C3-3AD4945CBE56', 'name': 'IEEE39', 'swingbus':'31'},
  {'id': '1783D2A8-1204-4781-A0B4-7A73A2FA6038', 'name': 'IEEE118', 'swingbus':'131'},
  {'id': '2540AF5C-4F83-4C0F-9577-DEE8CC73BBB3', 'name': 'WECC240', 'swingbus':'2438'},
  {'id': '93EA6BF1-A569-4190-9590-98A62780489E', 'name': 'XFMRSAT', 'swingbus':'1'}
]

FUELS = {
  'hydro':  {'c2':1.0e-5, 'c1': 1.29, 'c0': 0.0},
  'wind':   {'c2':1.0e-5, 'c1': 0.01, 'c0': 0.0},
  'solar':  {'c2':1.0e-5, 'c1': 0.01, 'c0': 0.0},
  'coal':   {'c2':0.0009, 'c1': 19.0, 'c0': 2128.0},
  'ng':     {'c2':0.0060, 'c1': 45.0, 'c0': 2230.0},
  'nuclear':{'c2':0.00019, 'c1': 8.0, 'c0': 1250.0}
}

# global constants
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
      if b[fld] is None:
        row[fld] = None
      elif fld in ['pname', 'name', 'conn', 'sysid', 'bus', 'bus1', 'bus2', 'id', 'eqid', 'endid']:
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
              'EMTPowerXfmrMesh', 'EMTXfmrTap', 'EMTXfmrSaturation', 'EMTCompShunt', 'EMTCompSeries',
              'EMTSyncMachine', 'EMTSolar', 'EMTWind', 'EMTGovSteamSGO', 'EMTExcST1A',
              'EMTPssIEEE1A', 'EMTWeccREGCA', 'EMTWeccREECA', 'EMTWeccREPCA',
              'EMTWeccWTGTA', 'EMTWeccWTGARA', 'EMTEnergySource', 'EMTDisconnectingCircuitBreaker',
              'EMTXfmrLimit', 'EMTBranchLimit']:
    start_time = time.time()
    query_for_values (g, dict[key], sysid)
    print ('  Running {:40s} took {:6.3f} s for {:5d} rows'.format (key, time.time() - start_time, len(dict[key]['vals'])))
 #   list_dict_table (dict, key)
  return dict

def get_gencosts(fuel):
  c2 = 0.0
  c1 = 0.0
  c0 = 0.0
  if fuel in FUELS:
    c2 = FUELS[fuel]['c2']
    c1 = FUELS[fuel]['c1']
    c0 = FUELS[fuel]['c0']
  return c2, c1, c0

def add_mpc_generator (gens, data, bus_numbers, bus_generation, bus_headroom):
  busnum = bus_numbers[data['cn1id']]
  Pg = data['p']/1.0e6
  Pmax = data['maxP']/1.0e6
  Pheadroom = Pmax - Pg
  if busnum in bus_generation:
    bus_generation[busnum] += Pg
  else:
    bus_generation[busnum] = Pg
  if busnum in bus_headroom:
    bus_headroom[busnum] += Pheadroom
  else:
    bus_headroom[busnum] = Pheadroom
  status = 1
  if Pg <= 0.0:
    status = 1
  gens.append ({'bus':busnum,
                'Pg':Pg,
                'Qg':data['q']/1.0e6,
                'Qmax':data['maxQ']/1.0e6,
                'Qmin':data['minQ']/1.0e6,
                'Vg':1.0,
                'mBase':data['ratedS']/1.0e6,
                'status':status,
                'Pmax':Pmax,
                'Pmin':data['minP']/1.0e6,
                'Pc1':0.0, 'Pc2':0.0, 'Qc1min':0.0, 'Qc1max':0.0, 'Qc2min':0.0, 'Qc2max':0.0,
                'ramp_agc':0.0, 'ramp_10':0.0, 'ramp_30':0.0, 'ramp_q':0.0, 'apf':0.0})

def build_bus_lists (d):
  bNumeric = True
  for key, data in d['EMTBus']['vals'].items():
    if not data['name'].isdigit():
      bNumeric = False
      break
  if bNumeric:
    ordered_buses = dict(sorted(d['EMTBus']['vals'].items(), key=lambda x:int(x[1]['name'])))
  else:
    ordered_buses = d['EMTBus']['vals']
  bus_numbers = {}
  busnum = 1
  for key, data in ordered_buses.items(): # data has name and nomv
    bus_numbers[key] = busnum
    busnum += 1
  return ordered_buses, bus_numbers

def get_swingbus_id (ordered_buses, swingbus):
  for cnid, data in ordered_buses.items():
    if data['name'] == swingbus:
      return cnid

def find_branch_normal_rating (eqid, d):
  val = 0.0
  for key, data in d['EMTBranchLimit']['vals'].items():
    if eqid == data['eqid']:
      if data['inf'] == 'true':
        val = data['value']
        return val / 1.0e6
  return val

def constant_impedance (z, i, p):
  if z > (i+p):
    return True
  return False

def build_matpower (d, sys_name, fp, swingbus):
  print ('function mpc = {:s}'.format(sys_name), file=fp)
  print ('mpc.version = "2";', file=fp)
  print ('mpc.baseMVA = {:.1f};'.format(MVA_BASE), file=fp)

  print ("""
%% bus data
%	bus_i type Pd Qd Gs Bs area Vm Va baseKV zone Vmax Vmin
mpc.bus = [""", file=fp)
  mpc_buses = []
  mpc_bus_names = []
  # MATPOWER needs to number the buses as consecutive integers, and
  # we need to map the bus names (not necessarily integer) to MATPOWER bus numbers
  ordered_buses, bus_numbers = build_bus_lists(d)
  for key, data in ordered_buses.items():
    mpc_buses.append ({'bus_i':len(mpc_buses)+1,
                       'type':1,
                       'Pd':0.0,
                       'Qd':0.0,
                       'Gs':0.0,
                       'Bs':0.0,
                       'area':1,
                       'Vm':1.0,
                       'Va':0.0,
                       'baseKV':data['nomv'] * 0.001,
                       'zone':1,
                       'Vmax':1.1,
                       'Vmin':0.9})
    mpc_bus_names.append (data['name']) # (key)
  # add loads and shunts to buses
  total_load = 0.0
  for key, data in d['EMTLoad']['vals'].items():
    idx = bus_numbers[data['cn1id']]-1
    Pd = data['p'] / 1.0e6
    Qd = data['q'] / 1.0e6
    total_load += Pd
    if constant_impedance (data['pz'], data['pi'], data['pp']):
      mpc_buses[idx]['Gs'] += Pd
    else:
      mpc_buses[idx]['Pd'] += Pd
    if constant_impedance (data['qz'], data['qi'], data['qz']):
      mpc_buses[idx]['Bs'] -= Qd
    else:
      mpc_buses[idx]['Qd'] += Qd
  for key, data in d['EMTCompShunt']['vals'].items():
    idx = bus_numbers[data['cn1id']]-1
    scale = data['sections']*data['nomu']*data['nomu']/1.0e6
    mpc_buses[idx]['Gs'] += data['gsection']*scale
    mpc_buses[idx]['Bs'] += data['bsection']*scale
  # any bus with a generator is type 2; bus with most total generation is type 3
  mpc_generators = []
  mpc_genfuels = []
  mpc_gentypes = []
  bus_generation = {}
  bus_headroom = {}
  for key, data in d['EMTSyncMachine']['vals'].items():
    idx = bus_numbers[data['cn1id']]-1
    mpc_buses[idx]['type'] = 2
    add_mpc_generator (mpc_generators, data, bus_numbers, bus_generation, bus_headroom)
    if data['type'] == 'Hydro':
      mpc_genfuels.append('hydro')
      mpc_gentypes.append('HY')
    elif data['type'] == 'Nuclear':
      mpc_genfuels.append('nuclear')
      mpc_gentypes.append('ST')
    else:
      mpc_genfuels.append('ng')
      mpc_gentypes.append('ST')
  for key, data in d['EMTSolar']['vals'].items():
    idx = bus_numbers[data['cn1id']]-1
    mpc_buses[idx]['type'] = 2
    add_mpc_generator (mpc_generators, data, bus_numbers, bus_generation, bus_headroom)
    mpc_genfuels.append('solar')
    mpc_gentypes.append('PV')
  for key, data in d['EMTWind']['vals'].items():
    idx = bus_numbers[data['cn1id']]-1
    mpc_buses[idx]['type'] = 2
    add_mpc_generator (mpc_generators, data, bus_numbers, bus_generation, bus_headroom)
    mpc_genfuels.append('wind')
    mpc_gentypes.append('WT')
  if len(bus_generation) > 0:
    max_bus = max(bus_generation, key=bus_generation.get)
    print ('bus {:d} has maximum generation of {:.2f} MW and headroom of {:.2f} MW'.format (max_bus, 
                                                                                            bus_generation[max_bus], 
                                                                                            bus_headroom[max_bus]))
  if len(bus_headroom) > 0:                                                                 
    head_bus = max(bus_headroom, key=bus_headroom.get)
    print ('bus {:d} has maximum headroom of {:.2f} MW and generation of {:.2f} MW'.format (head_bus, 
                                                                                            bus_headroom[head_bus], 
                                                                                            bus_generation[head_bus]))
  swingbus_num = bus_numbers[get_swingbus_id(ordered_buses, swingbus)]
  if len(mpc_generators) < 1:
    mpc_generators.append ({'bus':swingbus_num, 'Pg':total_load, 'Qg':0.0, 'Qmax':total_load, 'Qmin':-total_load,
                  'Vg':1.0, 'mBase':2*total_load, 'status':1, 'Pmax':2*total_load, 'Pmin':0.0,
                  'Pc1':0.0, 'Pc2':0.0, 'Qc1min':0.0, 'Qc1max':0.0, 'Qc2min':0.0, 'Qc2max':0.0,
                  'ramp_agc':0.0, 'ramp_10':0.0, 'ramp_30':0.0, 'ramp_q':0.0, 'apf':0.0})

  mpc_buses[swingbus_num-1]['type'] = 3
  for data in mpc_buses:
    print (' {:5d} {:2d} {:9.3f} {:9.3f} {:9.3f} {:9.3f} {:3d} {:7.4f} {:7.4f} {:7.3f} {:3d} {:6.3f} {:6.3f};'.format(
      data['bus_i'], data['type'], data['Pd'], data['Qd'], data['Gs'], data['Bs'], data['area'], data['Vm'], data['Va'], 
      data['baseKV'], data['zone'], data['Vmax'], data['Vmin']), file=fp)
  print ('];', file=fp)

  print ("""
%% generator data - SyncMachine+Solar+Wind
%	bus Pg Qg Qmax Qmin Vg mBase status Pmax Pmin Pc1 Pc2 Qc1min Qc1max Qc2min Qc2max ramp_agc ramp_10 ramp_30 ramp_q apf
mpc.gen = [""", file=fp)
  total_gen = 0.0
  for data in mpc_generators:
    total_gen += data['Pg']
    print (' {:5d} {:8.3f} {:8.3f} {:8.3f} {:8.3f} {:6.4f} {:8.3f} {:1d} {:8.3f} {:8.3f} {:.1f} {:.1f} {:.1f} {:.1f} {:.1f} {:.1f} {:.1f} {:.1f} {:.1f} {:.1f} {:.1f};'.format(
      data['bus'], data['Pg'], data['Qg'], data['Qmax'], data['Qmin'], data['Vg'], data['mBase'], data['status'], data['Pmax'], 
      data['Pmin'], data['Pc1'], data['Pc2'], data['Qc1min'], data['Qc1max'], data['Qc2min'], data['Qc2max'],
      data['ramp_agc'], data['ramp_10'], data['ramp_30'], data['ramp_q'], data['apf']), file=fp)
  print ('];', file=fp)

  # accumulate the transformer windings and taps into transformers
  xfmrs = {}
  for key, data in d['EMTPowerXfmrWinding']['vals'].items():
    toks = key.split(':')
    pname = toks[0]
    bus = bus_numbers[data['cn1id']]
    if pname not in xfmrs:
      fid = data['id']
      ratio = 1.0
      if fid in d['EMTXfmrTap']['vals']:
        ratio = 1.0 + (d['EMTXfmrTap']['vals'][fid]['svi']*d['EMTXfmrTap']['vals'][fid]['step']) / 100.0
        print (' * found tap={:8.6f} for winding {:s}'.format (ratio, fid))
      mva = data['ratedS'] / 1.0e6
      kv = data['ratedU'] / 1.0e3
      zbase = kv*kv / MVA_BASE # mva # on system MVA base, not on transformer MVA
      xfmrs[pname] = {'from':bus, 'mva':mva, 'ratio': ratio}
    else:
      xfmrs[pname]['to'] = bus
      tid = data['id']
      mesh = d['EMTPowerXfmrMesh']['vals']['{:s}:{:s}'.format(fid, tid)]
      r = mesh['r'] / zbase
      x = mesh['x'] / zbase
      xfmrs[pname]['r'] = r
      xfmrs[pname]['x'] = x

  print ("""
%% branch data - BESLine+BESCompSeries+collected transformers
%	fbus tbus r x b rateA rateB rateC ratio angle status angmin angmax
mpc.branch = [""", file=fp)
  for key, data in d['EMTLine']['vals'].items():
    rateA = find_branch_normal_rating (key, d)
    bus1 = bus_numbers[data['cn1id']]
    bus2 = bus_numbers[data['cn2id']]
    kvbase = data['basev']/1000.0
    zbase = kvbase*kvbase/MVA_BASE
    q = data['b']*kvbase*kvbase
    r = data['r']/zbase
    x = data['x']/zbase
    b = q/MVA_BASE
    print (' {:5d} {:5d} {:9.6f} {:9.6f} {:9.6f} {:8.3f} 0.0 0.0 0.0 0.0 1 0.0 0.0;'.format (bus1, bus2, r, x, b, rateA), file=fp)
  for key, data in d['EMTCompSeries']['vals'].items():
    rateA = find_branch_normal_rating (key, d)
    bus1 = bus_numbers[data['cn1id']]
    bus2 = bus_numbers[data['cn2id']]
    kvbase = data['basev']/1000.0
    zbase = kvbase*kvbase/MVA_BASE
    r = data['r']/zbase
    x = data['x']/zbase
    print (' {:5d} {:5d} {:9.6f} {:9.6f} 0.0 {:8.3f} 0.0 0.0 0.0 0.0 1 0.0 0.0;'.format (bus1, bus2, r, x, rateA), file=fp)
  for key, data in d['EMTDisconnectingCircuitBreaker']['vals'].items():
    rateA = find_branch_normal_rating (key, d)
    bus1 = bus_numbers[data['cn1id']]
    bus2 = bus_numbers[data['cn2id']]
    print (' {:5d} {:5d} 0.0 1.0e-6 0.0 {:8.3f} 0.0 0.0 0.0 0.0 1 0.0 0.0;'.format (bus1, bus2, rateA), file=fp)

  for key, data in xfmrs.items():
    rateA = data['mva']
    rateB = rateA * 4.0 / 3.0
    rateC = rateA * 5.0 / 3.0
    print (' {:5d} {:5d} {:9.6f} {:9.6f} 0.0 {:8.3f} {:8.3f} {:8.3f} {:8.6f} 0.0 1 0.0 0.0;'.format (data['from'], 
      data['to'], data['r'], data['x'], rateA, rateB, rateC, data['ratio']), file=fp)
  print ('];', file=fp)

  print ("""
%%-----  OPF Data  -----%%
%% generator cost data
%	1 startup shutdown n x1 y1 ... xn yn
%	2 startup shutdown n c(n-1) ... c0
mpc.gencost = [""", file=fp)
  for fuel in mpc_genfuels:
    c2, c1, c0 = get_gencosts(fuel)
    print ('  2 0 0 3 {:.7f} {:.3f} {:.3f};'.format (c2, c1, c0), file=fp)
  print ('];', file=fp)

  print ("""
%% generator unit type (see GENTYPES)
% use WT, PV, HY, ST, CT, ST for corresponding GENFUELS
% WT and PV will use WECC dynamics; the others will use Gov/Exc/PSS dynamics
mpc.gentype = {""", file=fp)
  for name in mpc_gentypes:
    print ("""  '{:s}';""".format(name), file=fp)
  print ('};', file=fp)

  print ("""
%% generator fuel type (see GENFUELS); use wind, solar, hydro, nuclear, ng, coal
mpc.genfuel = {""", file=fp)
  for name in mpc_genfuels:
    print ("""  '{:s}';""".format(name), file=fp)
  print ('};', file=fp)

  print ("""
%% bus names
mpc.bus_name = {""", file=fp)
  for name in mpc_bus_names:
    print ("""  '{:s}';""".format(name), file=fp)
  print ('};', file=fp)

#  print ("""
#%%-----  DC Line Data  -----%%
#%	fbus tbus status Pf Pt Qf Qt Vf Vt Pmin Pmax QminF QmaxF QminT QmaxT loss0 loss1 muPmin muPmax muQminF muQmaxF muQminT muQmaxT
#mpc.dcline = [""", file=fp)
#  print ('];', file=fp)

  print ('wrote {:d} generators totaling {:.2f} MW for loads totaling {:.2f} MW'.format(len(mpc_generators), total_gen, total_load))
  print ('suggest mpc = scale_load ({:.4f}, mpc)'.format(total_gen/total_load))

if __name__ == '__main__':
  case_id = 3
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
  #list_dict_table (d, 'EMTBranchLimit')
  #list_dict_table (d, 'EMTLoad')
  #list_dict_table (d, 'EMTDisconnectingCircuitBreaker')

  fp = open ('../matpower/' + sys_name + '.m', 'w')
  build_matpower (d, sys_name, fp, CASES[case_id]['swingbus'])
  fp.close()

