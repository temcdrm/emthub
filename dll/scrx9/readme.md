# SCRX9 Example

This is an example DLL for the IEEE/Cigre specification, a static exciter model
for synchronous machines. Developed by Electranix.

## Build Instructions - Windows

Install compiler and Cmake from: https://visualstudio.microsoft.com/downloads/
(find *Build Tools for Visual Studio 2022* under *Tools for Visual Studio 2022*)

Then follow these instructions:

1. Open the *x64 Native Tools Command Prompt for VS 2022* from Windows Start Menu
2. From the _SCRX9_ project directory:
    1. `md build`
    2. `cd build`
    3. `cmake ..`
    4. `cmake --build . --config Release` or `cmake --build . --config Debug`
    5. `cmake --install .`
3. From the _SCRX9/build_ directory, check the exported functions with no wrapper:
    1. `dumpbin /exports release/SCRX9.dll` or `dumpbin /exports debug/SCRX9.dll`
    2. `release/test` generates an output CSV file in the _../../bin_ directory
    3. From the _../bin_ directory, relative to _SCRX9_, check outputs with `python plotdlltest.py`
4. From the _../bin_ directory, check the **DLL wrapper**:
    1. `test_scrx9` should give the same results as `release/test` above
    2. Verify with `python plotdlltest.py` from the _../bin_ directory relative to _SCRX9_

To build 32-bit DLLs, repeat the process using `cmake -A Win32 ..` in step 2.3.

## File Directory

- _CMakeLists.txt_ generates the detailed build instructions
- _SCRX9.c_ is the (nearly) unmodified example file from Garth Irwin of Electranix
- _test.c_ is a test harness, mimicking the DLL import and calling functions of a simulation tool
- _test_scrx9.c_ is a test harness, invoking the DLL through an EMTHub wrapper that supports all IEEE/Cigre DLLs

Copyright &copy; 2024-25, Meltran, Inc
