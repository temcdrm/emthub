# Copyright (C) 2025-2026 Meltran, Inc

"""
  Helper functions that read *rawfile* and *dyrfile* data into Python dictionaries. These
  dictionaries are then used to create RDF CIM data.
"""

import json
import csv
import importlib.resources
import os
import pandas as pd
import re
import io
import math

DYNAMICS_DEFAULTS = 'dynamics_defaults.json'
DYNAMICS_MAPPING = 'dyr_mapping.json'
METAFILE = 'psseraw.json'

def load_psse_dyrfile (case):
  """Load contents of a PSSE dyrfile into a Pandas dataframe.

  The PSSE DYR file does not conform to CSV standards:

    1) A line beginning with / or // is a comment to be ignored
    2) Rows span lines. Each row ends with a single /
    3) Field delimiters are comma (,) or any number of blanks
    4) Each row generally begins with bus number (int), model name (str), and ID (str) but the ID is not always quoted

  So, it is loaded into a Pandas data structure that offers more robust parsing, and flexible sizing, than standard Python
  arrays and CSV parsers.

  Args:
    case (dict): an example chosen from *emthub.cim_examples.CASES*

  Returns:
    dyr(DataFrame): the dynamics input data.
  """
  dyr = None
  dyrfile = case['name']+'.dyr'
  if os.path.exists(dyrfile):
    buf = io.StringIO()
    maxcols = 0
    ncols = 0
    with open (dyrfile, 'r') as file:
      for line in file:
        line = line.strip()
        line = line.replace("'", "")
        if len(line) == 0 or line.startswith ('/'):
          continue
        s = re.sub (r'[ ,\t]+', ',', line)
        if s.endswith('/'):
          s = s.replace(',/','\n')
          s = s.replace('/','\n')
          ncols += s.count(',')
          if ncols > maxcols:
            maxcols = ncols
          ncols = 0
        else:
          s = s + ','
          ncols += s.count(',')
        buf.write(s)
#    buf.seek(0)
#    print (buf.read())
    maxcols += 1
#    print ('maxcols', maxcols)
    buf.seek(0)
    dyr = pd.read_csv (buf, names=range(maxcols))
    buf.close()
  return dyr

def row_length (row):
  for i in range(2, len(row)):
    if isinstance(row[i], float) and math.isnan(row[i]):
      return i
  return len(row)

def summarize_psse_dyrfile (dyr, case, bDetails=False):
  """Enumerate contents of a loaded PSSE dyrfile dataframe.

  Use this for checking the numbers and sizes of dynamic models read.
  Each model of the same type should have the same size. Names of the
  parameters are not available from dyr files, so not available in
  this function.

  Args:
    dyr (DataFrame): return value from *load_psse_dyrfile*
    case (dict): an example chosen from *emthub.cim_examples.CASES*
    bDetails (bool): print *dyr* using built-in Pandas formatting

  Returns:
    models (dict): a dictionary of the dynamic models found, with sizes and instance counts
  """
  print ('Dynamics data from', case['name']+'.dyr', 'size =', dyr.shape)
  if bDetails:
    print (dyr)
  models = {}
  for row in dyr.itertuples(index=False):
    model_type = str(row[1])
    n = row_length (row)
    if model_type not in models:
      models[model_type] = {'count': 1, 'min_len': n, 'max_len': n}
    else:
      models[model_type]['count'] += 1
      if n < models[model_type]['min_len']:
        models[model_type]['min_len'] = n
      if n > models[model_type]['max_len']:
        models[model_type]['max_len'] = n

  print (case['name'])
  print ('Model   Count   Nmin   Nmax')
  for key in sorted (models):
    row = models[key]
    print ('{:6s} {:6d} {:6d} {:6d}'.format (key, row['count'], row['min_len'], row['max_len']))
  return models

def match_dyr_generators (df, bPrint=False):
  """Collect dyrfile models from Pandas dataframe into a Python dictionary by generator name/id.

  A conventional generator may have several dynamics models, e.g., the machine itself,
  excitation system, governor, power system stabilizer, etc. An IBR may also have several
  dynamic models associated with it, e.g., plant controller, regulator, converter controller,
  wind dynamics, etc. So, the return dictionary is keyed on generator, than one or more
  model types.  The model types are taken from column 2 of each dyr file entry.

  Args:
    df (DataFrame): the return value from *load_psse_dyrfile*
    bPrint (bool): print the dynamic model types and data found for each generator

  Returns:
    d (dict): a dictionary of dynamic models, keyed on generator ID and then model type
  """
  d = {}
  for row in df.itertuples(index=False):
    bus = str(row[0])
    model_type = str(row[1])
    genid = str(row[2])
    key = '{:s}_{:s}'.format (bus, genid)
    if key not in d:
      d[key] = {}
    n = row_length (row)
    d[key][model_type] = []
    a = d[key][model_type]
    for i in range(3,n):
      a.append (row[i])
    if bPrint:
      print ('Dyr Entry:', key, model_type, a)
  return d

def load_dynamics_defaults():
  """Load example default settings for dynamics into a Python dictionary.

  The data comes from a JSON file included in the package named *dynamics_defaults.json*.

  Returns:
    dyn_settings(dict): dictionary of default values, keyed on model type and then attribute.
  """
  s = importlib.resources.read_text ('emthub.queries', DYNAMICS_DEFAULTS)
  dyn_settings = json.loads (s)
  return dyn_settings

def load_dynamics_mapping(bReverseLookup = True):
  """Load a dictionary of CIM classes and attributes corresponding to dyr file contents.

  The data comes from a JSON file included in the package named *dyr_mapping.json*.
  Use this function to translate *dyrfile* contents to the CIM classes and attributes.
  A reverse lookup option keys on CIM classes, to create missing *dyrfile* data from
  a CIM model based only on a *rawfile*.

  Args:
    bReverseLookup (bool): key on the CIM class instead of the dyr model name

  Returns:
    attmap(dict): dictionary keyed on a dyr model name, with CIM class and attributes.
  """
  s = importlib.resources.read_text ('emthub.queries', DYNAMICS_MAPPING)
  d = json.loads (s)
  if not bReverseLookup:
    return d
  attmap = {}
  for dyr, item in d.items():
    cls = item['CIMclass']
    attmap[dyr] = {'CIMclass': cls, 'AttMap': {}}
    for i in range(len(item['parameters_after_ID'])):
      att = item['parameters_after_ID'][i]
      attmap[dyr]['AttMap'][att['cim']] = i
  return attmap

def load_psse_meta():
  """Load PSSE rawfile metadata into a Python dictionary.

  The data comes from a JSON file included in the package named *psseraw.json*.
  It currently supports versions 33, 34, and 35. This function does not have
  to called separately from *load_psse_rawfile*.

  Returns:
    meta(dict): schema of tables found in supported *rawfile* versions.
  """
  s = importlib.resources.read_text ('emthub.queries', METAFILE)
  meta = json.loads (s)
  return meta

def print_psse_table (tables, table_name):
  """Print a named dictionary loaded from section of a PSSE rawfile.

  Use this function to verify the data imported from *load_psse_rawfile*.
  Also reveals the column names in each table.

  Args:
    tables (dict): returned from *load_psse_rawfile*
    table_name (str): name of the table to print. Should be one of 'BUS', 'LOAD', 'FIXED SHUNT', 'SWITCHED SHUNT', 'GENERATOR', 'BRANCH', 'SYSTEM SWITCHING DEVICE', 'TRANSFORMER'
  """
  if table_name not in tables:
    print ('***', table_name, 'not found')
    return
  table = tables[table_name]
  print (table_name, 'has', len(table['data']), 'rows of', table['col_names'])
  if table_name == 'TRANSFORMER':
    for i in range (len(table['data'])):
      print (table['data'][i], table['winding_data'][i])
  else:
    for row in table['data']:
      print (row)

def read_version_33_34(tables, baseMVA, reader, sections, bTwoTitles, bPrint=False):
  for section in sections:
    sect = sections[section]
    columns = sect['columns']
    column_names = ','.join([columns[i]['Name'] for i in range(len(columns))])
    if bPrint:
      print ('Table "{:s}" has {:d} raw columns, using {:d}: {:s}'.format (section, sect['column_count'], len(columns), column_names))
  title = ','.join(next(reader))
  if bPrint:
    print('MVA base = {:.1f}, Title: {:s}'.format(baseMVA, title))
  if bTwoTitles:
    title = ','.join(next(reader))
    if bPrint:
      print ('Second Title: ', title)
  table = None
  bTransformer = False
  for row in reader:
#    print (row)
    if '@!' in row[0]:
      continue
    if len(row) > 1 and 'END OF' in row[0] and 'BEGIN' in row[1]: # start a new table
      i1 = row[1].find('BEGIN') + 6
      i2 = row[1].find(' DATA')
      table_name = row[1][i1:i2]
      if table_name in sections:
        sect = sections[table_name]
        n_columns = len(sect['columns'])
        total_columns = sect['column_count']
        column_names = [sect['columns'][i]['Name'] for i in range(n_columns)]
        column_indices = [sect['columns'][i]['Index'] for i in range(n_columns)]
        column_types = [sect['columns'][i]['Type'] for i in range(n_columns)]
        if bPrint:
          print ('found', table_name, 'data with', total_columns, 'columns, using', n_columns)
          print ('  column_names:', column_names)
          print ('  column_index:', column_indices)
          print ('  column_types:', column_types)
        # create a new table to hold the data of interest
        table = {'col_names': column_names, 'col_types': column_types, 'data': []}
        if table_name == 'TRANSFORMER':
          table['winding_data'] = [] # impedances, ratings, and taps on extra lines
          bTransformer = True
        else:
          bTransformer = False
        tables[table_name] = table
        if bPrint:
          print (table)
      else:
        if bPrint:
          print ('ignoring', table_name, 'raw file data')
        table = None
    elif table is not None:
      data = []
      ncol_read = len(row)
      for i in range(n_columns):
        idx = column_indices[i]
        if idx >= ncol_read:
          print ('** need column index {:d} but read only {:d} columns a'.format (idx, ncol_read))
          quit()
        val = row[idx]
        if column_types[i] == 'Float':
          data.append(float(val))
        elif column_types[i] == 'Integer':
          data.append(int(val))
        else:
          data.append(val.strip('\' '))
      if bTransformer: # impedance and winding data is provided on extra lines
        #print (data)
        row = next(reader)
        #print (row)
        ncol_read = len(row)
        if data[2] > 0.0:
          if ncol_read > 8:
            nwdgs = 3
            winding_data = {'nwdgs': nwdgs, 'r12':float(row[0]), 'x12':float(row[1]), 's12':float(row[2]),
                            'r23':float(row[3]), 'x23':float(row[4]), 's23':float(row[5]),
                            'r13':float(row[6]), 'x13':float(row[6]), 's13':float(row[7]), 
                            'taps':[], 'kvs':[], 'mvas':[]}
          else:
            print ('** need 9 impedance values for a 3-winding transformer, but read only {:d}'.format (ncol_read))
            quit()
        else:
          if ncol_read > 2:
            nwdgs = 2
            winding_data = {'nwdgs': nwdgs, 'r12':float(row[0]), 'x12':float(row[1]), 's12':float(row[2]), 'taps':[], 'kvs':[], 'mvas':[]}
          else:
            print ('** need 3 impedance values for a 2-winding transformer, but read only {:d}'.format (ncol_read))
            quit()
        for i in range(nwdgs):
          row = next(reader)
          ncol_read = len(row)
          winding_data['taps'].append(float(row[0]))
          winding_data['kvs'].append(float(row[1])) # this may be zero, in which case take from the bus nominal voltages
          if ncol_read > 5:
            winding_data['mvas'].append(float(row[3])) # this may still be zero in the rawfile, TODO: verify index 3 or 5
          else:
            winding_data['mvas'].append(0.0)
        table['winding_data'].append (winding_data)
      table['data'].append (data)

def load_psse_rawfile(fname, bPrint=False):
  """Load contents of a PSSE rawfile into a Python dictionary.

  Versions 33, 34, and 35 are supported. The corresponding dynamics data should be read using
  *load_psse_dyrfile*, which does not have versions.

  Args:
    fname (str): name of the PSSE *rawfile* to read.
    bPrint (bool): for debugging, print the contents of each *rawfile* row as it's parsed.

  Returns:
    tables(dict): dictionary of table data, following the schema from *load_psse_meta*.
    kvbases(dict): dictionary of voltage (kV) bases found in the system data, keyed on a constructed name for CIM *BaseVoltage* instances.
    bus_kvbases(dict): dictionary of voltage (kV) bases for each bus in the system.
    baseMVA(float): the system MVA base.
  """
  meta = load_psse_meta()
  tables = {}
  bus_kvbases = {}
  kvbases = {}
  baseMVA = -1.0
  with open(fname, 'r') as csvfile:
    reader = csv.reader(csvfile, quotechar="'") # don't use " because it causes problems for CSV reader in title lines
    row = next(reader)
    while row[0].startswith ('@!'):
      row = next(reader)
    baseMVA = float(row[1])
    raw_version = int(row[2])
    if bPrint:
      print ('Rawfile Base MVA', baseMVA, ', version', raw_version)
    if raw_version == 33:
      read_version_33_34 (tables, baseMVA, reader, meta['version_sections']['33'], bTwoTitles=False, bPrint=bPrint)
    elif raw_version == 34:
      read_version_33_34 (tables, baseMVA, reader, meta['version_sections']['34'], bTwoTitles=True, bPrint=bPrint)
    elif raw_version == 35:
      read_version_33_34 (tables, baseMVA, reader, meta['version_sections']['35'], bTwoTitles=True, bPrint=bPrint)
    else:
      print ('Unknown RAW File Version = {:d} from {:s}'.format (raw_version, fname))
      quit()

  for bus in tables['BUS']['data']:
    bus_kvbases[bus[0]] = bus[2]
    kvbases['BV_{:.2f}'.format(bus[2])] = bus[2]

  return tables, kvbases, bus_kvbases, baseMVA

