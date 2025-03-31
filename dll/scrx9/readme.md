# SCRX9 Example

This is an example DLL for the IEEE/Cigre specification, a static exciter model
for synchronous machines. Developed by Electranix.

## Build Instructions - Windows

Install compiler and Cmake from: https://visualstudio.microsoft.com/downloads/
(find *Build Tools for Visual Studio 2022* under *Tools for Visual Studio 2022*)

Then follow these instructions to make 64-bit and 32-bit versions of the DLL:

1. Open the *x64 Native Tools Command Prompt for VS 2022* from Windows Start Menu
2. From the _SCRX9_ project directory (`rd /s build` and `rd /s build32` if they exist):
    1. `md build`
    2. `md build32`
    3. `cmake -B build -A x64`
    4. `cmake -B build32 -A Win32`
    5. `cmake --build build --config Release` or `cmake --build build --config Debug`
    6. `cmake --install build`
    7. `cmake --build build32 --config Release` or `cmake --build build32 --config Debug`
    8. `cmake --install build32`
3. From the _SCRX9/build_ and _SCRX9/build32_ directories, check the exported functions with no wrapper:
    1. `dumpbin /exports release/SCRX9.dll` or `dumpbin /exports debug/SCRX9.dll`
    2. `release/test` generates an output CSV file in the _../../bin_ directory
    3. From the _../bin_ directory, relative to _SCRX9_, check outputs with `python plotdlltest.py`
4. From the _../bin_ and _../bin32_ directories, check the **DLL wrapper**:
    1. `test_scrx9` should give the same results as `release/test` above
    2. Verify with `python plotdlltest.py` from the _../bin_ and _../bin32_ directories relative to _SCRX9_

## File Directory

- _CMakeLists.txt_ generates the detailed build instructions
- _SCRX9.c_ is the (nearly) unmodified example file from Garth Irwin of Electranix
- _test.c_ is a test harness, mimicking the DLL import and calling functions of a simulation tool
- _test_scrx9.c_ is a test harness, invoking the DLL through an EMTHub wrapper that supports all IEEE/Cigre DLLs

Copyright &copy; 2024-25, Meltran, Inc
