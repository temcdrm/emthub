# Copyright (C) 2025 Meltran, Inc

import json
import csv

RAWFILE = '../../cimhub/bes/raw/ieee118/ieee-118-bus-v4.raw'
METAFILE = 'psseraw.json'

tables = {}
baseMVA = -1.0
kvbases = {}

def print_table (table_name):
  table = tables[table_name]
  if table is None:
    print ('***', table_name, 'not found')
    return
  print (table_name, 'has', len(table['data']), 'rows of', table['col_names'])
  for row in table['data']:
    print (row)

if __name__ == '__main__':
  with open(METAFILE, 'r') as file:
    meta = json.load (file)
  for section in meta['sections']:
    sect = meta['sections'][section]
    columns = sect['columns']
    column_names = ','.join([columns[i]['Name'] for i in range(len(columns))])
    print ('Table "{:s}" has {:d} raw columns, using {:d}: {:s}'.format (section, sect['column_count'], len(columns), column_names))

  table = None
  with open(RAWFILE, 'r') as csvfile:
    reader = csv.reader(csvfile)
    row = next(reader)
    baseMVA = float(row[1])
    title = next(reader)[0]
    print('MVA base = {:.1f}, Title = {:s}'.format(baseMVA, title))
    for row in reader:
      if len(row) > 1 and 'END OF' in row[0] and 'BEGIN' in row[1]: # start a new table
        i1 = row[1].find('BEGIN') + 6
        i2 = row[1].find(' DATA')
        table_name = row[1][i1:i2]
        if table_name in meta['sections']:
          sect = meta['sections'][table_name]
          n_columns = len(sect['columns'])
          total_columns = sect['column_count']
          column_names = [sect['columns'][i]['Name'] for i in range(n_columns)]
          column_indices = [sect['columns'][i]['Index'] for i in range(n_columns)]
          column_types = [sect['columns'][i]['Type'] for i in range(n_columns)]
          print ('found', table_name, 'data with', total_columns, 'columns, using', n_columns)
          print ('  column_names:', column_names)
          print ('  column_index:', column_indices)
          print ('  column_types:', column_types)
          # create a new table to hold the data of interest
          table = {'col_names': column_names, 'col_types': column_types, 'data': []}
          tables[table_name] = table
          print (table)
        else:
          print ('ignoring', table_name, 'raw file data')
          table = None
      elif table is not None:
        data = []
        while len(row) < total_columns:
          row = row + next(reader)
          if len(row) > total_columns:
            print ('*** read', len(row), table_name, 'columns from the raw file. Need to match', total_columns)
        for i in range(n_columns):
          val = row[column_indices[i]]
          if column_types[i] == 'Float':
            data.append(float(val))
          elif column_types[i] == 'Integer':
            data.append(int(val))
          else:
            data.append(val.strip('\' '))
        table['data'].append (data)

  print_table ('BUS')
  print_table ('LOAD')
  print_table ('FIXED SHUNT')
  print_table ('GENERATOR')
  print_table ('BRANCH')
  print_table ('TRANSFORMER')

  for bus in tables['BUS']['data']:
    kvbases[bus[0]] = bus[2]

  print ('Bus kV Bases =', kvbases)
  

