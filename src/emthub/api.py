# Copyright (C) 2017-2023 Battelle Memorial Institute
# Copyright (C) 2025 Meltran, Inc.
# file: api.py
"""Functions intended for public access.

Example:
    To show print CIM summaries interface::

        import emthub.api as emthub
        emthub.print_cim_summaries(['XfmrSat','IEEE39','IEEE118','WECC240'])

Public Functions:
    :print_cim_summaries: Print class names and counts found in list of Turtle files.
"""

from __future__ import absolute_import

from .cim_summary import print_cim_summaries

from .version import __version__


