# Copyright (C) 2026 Meltran, Inc

import json
import rdflib

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

# try to match a PSSE DYR schema to CIM dynamics profile classes
if __name__ == '__main__':
#  onto = owl.get_ontology('../emtiop/emtiop.owl').load()
  g = rdflib.Graph()
  g.parse('../emtiop/emtiop.owl')
  summarize_graph (g)

  with open('dyr_config.json', 'r', encoding='utf-8-sig') as file:
    dyr = json.load (file)
  print ('PSSE       CIM                                      #dyr')
  for key, row in dyr.items():
    CIMclass = row['CIMclass']
    if len(CIMclass) > 0:
      print ('{:10s} {:40s} {:4d}'.format (key, row['CIMclass'], len(row['inputs'])))


