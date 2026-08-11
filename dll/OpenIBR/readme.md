# GFM GFL IBR2 Example

This example is based on HeronPower's OpenIBR library under an Apache 2.0 license.
The library is incorporated using `git submodule add  https://github.com/HeronPower/OpenIBR.git dll/ThirdParty/HeronPower/OpenIBR`.
Library documentation is in the `dll/ThirdParty/HeronPower/OpenIBR/documentation` subdirectory; just open the **md** files in your browser from GitHub.

The example connects a reference implementation of the WECC REGFM_C1
grid-forming hybrid control model, powered by a battery source, to
a SMIB. The supporting library comes with PV and data center examples,
and Simulink test cases. In this repository, we use the IEEE CIGRE DLL
interface to access the same functionality from a Python test harness.
By using the IEEE CIGRE DLL interface, this example may run in other EMT
simulators.

## Build Instructions - Windows

Install compiler and Cmake from: https://visualstudio.microsoft.com/downloads/
(find *Build Tools for Visual Studio 2022* under *Tools for Visual Studio 2022*)

Then follow these instructions to make 64-bit and 32-bit versions of the DLL:

1. Open the *x64 Native Tools Command Prompt for VS 2022* from Windows Start Menu
2. From the _OpenIBR_ project directory (`rd /s build` and `rd /s build32` if they exist):
    1. `md build`
    2. `md build32`
    3. `cmake -B build -A x64`
    4. `cmake -B build32 -A Win32`
    5. `cmake --build build --config Release` or `cmake --build build --config Debug`
    6. `cmake --install build`
    7. `cmake --build build32 --config Release` or `cmake --build build32 --config Debug`
    8. `cmake --install build32`
3. From the _../bin_ and _../bin32_ directories, check the **DLL wrapper**:
    1. `test_ibr2` should produce an output _ibr2.csv_ file
    2. Verify with `python plotdlltest.py ibr2.csv`

## File Directory

- _CMakeLists.txt_ generates the detailed build instructions
- _OpenIBR.c_ is the example file using HeronPower's OpenIBR library
- _test_OpenIBR.c_ is a test harness, mimicking the DLL import and calling functions of a simulation tool

Copyright &copy; 2024-26, Meltran, Inc
