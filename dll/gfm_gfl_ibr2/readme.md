# GFM GFL IBR2 Example

This is an example DLL for the IEEE/Cigre specification, implementing grid-forming (GFL) 
and grid-following (GFL) behaviors for inverter-based resources (IBR). Developed by EPRI.
See https://www.epri.com/research/products/3002028322. 

## Build Instructions - Windows

Install compiler and Cmake from: https://visualstudio.microsoft.com/downloads/
(find *Build Tools for Visual Studio 2022* under *Tools for Visual Studio 2022*)

Then follow these instructions to make 64-bit and 32-bit versions of the DLL:

1. Open the *x64 Native Tools Command Prompt for VS 2022* from Windows Start Menu
2. From the _gfm_gfl_ibr2_ project directory (`rd /s build` and `rd /s build32` if they exist):
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
- _gfm_gfl_ibr2.c_ is the unmodified example file from Vishal Verma of EPRI, OCR-scanned from the report downloadable from https://www.epri.com/research/products/3002028322
- _test_ibr2.c_ is a test harness, mimicking the DLL import and calling functions of a simulation tool

## License

Copyright &copy; 2023 Electric Power Research Institute (EPRI), Inc.

Title: Code Based Generic Inverter Based Resource Model, see https://www.epri.com/research/products/3002028322

Author: Vishal Verma

Adapted under CC BY 4.0, https://creativecommons.org/licenses/by/4.0/

Modified 2025-2026 by Meltran, Inc, as follows:

- Remove currTime input, edit parameter descriptions, add Pout and Qout
- Add Vref input signal and more filter parameters
- Fixed choke units, Q control, AW clamps
- Pre-windup protection for Qcl, added Tv

This model now has:

- 15 inputs (input current time has been removed, Vref added) 
- 15 outputs (3 ouputs are essential, others can be used for debugging) 
- 58 parameters

See the git repository change log for full details.

Copyright &copy; 2024-26, Meltran, Inc
