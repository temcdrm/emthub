# Copyright (C) 2018-2023 Battelle Memorial Institute
# Copyright (C) 2024 Meltran, Inc
# file: EMTHubConfig.py
"""Set the CIM namespace and Blazegraph URL
"""
import json
import urllib.request

DB_URL = ''
EMTHUB_PATH = ''
EMTHUB_PROG = ''

#******************************************************************************
# URL for the lyrasis Blazegraph container
blazegraph_url = "http://localhost:8889/bigdata/namespace/kb/sparql"

#******************************************************************************
# Default prefix for blazegraph queries; canonical version is now CIM100

cim100 = '<http://iec.ch/TC57/CIM100#'
# Prefix for all queries.
prefix = """PREFIX r: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX c: {cimURL}>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
""".format(cimURL=cim100)

def ConfigFromJsonFile (fname):
  global blazegraph_url, prefix, cim_ns, DB_URL, EMTHUB_PATH, EMTHUB_PROG
  with open(fname) as fp: 
    cfg = json.load(fp)
    if 'blazegraph_url' in cfg:
      blazegraph_url = cfg['blazegraph_url']
      DB_URL = blazegraph_url
#      print ('Configured URL to', blazegraph_url)
    if 'cim_ns' in cfg:
      cim_ns = cfg['cim_ns']
      prefix = """PREFIX r: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX c: {cimURL}>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
""".format(cimURL=cim_ns)
#      print ('Configured CIM Namespace to', cim_ns)
    if 'use_proxy' in cfg:
      if cfg['use_proxy'] == True:
        proxy_support = urllib.request.ProxyHandler({})
        opener = urllib.request.build_opener(proxy_support)
        urllib.request.install_opener(opener)
    if 'EMTHUB_PATH' in cfg:
      EMTHUB_PATH = cfg['EMTHUB_PATH']
    if 'EMTHUB_PROG' in cfg:
      EMTHUB_PROG = cfg['EMTHUB_PROG']

