# Copyright (C) 2024-25 Meltran, Inc

import os
import sys
import json

mod_name = 'IBR2'
json_name = 'gfm_gfl_ibr2.json'

if __name__ == '__main__':
  if len(sys.argv) > 1:
    json_name = sys.argv[1]

  with open(json_name, 'r') as file:
    d = json.load(file)

  dll_name = os.path.basename (d['location'])
  function_name, function_ext = os.path.splitext (dll_name)

  fp = open(mod_name + '.mod', 'wt')
  print ('MODEL m{:s}'.format (mod_name), file=fp)
  print ('INPUT', file=fp)
  print ('  {:s}'.format (','.join([d['InputPortsInfo'][i]['Name'] for i in range(d['NumInputPorts'])])), file=fp)
  print ('DATA', file=fp)
  for i in range(d['NumParameters']):
    print ('  {:12s} {{dflt: {:f}}}'.format (d['ParametersInfo'][i]['Name'], d['ParametersInfo'][i]['DefaultValue']), file=fp)
  print ('OUTPUT', file=fp)
  print ('  {:s}'.format (','.join([d['OutputPortsInfo'][i]['Name'] for i in range(d['NumOutputPorts'])])), file=fp)
  print ('VAR', file=fp)
  print ('  {:s}'.format (','.join([d['OutputPortsInfo'][i]['Name'] for i in range(d['NumOutputPorts'])])), file=fp)
  print ('INIT', file=fp)
  for i in range(d['NumOutputPorts']):
    print ('  {:s}:=0.0'.format (d['OutputPortsInfo'][i]['Name']), file=fp)
  print ('ENDINIT', file=fp)
  print ('MODEL m1 FOREIGN {:s} {{ixdata:{:d}, ixin:{:d}, ixout:{:d}, ixvar:0}}'.format (function_name.upper(), 
         d['NumParameters'], 
         d['NumInputPorts']+2, # appending ATP t and stoptime
         d['NumOutputPorts']), file=fp)
  print ('EXEC', file=fp)
  print ('  USE m1 AS m1', file=fp)
  for i in range(d['NumParameters']):
    print ('    DATA xdata[{:d}] := {:12s} -- {:s}'.format (i+1, d['ParametersInfo'][i]['Name'], d['ParametersInfo'][i]['Unit']), file=fp)
  print ('    -- the DLL will convert inputs to kV, kA as needed', file=fp)
  for i in range(d['NumInputPorts']):
    print ('    INPUT xin[{:d}] := {:12s} -- {:s}'.format (i+1, d['InputPortsInfo'][i]['Name'], d['InputPortsInfo'][i]['Unit']), file=fp)
  print ('    INPUT xin[{:d}] := t'.format (d['NumInputPorts']+1), file=fp)
  print ('    INPUT xin[{:d}] := stoptime'.format (d['NumInputPorts']+2), file=fp)
  print ('    -- the DLL will convert inverter voltages from kV to V', file=fp)
  for i in range(d['NumOutputPorts']):
    print ('    OUTPUT {:12s} := xout[{:d}] -- {:s}'.format (d['OutputPortsInfo'][i]['Name'], i+1, d['OutputPortsInfo'][i]['Unit']), file=fp)
  print ('  ENDUSE', file=fp)
  print ('ENDEXEC', file=fp)
  print ('ENDMODEL', file=fp)
  fp.close()



