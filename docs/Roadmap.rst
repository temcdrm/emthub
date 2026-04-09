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

#. :ref:`target-installation` of the Python code and cloning examples from the :ref:`target-repository` are prerequisites.
#. Consider whether to download `MATPOWER <https://matpower.org/>`_ for the power flow examples. This is open-source software that runs in open-source `Octave <https://octave.org/>`_, or in MATLAB.
#. Consider whether to download `ATP <https://www.atp-emtp.org/>`_ for the EMT examples. This is free-to-use, but has restrictive license terms. Utilities, researchers, and some consultants are generally able to license ATP, but generally not EMT tool developers.

   a. Contributors are invited to provide examples that run in other EMT simulators.

#. Run all five :ref:`target-examples-network`.

.. _target-roadmap-profile:

Profile Maintainers
-------------------

This roadmap applies to stakeholders that primarily manage CIM UML and profiles. They do not necessarily run EMT simulations.

#. :ref:`target-roadmap-users` Roadmap is a pre-requisite.
#. **Talk about obtaining CIM UML, a UML editor, and CIMTool.**

.. _target-roadmap-network:

Network Model Developers
------------------------

This roadmap applies to stakeholders that primarily import CIM network models to an EMT simulator's native format, i.e., EMT software developers.

#. :ref:`target-roadmap-users` Roadmap is a pre-requisite.
#. Run all five :ref:`target-examples-dll`.
#. **Suggest specific Python files that create ATP netlists. This can be a starting point for implementing other CIM importers for EMT.**

.. _target-roadmap-dll:

DLL Developers
--------------

This roadmap applies to stakeholders that primarily build DLL models of IBR and other controllers. This includes IBR hardware vendors, their consultants,
researchers, and EMT software developers who are building test cases.

#. :ref:`target-roadmap-users` Roadmap is a pre-requisite.
#. Run all five :ref:`target-examples-dll`.
#. **Talk about build tools (already addressed in examples), P3597 involvement, and testing in a SMIB with an EMT simulator.**
