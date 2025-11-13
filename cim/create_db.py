# Copyright (C) 2025 Meltran, Inc

import sqlite3

if __name__ == '__main__':
  con = sqlite3.connect ('emtiop.db')
  cur = con.cursor ()
  with open ('emtiop.sql', 'r', encoding='utf8') as file:
    script = file.read()
  cur.executescript (script)
  print(cur.fetchall())
  con.close()

