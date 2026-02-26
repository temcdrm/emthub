# Copyright (C) 2026 Meltran, Inc

import sys
import emthub.api as emthub
 
case = {'id': '62CB0930-211D-4762-B5C1-27BF73EAC7C4',
 'name': 'SMIBDLL', 'xmlfile':'smibdll.xml', 'mridfile':'raw/smibdll_mrids.dat', 'ttlfile': 'smibdll.ttl',
 'wind_units': [], 'solar_units': ['1_1'], 'hydro_units': [], 'nuclear_units': [],
 'bus_ic': None, 'gen_ic': None, 'br_ic': None, 'ttl_ic': None,
 'swingbus': '5', 'load': 1.0, 'UseXfmrSaturation': True, 'dyrfile': None}

plant = {'generator': '1_1', 'dll_path': '../dll/bin/gfm_gfl_ibr2.dll',
         'components': [['ACLineSegment', '2_3_1'],
                        ['PowerTransformer', '2_1_0_1'],
                        ['PowerTransformer', '4_3_0_1']]
         }

tables = {
  'BUS': {
    'col_names': ['Number', 'Name', 'BaseKV', 'Type'], 
    'col_types': ['Integer', 'String', 'Float', 'Integer'], 
    'data': [
      [ 1, 'VSC',       0.6, 2], 
      [ 2, 'FdrIn',    34.5, 1], 
      [ 3, 'FdrOut',   34.5, 1], 
      [ 4, 'POC RPA', 230.0, 1], 
      [ 5, 'Grid', 230.0, 3],
      [ 6, 'SCR1', 230.0, 1],
      [ 7, 'SCR2', 230.0, 1],
      [ 8, 'SCR3', 230.0, 1],
      [ 9, 'SCR4', 230.0, 1],
      [10, 'SCR5', 230.0, 1],
      [11, 'SCR6', 230.0, 1],
      [12, 'SCR7', 230.0, 1]
      ]}, 
  'LOAD': {
    'col_names': ['Bus', 'Circuit', 'Status', 'PconstP', 'QconstP', 'PconstI', 'QconstI', 'PconstY', 'QconstY', 'Scale'], 
    'col_types': ['Integer', 'String', 'Integer', 'Float', 'Float', 'Float', 'Float', 'Float', 'Float', 'Float'], 
    'data': [
      ]}, 
  'FIXED SHUNT': {
    'col_names': ['Bus', 'ID', 'Status', 'P', 'Q'], 
    'col_types': ['Integer', 'String', 'Integer', 'Float', 'Float'], 
    'data': [
      ]}, 
  'GENERATOR': {
    'col_names': ['Bus', 'ID', 'P', 'Q', 'QT', 'QB', 'BaseMVA', 'Status'], 
    'col_types': ['Integer', 'String', 'Float', 'Float', 'Float', 'Float', 'Float', 'Integer'], 
    'data': [
      [1, '1', 100.0, 0.0, 50.0, -50.0, 100.0, 1]
      ]}, 
  'BRANCH': {
    'col_names': ['Bus1', 'Bus2', 'Circuit', 'R', 'X', 'B', 'RATE1', 'Status'], 
    'col_types': ['Integer', 'Integer', 'String', 'Float', 'Float', 'Float', 'Float', 'Integer'], 
    'data': [
      [2,  3, '1', 0.0100, 0.0400, 0.08, 200.0, 1],
      [5,  6, '1', 0.0099, 0.0990, 0.0, 200.0, 1],
      [5,  7, '1', 0.0199, 0.1990, 0.0, 200.0, 1],
      [5,  8, '1', 0.0249, 0.2490, 0.0, 200.0, 1],
      [5,  9, '1', 0.0332, 0.3323, 0.0, 200.0, 1],
      [5, 10, '1', 0.0399, 0.3990, 0.0, 200.0, 1],
      [5, 11, '1', 0.0499, 0.4990, 0.0, 200.0, 1],
      [5, 12, '1', 0.0666, 0.6657, 0.0, 200.0, 1]
      ]}, 
  'SYSTEM SWITCHING DEVICE': {
    'col_names': ['Bus1', 'Bus2', 'Circuit', 'X', 'RATE1', 'Status'], 
    'col_types': ['Integer', 'Integer', 'String', 'Float', 'Float', 'Integer'], 
    'data': [
      [4,  6, '1', 0.0, 200.0, 1], 
      [4,  7, '1', 0.0, 200.0, 1],
      [4,  8, '1', 0.0, 200.0, 1],
      [4,  9, '1', 0.0, 200.0, 1],
      [4, 10, '1', 0.0, 200.0, 1],
      [4, 11, '1', 0.0, 200.0, 1],
      [4, 12, '1', 0.0, 200.0, 1]
      ]}, 
  'TRANSFORMER': {
    'col_names': ['Bus1', 'Bus2', 'Bus3', 'Circuit', 'Status'], 
    'col_types': ['Integer', 'Integer', 'Integer', 'String', 'Integer'], 
    'data': [
      [4, 3, 0, '1', 1],
      [2, 1, 0, '1', 1]
      ], 
    'winding_data': [
      {'nwdgs': 2, 'r12': 0.01, 'x12': 0.08, 's12': 120.0, 'taps': [1.0, 1.0], 'kvs': [230.0, 34.5], 'mvas': [120.0, 0.0]},
      {'nwdgs': 2, 'r12': 0.0031, 'x12': 0.025, 's12': 120.0, 'taps': [1.0, 1.0], 'kvs': [34.5, 0.6], 'mvas': [120.0, 0.0]}
      ]}, 
  'SWITCHED SHUNT': {
    'col_names': ['Bus', 'Status', 'BINIT', 'N1', 'B1'], 
    'col_types': ['Integer', 'Integer', 'Float', 'Integer', 'Float'], 
    'data': [
      ]}}

if __name__ == '__main__':
  # create rawfile tables from Python dictionary
  baseMVA = 100.0
  bus_kvbases = {}
  kvbases = {}
  for bus in tables['BUS']['data']:
    bus_kvbases[bus[0]] = bus[2]
    kvbases['BV_{:.2f}'.format(bus[2])] = bus[2]

  g, ns1, ns2 = emthub.create_cim_rdf (tables, kvbases, bus_kvbases, baseMVA, case, bSerialize=False, bWantGraph=True)
  g, ns1, ns2 = emthub.add_ibr_plant (case, plant, g, ns1, ns2)
  emthub.write_cim_rdf (case, g, ns1, ns2)
  

