.. role:: math(raw)
   :format: html latex
..

Overview
========

EMTHub\ |reg| provides software and data schemas for standards-based model building and validation to perform electromagnetic transient (EMT) 
studies of electric utility power systems. The focus is on inverter-based resources (IBR), e.g., wind, solar, and storage, 
in electric utility systems. Network EMT models are based on an extension and profile of the Common Information Model (CIM), available
under the Apache 2.0 :ref:`target-license`. Unit and plant IBR models interface to a Cigre/IEEE specification on real-code modeling through dynamics link 
library (DLL) interfaces.

As part of IEEE P3743, Recommended Practice for Electromagnetic Transient Model Interoperability for Electric Power Transmission Systems, this
content will shortly move to an IEEE open-source project called `EMTIOP <https://opensource.ieee.org/emtiop>`_. The document under development by the P3743
Working Group is considered normative for the open-source software, and vice versa. For now, only members of the P3743 Working Group can access
draft versions of the document at `iMeet <https://ieee-sa.imeetcentral.com/p3743/>`_. Others may view the scope and purpose of P3743, and express
interest in joining its Working Group, at the `P3743 PAR Site <https://standards.ieee.org/ieee/3743/12233/>`_. In the meantime, until P3743 is
published, scripts and examples will run as documented here.

This content may also depend on `IEEE P3597 <https://standards.ieee.org/ieee/3597/12053/>`_, which aims to standardize the DLL interface. 
P3597 begins meeting in July 2026 at the IEEE PES General Meeting in Montreal.

The IEC CIM standards are not normative for P3743. The open-source software is based on the `CIM UML <https://cimug.org/cimdocs/standards-artifacts/>`_,
under an Apache 2.0 license.

.. _target-installation:

Installation
------------

Python 3.11.4 or greater is required. If necessary, install or update `Python <https://www.python.org/downloads/>`_. 
Then install the Python package::

    pip install emthub

For now, the GitHub :ref:`target-repository` should also be cloned to obtain the examples.

Quick Start
-----------

Choose one of the roadmaps to follow:

- :ref:`target-roadmap-users` to just run examples.
- :ref:`target-roadmap-profile` for maintaining the CIM extensions and profile.
- :ref:`target-roadmap-network` for developing and testing CIM data import to EMT tools.
- :ref:`target-roadmap-dll` for developing and testing DLL models.

Consult the :ref:`target-bibliography` as needed for background information. 

.. _target-repository:

Repository
----------

See `EMTHub directory <https://github.com/temcdrm/emthub>`_

To make a local copy, first `Install Git <https://github.com/git-guides/install-git>`_. Then 
invoke this command from a directory where source code will be kept, such as `c:\src`::

    git clone https://github.com/temcdrm/emthub.git

.. |reg|    unicode:: U+000AE .. REGISTERED SIGN
.. |copy|   unicode:: U+000A9 .. COPYRIGHT SIGN
.. |trade|  unicode:: U+2122 .. TRADEMARK

