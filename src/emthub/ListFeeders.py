# Copyright (C) 2018-2023 Battelle Memorial Institute
# Copyright (C) 2024 Meltran, Inc
"""List the distribution feeders found in a Blazegraph database.
"""
from SPARQLWrapper import SPARQLWrapper2
import emthub.EMTHubConfig as EMTHubConfig
import sys

def list_feeders (cfg_file=None):
  """ List the names and mRID values of distribution feeders found in the Blazegraph database.

  Blazegraph must already be started. If not already configured, cfg_file must be provided.
  Writes a list of feeder names and mRIDs to the console.

  Args:
    cfg_file (str): configuration file for Blazegraph.
  """

  if cfg_file is not None:
    EMTHubConfig.ConfigFromJsonFile (cfg_file)

  sparql = SPARQLWrapper2(EMTHubConfig.blazegraph_url)

  sparql.setQuery(EMTHubConfig.prefix + 
      """
      SELECT ?feeder ?fid ?station ?sid ?subregion ?sgrid ?region ?rgnid WHERE {
       ?s r:type c:Feeder.
       ?s c:IdentifiedObject.name ?feeder.
       ?s c:IdentifiedObject.mRID ?fid.
       ?s c:Feeder.NormalEnergizingSubstation ?sub.
       ?sub c:IdentifiedObject.name ?station.
       ?sub c:IdentifiedObject.mRID ?sid.
       ?sub c:Substation.Region ?sgr.
       ?sgr c:IdentifiedObject.name ?subregion.
       ?sgr c:IdentifiedObject.mRID ?sgrid.
       ?sgr c:SubGeographicalRegion.Region ?rgn.
       ?rgn c:IdentifiedObject.name ?region.
       ?rgn c:IdentifiedObject.mRID ?rgnid.
      }
      ORDER by ?station ?feeder
  """)

  ret = sparql.query()
  #print ('binding keys are:',ret.variables)
  print ('Feeder names and mRIDs:')
  for b in ret.bindings:
    print (b['feeder'].value,b['fid'].value)

if __name__ == '__main__':
  cfg_file = None
  if len(sys.argv) > 1:
    cfg_file = sys.argv[1]
  list_feeders (cfg_file)

