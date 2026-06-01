# Copyright (C) 2026 Meltran, Inc

"""
  Functions that document SPARQL queries for ReadTheDocs.
"""

import rdflib
import time
import xml.etree.ElementTree as ET
import importlib.resources
import sys

XML_QUERY_FILE = 'sparql_queries.xml'
PREFIX = None
DELIM = ':'
ROOT = None
PROFILE = 'profile.html#'

def load_root_queries(bPrint=False):
  global ROOT, PREFIX
  if ROOT is None:
    # read the queries into dict
    s = importlib.resources.read_text ('emthub.queries', XML_QUERY_FILE)
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
  print ('***** No CIM attribute found for', col, 'in', atts)
  return str(None)

def formatted_link (cls):
  if cls.startswith('From'):
    if cls.endswith('ConnectivityNode'):
      return '**From** `ConnectivityNode <{:s}ConnectivityNode>`_'.format (PROFILE)
    elif cls.endswith('TransformerEnd'):
      return '**From** `TransformerEnd <{:s}TransformerEnd>`_'.format (PROFILE)
  elif cls.startswith('To'):
    if cls.endswith('ConnectivityNode'):
      return '**To** `ConnectivityNode <{:s}ConnectivityNode>`_'.format (PROFILE)
    elif cls.endswith('TransformerEnd'):
      return '**To** `TransformerEnd <{:s}TransformerEnd>`_'.format (PROFILE)
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

