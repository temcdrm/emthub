# Copyright (C) 2025-2026 Meltran, Inc
import emthub.api as emthub

def main():
  """Tabulates the CIM classes and instance counts found in 5 example files.
  """
  emthub.print_cim_summaries (['XfmrSat', 'IEEE39', 'IEEE118', 'WECC240', 'SMIBDLL'])

if __name__ == '__main__':
  main()

