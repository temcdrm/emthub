.. role:: math(raw)
   :format: html latex
..

Roadmap
=======

These subsections provide a suggested order of activities for different
kinds of stakeholders approaching EMT model interoperability.

.. _target-roadmap-users:

Users
-----

This roadmap applies to stakeholders that primarily run EMT simulations. It's also a good starting point for developers to become familiar
with content of the open-source software.

#. :ref:`target-installation` of the Python code and testing from the :ref:`target-quick-start` are prerequisites.
#. Consider whether to download `MATPOWER <https://matpower.org/>`_ for the power flow examples. This is open-source software that runs in open-source `Octave <https://octave.org/>`_, or in MATLAB.
#. Consider whether to download `ATP <https://www.atp-emtp.org/>`_ for the EMT examples. This is free-to-use, but has restrictive license terms. Utilities, researchers, and some consultants are generally able to license ATP, but generally not EMT tool developers.

   a. Contributors are invited to provide examples that run in other EMT simulators.

#. Run the five cases in :ref:`target-examples-network` using the following scripts.

This batch file extracts all five examples to CIM RDF, with ATP and MATPOWER netlisting. It also solves four examples in MATPOWER::

    @echo off
    for /L %%i in (0,1,3) do (
        emthub-extract-case %%i
        python raw_to_rdf.py %%i
        python bps_make_mpow.py %%i
        python mpow.py %%i
        python ic_to_rdf.py %%i
        python cim_to_atp.py %%i
        )
    emthub-extract-case 4
    python create_smib_dll.py 4
    python cim_to_atp.py 4
    python cim_summary.py

The last command summarizes CIM class counts in each example.

This batch file runs all five examples in ATP. In this version, plots are saved in `png` format so the batch file continues uninterrupted::

    @echo off
    for /L %%i in (0,1,4) do (
        python atp.py %%i "run"
        python atp.py %%i "convert"
        python atp.py %%i "png"
        )

With a MATPOWER installation, you should obtain summary power flow output with bus voltages usually in the range 0.95 to 1.05 per-unit.
However, the *XfmrSat* example has low initial voltage at the load end of the line. The *WECC240* case has a few dozen overloaded branches.
The *SMIBDLL* example initializes from zero, so MATPOWER is not used with it.

With an ATP installation, you should be able to match the outputs in :ref:`target-examples-network`.

.. _target-roadmap-profile:

Profile Maintainers
-------------------

.. note::
    To be completed.

This roadmap applies to stakeholders that primarily manage CIM UML and profiles. They do not necessarily run EMT simulations.

#. :ref:`target-roadmap-users` Roadmap is a pre-requisite.
#. **Talk about obtaining CIM UML, a UML editor, and CIMTool.**

.. image:: ../ProfileFlow.png

.. _target-roadmap-network:

Network Model Developers
------------------------

This roadmap applies to stakeholders that primarily import CIM network models to an EMT simulator's native format, i.e., EMT software developers.

#. :ref:`target-roadmap-users` Roadmap is a pre-requisite.
#. Examine the *create_atp.py* file that creates ATP netlists. This can be a starting point for implementing other CIM importers for EMT, even without having an ATP license.

   a. This script creates a file ending in *_net.atp*. That file syntax should be readable to developers familiar with EMT, even without ATP documentation. For more help, try this `book <https://doi.org/10.1002/9781119480549>`_. It has examples with segments of ATP input text.
   b. The script may be found in the GitHub repository: `create_atp.py <https://github.com/temcdrm/emthub/blob/main/src/emthub/create_atp.py>`_.
   c. The script may also be found in your local *emthub* package installation. From a Windows Command Prompt, type ``pip show emthub``. That will return a **Location** of your local *emthub* installation. Then you may find the ATP netlisting script at *Location\\emthub\\create_atp.py*. Using this method, you can examine other script and data files from your local *emthub* installation.

#. Become generally familiar with the :ref:`target-cim-profile`. This is a reference, not meant to read from beginning to end.
#. Become generally familiar with the :ref:`target-queries`. This is also a reference, not meant to read from beginning to end.
#. Develop and test the CIM-to-EMT conversion script for your own EMT simulator.

   a. Try testing the *XfmrSat* example first. It is the smallest example and has no generator dynamics.
   b. Try testing the *IEEE39* example next. It includes one IBR plant and some other machine dynamics..
   c. Try testing the *SMIBDLL* example next.  This adds the essential DLL interface to the baseline features already tested.
   d. Try testing *IEEE118* and then *WECC240*. These are similar to but larger than *IEEE39* and they add a few more types of network model components.

.. image:: ../FileFlow.png

.. _target-roadmap-dll:

DLL Developers
--------------

.. note::
    To be completed.

This roadmap applies to stakeholders that primarily build DLL models of IBR and other controllers. This includes IBR hardware vendors, their consultants,
researchers, and EMT software developers who are building test cases.

#. :ref:`target-roadmap-users` Roadmap is a pre-requisite.
#. Run all five :ref:`target-examples-dll`.
#. **Talk about build tools (already addressed in the DLL examples), P3597 involvement, and testing in a SMIB with an EMT simulator.**
