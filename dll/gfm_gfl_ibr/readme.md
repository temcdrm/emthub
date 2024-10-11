# GFM GFL IBR Example

This is an example DLL for the IEEE/Cigre specification, implementing grid-forming (GFL) 
and grid-following (GFL) behaviors for inverter-based resources (IBR). Developed by EPRI.

## Build Instructions - Windows

Install compiler and Cmake from: https://visualstudio.microsoft.com/downloads/
(find *Build Tools for Visual Studio 2022* under *Tools for Visual Studio 2022*)

Then follow these instructions:

1. Open the *x64 Native Tools Command Prompt for VS 2022* from Windows Start Menu
2. From the _GFM_GFL_IBR_ project directory:
    1. `md build`
    2. `cd build`
    3. `cmake ..`
    4. `cmake --build . --config Release`
    5. `cmake --build . --config Debug`
3. From the build/Release or build/Debug output directory, check the exported functions:
    1. `dumpbin /exports GFM_GFL_IBR.dll`
    2. `test`
