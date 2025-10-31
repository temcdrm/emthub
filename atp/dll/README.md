## IEEE/Cigre DLL Support for ATP

These code files and examples illustrate the IEEE/Cigre DLL Interface (Cigre TB 958,
_Guidelines for use of real-code in EMT models for HVDC, FACTs and inverter based generators in power systems analysis_,
February 2025) in the [Alternative Transients Program (ATP)](https://www.atp-emtp.org/).

The DLL interface is implemented as a "foreign model" in the ATP MODELS language feature. MODELS may
take about 5x longer execution times than the legacy Transient Analysis of Control Systems (TACS)
feature of ATP. In addition, MODELS instances may show unwanted interactions, i.e, "bugs", in some cases.
For these EMTHub&reg; examples, MODELS is used only to "wrap" a call to the IEEE/Cigre DLL. All other controls and
signal sources are implemented in TACS.

### Users with an ATP License

Steps for preparation:

- Verify or obtain ATP license, then download ATPDraw (version 7.5 tested) and the Japanese ATP User Group (JAUG) distribution. The JAUG distribution comes with MinGW compiler, linker, and object files needed to customize ATP. The European EMTP User Group (EEUG) distribution is available with object files, too, but only for those who join EEUG and pay dues.
- Add `c:\atp\atpmingw` to the Windows PATH variable. This enables command-line execution of ATP.
- Add `C:\ATP\atpmingw\make\MinGW\bin` to the Windows PATH variable. This enables command-line compilation of ATP with DLL interface.
- Add `c:\atp\gtppl32` to the Windows PATH variable. This enables command-line plotting of ATP simulation results.
- Set the environment variable `GNUDIR=c:\atp\atpmingw\`, which is required by ATP, and please note the trailing `\` is required.
- Setup the ATP solver in ATPDraw to be `c:\atp\atpmingw\mytpbig.exe`, which will work after you build `mytpbig.exe` in the following steps. Save this configuration.
- Assuming you cloned this repository into `c:\src\emthub`, clone the following from a command prompt in `c:\src`:
    - `git clone https://github.com/pnnl/pecblocks`, which is required for the _hwpv_ example.
    - `git clone https://github.com/temcdrm/emthubsupport.git`, which contains "ATP materials" that require an ATP license for access. However, _emthubsupport_ is a private repository. You will need a GitHub id and self-certify as an ATP licensee to gain access to this private repository. Please message the site maintainer on GitHub if interested. There is an alternative to the private repository described later.
- Build and test four 32-bit example DLLs into `c:\src\emthub\dll\bin32`, following the [directions](../../dll/readme.md). The ATP Makefile relies on these DLLs.
- Copy some necessary files used in rebuilding the ATP solver to call the DLL models:
    - Switch to a command prompt in `c:\src\emthub\atp\dll`
    - If you cloned _emthubspport_, issue the command `prep_build.bat` to copy the files.
    - Otherwise:
         - Manually copy the files listed in _prep_build.bat_. They are typically found in _c:\atp\atpmingw\make_ and _c:\atp\atpmingw\make\sample_ from the JAUG installation.
         - Manually edit the JAUG's _fgnmod.f_ in two locations:
             - Around line 20, you should add 4 lines like this, `DATA refnam(3) / 'SCRX9' /`, one for each DLL model.
             - Around line 70, you should modify the logic with `CALL dll_scrx9_i(xdata, xin, xout, xvar)` and `CALL dll_scrx9_m(xdata, xin, xout, xvar)` under the appropriate conditions. Do likewise for the _dll_hwpv_i_, _dll_hwpv_m_, _dll_gfm_gfl_ibr_i_, _dll_gfm_gfl_ibr_m_, _dll_gfm_gfl_ibr2_i_ and _dll_gfm_gfl_ibr2_m_ function calls.
- From a command prompt in `c:\src\emthub\atp\dll`, issue the command `make`. It should call the MinGW tools as supplied by JAUG, compile some custom source files, link `c:\atp\atpmingw\mytpbig.exe`, and copy four example DLLs into `c:\atp\atpmingw`.
- From the command prompt, invoke `mytpbig tacs_models.atp` to test the functionality of MODELS with TACS, and `mytpbig ex_dll.atp` to test a simple external C function that was linked into `mytpbig.exe`

When these steps are complete, you are ready to run four examples in the following directories:

- _gfm_gfl_ibr_: An average grid-forming (GFM) and grid-following (GFL) inverter-based resource (IBR) model developed by the Electric Power Research Institute (EPRI), developmental version used by the Cigre/IEEE DLL Task Force.
- _gfm_gfl_ibr2_: A newer average grid-forming (GFM) and grid-following (GFL) inverter-based resource (IBR) model developed by the Electric Power Research Institute (EPRI), see [report](https://www.epri.com/research/products/3002028322).
- _hwpv_: A data-driven Hammerstein-Wiener Photovoltaic (HWPV) model as described in [paper](https://ieeexplore.ieee.org/document/10842890), [report](https://www.osti.gov/servlets/purl/2481660/), and [pecblocks repository](https://pecblocks.readthedocs.io/en/latest/).
- _scrx9_: A synchronous machine exciter example as presented in Cigre TB 958 and [Modelica paper](https://ecp.ep.liu.se/index.php/modelica/article/view/1132) with [repository](https://github.com/embeddedhao/OpenIPSL/tree/cigre_dll_pr).

Local files that you may need to edit:

- _Makefile_: for MinGW compiler and linker, modified from the JAUG example. If you installed files into locations other than assumed above, you may need to edit this file. Please consult on-line documentation of GNU Makefiles for guidance.
- _tacs_models.atp_: a modified version of an example from the ATP MODELS Primer, modified to use TACS instead of MODELS for the trig function calls.
- _usedll.c_: defines a simple foreign function to test the custom build, and four IEEE/Cigre DLL interfaces. To add more DLL interfaces, you would add two functions here. One function, with suffix `_i`, is called to initialize the DLL model. The other function, with suffix `_m`, is called to run the DLL model at each ATP time step.
- _fgnmod.f_ (after copied from _emthubsupport_): based on the DLL name from MODELS, this code should call the correct functions in _usedll.c_. To add more DLL interfaces, you would add the name lookup at line 23, and two function calls after line 90.
- _Ex_DLL.atp_: a simple ATP netlist that calls a simple C function defined in _usedll.c_.
- _clean.bat_: may be used in this directory, or the example subdirectories, to remove output files and temporary files after ATP execution or building `mytpbig.exe`
- _prep_build.bat_: may be altered to obtain the JAUG build files from another location than a cloned _emthubsupport_ repository.

Some issues are still under investigation:

- Only floating-point parameters can be passed to a foreign models function. For the _scrx9_ example, one DLL input parameter is an integer. The ATP interface casts that parameter from _double_ to _int_.
- The _hwpv_ DLL takes one parameter, a string file name where the HWPV data is stored in JSON format. For now, this parameter is hard-coded in the ATP interface. At some future time, an integer index could be passed for use with a hard-coded configuration file name. The configuration file would be named _hwpv_models.txt_, to be collocated with _hwpv.dll_, storing one JSON file name per line. The integer parameter in the ATP interface could index the file name to be used from _hwpv_models.txt_. Unfortunately, the JAUG distribution did not include the header file, _stdio.h_, for the ATP interface to use file operations from C code. So, implementation of this more flexible interface would require a full installation of the MinGW C compiler.
- The _gfm_gfl_ibr_ example shows some instability in steady-state output. One possibility is that the default DLL parameters need tuning. Another possibility is that the IBR filter circuit uses a topology different than what has been assumed here.
- In ATPDraw, the "default" parameter values provided in the MODEL definition don't propagate upward to the user interface dialog. Parameters have to be entered manually in the dialog, even if they are the same as default values.
- When calling the initialization function, MODELS does not seem to pass in the user-initialized output variables. The HWPV case is not affected because it starts from rest. However, effects were seen in the startup of _scrx9_, mitigated by inserting 1-pu initialization in the time-step function, _dll_scrx9_m_. This workaround would be more complicated in the _gfm_gfl_ibr_m_ time-step function because of the need to initialize the instantaneous voltage and currents for non-zero power flow. For that case, a better solution might be to ramp from zero initial conditions. However, possible errors in the output filtering should be addressed first. 

### Users without an ATP License

You will not be able to build or run these examples. There may be some value in reviewing the following files as examples:

- _usedll.c_: illustrates four IEEE/Cigre DLL interfaces. Each ATP DLL interface has two functions. One function, with suffix `_i`, is called to initialize the DLL model. The other function, with suffix `_m`, is called to run the DLL model at each ATP time step.
- _gfm_gfl_ibr/\*.mod_ and _\*.atp_: test circuit inputs for an average grid-forming (GFM) and grid-following (GFL) inverter-based resource (IBR) model developed by the Electric Power Research Institute (EPRI), developmental version used by the Cigre/IEEE DLL Task Force.
- _gfm_gfl_ibr2/\*.mod_ and _\*.atp_: test circuit inputs for a newer average grid-forming (GFM) and grid-following (GFL) inverter-based resource (IBR) model developed by the Electric Power Research Institute (EPRI), see [report](https://www.epri.com/research/products/3002028322).
- _hwpv/\*.mod_ and _\*.atp_: test circuit inputs for a data-driven Hammerstein-Wiener Photovoltaic (HWPV) model as described in [paper](https://ieeexplore.ieee.org/document/10842890), [report](https://www.osti.gov/servlets/purl/2481660/), and [pecblocks repository](https://pecblocks.readthedocs.io/en/latest/).
- _scrx9/\*.mod_ and _\*.atp_: test circuit inputs for a synchronous machine exciter example as presented in Cigre TB 958 and [Modelica paper](https://ecp.ep.liu.se/index.php/modelica/article/view/1132) with [repository](https://github.com/embeddedhao/OpenIPSL/tree/cigre_dll_pr).

Copyright &copy; 2024-25, Meltran, Inc

