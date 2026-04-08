#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
import os
import sys
sys.path.insert(0, os.path.abspath('..'))

# -- General configuration ------------------------------------------------
needs_sphinx = '5.0.2'
numfig = True
extensions = ['sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.imgmath',
    'sphinx.ext.githubpages',
    'sphinx.ext.napoleon',
    'sphinx.ext.todo',
    'sphinx-jsonschema',
    'sphinx.ext.intersphinx',
    'sphinx_exec_code']
templates_path = ['_templates']
from recommonmark.parser import CommonMarkParser
source_suffix = ['.rst', '.md']
source_parsers = {
		'.md': CommonMarkParser,
}

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'emthub'
copyright = '2024-26, Meltran, Inc'
author = 'Meltran, Inc'
version = '0.0.4'
release = '0.0.4'
language = 'en'

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
pygments_style = 'sphinx'
todo_include_todos = True

html_theme = 'sphinx_rtd_theme'

html_static_path = ['assets']
htmlhelp_basename = 'emthub'
latex_elements = {
}

latex_documents = [
    (master_doc, 'emthub.tex', 'emthub Documentation',
     'Meltran, Inc', 'manual'),
]
man_pages = [
    (master_doc, 'emthub', 'emthub Documentation',
     [author], 1)
]
texinfo_documents = [
    (master_doc, 'emthub', 'emthub Documentation',
     author, 'emthub', 'IEEE P3743, EMT Model Interoperability.',
     'Miscellaneous'),
]

napoleon_custom_sections = [('Returns', 'params_style')]

# from Google

import json
from docutils import nodes
from docutils.parsers.rst import Directive

class PrettyPrintDict(Directive):
  required_arguments = 1
  def run(self):
    # Import the dictionary dynamically
    module_path, dict_name = self.arguments[0].rsplit('.', 1)
    mod = __import__(module_path, fromlist=[dict_name])
    data = getattr(mod, dict_name)

    # Format as a pretty JSON string
    pretty_data = json.dumps(data, indent=4, sort_keys=True)
    content = f".. code-block:: json\n\n  {pretty_data}"

    # Parse the generated rST content
    node = nodes.section()
    self.state.nested_parse([content], 0, node)
    return node.children

def setup(app):
  app.add_directive('pretty-dict', PrettyPrintDict)

