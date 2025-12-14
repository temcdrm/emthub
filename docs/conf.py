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
    'sphinx.ext.intersphinx']
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
copyright = '2024-25, Meltran, Inc'
author = 'Meltran, Inc'
version = '0.0.3'
release = '0.0.3'
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
    (master_doc, 'emthub', 'pecblocks Documentation',
     author, 'emthub', 'Power Electronic Converter Blocks.',
     'Miscellaneous'),
]

napoleon_custom_sections = [('Returns', 'params_style')]

