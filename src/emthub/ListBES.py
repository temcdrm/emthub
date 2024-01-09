# Copyright (C) 2018-2023 Battelle Memorial Institute
# Copyright (C) 2024 Meltran, Inc
from SPARQLWrapper import SPARQLWrapper2
import emthub.EMTHubConfig as EMTHubConfig
import sys

def list_bes (cfg_file=None):

  if cfg_file is not None:
    EMTHubConfig.ConfigFromJsonFile (cfg_file)

  sparql = SPARQLWrapper2(EMTHubConfig.blazegraph_url)

  sparql.setQuery(EMTHubConfig.prefix + 
      """
      SELECT ?name ?id WHERE {
       ?s r:type c:ConnectivityNodeContainer.
       ?s c:IdentifiedObject.name ?name.
       ?s c:IdentifiedObject.mRID ?id.
      }
      ORDER by ?name
  """)

  ret = sparql.query()
  #print ('binding keys are:',ret.variables)
  print ('Bulk Electric System names and mRIDs:')
  for b in ret.bindings:
    print (b['name'].value,b['id'].value)

if __name__ == '__main__':
  cfg_file = None
  if len(sys.argv) > 1:
    cfg_file = sys.argv[1]
  list_bes (cfg_file)

