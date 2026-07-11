# Configuration file for the Sphinx documentation builder.

project = "MAPS"
copyright = '2026, dbj'
author = 'hpw'

extensions = [
    "sphinx.ext.mathjax",
    "sphinx_copybutton",
    "myst_nb",
    "sphinx_design",
]

master_doc = "index"
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "myst-nb",
    ".ipynb": "myst-nb",
}

exclude_patterns = [
    "_build",
    "**.ipynb_checkpoints",
    "notebooks/README.rst",
    "notebooks/CONTRIBUTING.rst",
]

nb_execution_mode = "off"
myst_enable_extensions = [
    "colon_fence",
    "dollarmath",
    "amsmath",
]
myst_heading_anchors = 3

pygments_style = "tango"
pygments_dark_style = "monokai"

html_theme = "furo"
html_static_path = ["_static"]
html_show_sphinx = False
html_show_sourcelink = False
html_theme_options = {
    "sidebar_hide_name": True,
    "light_logo": "img/light_mode_logo.png",
    "dark_logo": "img/dark_mode_logo.png",
    "light_css_variables": {
        "color-brand-primary": "#5c7c9b",
        "color-brand-content": "#5c7c9b",
        "admonition-font-size": "var(--font-size-normal)",
        "admonition-title-font-size": "var(--font-size-normal)",
        "code-font-size": "var(--font-size--small)",
    },
}
