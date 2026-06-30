# Grid Test Harness

This tests a single-machine, infinite-bus (SMIB) grid that an inverter model may be connected to.
The grid consists of a three-phase voltage source with three-phase source impedance.
Trapezoidal integration is used to solve for currents in the source impedance, given 
the voltages on each terminal of the impedance. One terminal voltage is defined by the
SMIB voltage source. The other terminal voltage is defined by the connected DLL's output.

In this example, the DLL's output voltage is mimiced in code. The purpose of this test
is to verify proper execution of the trapezoidal integration at each time step. The output should
show inductive currents all beginning at zero, then gradually assume the expected
sinusoidal shapes, 120 degrees apart, with no DC offset in the current. The DLL
controller action is not included. To do that, code from this example is incorporated into 
the _../gfm_gfl_ibr/test_ibr.c_ and _../gfm_gfl_ibr2/test_ibr2.c_ source files.

## Build Instructions - Windows

Install compiler and Cmake from: https://visualstudio.microsoft.com/downloads/
(find *Build Tools for Visual Studio 2022* under *Tools for Visual Studio 2022*)

Then follow these instructions to make a 64-bit version of the test harness:

1. Open the *x64 Native Tools Command Prompt for VS 2022* from Windows Start Menu
2. From the _grid_ project directory (`rd /s build` if it exists):
    1. `md build`
    2. `cmake -B build -A x64`
    3. `cmake --build build --config Release` or `cmake --build build --config Debug`
    4. `cmake --install build`
3. From the _../bin_ directory, check the trapezoidal integration output:
    1. `test_grid` should produce an output _grid.csv_ file
    2. Verify with `python plotdlltest.py grid.csv`

## File Directory

- _CMakeLists.txt_ generates the detailed build instructions
- _test_grid.c_ implements trapezoidal integration for current in a three-phase source impedance

Copyright &copy; 2024-26, Meltran, Inc
