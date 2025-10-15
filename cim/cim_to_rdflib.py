# Copyright (C) 2025 Meltran, Inc

import rdflib

CIMFILE = 'raw/IEEE118_CIM.xml'
LOCFILE = 'raw/IEEE118_CIM_Loc.xml'

if __name__ == '__main__':
  g = rdflib.Graph()
  g.parse (CIMFILE)
  g.parse (LOCFILE)
  print ('read', len(g), 'statements')

  q = """
  SELECT ?class (COUNT(?class) as ?cnt) WHERE {
    ?s a ?class .
  } group by ?class order by ?class"""

  print ('{:30s} {:30s} {:5s}'.format ('Namespace', 'Class Name', 'Count'))
  for r in g.query(q):
    nscls = r['class']
    idx = nscls.find('#')
    ns = nscls[:idx]
    cls = nscls[idx+1:]
    print('{:30s} {:30s} {:5d}'.format (ns, cls, int(r['cnt'])))

