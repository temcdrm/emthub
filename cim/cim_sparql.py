# Copyright (C) 2025 Meltran, Inc

import rdflib
import time
import xml.etree.ElementTree as ET

PREFIX = None
DELIM = ':'

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
      if fld in ['name', 'conn', 'sysid', 'bus1', 'bus2', 'id', 'eqid']:
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
              'EMTWeccWTGTA', 'EMTWeccWTGARA']:
    start_time = time.time()
    query_for_values (g, dict[key], sysid)
    print ('  Running {:40s} took {:6.3f} s for {:5d} rows'.format (key, time.time() - start_time, len(dict[key]['vals'])))
 #   list_dict_table (dict, key)
  return dict

if __name__ == '__main__':
  case = CASES[1]
  g = rdflib.Graph()
  fname = case['name'] + '.xml'
  g.parse (fname)
  print ('read', len(g), 'statements from', fname)
  #summarize_graph (g)

  start_time = time.time()
  d = load_emt_dict (g, 'sparql_queries.xml', case['id'])
  print ('Total query time {:6.3f} s'.format (time.time() - start_time))


