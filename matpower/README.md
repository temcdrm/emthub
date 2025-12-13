# MATPOWER System Examples

These examples calculate initial conditions for EMT simulations in ATP, for three network examples, i.e.,
IEEE 39-bus, IEEE 118-bus, and WECC 240-bus with IBR. A [MATPOWER](https://matpower.org/) installation is required. The Python
scripts are written to work with [Octave](https://octave.org/), but the files may also be run manually in MATLAB.

These examples are necessary to run EMT simulations in ATP. They also demonstrate use of CIM
extensions to produce network models for another power flow tool.

Files of interest include:

- _\[IEEE39|IEEE118|WECC240].m_: Three specific MATPOWER example files, created from scripts and rawfiles in the sibling _../cim_ directory.
- _mpow.py_: Python script that runs MATPOWER; use a command-line argument of 0, 1, or 2 to select which case to run.
- _\*summary.txt_: Summary power flow output for the three examples.
- _\*mg.txt_: Generator injections for the three examples; used for ATP initial conditions.
- _\*mb.txt_: Bus voltage magnitudes and angles for the three examples; used for ATP initial conditions.
- _clean.bat_: Deletes MATPOWER temporary files.
- _matpower_gen_type.m_: Support function that will move to the _emthub_ Python package.

Copyright &copy; 2024-25, Meltran, Inc
