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

import xml.etree.ElementTree as ET

def process_xml (basename):
  # read the XML without cwd prefixed to the internal URIs
  with open('../test/'+basename+'.xml', 'r', encoding='utf-8') as file:
    xml_str = file.read()

  # load the XML tree and namespaces
  ET.register_namespace ('cim', 'http://www.ucaiug.org/grid18v15#')
  ET.register_namespace ('emt', 'http://opensource.ieee.org/emtiop01v01#')
  rdf_ns = 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'
  about_attr = f'{{{rdf_ns}}}about'
  root = ET.fromstring(xml_str)

  # Sort the children (Description elements) by their rdf:about values
  # Blank nodes or missing attributes safely fall back to an empty string
  root[:] = sorted(root, key=lambda child: child.get(about_attr, ""))

  # Sort the nested property tags inside each description element
  for description in root:
    description[:] = sorted(description, key=lambda prop: (prop.tag, prop.text or ""))

  # Save the perfectly sorted XML back to an XML RDF file
  tree = ET.ElementTree(root)
  ET.indent(tree, space='  ', level=0)  # Keeps the XML human-readable
  with open(basename+'.xml', 'wb') as f:
    f.write(b'<?xml version="1.0" encoding="utf-8"?>\n')
    tree.write(f, encoding='utf-8', xml_declaration=False)
  print('Saved cleanly sorted RDF/XML file to', basename+'.xml')

if __name__ == '__main__':
  for root in ['XfmrSat', 'XfmrSat_ic', 'IEEE39', 'IEEE39_ic', 'IEEE118', 'IEEE118_ic',
               'WECC240', 'WECC240_ic', 'SMIBDLL']:
    process_xml (root)


