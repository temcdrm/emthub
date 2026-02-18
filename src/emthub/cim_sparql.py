# Copyright (C) 2025-2026 Meltran, Inc

import rdflib
import time
import xml.etree.ElementTree as ET
import pkg_resources as pkg

XML_QUERY_FILE = 'sparql_queries.xml'
PREFIX = None
DELIM = ':'
ROOT = None

def summarize_graph (g):
  q = """
  SELECT ?class (COUNT(?class) as ?cnt) WHERE {
    ?s a ?class .
  } group by ?class order by ?class"""

  print ('{:40s} {:40s} {:5s}'.format ('Namespace', 'Class Name', 'Count'))
  for r in g.query(q):
    nscls = r['class']
    idx = nscls.find('#')
    ns = nscls[:idx]
    cls = nscls[idx+1:]
    print('{:40s} {:40s} {:5d}'.format (ns, cls, int(r['cnt'])))

def list_dict_table(dict, tag=None):
  bMultiKey = False
  if tag is None:
    tbl = dict
    tag = 'Adhoc Query'
  else:
    if '*' in tag:
      bMultiKey = True
    tbl = dict[tag]
  print ('\n{:s}: key,{:s}'.format(tag, str(tbl['columns'])))
  if bMultiKey:
    for key, ary in tbl['vals'].items():
      for row in ary:
        print ('{:s},{:s}'.format (key, ','.join(str(row[c]) for c in tbl['columns'])))
  else:
    for key, row in tbl['vals'].items():
      print ('{:s},{:s}'.format (key, ','.join(str(row[c]) for c in tbl['columns'])))

def build_query (prefix, base, sysid):
  if sysid is not None:
    idx = base.find('WHERE {') + 8
    return prefix + '\n' + base[:idx] + """ VALUES ?sysid {{"{:s}"^^c:String}}\n""".format (sysid) + base[idx:]
  return prefix + '\n' + base

def query_for_values (g, tbl, sysid):
  bMultiKey = False
  if '*' in tbl['keyfld']:
    bMultiKey = True
  keyflds = tbl['keyfld'].strip('*').split(':')
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
    if bMultiKey:
      if key not in tbl['vals']:
        tbl['vals'][key] = []
      tbl['vals'][key].append(row)
    else:
      tbl['vals'][key] = row

def load_root_queries(bPrint=False):
  global ROOT, PREFIX
  if ROOT is None:
    # read the queries into dict
    xml_file = pkg.resource_filename (__name__, 'queries/{:s}'.format(XML_QUERY_FILE))
    if bPrint:
      print ('SPARQL from', xml_file)
    tree = ET.parse(xml_file)
    ROOT = tree.getroot()
    nsCIM = ROOT.find('nsCIM').text.strip()
    nsRDF = ROOT.find('nsRDF').text.strip()
    nsEMT = ROOT.find('nsEMT').text.strip()
    PREFIX = """PREFIX r: <{:s}>\nPREFIX c: <{:s}>\nPREFIX e: <{:s}>""".format (nsRDF, nsCIM, nsEMT)
    if bPrint:
      print (PREFIX)

def load_emt_dict (g, sysid, bTiming=False):
  global ROOT
  start_time = time.time()
  load_root_queries()
  dict = {}
  for query in ROOT.findall('query'):
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
              'EMTXfmrLimit', 'EMTBranchLimit', 'EMTBusVoltage', 'EMTBranchFlow', 'EMTXfmrFlow',
              'EMTIBRPlant*', 'EMTRotatingMachinePlant*']:
    if bTiming:
      query_start_time = time.time()
    query_for_values (g, dict[key], sysid)
    if bTiming:
      print ('  Running {:40s} took {:6.3f} s for {:5d} rows'.format (key, time.time() - query_start_time, len(dict[key]['vals'])))
  if bTiming:
    print ('Total query time {:6.3f} s'.format (time.time() - start_time))
  return dict

def load_ic_dict (g, bPrint=False):
  global ROOT
  start_time = time.time()
  # read the queries into dict
  load_root_queries()
  dict = {}
  for query in ROOT.findall('query'):
    qid = query.find('id').text.strip()
    dict[qid] = {}
    dict[qid]['keyfld'] = query.find('keyfld').text
    dict[qid]['sparql'] = query.find('value').text.strip()
    dict[qid]['columns'] = []
    dict[qid]['vals'] = {}
    #print (' ', qid, dict[qid]['keyfld'])

  for key in ['EMTBusVoltageIC', 'EMTBranchFlowIC', 'EMTXfmrFlowIC']:
    query_for_values (g, dict[key], sysid=None)

  if bPrint:
    print ('Total query time {:6.3f} s'.format (time.time() - start_time))
  return dict

def adhoc_sparql_dict (g, q, key_field):
  load_root_queries()
  dict = {}
  dict['keyfld'] = key_field
  dict['sparql'] = q
  dict['columns'] = []
  dict['vals'] = {}
  query_for_values (g, dict, sysid=None)
  return dict

