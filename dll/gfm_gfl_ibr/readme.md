# GFM GFL IBR Example

This is an example DLL for the IEEE/Cigre specification, implementing grid-forming (GFL) 
and grid-following (GFL) behaviors for inverter-based resources (IBR). Developed by EPRI.

## Build Instructions - Windows

Install compiler and Cmake from: https://visualstudio.microsoft.com/downloads/
(find *Build Tools for Visual Studio 2022* under *Tools for Visual Studio 2022*)

Then follow these instructions:

1. Open the *x64 Native Tools Command Prompt for VS 2022* from Windows Start Menu
2. From the _GFM_GFL_IBR_ project directory:
    a. `md build`
    b. `cd build`
    c. `cmake ..`
    d. `cmake --build . --config Release`
    e. `cmake --build . --config Debug`
3. From the build/Release or build/Debug output directory, check the exported functions:
    a. `dumpbin /exports GFM_GFL_IBR.dll`
    b. `test`
