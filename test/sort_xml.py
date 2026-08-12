"""
Copyright 2026 3743 Authors

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

See the LICENSE file distributed with this work for copyright and
licensing information, the AUTHORS file for a list of copyright
holders, and the CONTRIBUTORS file for the list of contributors.

SPDX-License-Identifier: Apache-2.0"""

import os
import pathlib
#from lxml import etree
import xml.etree.ElementTree as ET
from rdflib import Graph, URIRef

def process_xml (g, root):
  print ('processing', root, 'to xml')
  raw_xml_str = g.serialize(format='pretty-xml')

  # 7. Parse the XML and sort <rdf:Description> elements by their URI
  rdf_ns = 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'
  about_attr = f'{{{rdf_ns}}}about'

  root = ET.fromstring(raw_xml_str)

  # Sort the children (Description elements) by their rdf:about values
  # Blank nodes or missing attributes safely fall back to an empty string
  root[:] = sorted(root, key=lambda child: child.get(about_attr, ""))

  # Optional: Sort the nested property tags inside each description element
  for description in root:
    description[:] = sorted(description, key=lambda prop: (prop.tag, prop.text or ""))

  # 8. Save the perfectly sorted XML back to an RDF file
  tree = ET.ElementTree(root)
  ET.indent(tree, space='  ', level=0)  # Keeps the XML human-readable
  with open('cleaned_output.rdf', "wb") as f:
    f.write(b'<?xml version="1.0" encoding="utf-8"?>\n')
    tree.write(f, encoding='utf-8', xml_declaration=False)
  print('Saved cleanly sorted RDF/XML file to: cleaned_output.rdf')

# # Sort triples deterministically (Subject, Predicate, Object) - from Google Search AI
# sorted_triples = sorted(g, key=lambda trip: (str(trip[0]), str(trip[1]), str(trip[2])))
#
# # Build a clean, predictable XML tree or use a sorted serialization workflow
# # (For strict VC diffs, W3C XML Canonicalization via lxml ensures clean diffs)
# #   - from Google Search AI
# canonical_data = etree.tostring(etree.fromstring(g.serialize(format='xml').encode('utf-8')), method='c14n2')
#
# with open(root + '.xml', 'wb') as f:
#   f.write(canonical_data)

def clean_ttl (root):
  g1 = Graph()
  g2 = Graph()

  g1.parse (root+'.ttl')

  cwd_uri = pathlib.Path(os.getcwd()).as_uri() + '/'
  target = ''
  print ('removing', cwd_uri, 'from internal URIs')

  for s, p, o in g1:
    s2 = URIRef(str(s).replace(cwd_uri, target)) if str(s).startswith(cwd_uri) else s
    p2 = URIRef(str(p).replace(cwd_uri, target)) if str(p).startswith(cwd_uri) else p
    o2 = URIRef(str(o).replace(cwd_uri, target)) if (isinstance(o, URIRef) and str(o).startswith(cwd_uri)) else o    
    g2.add((s2, p2, o2))

  g2.bind ('cim', 'http://www.ucaiug.org/grid18v15#')
  g2.bind ('emt', 'http://opensource.ieee.org/emtiop01v01#')

#  print (g2.serialize (format='pretty-xml', max_depth=1))
  return g2

if __name__ == '__main__':
  for root in ['XfmrSat', 'XfmrSat_ic', 'IEEE39', 'IEEE39_ic', 'IEEE118', 'IEEE118_ic',
               'WECC240', 'WECC240_ic', 'SMIBDLL']:
    #process_xml (root)
    g = clean_ttl (root)
    process_xml (g, root)
    quit()


