# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os 
import sys

sys.path.insert(0, os.path.abspath('C:/Users/eliza/OneDrive/Documents/cambridge_DIS/c1/example_class2/brownian_motion/pygbm'))

project = 'pygbm'
copyright = '2024, Liz Tan'
author = 'Liz Tan'
release = '0.1.0.'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',            # For Google/NumPy-style docstrings
    'sphinx_autodoc_typehints',       # For automatic type hints in docs
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
