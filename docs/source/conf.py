# Configuration file for the Sphinx documentation builder.  # noqa: D100, INP001
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "project-name"
copyright = "2023, Lari Liuhamo"  # noqa: A001
author = "Lari Liuhamo"
release = "0.1"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []  # type: ignore  # noqa: PGH003

templates_path = ["_templates"]
exclude_patterns = []  # type: ignore  # noqa: PGH003


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "alabaster"
html_static_path = ["_static"]
