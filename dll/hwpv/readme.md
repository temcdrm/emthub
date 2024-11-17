# HWPV Example

This is an example DLL for the IEEE/Cigre specification, implementing generalized
block diagram models for solar photovoltaic inverters. See https://pecblocks.readthedocs.io/en/latest/ 
for more information.

## Build Instructions - Windows

Install compiler and Cmake from: https://visualstudio.microsoft.com/downloads/
(find *Build Tools for Visual Studio 2022* under *Tools for Visual Studio 2022*)

Download and build the required JSON support library, from a sibling directory
to the

Then follow these instructions:

1. Open the *x64 Native Tools Command Prompt for VS 2022* from Windows Start Menu
2. Download and build the required JSON support library (https://jansson.readthedocs.io/en/latest/), into a sibling directory of _EMTHub_.
    1. From the parent directory of _EMTHub_, `git clone https://github.com/akheron/jansson.git`
    2. `md build`
    3. `cd build`
    4. `cmake -DCMAKE_INSTALL_PREFIX=/src/emthub/dll ..` (edit the -D directory to match your local directory structure)
    5. `cmake --build . --config Release`
    6. `cmake --install .`
3. Clone the _pecblocks_ repository, into a sibling directory of _EMTHub_, for some example models:
    1. From the parent directory of _EMTHub_, `git clone https://github.com/pnnl/pecblocks.git`
    2. The generalized block diagram models are located in various _json_ files under the _examples_ directory. Some of these must be run at reduced power output, until new versions are trained with sensitivity optimization, as described at https://pecblocks.readthedocs.io/en/latest/
4. From this _hwpv_ project directory:
    1. `md build`
    2. `cd build`
    3. `cmake ..`
    4. `cmake --build . --config Release` or `cmake --build . --config Debug`
    5. `cmake --install .`
5. From the _../bin_ directory, check the **DLL wrapper**:
    1. `test_hwpv` should produce an output _hwpv.csv_ file
    2. Verify with `python plotdlltest.py hwpv.csv`

## File Directory

- _CMakeLists.txt_ generates the detailed build instructions
- _hwpv.c_ implements forward evaluation of the trained generalized block diagram model
- _test_hwpv.c_ is a test harness, mimicking the DLL import and calling functions of a simulation tool

Copyright &copy; 2024, Meltran, Inc
