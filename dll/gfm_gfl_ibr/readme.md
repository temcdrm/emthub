# GFM GFL IBR Example

This is an example DLL for the IEEE/Cigre specification, implementing grid-forming (GFL) 
and grid-following (GFL) behaviors for inverter-based resources (IBR). Developed by EPRI.

## Build Instructions - Windows

Install compiler and Cmake from: https://visualstudio.microsoft.com/downloads/
(find *Build Tools for Visual Studio 2022* under *Tools for Visual Studio 2022*)

Then follow these instructions to make 64-bit and 32-bit versions of the DLL:

1. Open the *x64 Native Tools Command Prompt for VS 2022* from Windows Start Menu
2. From the _GFM_GFL_IBR_ project directory (`rd /s build` and `rd /s build32` if they exist):
    1. `md build`
    2. `md build32`
    3. `cmake -B build -A x64`
    4. `cmake -B build32 -A Win32`
    5. `cmake --build build --config Release` or `cmake --build build --config Debug`
    6. `cmake --install build`
    7. `cmake --build build32 --config Release` or `cmake --build build32 --config Debug`
    8. `cmake --install build32`
3. From the _../bin_ and _../bin32_ directories, check the **DLL wrapper**:
    1. `test_ibr` should produce an output _ibr.csv_ file
    2. Verify with `python plotdlltest.py ibr.csv`

## File Directory

- _CMakeLists.txt_ generates the detailed build instructions
- _GFM_GFL_IBR.c_ is the unmodified example file from Deepak Ramasubramanian of EPRI
- _test_ibr.c_ is a test harness, mimicking the DLL import and calling functions of a simulation tool

Copyright &copy; 2024-25, Meltran, Inc
