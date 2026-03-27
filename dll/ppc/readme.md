# REPCA1 PPC

This directory contains an IEEE/CIGRE DLL wrapper around an FMU exported from OpenIPSL[1]'s `REPCA1` plant controller implementation.

[1] M. De Castro et al., “Version [OpenIPSL 2.0.0] - [iTesla Power Systems Library (iPSL): A Modelica library for phasor time-domain simulations],” SoftwareX, vol. 21, p. 101277, Feb. 2023, doi: 10.1016/j.softx.2022.101277.

Other Resources:

[2] “Inverter-Based Resources Power Plant  Modeling and Validation Guideline.” WECC. [Online]. Available: https://www.wecc.org/sites/default/files/documents/meeting/2026/IBR%20Power%20Plant%20Modeling%20and%20Validation%20Guideline.pdf
[3] “Model User Guide for Generic Renewable Energy Systems.” [Online]. Available: https://www.epri.com/research/products/000000003002027129


## File description

- `fmu/PPC.mo`: wrapper model around `OpenIPSL.Electrical.Renewables.PSSE.PlantController.REPCA1`
- `fmu/export_fmu.mos`: OpenModelica FMU export script
- `fmu/generate_fmu_build.py`: regenerates `dll/ppc/CMakeLists.txt` after FMU export
- `PPC.c`: IEEE/CIGRE DLL wrapper around the exported FMU
- `test_ppc.c`: test harness using `DLLWrapper`

## Limitations
- Parameters are fixed at initialization
- Snapshots and states are unsupported

## Build Instructions - Windows

Install compiler and CMake from: https://visualstudio.microsoft.com/downloads/
(find *Build Tools for Visual Studio 2022* under *Tools for Visual Studio 2022*)

Prerequisites:

- OpenModelica (Tested with version 1.26.3)
- Python 3 (Tested with version 3.14.3)

Then follow these instructions to make 64-bit and 32-bit versions of the DLL:

1. Open the *x64 Native Tools Command Prompt for VS 2022* from Windows Start Menu.
2. From the repository root:
    1. Checkout git submodule "OpenIPSL" from its git repository:
       `git submodule update --init --recursive`
    2. Regenerate the FMU build files (default as-tested path to omc.exe is shown):
       `python dll\ppc\fmu\generate_fmu_build.py --omc-cmd "c:\program files\openmodelica1.26.3-64bit\bin\omc.exe"`
    3. Remove `build` and `build32` if they already exist.
    4. `md build`
    5. `md build32`
    6. `cmake -S dll\ppc -B build -A x64`
    7. `cmake -S dll\ppc -B build32 -A Win32`
    8. `cmake --build build --config Release` or `cmake --build build --config Debug`
    9. `cmake --install build`
    10. `cmake --build build32 --config Release` or `cmake --build build32 --config Debug`
    11. `cmake --install build32`
3. From the `build` and `build32` directories, check the exported functions:
    1. `dumpbin /exports Release\PPC.dll` or `dumpbin /exports Debug\PPC.dll`
    2. `Release\TEST_PPC.exe` generates CSV output for the wrapper-based harness
    3. `python ..\dll\bin\plotdlltest.py ppc_voltage_step.csv` plots one of the CSV output files
4. From the installed output directories:
    1. x64 installs to `dll\bin`
    2. Win32 installs to `dll\bin32`
    3. `TEST_PPC.exe` can also be run from those installed directories

The tests write CSV outputs for the configured scenarios.

## Changelog
- Prabhpreet Dua:  IEEE/CIGRE DLL PPC based on OpenIPSL REPCA1 FMU exported 

## License
Contributions as per IEEE Open Source Apache 2.0 CLA for P3743 WG EMTIOP

### OpenIPSL
OpenIPSL license as per open-source license in repository source (https://github.com/OpenIPSL/OpenIPSL.git):

```
BSD 3-Clause License

Copyright (c) 2016-2026 Luigi Vanfretti, ALSETLab (formerly SmarTS Lab) and contributors.
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.

* Neither the name of the copyright holder nor the names of its
  contributors may be used to endorse or promote products derived from
  this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
```
