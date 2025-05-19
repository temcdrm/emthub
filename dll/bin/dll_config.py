# Copyright (C) 2024-25 Meltran, Inc

import os
import sys
from ctypes import *

dll_name = 'c:/src/emthub/dll/bin/gfm_gfl_ibr2.dll'

class DLLINFO(Structure):
  _fields_ = [('DLLInterfaceVersion', c_ubyte),
              ('DLLInterfaceVersion2', c_ubyte),
              ('DLLInterfaceVersion3', c_ubyte),
              ('DLLInterfaceVersion4', c_ubyte),
              ('ModelName', c_char_p),
              ('ModelVersion', c_char_p),
              ('ModelDescription', c_char_p),
              ('GeneralInformation', c_char_p),
              ('ModelCreated', c_char_p),
              ('ModelCreator', c_char_p),
              ('ModelLastModifiedDate', c_int),
              ('ModelLastModifiedBy', c_char_p),
              ('ModelModifiedComment', c_char_p),
              ('ModelModifiedHistory', c_char_p),
              ('FixedStepBaseSampleTime', c_double),
              ('NumInputPorts', c_int),
              ('InputPortsInfo', c_int),
              ('NumOutputPorts', c_int),
              ('OutputPortsInfo', c_int),
              ('NumParameters', c_int),
              ('ParametersInfo', c_int),
              ('NumIntStates', c_int),
              ('NumFloatStates', c_int),
              ('NumDoubleStates', c_int)]

if __name__ == '__main__':
  if len(sys.argv) > 1:
    dll_name = sys.argv[1]
  dll = CDLL (dll_name)
  print (dll_name, dll)
  inf = dll.Model_GetInfo
  inf.restype = DLLINFO
  ret = inf()

  print ('Model_GetInfo call', inf())
  print ('DLLInterfaceVersion', ret.DLLInterfaceVersion)
  print ('DLLInterfaceVersion2', ret.DLLInterfaceVersion2)
  print ('DLLInterfaceVersion3', ret.DLLInterfaceVersion3)
  print ('DLLInterfaceVersion4', ret.DLLInterfaceVersion4)
  print ('ModelName', ret.ModelName)
  print ('ModelVersion', ret.ModelVersion)
  print ('ModelDescription', ret.ModelDescription)
  print ('GeneralInformation', ret.ModelGeneralInformation)
  print ('ModelCreated', ret.ModelCreated)
  print ('ModelCreator', ret.ModelCreator)
  print ('ModelLastModifiedDate', ret.ModelLastModifiedDate)
  print ('ModelLastModifiedBy', ret.ModelLastModifiedBy)
  print ('ModelModifiedComment', ret.ModelModifiedComment)
  print ('ModelModifiedHistory', ret.ModelModifiedHistory)
  print ('FixedStepBaseSampleTime', ret.FixedStepBaseSampleTime)
  print ('NumIntStates', ret.NumIntStates)
  print ('NumFloatStates', ret.NumFloatStates)
  print ('NumDoubleStates', ret.NumDoubleStates)
  quit()

  print ('Model_GetInfo', dll.Model_GetInfo)
  print ('Model_PrintInfo', dll.Model_PrintInfo)
  print ('Model_Initialize', dll.Model_Initialize)
  print ('Model_CheckParameters', dll.Model_CheckParameters)
  print ('Model_Outputs', dll.Model_Outputs)
  print ('Model_Terminate', dll.Model_Terminate)
  print ('Model_FirstCall', dll.Model_FirstCall)
  print ('Model_Iterate', dll.Model_Iterate)



