"""Sphinx configuration for LangChain StackSpot AI documentation."""

import os
import sys
import datetime

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath('../..'))

# Project information
project = 'LangChain StackSpot AI'
copyright = f'{datetime.datetime.now().year}, StackSpot'
author = 'StackSpot'

# The full version, including alpha/beta/rc tags
import langchain_stackspot_ai
release = langchain_stackspot_ai.__version__

# Extensions
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx.ext.intersphinx',
    'myst_parser',
]

# Add any paths that contain templates
templates_path = ['_templates']

# List of patterns to exclude from source
exclude_patterns = []

# The theme to use for HTML and HTML Help pages
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files
html_static_path = ['_static']

# Intersphinx mapping
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'langchain': ('https://python.langchain.com/en/latest/', None),
}

# Napoleon settings
napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = True
napoleon_use_admonition_for_notes = True
napoleon_use_admonition_for_references = True
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_preprocess_types = False
napoleon_type_aliases = None
napoleon_attr_annotations = True

# MyST settings
myst_enable_extensions = [
    "colon_fence",
    "deflist",
]
myst_heading_anchors = 3
