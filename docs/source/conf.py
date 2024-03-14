# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'qnngds'
copyright = '2024, QNN group'
author = 'QNN group'

release = '0.1'
version = '0.1.0'

import sys 
import os
# script_dir = os.path.dirname(os.path.abspath(__file__))
# qnngds_path = os.path.abspath(os.path.join(script_dir, '..', 'src\qnngds'))
sys.path.insert(0, os.path.abspath(os.path.join('..', '..', 'src', 'qnngds')))

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

autodoc_member_order = 'bysource'

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
