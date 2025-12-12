# Copyright (C) 2025 Meltran, Inc

import rdflib

def summarize_graph (g, classes_found):
  q = """
  SELECT ?class (COUNT(?class) as ?cnt) WHERE {
    ?s a ?class .
  } group by ?class order by ?class"""

  g = rdflib.Graph()
  fname = root + '.ttl'
  g.parse (fname)

  d = {}
  d['statements'] = len(g)
  d['root'] = root
  d['classes'] = {}
  for r in g.query(q):
    nscls = r['class']
    idx = nscls.find('#')
    ns = nscls[:idx]
    cls = nscls[idx+1:]
    cnt = int(r['cnt'])
    d['classes'][cls] = cnt
    classes_found.add (cls)
  return d

if __name__ == '__main__':
  d = {}
  classes_found = set()
  for root in ['XfmrSat', 'IEEE39', 'IEEE118', 'WECC240']:
    d[root] = summarize_graph (root, classes_found)

  print ('{:39s} {:>8s} {:>8s} {:>8s} {:>8s}'.format ('Quantity in Example:', 'XfmrSat',  'IEEE39', 'IEEE118', 'WECC240'))
  print ('{:39s} {:8d} {:8d} {:8d} {:8d}'.format ('Statements (RDF Triples)', d['XfmrSat']['statements'], d['IEEE39']['statements'], d['IEEE118']['statements'], d['WECC240']['statements']))
  for cls in sorted(classes_found):
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    if cls in d['XfmrSat']['classes']:
      count1 = d['XfmrSat']['classes'][cls]
    if cls in d['IEEE39']['classes']:
      count2 = d['IEEE39']['classes'][cls]
    if cls in d['IEEE118']['classes']:
      count3 = d['IEEE118']['classes'][cls]
    if cls in d['WECC240']['classes']:
      count4 = d['WECC240']['classes'][cls]
    print ('{:39s} {:8d} {:8d} {:8d} {:8d}'.format (cls, count1, count2, count3, count4))

