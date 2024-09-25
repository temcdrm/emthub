# Copyright (C) 2012-2023 Battelle Memorial Institute
# Copyright (C) 2024 Meltran, Inc
"""Write Alternative Transients Program (ATP) netlist from CIM.
"""

CASES = [
  {'id': '1783D2A8-1204-4781-A0B4-7A73A2FA6038', 
   'name': 'IEEE118', 
   'bus_ic': 'c:/src/cimhub/bes/ieee118mb.txt',
   'gen_ic': 'c:/src/cimhub/bes/ieee118mg.txt',
   'swingbus':'131', 
   'load': 0.6748},
  {'id': '2540AF5C-4F83-4C0F-9577-DEE8CC73BBB3', 
   'name': 'WECC240', 
   'bus_ic': 'c:/src/cimhub/bes/wecc240mb.txt',
   'gen_ic': 'c:/src/cimhub/bes/wecc240mg.txt',
   'swingbus':'2438', 
   'load': 1.0425}
]
"""Dictionary of example systems, IEEE118 and WECC240. Elements are:

   - id (str): mRID of the BES network model to export
   - name (str): root name of the exported ATP files
   - bus_ic (str): initial bus voltage magnitudes and angles from a load flow solution, e.g., from MATPOWER
   - gen_ic (str): initial generator injections from a load flow solution, e.g., from MATPOWER
   - swingbus (str): name of the bus for Thevenin equivalent, i.e., a Type 14 source
   - load (float): scaling factor on the nominal loads
"""

def reset_globals(case):
  """Reset counters and limits for the next ATP netlist export.
  
  Args:
    case (dict): one of the CASES
  """
  print ('This function requires an ATP user license.')

def convert_one_atp_model (query_file, fpath, case):
  """Reset counters and limits for the next ATP netlist export.

  Writes a file ending in *_net.atp*, which references support files for machines,
  IBR, controls, and other components. An ATP user license is required for the
  support files, and to run a simulation on the *_net.atp* file. Also writes an
  *atpmap* file that maps CIM bus (ConnectivityNode) names to ATP bus numbers.

  Args:
    query_file (str): definition of the SPARQL queries, should be qbes.xml
    fpath (str): relative path for ATP netlist files
    case (dict): one of the CASES
  """
  print ('This function requires an ATP user license.')

if __name__ == '__main__':
  print ('This function requires an ATP user license.')

