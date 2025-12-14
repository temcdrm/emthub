.. role:: math(raw)
   :format: html latex
..

Overview
========

EMTHub\ |reg| provides software and data schemas for standards-based model building and validation to perform electromagnetic transient (EMT) 
studies of electric utility power systems. The focus is on inverter-based resources (IBR), e.g., wind, solar, and storage, 
in electric utility systems. Network EMT models are based on the international standard Common Information Model (CIM). Unit and plant
IBR models are based on IEEE standards 2800 and P2800.2, along with a Cigre/IEEE specification on real-code modeling through
dynamics link library (DLL) interfaces.

Background
----------

For an overview, see `IEEE P3743 Introduction <_static/IEEE_P3743_Introduction.pdf>`_.

- For general background on **EMT modeling**, with a focus on IBR, see `IEEE Electrification Special Issue <https://ieeexplore.ieee.org/xpl/tocresult.jsp?isnumber=10334426&punumber=6508996>`_.
- For background on the North American Electric Reliability Corporation (**NERC**) guidelines on EMT modeling for IBR, see its `Reliability Guideline <https://www.nerc.com/comm/RSTC_Reliability_Guidelines/Reliability_Guideline-EMT_Modeling_and_Simulations.pdf>`_ and its `EMT Task Force <https://www.nerc.com/comm/RSTC/Pages/EMTTF.aspx>`_.
- For information about the **DLL interface** for IBR modeling, see `Joint IEEE/Cigre Task Force Web Site <https://www.electranix.com/ieee-pes-tass-realcodewg/>`_ and `EPRI Report 3002028322 <https://www.epri.com/research/products/3002028322>`_.
- For background on the **WECC generic IBR** models, see `EPRI Report 3002027129 <https://www.epri.com/research/products/000000003002027129>`_.
- For technical background on maintaining EMT **network models**, see `Thapa, et. al. <https://doi.org/10.1109/ACCESS.2023.3305394>`_, `Abdelmalak, et. al. <https://doi.org/10.1109/PESGM46819.2021.9637930>`_,  `Noda, et. al. <https://doi.org/10.1109/MELE.2023.3320521>`_, and `Zhao, et. al. <https://doi.org/10.1109/APEEC.2019.8720692>`_.
- For background on the **CIM**, see `EPRI CIM Primer 3002026852 <https://www.epri.com/research/products/3002026852>`_ and `CIMHub <https://cimhub.readthedocs.io/en/latest/>`_.
- For applications of **CIM dynamics modeling**, including the Western Electricity Coordinating Council (WECC) generic IBR models, see `Common Grid Model Exchange Specification (Dynamics) <https://cgmes.github.io/dynamics/#dynamics>`_
- For applications of **CIM EMT modeling**, see `Martin and Fillion <https://www.ipstconf.org/papers/Proc_IPST2017/17IPST099.pdf>`_.
- For early examples of **scripted IBR model validation**, see `NERC/i2X EMT Bootcamp Files <https://github.com/pnnl/i2x/tree/master/emt-bootcamp>`_.
- For description of medium-scale public test systems with IBR, see `Pena et. al. <https://doi.org/10.1109/TPWRS.2017.2695963>`_ for a modified **IEEE 118-bus system** and `Yuan et. al. <https://doi.org/10.1109/TD39804.2020.9299666>`_ for a modified **WECC 240-bus system**.

Installation
------------

To install the Python package::

    pip install emthub

Quick Start
-----------

TBD; running examples in this order:

- `CIM <https://github.com/temcdrm/emthub/tree/main/cim>`_.
- `MATPOWER <https://github.com/temcdrm/emthub/tree/main/matpower>`_.
- `ATP <https://github.com/temcdrm/emthub/tree/main/atp/data>`_.

Repository
----------

See `EMTHub directory <https://github.com/temcdrm/emthub>`_

.. |reg|    unicode:: U+000AE .. REGISTERED SIGN
.. |copy|   unicode:: U+000A9 .. COPYRIGHT SIGN
.. |trade|  unicode:: U+2122 .. TRADEMARK

