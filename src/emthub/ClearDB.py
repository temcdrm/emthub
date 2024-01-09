# Copyright (C) 2018-2023 Battelle Memorial Institute
# Copyright (C) 2024 Meltran, Inc
from SPARQLWrapper import SPARQLWrapper2
import re
import emthub.EMTHubConfig as EMTHubConfig

drop_all = """drop all
"""

def clear_db (cfg_file=None):
  if cfg_file is not None:
    EMTHubConfig.ConfigFromJsonFile (cfg_file)
  sparql = SPARQLWrapper2 (EMTHubConfig.blazegraph_url)
  sparql.method = 'POST'
  sparql.setQuery (drop_all)
  ret = sparql.query()

