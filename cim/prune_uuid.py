# Copyright (C) 2026 Meltran, Inc

#import sys
import rdflib
#import uuid
import re

CIM_NS = 'http://www.ucaiug.org/ns#'
EMT_NS = 'http://opensource.ieee.org/emtiop#'
ref_prefix = 'file:///C:/src/emthub/cim/'

fnetwork = 'IEEE39.ttl'
fuidname = 'raw/ieee39mrids.dat'

fnetwork = 'WECC240.ttl'
fuidname = 'raw/wecc240mrids.dat'

def uuid_in_graph (val, g):
  ref = rdflib.URIRef (ref_prefix + val)
  return (ref, None, None) in g

if __name__ == '__main__':
  # read the existing mRID map for persistence
  uuids = {}
  fuid = open (fuidname, 'r')
  for uuid_ln in fuid.readlines():
    uuid_toks = re.split(r'[,\s]+', uuid_ln)
    if len(uuid_toks) > 2 and not uuid_toks[0].startswith('//'):
      cls = uuid_toks[0]
      nm = uuid_toks[1]
      key = cls + ':' + nm
      val = uuid_toks[2]
      uuids[key] = val
  fuid.close()
  print ('read {:d} instance mRIDs from {:s}'.format (len(uuids), fuidname))

  CIM = rdflib.Namespace (CIM_NS)
  EMT = rdflib.Namespace (EMT_NS)
  g = rdflib.Graph()
  g.bind('cim', CIM)
  g.bind('emt', EMT)

  g.parse (fnetwork, publicID="")
  print ('Read', len(g), 'network statements from', fnetwork)

  missing_uuids = []
  for key, val in uuids.items():
    bFound = uuid_in_graph (val, g)
    if not bFound:
      #print (key, val, bFound)
      missing_uuids.append(key)

  print ('Removing', len(missing_uuids), 'uuids not found')
  for key in missing_uuids:
    print (key, uuids[key])
    del uuids[key]

  print ('Leaves', len(uuids), 'uuids to write back to', fuidname)
  fuid = open(fuidname, 'w')
  for key, val in uuids.items():
      print('{:s},{:s}'.format(key.replace(':', ',', 1), val), file=fuid)
  fuid.close()

