"""Configuration file for the Sphinx documentation builder.

Run `sphinx-apidoc -f -o docs {{ cookiecutter.project_slug }}` to build the documentation.

For the full list of built-in configuration values, see the documentation:
https://www.sphinx-doc.org/en/master/usage/configuration.html

-- Project information -----------------------------------------------------
https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(Path.cwd() / "../{{ cookiecutter.project_slug }}")))


project = "{{ cookiecutter.project_name }}"
author = "{{ cookiecutter.author }}"
copyright = "{% now 'local', '%Y' %}, {{ cookiecutter.author }}"
release = "0.1.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.doctest",
    "sphinx_rtd_theme",
]

templates_path = ["_templates"]
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
