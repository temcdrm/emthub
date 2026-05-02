# Copyright (C) 2025-2026 Meltran, Inc

import importlib.resources
import shutil
import sys
import os

RDIR = 'emthub.examples'

CASES = [
  {'id': '6477751A-0472-4FD6-B3C3-3AD4945CBE56',
   'name': 'IEEE39', 
   'desc': '39 buses, 9 machines, 1 IBR',
   'legend_loc': 'lower right',
   'wind_units': [], 
   'solar_units': ['30_1'], 
   'hydro_units': [], 
   'nuclear_units': [],
   'swingbus': '31',
   'load': 1.0, 
   'UseXfmrSaturation': False,
   'UseMATPOWER': True},
  {'id': '1783D2A8-1204-4781-A0B4-7A73A2FA6038', 
   'name': 'IEEE118', 
   'desc': '193 buses, 56 machines, 19 IBR',
   'legend_loc': 'best', 
   'wind_units': ['132_W', '136_W', '138_W', '168_W', '180_W'],
   'solar_units': ['126_S', '128_S', '130_S', '140_S', '149_S', 
                   '151_S', '159_S', '165_S', '175_S', '179_S', 
                   '183_S', '185_S', '188_S', '191_S'],
   'hydro_units': [], 
   'nuclear_units': [],   
   'swingbus':'131', 
   'load': 0.6748, 
   'UseXfmrSaturation': False,
   'UseMATPOWER': True},
  {'id': '2540AF5C-4F83-4C0F-9577-DEE8CC73BBB3', 
   'name': 'WECC240', 
   'desc': '333 buses, 105 machines, 35 IBR',
   'legend_loc': 'best',
   'wind_units': ['10322_S', '10342_W', '13332_S', '21301_G',  '2332_S', 
                   '2431_S',  '2434_S', '24382_RG', '24386_SW', '2439_S'],
   'solar_units': ['2533_S', '2631_S', '32343_NW', '34331_S', '38351_NG', 
                   '3932_S', '3933_CG', '39331_NB', '40311_H', '40312_S', 
                   '4035_C', '40392_W', '41312_W', '42321_H', '5032_C', 
                   '50324_W', '61322_H', '61324_W', '62351_H', '63331_W', 
                   '64333_W', '6533_C', '65331_G', '70312_P', '70321_G'],
   'hydro_units': ['12321_H', '13311_H', '21302_H', '2637_H', '2638_H', 
                   '40352_H', '40391_H', '41311_H', '41321_H', '42312_H', 
                   '50311_H', '63352_H', '65332_H', '70322_H', '8033_H', 
                   '80341_H'],
   'nuclear_units': ['14311_N', '41322_N'],
   'swingbus':'3831',
   'old_swingbus':'2438', 
   'load': 1.02, 
   'UseXfmrSaturation': False,
   'UseMATPOWER': True},
  {'id': '93EA6BF1-A569-4190-9590-98A62780489E', 
   'name':'XfmrSat', 
   'desc': '5 buses, load rejection with transformer saturation',
   'legend_loc': 'best', 
   'wind_units':[], 
   'solar_units':[], 
   'hydro_units':[], 
   'nuclear_units':[],
   'swingbus': '1', 
   'load':1.0, 
   'emergency_ratings': True, 
   'UseXfmrSaturation': True,
   'UseMATPOWER': True},
  {'id': '62CB0930-211D-4762-B5C1-27BF73EAC7C4',
   'name': 'SMIBDLL', 
   'desc': '12 buses in a test harness, 1 IBR in a DLL',
   'legend_loc': 'best', 
   'wind_units': [], 
   'solar_units': ['1_1'], 
   'hydro_units': [], 
   'nuclear_units': [],
   'swingbus': '5', 
   'load': 1.0, 
   'UseXfmrSaturation': True,
   'UseMATPOWER': False,
   'ExtraFiles': ['create_smib_dll.py', 'gfm_gfl_ibr2.dll', 'gfm_gfl_ibr2.dll32']}
]
"""A list containing example case configurations as dictionaries."""

def list_cases():
  """List the names and descriptions of examples provided with the package.

  Prints information to the console. Use the *Idx* as an argument to *extract_case*
  to copy the example files for one case into the current directory.
  """
  print ('Idx {:8s} {:36s} {:s}'.format ('Name', 'mRID', 'Description'))
  for i in range(len(CASES)):
    print ('{:3d} {:8s} {:36s} {:s}'.format (i, CASES[i]['name'], CASES[i]['id'], CASES[i]['desc']))

def extract_case ():
  """Copy example files for one case into the current directory.

  Select the case by index, as obtained from *list_cases*. The 
  index must be passed as an argument on the command line.
  """
  idx = int(sys.argv[1])
  case = CASES[idx]
  root = case['name']

  # case-specific example files
  for ext in ['.raw', '.dyr', '_Network.json', '_mRIDs.dat', '.atp', '.prm']:
    src = importlib.resources.files(RDIR).joinpath('{:s}{:s}'.format(root, ext))
    with importlib.resources.as_file(src) as fpath:
      if os.path.isfile(fpath):
        shutil.copy(fpath, '.')

  if 'ExtraFiles' in case:
    for fname in case['ExtraFiles']:
      if not os.path.isfile('./{:s}'.format(fname)):
        src = importlib.resources.files(RDIR).joinpath(fname)
        with importlib.resources.as_file(src) as fpath:
          if os.path.isfile(fpath):
            shutil.copy(fpath, '.')

  # MATPOWER and ATP support files
  for fname in ['matpower_write_ic.m', 'ibr.pch', 'syncmach.pch', 'tacspv3.pch']:
    if not os.path.isfile('./{:s}'.format(fname)):
      src = importlib.resources.files(RDIR).joinpath(fname)
      with importlib.resources.as_file(src) as fpath:
        if os.path.isfile(fpath):
          shutil.copy(fpath, '.')

  # Python script files
  for fname in ['raw_to_rdf.py', 'bps_make_mpow.py', 'mpow.py', 'ic_to_rdf.py', 
                'cim_to_atp.py', 'atp.py', 'plot_bps.py', 'cim_summary.py',
                'test_cim_sparql.py']:
    if not os.path.isfile('./{:s}'.format(fname)):
      src = importlib.resources.files(RDIR).joinpath(fname)
      with importlib.resources.as_file(src) as fpath:
        if os.path.isfile(fpath):
          shutil.copy(fpath, '.')




