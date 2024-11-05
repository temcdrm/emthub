# DLL Wrapper

This is an example DLL for the IEEE/Cigre specification, a static exciter model
for synchronous machines. Developed by Electranix.

## Build Instructions - Windows

Install compiler and Cmake from: https://visualstudio.microsoft.com/downloads/
(find *Build Tools for Visual Studio 2022* under *Tools for Visual Studio 2022*)

Then follow these instructions:

1. Open the *x64 Native Tools Command Prompt for VS 2022* from Windows Start Menu
2. From the _wrapper_ project directory:
    1. `md build`
    2. `cd build`
    3. `cmake ..`
    4. `cmake --build . --config Release` or `cmake --build . --config Debug`
    5. `cmake --install .`
3. Use _SCRX9_ project for testing the **DLL wrapper**:

## File Directory

- _CMakeLists.txt_ generates the detailed build instructions
- _IEEE_Cigre_DLLWrapper.c_ encapsulates the IEEE Cigre DLL interface for static linking

Copyright &copy; 2024, Meltran, Inc
