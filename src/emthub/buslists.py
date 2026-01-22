# Copyright (C) 2023-2024 Battelle Memorial Institute
# Copyright (C) 2025-2026 Meltran, Inc

def build_bus_lists (d):
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
  for cnid, data in ordered_buses.items():
    if data['name'] == swingbus:
      return cnid


