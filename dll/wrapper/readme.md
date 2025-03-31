# DLL Wrapper

This is a static wrapper library for the IEEE/Cigre DLL specification. It helps manage
memory allocations, input, and output.

## Build Instructions - Windows

Install compiler and Cmake from: https://visualstudio.microsoft.com/downloads/
(find *Build Tools for Visual Studio 2022* under *Tools for Visual Studio 2022*)

Then follow these instructions to make 64-bit and 32-bit versions of the wrapper:

1. Open the *x64 Native Tools Command Prompt for VS 2022* from Windows Start Menu
2. From the _wrapper_ project directory (`rd /s build` and `rd /s build32` if they exist):
    1. `md build`
    2. `md build32`
    3. `cmake -B build -A x64`
    4. `cmake -B build32 -A Win32`
    5. `cmake --build build --config Release` or `cmake --build build --config Debug`
    6. `cmake --install build`
    7. `cmake --build build32 --config Release` or `cmake --build build32 --config Debug`
    8. `cmake --install build32`
3. Use _SCRX9_ project for testing the **DLL wrapper**:

## File Directory

- _CMakeLists.txt_ generates the detailed build instructions
- _IEEE_Cigre_DLLWrapper.c_ encapsulates the IEEE Cigre DLL interface for static linking

Copyright &copy; 2024-25, Meltran, Inc
