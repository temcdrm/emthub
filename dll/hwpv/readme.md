# HWPV Example

This is an example DLL for the IEEE/Cigre specification, implementing generalized
block diagram models for solar photovoltaic inverters. See https://pecblocks.readthedocs.io/en/latest/ 
for more information.

## Build Instructions - Windows

Install compiler and Cmake from: https://visualstudio.microsoft.com/downloads/
(find *Build Tools for Visual Studio 2022* under *Tools for Visual Studio 2022*)

Then follow these instructions:

1. Open the *x64 Native Tools Command Prompt for VS 2022* from Windows Start Menu
2. From the _hwpv_ project directory:
    1. `md build`
    2. `cd build`
    3. `cmake ..`
    4. `cmake --build . --config Release` or `cmake --build . --config Debug`
    5. `cmake --install .`
3. From the _../bin_ directory, check the **DLL wrapper**:
    1. `test_hwpv` should produce an output _hwpv.csv_ file
    2. Verify with `python plotdlltest.py hwpv.csv`

## File Directory

- _CMakeLists.txt_ generates the detailed build instructions
- _hwpv.c_ implements forward evaluation of the trained generalized block diagram model
- _test_hwpv.c_ is a test harness, mimicking the DLL import and calling functions of a simulation tool

Copyright &copy; 2024, Meltran, Inc
