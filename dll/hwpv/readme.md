# HWPV Example

This is an example DLL for the IEEE/Cigre specification, implementing generalized
block diagram models for solar photovoltaic inverters. See https://pecblocks.readthedocs.io/en/latest/ 
for more information.

## Build Instructions - Windows

Install compiler and Cmake from: https://visualstudio.microsoft.com/downloads/
(find *Build Tools for Visual Studio 2022* under *Tools for Visual Studio 2022*)

Then follow these instructions to make 64-bit and 32-bit versions of the DLL:

1. Open the *x64 Native Tools Command Prompt for VS 2022* from Windows Start Menu
2. Download and build the required JSON support library (https://jansson.readthedocs.io/en/latest/), into a sibling directory of _EMTHub_.
    1. From the parent directory of _EMTHub_, `git clone https://github.com/akheron/jansson.git`
    2. `cd jansson`
    3. `md build`
    4. `md build32`
    5. `cmake -B build -A x64`
    6. `cmake -B build32 -A Win32`
    7. `cmake --build build --config Release`
    8. `cmake --build build32 --config Release`
    9. `copy build\lib\release\jansson.lib ..\emthub\dll\lib`
    10. `copy build32\lib\release\jansson.lib ..\emthub\dll\lib32`
3. Clone the _pecblocks_ repository, into a sibling directory of _EMTHub_, for some example models:
    1. From the parent directory of _EMTHub_, `git clone https://github.com/pnnl/pecblocks.git`
    2. The generalized block diagram models are located in various _json_ files under the _examples_ directory. Some of these must be run at reduced power output, until new versions are trained with sensitivity optimization, as described at https://pecblocks.readthedocs.io/en/latest/
4. From this _hwpv_ project directory (`rd /s build` and `rd /s build32` if they exist):
    1. `md build`
    2. `md build32`
    3. `cmake -B build -A x64`
    4. `cmake -B build32 -A Win32`
    5. `cmake --build build --config Release` or `cmake --build build --config Debug`
    6. `cmake --install build`
    7. `cmake --build build32 --config Release` or `cmake --build build32 --config Debug`
    8. `cmake --install build32`
5. From the _../bin_ and _../bin32_ directories, check the **DLL wrapper**:
    1. `test_hwpv` should produce an output _hwpv.csv_ file
    2. Verify with `python plotdlltest.py hwpv.csv`

## File Directory

- _CMakeLists.txt_ generates the detailed build instructions
- _hwpv.c_ implements forward evaluation of the trained generalized block diagram model
- _test_hwpv.c_ is a test harness, mimicking the DLL import and calling functions of a simulation tool

Copyright &copy; 2024-25, Meltran, Inc
