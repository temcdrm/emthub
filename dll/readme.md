# IEEE/Cigre DLL Examples

These projects build a supporting wrapper around the IEEE/Cigre specification
for dynamic link libraries (DLLs), and three examples. They should be built
in the following order.

1. First, install the compiler and Cmake from: https://visualstudio.microsoft.com/downloads/
(find *Build Tools for Visual Studio 2022* under *Tools for Visual Studio 2022*). Python is also used for plotting test results.
2. All DLL builds are performed in the *x64 Native Tools Command Prompt for VS 2022*, which is on the Windows Start Menu.
3. Build the _wrapper_ project, as the following three examples depend on it.
4. Build and test the _SCRX9_ example, which is a self-contained static exciter DLL from Electranix.
5. Build and test the _GFM_GFL_IBR_ example, which is a self-contained inverter-based resource (IBR) controller from EPRI.
6. Build and test the _HWPV_ example, which is a data-driven IBR model from PNNL and UCF. This example is not self-contained; you will have to download and build a JSON support library, and sample data-driven model files.

The build instructions will produce 64-bit and 32-bit versions of all example DLLs, test harnesses, and support libraries. A 32-bit simulator, such as ATP, will need the 32-bit DLLs.

Copyright &copy; 2025, Meltran, Inc
