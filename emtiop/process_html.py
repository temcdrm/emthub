# Copyright (C) 2026 Meltran, Inc

import sys

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

  fp = open (outfile, 'w', encoding='utf-8')
  with open (infile, 'r', encoding='utf-8') as file:
    for line in file:
      fp.write (process_line (line))

  fp.close()

