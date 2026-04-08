# Copyright (C) 2023-2024 Battelle Memorial Institute
# Copyright (C) 2025-2026 Meltran, Inc

"""
  Helper functions that navigate sequential bus numbers and CIM ConnectivityNode IDs.
"""

def build_bus_lists (d):
  """Order the buses (connectivity nodes) sequentially.

  Creates two efficient dictionaries to access buses by their
  sequential number, or by ConnectivityNode ID.

  Args:
    d (dict): The dictionary of CIM query results for a network.

  Returns:
    ordered_buses(dict): The *EMTBus* dictionary, re-ordered by bus number.
    bus_numbers(dict): Reverse lookup the ConnectivityNode ID by bus number.
  """
  bNumeric = True
  for key, data in d['EMTBus']['vals'].items():
    if not data['name'].isdigit():
      bNumeric = False
      break
  if bNumeric:
    ordered_buses = dict(sorted(d['EMTBus']['vals'].items(), key=lambda x:int(x[1]['name'])))
    print ('Numeric ordered buses')
  else:
    ordered_buses = d['EMTBus']['vals']
    print ('Non-numeric ordered buses')
  bus_numbers = {}
  busnum = 1
  for key, data in ordered_buses.items(): # data has name and nomv
    bus_numbers[key] = busnum
    busnum += 1
  return ordered_buses, bus_numbers

def get_swingbus_id (ordered_buses, swingbus):
  """Find the CIM ConnectivityNode ID by matching the Name/Number from the original raw file.

  The swing bus is used in MATPOWER or another power flow, and the Thevenin equivalent
  source in some EMT models.

  Args:
    ordered_buses (dict): a dictionary of *EMTBus* sorted by bus number
    swingbus (str): the swing bus number, as a string name

  Returns:
    cnid (str): the ConnectivityNode ID corresponding to the swing bus.
  """
  for cnid, data in ordered_buses.items():
    if data['name'] == swingbus:
      return cnid


