# Copyright (C) 2024-26 Meltran, Inc

import os
import sys
import json
from ctypes import *
from enum import IntEnum

class DLLDataType(IntEnum): 
  char_T     = 1
  int8_T     = 2
  uint8_T    = 3
  int16_T    = 4
  uint16_T   = 5
  int32_T    = 6
  uint32_T   = 7
  real32_T   = 8
  real64_T   = 9
  c_string_T = 10

def get_cim_parameter_kind (idx):
  if idx == 1:
    return 'Char_Val'
  if idx == 2:
    return 'Int8_Val'
  if idx == 3:
    return 'Uint8_Val'
  if idx == 4:
    return 'Int16_Val'
  if idx == 5:
    return 'Uint16_Val'
  if idx == 6:
    return 'Int32_Val'
  if idx == 7:
    return 'Uint32_Val'
  if idx == 8:
    return 'Real32_Val'
  if idx == 9:
    return 'Real64_Val'
  if idx == 10:
    return 'Char_Ptr'
  

class DLLReturnValue(IntEnum):
  OK = 0
  Message = 1
  Error = 2

class DLLSIGNAL(Structure):
  _fields_ = [('Name', c_char_p),
              ('Description', c_char_p),
              ('Unit', c_char_p),
              ('DataType', c_int),
              ('Width', c_int)]

class DLLDEFAULT(Union):
  _fields_ = [('char_T', c_char),
              ('char_T_p', c_char_p),
              ('int8_T', c_int),
              ('uint8_T', c_int),
              ('int16_T', c_int),
              ('uint16_T', c_int),
              ('int32_T', c_int),
              ('uint32_T', c_int),
              ('real32_T', c_float),
              ('real64_T', c_double)]

class DLLMINMAX(Union):
  _fields_ = [('char_T', c_char),
              ('int8_T', c_int),
              ('uint8_T', c_int),
              ('int16_T', c_int),
              ('uint16_T', c_int),
              ('int32_T', c_int),
              ('uint32_T', c_int),
              ('real32_T', c_float),
              ('real64_T', c_double)]

class DLLPARAMETER(Structure):
  _fields_ = [('Name', c_char_p),
              ('GroupName', c_char_p),
              ('Description', c_char_p),
              ('Unit', c_char_p),
              ('DataType', c_int),
              ('FixedValue', c_int),
              ('DefaultValue', DLLDEFAULT),
              ('MinValue', DLLMINMAX),
              ('MaxValue', DLLMINMAX)
              ]

class DLLINFO(Structure):
  _fields_ = [('DLLInterfaceVersion', c_ubyte * 4),
              ('ModelName', c_char_p),
              ('ModelVersion', c_char_p),
              ('ModelDescription', c_char_p),
              ('GeneralInformation', c_char_p),
              ('ModelCreated', c_char_p),
              ('ModelCreator', c_char_p),
              ('ModelLastModifiedDate', c_char_p),
              ('ModelLastModifiedBy', c_char_p),
              ('ModelModifiedComment', c_char_p),
              ('ModelModifiedHistory', c_char_p),
              ('FixedStepBaseSampleTime', c_double),
              ('EMT_RMS_Mode', c_ubyte),
              ('NumInputPorts', c_int),
              ('InputPortsInfo', c_void_p),
              ('NumOutputPorts', c_int),
              ('OutputPortsInfo', c_void_p),
              ('NumParameters', c_int),
              ('ParametersInfo', c_void_p),
              ('NumIntStates', c_int),
              ('NumFloatStates', c_int),
              ('NumDoubleStates', c_int)]

class DLLINSTANCE(Structure): # TODO: not tested yet
  _fields_ = [('ExternalInputs', c_void_p),
              ('ExternalOutputs', c_void_p),
              ('Parameters', c_void_p),
              ('Time', c_double),
              ('SimTool_EMT_RMS_Mode', c_ubyte),
              ('LastErrorMessage', c_char_p),
              ('LastGeneralMessage', c_char_p),
              ('IntStates', c_void_p),      # to c_int[]
              ('FloatStates', c_void_p),    # to c_float[]
              ('DoubleStates', c_void_p)]   # to c_double[]

def get_dll_interface (dll_name, bPrint = True):
  dll = CDLL (dll_name)
  if bPrint:
    print (dll_name, dll)

  dll.Model_GetInfo.restype = c_void_p
  info = DLLINFO.from_address(dll.Model_GetInfo())
  if bPrint:
    print ('Model_GetInfo call', info)
    print ('DLLInterfaceVersion', info.DLLInterfaceVersion[0], info.DLLInterfaceVersion[1], info.DLLInterfaceVersion[2], info.DLLInterfaceVersion[3])
    print ('ModelName', info.ModelName)
    print ('ModelVersion', info.ModelVersion)
    print ('ModelDescription', info.ModelDescription)
    print ('GeneralInformation', info.GeneralInformation)
    print ('ModelCreated', info.ModelCreated)
    print ('ModelCreator', info.ModelCreator)
    print ('ModelLastModifiedDate', info.ModelLastModifiedDate)
    print ('ModelLastModifiedBy', info.ModelLastModifiedBy)
    print ('ModelModifiedComment', info.ModelModifiedComment)
    print ('ModelModifiedHistory', info.ModelModifiedHistory)
    print ('FixedStepBaseSampleTime', info.FixedStepBaseSampleTime)
    print ('EMT_RMS_Mode', info.EMT_RMS_Mode)
    print ('InputPorts', info.NumInputPorts, 'ptr', info.InputPortsInfo)
    print ('OutputPorts', info.NumOutputPorts, 'ptr', info.OutputPortsInfo)
    print ('Parameters', info.NumParameters, 'ptr', info.ParametersInfo)
    print ('NumIntStates', info.NumIntStates)
    print ('NumFloatStates', info.NumFloatStates)
    print ('NumDoubleStates', info.NumDoubleStates)

  offset = sizeof(DLLSIGNAL)
  inputs = [DLLSIGNAL.from_address(info.InputPortsInfo + offset*i) for i in range(info.NumInputPorts)]
  outputs = [DLLSIGNAL.from_address(info.OutputPortsInfo + offset*i) for i in range(info.NumOutputPorts)]
  offset = sizeof(DLLPARAMETER)
  parameters = [DLLPARAMETER.from_address(info.ParametersInfo + offset*i) for i in range(info.NumParameters)]

  if bPrint:
    print ('\nInput Ports')
    print ('  Idx Name         Description                                                            Unit       Type Width')
    for i in range(info.NumInputPorts):
      print ('  {:3d} {:12s} {:70s} {:10s} {:4d} {:5d}'.format (i, 
                                                          inputs[i].Name.decode('utf-8'), 
                                                          inputs[i].Description.decode('utf-8'), 
                                                          inputs[i].Unit.decode('utf-8'),
                                                          inputs[i].DataType, 
                                                          inputs[i].Width))

    print ('\nOutput Ports')
    print ('  Idx Name         Description                                                            Unit       Type Width')
    for i in range(info.NumOutputPorts):
      print ('  {:3d} {:12s} {:70s} {:10s} {:4d} {:5d}'.format (i, 
                                                          outputs[i].Name.decode('utf-8'), 
                                                          outputs[i].Description.decode('utf-8'), 
                                                          outputs[i].Unit.decode('utf-8'),
                                                          outputs[i].DataType, 
                                                          outputs[i].Width))

    print ('\nParameters')
    print ('  Idx Name         Description                                                            Unit       Type Fix   Default       Min       Max')
    for i in range(info.NumParameters):
      print ('  {:3d} {:12s} {:70s} {:10s}   {:2d}  {:2d} {:9.3g} {:9.3g} {:9.3g}'.format (i, 
                                                          parameters[i].Name.decode('utf-8'), 
                                                          parameters[i].Description.decode('utf-8'), 
                                                          parameters[i].Unit.decode('utf-8'),
                                                          parameters[i].DataType, 
                                                          parameters[i].FixedValue,
                                                          parameters[i].DefaultValue.real64_T,
                                                          parameters[i].MinValue.real64_T,
                                                          parameters[i].MaxValue.real64_T))  #TODO: match union members to DataType

  # DLL dictionary for JSON serialization
  d = {'location': dll_name, 
       'DLLInterfaceVersion': [info.DLLInterfaceVersion[i] for i in range(4)],
       'ModelName': info.ModelName.decode('utf-8'), 
       'ModelVersion': info.ModelVersion.decode('utf-8'), 
       'ModelDescription': info.ModelDescription.decode('utf-8'), 
       'GeneralInformation': info.GeneralInformation.decode('utf-8'), 
       'ModelCreated': info.ModelCreated.decode('utf-8'), 
       'ModelCreator': info.ModelCreator.decode('utf-8'), 
       'ModelLastModifiedDate': info.ModelLastModifiedDate.decode('utf-8'), 
       'ModelLastModifiedBy': info.ModelLastModifiedBy.decode('utf-8'), 
       'ModelModifiedHistory': info.ModelModifiedHistory.decode('utf-8'), 
       'FixedStepBaseSampleTime': info.FixedStepBaseSampleTime,
       'EMT_RMS_Mode': info.EMT_RMS_Mode,
       'NumInputPorts': info.NumInputPorts,
       'NumOutputPorts': info.NumOutputPorts,
       'NumParameters': info.NumParameters,
       'NumIntStates': info.NumIntStates,
       'NumFloatStates': info.NumFloatStates,
       'NumDoubleStates': info.NumDoubleStates,
       'InputPortsInfo': [None] * info.NumInputPorts,
       'OutputPortsInfo': [None] * info.NumOutputPorts,
       'ParametersInfo': [None] * info.NumParameters}
  for i in range(info.NumInputPorts):
    row = {'Name': inputs[i].Name.decode('utf-8'),
           'Description': inputs[i].Description.decode('utf-8'),
           'Unit':  inputs[i].Unit.decode('utf-8'),
           'DataType': inputs[i].DataType,
           'Width': inputs[i].Width}
    d['InputPortsInfo'][i] = row

  for i in range(info.NumOutputPorts):
    row = {'Name': outputs[i].Name.decode('utf-8'),
           'Description': outputs[i].Description.decode('utf-8'),
           'Unit':  outputs[i].Unit.decode('utf-8'),
           'DataType': outputs[i].DataType,
           'Width': outputs[i].Width}
    d['OutputPortsInfo'][i] = row

  for i in range(info.NumParameters):
    row = {'Name': parameters[i].Name.decode('utf-8'),
           'Description': parameters[i].Description.decode('utf-8'),
           'Unit':  parameters[i].Unit.decode('utf-8'),
           'DataType': parameters[i].DataType,  # TODO: account for this in Default/Min/Max values
           'FixedValue': parameters[i].FixedValue,
           'DefaultValue': parameters[i].DefaultValue.real64_T,
           'MinValue': parameters[i].MinValue.real64_T,
           'MaxValue': parameters[i].MaxValue.real64_T}
    d['ParametersInfo'][i] = row

  return d

  # function handles
# print ('Model_GetInfo', dll.Model_GetInfo)
# print ('Model_PrintInfo', dll.Model_PrintInfo)
# print ('Model_Initialize', dll.Model_Initialize)
# print ('Model_CheckParameters', dll.Model_CheckParameters)
# print ('Model_Outputs', dll.Model_Outputs)
# print ('Model_Terminate', dll.Model_Terminate)
# print ('Model_FirstCall', dll.Model_FirstCall)
# print ('Model_Iterate', dll.Model_Iterate)

def write_atp_dll_interface (dll_fullname, atp_path, parm_vals):
  mod_name = 'DLL1' # ATP only allows one instance, and the DLL name must already be compiled and linked into the ATP solver

  d = get_dll_interface (dll_fullname, bPrint=False)
  dll_name = os.path.basename (dll_fullname)
  dll_path = os.path.dirname (dll_fullname)
  function_name, function_ext = os.path.splitext (dll_name)
  mod_fullname = os.path.join (atp_path, mod_name+'.mod')
  print (mod_fullname)

  fp = open(mod_fullname, 'wt')
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


