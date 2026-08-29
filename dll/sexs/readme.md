# SEXS Example

This is an example DLL for the IEEE/Cigre specification. It is a legacy 
static excitation system model, prohibited by NERC for use in new 
interconnection studies, but still useful in demonstrations. 

## Build Instructions - Windows

Install compiler and Cmake from: https://visualstudio.microsoft.com/downloads/
(find *Build Tools for Visual Studio 2022* under *Tools for Visual Studio 2022*)

Then follow these instructions to make 64-bit and 32-bit versions of the DLL:

1. Open the *x64 Native Tools Command Prompt for VS 2022* from Windows Start Menu
2. From the _sexs_ project directory (`rd /s build` and `rd /s build32` if they exist):
    1. `md build`
    2. `md build32`
    3. `cmake -B build -A x64`
    4. `cmake -B build32 -A Win32`
    5. `cmake --build build --config Release` or `cmake --build build --config Debug`
    6. `cmake --install build`
    7. `cmake --build build32 --config Release` or `cmake --build build32 --config Debug`
    8. `cmake --install build32`
3. From the _sexs/build_ and _sexs/build32_ directories, check the exported functions:
    1. `dumpbin /exports release/SEXS.dll` or `dumpbin /exports debug/SEXS.dll`
4. From the _../bin_ and _../bin32_ directories, check the **DLL wrapper**:
    1. `TEST_SEXS` should produce `sexs.csv` otuput data.
    2. Verify results with `python plotdlltest.py sexs.csv`

## File Directory

- _CMakeLists.txt_ generates the detailed build instructions
- _sexs.c_ implements the static excitation system model
- _test_sexs.c_ is a test harness, invoking the DLL through an EMTHub wrapper that supports all IEEE/Cigre DLLs

Copyright &copy; 2024-26, Meltran, Inc
