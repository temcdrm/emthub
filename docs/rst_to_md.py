# Copyright (C) 2026 Meltran, Inc

"""
  Convert rst to md files.
"""
import subprocess

if __name__ == '__main__':
  for base in ['api', 'Bibliography', 'DLLExamples', 'Dynamics', 'dynamics_doc', 'index',
               'LICENSE', 'NetworkExamples', 'Overview', 'profile', 'profile_reference',
               'Queries', 'query_doc', 'Roadmap']:
    cmd = 'pandoc {:s}.rst -o ./md/{:s}.md'.format (base, base)
    subprocess.run (cmd)

