# Copyright (C) 2026 Meltran, Inc

import sys
import json

cim_class = None
cim_attribute = None
cim_type = None
cim_default = None
bTypeComesNext = False
bNeedType = False
bNeedDefault = False

def process_default (s, cim_type):
  if cim_type == 'Boolean':
    if '1' in s or 'true' in s:
      return True
    else:
      return False
  if s[-1] == '.':
    s = s[:-1]
  s = s.replace (',', '.')
  if cim_type == 'Integer':
    return int(s)
  if cim_type.endswith ('Kind'):
    return s
  return float(s)

def find_between (s, first, last):
  start = s.index(first) + len(first)
  end = s.index (last, start)
  return s[start:end]

def process_attributes (line, d):
  global bNeedDefault, bNeedType, bTypeComesNext, cim_class, cim_attribute, cim_type, cim_default

  if bNeedType and bTypeComesNext:
    cim_type = find_between (line, '>', '<')
    #print ('  cim_type', cim_type)
    bNeedType = False
    d[cim_class][cim_attribute]['type'] = cim_type
  elif '<p class="name" id="' in line:
    toks = find_between (line, '<p class="name" id="', '">').split('.')
    cim_class = toks[0]
    cim_attribute = toks[1]
    #print ('cim_class', cim_class, 'cim_attribute', cim_attribute)
    bNeedType = True
    bNeedDefault = True
    if cim_class not in d:
      d[cim_class] = {}
    if cim_attribute not in d[cim_class]:
      d[cim_class][cim_attribute] = {'type':None, 'default': None}
  if bNeedType and '<p class="type">' in line:
    bTypeComesNext = True
  else:
    bTypeComesNext = False
  if bNeedDefault and 'Typical value = ' in line:
    cim_default = process_default (find_between (line, 'Typical value = ', '</p>'), cim_type)
    #print ('  cim_default', cim_default)
    bNeedDefault = False
    d[cim_class][cim_attribute]['default'] = cim_default

def process_line (line):
  ret = line.replace('&lt;', '<')
  ret = ret.replace('&gt;', '>')
  ret = ret.replace('&amp;gt;', '>')
  ret = ret.replace('&amp;lt;', '<')
  return ret

if __name__ == '__main__':
  idx = 0
  if len(sys.argv) > 2:
    infile = sys.argv[1]
    outfile = sys.argv[2]
  else:
    print ('usage: python process_html.py input.html output.html')
    quit()

  d = {}
  fp = open (outfile, 'w', encoding='utf-8')
  with open (infile, 'r', encoding='utf-8') as file:
    for line in file:
      data = process_line (line)
      process_attributes (data, d)
      fp.write (process_line (data))
  fp.close()

  jp = open ('profile_attributes.json', 'w')
  json.dump (d, jp, indent=2)
  jp.close()

