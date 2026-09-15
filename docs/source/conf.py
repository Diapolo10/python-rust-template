# Configuration file for the Sphinx documentation builder.  # noqa: D100, INP001
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import tomllib
from pathlib import Path

root_dir = Path(__file__).parents[2]
config_file = root_dir / 'pyproject.toml'
cargo_config_file = root_dir / 'Cargo.toml'
config = tomllib.loads(config_file.read_text(encoding='utf-8'))
cargo_config = tomllib.loads(cargo_config_file.read_text(encoding='utf-8'))
project_config = config['project']

project = project_config['name']
author = project_config['authors'][0]['name']
copyright = f"2023, {author}"  # noqa: A001
version = cargo_config['package']['version']
release = cargo_config['package']['version']

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []  # type: ignore  # noqa: PGH003

templates_path = ["_templates"]
exclude_patterns = []  # type: ignore  # noqa: PGH003


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "alabaster"
html_static_path = ["_static"]
