# Copyright (C) 2026 Meltran, Inc

"""
  Functions that document SPARQL queries and EMTDynamics models for ReadTheDocs.
"""

import rdflib
import time
import xml.etree.ElementTree as ET
import importlib.resources
import sys
import json

XML_QUERY_FILE = 'sparql_queries.xml'
PREFIX = None
DELIM = ':'
ROOT = None
PROFILE = 'profile.html#'

JSON_DYNAMICS_FILE = 'detailed_model_types.json'
TYPES = None

def load_root_queries(bPrint=False):
  global ROOT, PREFIX, TYPES
  if ROOT is None:
    # read the model types into dict
    jfile = importlib.resources.files('emthub.queries').joinpath(JSON_DYNAMICS_FILE)
    with open (jfile, 'r', encoding='utf-8', errors='strict') as fp:
      TYPES = json.load (fp)
    # read the queries into dict
    xfile = importlib.resources.files('emthub.queries').joinpath(XML_QUERY_FILE)
    with open (xfile, 'r', encoding='utf-8', errors='strict') as fp:
      s = fp.read()
    ROOT = ET.fromstring(s)
    nsCIM = ROOT.find('nsCIM').text.strip()
    nsRDF = ROOT.find('nsRDF').text.strip()
    nsEMT = ROOT.find('nsEMT').text.strip()
    PREFIX = """PREFIX r: <{:s}>\nPREFIX c: <{:s}>\nPREFIX e: <{:s}>""".format (nsRDF, nsCIM, nsEMT)
    if bPrint:
      print (PREFIX)

def add_header(label, level_char, fp):
  slen = len(label)
  shdr = level_char * slen
  print ('{:s}\n{:s}'.format (label, shdr), file=fp)

def find_cim_attribute (col, atts):
  for att in atts:
    if col == att.split('.')[1]:
      return att
  # catch one special case
  if col == 'sequenceNumber':
    return 'c:ACDCTerminal.sequenceNumber'
  print ('***** No CIM attribute found for', col, 'in', atts)
  return str(None)

def formatted_link (cls):
  if cls == 'FromTransformerEnd':
    return '**From** `TransformerEnd <{:s}TransformerEnd>`_'.format (PROFILE)
  if cls == 'ToTransformerEnd':
    return '**To** `TransformerEnd <{:s}TransformerEnd>`_'.format (PROFILE)
  if cls == 'ConnectivityNode1':
    return '`ConnectivityNode <{:s}ConnectivityNode>`_ **1**'.format (PROFILE)
  if cls == 'ConnectivityNode2':
    return '`ConnectivityNode <{:s}ConnectivityNode>`_ **2**'.format (PROFILE)
  return '`{:s} <{:s}{:s}>`_'.format (cls, PROFILE, cls)

def parse_columns (qry):
  d = {}

  # make a dictionary keyed on query return column names
  if 'DISTINCT' in qry:
    start = 'DISTINCT'
  else:
    start = 'SELECT'
  ret = qry.split(start)[1].split('WHERE')[0]
  if '(count(?' in ret:
    toks = ['mRID', 'count']
  else:
    toks = ret.split('?')[1:]
  cols = sorted ([s.strip() for s in toks])
  # print (cols)

  # make a list of referenced CIM class.attribute and class.association
  cim = []
  toks = qry.split()
  for tok in toks:
    if 'c:' in tok or 'e:' in tok:
      if tok[-1] != '.':
        cim.append (tok)
  #print (cim)

  # assign CIM class.attribute to columns
  for c in cols:
    cls = c.split('_')[0]
    if 'count' == c:
      d[c] = 'number of instances matching mRID'
    elif '_mRID' in c:
      d[c] = 'mRID for {:s}'.format (formatted_link(cls))
    elif '_name' in c:
      d[c] = 'name for {:s}'.format (formatted_link(cls))
    elif '_nominalVoltage' in c:
      d[c] = 'c:{:s}.nominalVoltage'.format (cls)
    elif '_type' in c:
      d[c] = 'class name of associated {:s}'.format (formatted_link(cls))
    elif '_endNumber' in c:
      d[c] = 'endNumber of the {:s}'.format (formatted_link(cls))
    elif 'mRID' in c:
      d[c] = 'c:IdentifiedObject.mRID'
    elif 'name' in c:
      d[c] = 'c:IdentifiedObject.name'
    elif 'amps' == c:
      d[c] = 'c:CurveData.xvalue'
    elif 'vs' == c:
      d[c] = 'c:CurveData.y1value'
    else:
      d[c] = find_cim_attribute (c, cim)
  return d

if __name__ == '__main__':
  load_root_queries(False)
  dict = {}
  for query in ROOT.findall('query'):
    qid = query.find('id').text.strip()
    dict[qid] = {}
    dict[qid]['keyfld'] = query.find('keyfld').text
    dict[qid]['sparql'] = query.find('value').text.strip()
    dict[qid]['columns'] = parse_columns (dict[qid]['sparql'])
    dict[qid]['description'] = query.find('description').text
    dict[qid]['classes'] = query.find('classes').text

  fp = open ('query_doc.rst', 'w')
#  print ('Header 2\n--------', file=fp)
#  print ('Header 3\n^^^^^^^^', file=fp)
#  print ('Header 4\n********', file=fp)
  for key in sorted(dict):
    if 'DEPRECATED' in dict[key]['description']:
      print ('Skipping deprecated query', key)
      continue
    add_header (key, '-', fp)
    q = dict[key]
    print (q['description'], file=fp)
    print ('\n', file=fp)

    # print cross-references to the main CIM classes of interest
    classes = q['classes'].split(',')
    class_links = '`{:s} <{:s}{:s}>`_'.format (classes[0], PROFILE, classes[0])
    suffix = ''
    if len(classes) > 1:
      suffix = 'es'
      for i in range(1, len(classes)):
        class_links = class_links + ', `{:s} <{:s}{:s}>`_'.format (classes[i], PROFILE, classes[i])
    print ('**CIM Class{:s}:** {:s}\n'.format(suffix, class_links), file=fp)
    if '*' in q['keyfld']:
      print ('**Python Multi-Key:** {:s}\n'.format(q['keyfld']), file=fp)
    else:
      print ('**Python Key:** {:s}\n'.format(q['keyfld']), file=fp)

    # print the query return table
    print ('.. list-table:: {:s} Query Dictionary\n   :widths: 50 50\n   :header-rows: 1\n'.format (key), file=fp)
    print ('   * - Python Field', file=fp)
    print ('     - CIM Attribute', file=fp)
    for col in sorted(q['columns']):
      print ('   * - {:s}\n     - {:s}'.format (col, q['columns'][col]), file=fp)
    print ('\n', file=fp)

  fp.close()

  # now document the detaield model types
  fp = open ('dynamics_doc.rst', 'w')
  for key in sorted(TYPES):
    mdl = TYPES[key]
    add_header (key, '_', fp)
    print ('**nameKind**: {:s}\n'.format (mdl['nameKind']), file=fp)
    print ('**modelKind**: {:s}\n'.format (mdl['modelKind']), file=fp)
    print ('**statusKind**: {:s}\n'.format (mdl['statusKind']), file=fp)
    print ('**description**: {:s}\n'.format (mdl['description']), file=fp)
    print ('**closestStandardModel**: {:s}\n'.format (mdl['closestStandardModel']), file=fp)
    print ('**mRID**: {:s}\n'.format (mdl['mRID']), file=fp)
    print ('.. list-table:: {:s} Parameters\n   :widths: 20 20 20 20 20\n   :header-rows: 1\n'.format (key), file=fp)
    print ('   * - Name', file=fp)
    print ('     - Number', file=fp)
    print ('     - Value', file=fp)
    print ('     - Unit', file=fp)
    print ('     - mRID', file=fp)
    for p in mdl['parameterDescriptors']:
      print ('   * - {:s}\n     - {:d}\n     - {:s}\n     - {:s}\n     - {:s}'.format (p['name'],
                                                                                       p['sequenceNumber'],
                                                                                       str(p['typicalValue']),
                                                                                       p['engineeringUnit'],
                                                                                       p['mRID']), file=fp)
    print ('\n', file=fp)

  fp.close()

