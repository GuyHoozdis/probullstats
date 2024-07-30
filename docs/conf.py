"""Sphinx configuration."""

project = "probullstats"
author = "Guy Hoozdis"
copyright = "2024, UB Bucking Company"  # noqa: A001

extensions = [
    "sphinx.ext.autodoc",
    "sphinx_autodoc_typehints",
]

html_theme = "furo"
