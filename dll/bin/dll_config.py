# Copyright (C) 2024-25 Meltran, Inc

import os
import sys
import json
from ctypes import *
from enum import IntEnum

dll_name = 'c:/src/emthub/dll/bin/gfm_gfl_ibr2.dll'
json_name = 'gfm_gfl_ibr2.json'

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

if __name__ == '__main__':
  if len(sys.argv) > 1:
    dll_name = sys.argv[1]
  dll = CDLL (dll_name)
  print (dll_name, dll)

  dll.Model_GetInfo.restype = c_void_p
  info = DLLINFO.from_address(dll.Model_GetInfo())
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
  print ('\nInput Ports')
  inputs = [DLLSIGNAL.from_address(info.InputPortsInfo + offset*i) for i in range(info.NumInputPorts)]
  print ('  Idx Name         Description                                                            Unit       Type Width')
  for i in range(info.NumInputPorts):
    print ('  {:3d} {:12s} {:70s} {:10s} {:4d} {:5d}'.format (i, 
                                                        inputs[i].Name.decode('utf-8'), 
                                                        inputs[i].Description.decode('utf-8'), 
                                                        inputs[i].Unit.decode('utf-8'),
                                                        inputs[i].DataType, 
                                                        inputs[i].Width))

  print ('\nOutput Ports')
  outputs = [DLLSIGNAL.from_address(info.OutputPortsInfo + offset*i) for i in range(info.NumOutputPorts)]
  print ('  Idx Name         Description                                                            Unit       Type Width')
  for i in range(info.NumOutputPorts):
    print ('  {:3d} {:12s} {:70s} {:10s} {:4d} {:5d}'.format (i, 
                                                        outputs[i].Name.decode('utf-8'), 
                                                        outputs[i].Description.decode('utf-8'), 
                                                        outputs[i].Unit.decode('utf-8'),
                                                        outputs[i].DataType, 
                                                        outputs[i].Width))

  offset = sizeof(DLLPARAMETER)
  print ('\nParameters')
  parameters = [DLLPARAMETER.from_address(info.ParametersInfo + offset*i) for i in range(info.NumParameters)]
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
       'ModelCreated': info.ModelCreator.decode('utf-8'), 
       'ModelCreator': info.ModelCreated.decode('utf-8'), 
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

  with open(json_name, 'w') as file:
    json.dump(d, file, indent=2)

  # function handles
# print ('Model_GetInfo', dll.Model_GetInfo)
# print ('Model_PrintInfo', dll.Model_PrintInfo)
# print ('Model_Initialize', dll.Model_Initialize)
# print ('Model_CheckParameters', dll.Model_CheckParameters)
# print ('Model_Outputs', dll.Model_Outputs)
# print ('Model_Terminate', dll.Model_Terminate)
# print ('Model_FirstCall', dll.Model_FirstCall)
# print ('Model_Iterate', dll.Model_Iterate)



