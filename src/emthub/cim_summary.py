# Copyright (C) 2025 Meltran, Inc
"""Summarizes the class counts in Turtle files
"""
import rdflib

def summarize_graph (root, classes_found):
  """ Create a dictionary of class names and counts found in an RDF graph.

  The Turtle file must exist in the current directory.

  Args:
    root (str): the basename of a Turtle file in tehe current directory.
    classes_found (set): adds each class (str) found to a set of classes found in many files.

  Returns:
    d: a dictionary of class names and their instance counts found in g.
  """

  q = """
  SELECT ?class (COUNT(?class) as ?cnt) WHERE {
    ?s a ?class .
  } group by ?class order by ?class"""

  g = rdflib.Graph()
  g.parse (root + '.ttl')

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

def print_cim_summaries (root_list):
  """ Prints a summary of class names and counts found in list of Turtle files.

  Only the list XfmrSat, IEEE39, IEEE118, and WECC240 is supported. The Turtle
  files must already exist in the current directory.

  Args:
    root_list (str): list of Turtle or base file names.
  """

  d = {}
  classes_found = set()
  for root in root_list:
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

