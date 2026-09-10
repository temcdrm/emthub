# Copyright (C) 2025-2026 Meltran, Inc

#import json
#import csv
import rdflib
#import os
import sys
from pathlib import Path
#from rdflib.namespace import XSD
#from otsrdflib import OrderedTurtleSerializer

import emthub.api as emthub

CIM_NS = 'http://www.ucaiug.org/grid18v15#'
EMT_NS = 'http://opensource.ieee.org/emtiop01v01#'

def main():
  idx = 4
  new_base = './models/'
  if len(sys.argv) > 1:
    idx = int(sys.argv[1])
  case = emthub.CASES[idx]

  g = rdflib.Graph(store='Oxigraph')
  fname = case['name']+'.ttl'
  g.parse (fname)
  print ('read', len(g), 'statements from', fname)
  q = """SELECT DISTINCT ?mRID ?name ?uri WHERE {
  ?s c:IdentifiedObject.name ?name.
  ?s c:IdentifiedObject.mRID ?mRID.
  ?s e:IEEECigreAPI.uri ?uri
 }
  """
  d = emthub.adhoc_sparql_dict (g, q, 'mRID')
  emthub.list_dict_table (d)
  for key, row in d['vals'].items():
    api_model = rdflib.URIRef (key)
    old_path = Path(row['uri'])
    new_path = Path(new_base + old_path.name).resolve()
    print ('change', old_path, '==>', new_path)

if __name__ == '__main__':
  main()

