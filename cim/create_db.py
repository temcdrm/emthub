# Copyright (C) 2025 Meltran, Inc

import sqlite3

if __name__ == '__main__':
  # remove existing tables
  con = sqlite3.connect ('emtiop.db')
  cur = con.cursor ()
  cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%';")
  tables = cur.fetchall()
  for table_name in tables:
      table_name = table_name[0]  # Extract table name from tuple
      print('  Dropping', table_name)
      cur.execute('DROP TABLE IF EXISTS {:s};'.format (table_name))
  con.commit()
  print('All tables dropped successfully.')

  # create the profile tables in correct order for the foreign keys?
  with open ('emtiop_lite.sql', 'r', encoding='utf8') as file:
    script = file.read()
  cur.executescript (script)
  print('Table Creation Result', cur.fetchall())

  con.close()

