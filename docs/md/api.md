# API Reference

::: automodule
emthub.\_\_init\_\_
:::

First `import emthub.api as emthub`, then invoke a function like
`emthub.print_cim_summaries([filename_roots])`

## api

::: {.automodule members="" special-members=""}
emthub.api
:::

## buslists

::: {.automodule members="" special-members=""}
emthub.buslists
:::

## cim_examples

::: {.autodata no-value=""}
emthub.cim_examples.CASES
:::

> #hide: start import json import emthub.api as emthub
> print(json.dumps(emthub.CASES, indent=2)) #hide: stop

## cim_sparql

::: {.automodule members="" special-members=""}
emthub.cim_sparql
:::

## cim_summary

::: {.automodule members="" special-members=""}
emthub.cim_summary
:::

## cim_support

::: {.automodule members="" special-members=""}
emthub.cim_support
:::

## create_atp

::: {.automodule members="" special-members=""}
emthub.create_atp
:::

## create_mpow

::: {.automodule members="" special-members=""}
emthub.create_mpow
:::

## create_rdf

::: {.automodule members="" special-members=""}
emthub.create_rdf
:::

## create_sql

::: {.automodule members="" special-members=""}
emthub.create_sql
:::

## dll_config

Functions to query an IEEE/Cigre DLL through its API.

::: autofunction
emthub.dll_config.get_dll_interface
:::

::: autofunction
emthub.dll_config.write_atp_dll_interface
:::

## mpow_utilities

::: {.automodule members="" special-members=""}
emthub.mpow_utilities
:::

## plot_utils

::: {.automodule members="" special-members=""}
emthub.plot_utils
:::

## Example Scripts for Users

These are distributed in the *examples* subdirectory, and obtainable by
*emthub-extract-case \#*. The command-line documentation follows.

### atp.py

::: {.autofunction noindex=""}
emthub.examples.atp.main
:::

### bps_make_mpow.py

::: {.autofunction noindex=""}
emthub.examples.bps_make_mpow.main
:::

### cim_summary.py

::: {.autofunction noindex=""}
emthub.examples.cim_summary.main
:::

### cim_to_atp.py

::: {.autofunction noindex=""}
emthub.examples.cim_to_atp.main
:::

### create_smib_dll.py

::: {.autofunction noindex=""}
emthub.examples.create_smib_dll.main
:::

### ic_to_rdf.py

::: {.autofunction noindex=""}
emthub.examples.ic_to_rdf.main
:::

### mpow.py

::: {.autofunction noindex=""}
emthub.examples.mpow.main
:::

### plot_bps.py

::: {.autofunction noindex=""}
emthub.examples.plot_bps.main
:::

### raw_to_rdf.py

::: {.autofunction noindex=""}
emthub.examples.raw_to_rdf.main
:::

### test_cim_sparql.py

::: {.autofunction noindex=""}
emthub.examples.test_cim_sparql.main
:::
