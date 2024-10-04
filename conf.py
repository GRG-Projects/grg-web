# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import glob
import os
import sys

project = "Garyfallidis Research Group"
copyright = "2024, GRG"
author = "GRG"
# release = ''

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration


try:
    import tomllib  # type: ignore
except ImportError:
    import tomli as tomllib

sys.path.append(os.path.abspath("sphinxext"))

# -- General configuration -----------------------------------------------------
rel = {}
# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.ifconfig",
    "sphinx_reredirects",
    "ablog",
]

templates_path = ["_templates"]

# The suffix of source filenames.
source_suffix = ".rst"

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "pydata_sphinx_theme"

html_static_path = ["_static"]

html_js_files = [
    "js/carousel.js",
    "js/splide.js",
    "js/search.js",
    "js/pagination.js",
    "js/publications.js",
    "js/modal.js",
]

html_css_files = [
    "css/common.css",
    "css/splide.css",
    "css/navbar.css",
    "css/footer.css",
    "css/home/hero.css",
    "css/home/research.css",
    "css/home/journals.css",
    "css/home/workshop.css",
    "css/team/team.css",
    "css/team/member.css",
    "css/research/research.css",
    "css/teaching/teaching.css",
    "css/publications/papers.css",
    "css/about/about.css",
    "css/software/software.css",
    "css/career/career.css",
]

# Load multiple TOML files
toml_files = ["context/others.toml", "context/publications.toml", "context/team.toml"]
config = {}

for toml_file in toml_files:
    with open(toml_file, "rb") as f:
        config.update(tomllib.load(f))

html_context = {
    "journal_slides": config["journal_slides"],
    "team_current": config["team_current"],
    "team_director": config["team_director"],
    "team_alumni": config["team_alumni"],
    "teaching_course": config["teaching_course"],
    "publication_paper": config["publication_paper"],
    "default_mode": "light",
}

html_favicon = "_static/images/logos/trident-favicon.png"

html_theme_options = {
    # "secondary_sidebar_items": ["page-toc"],
    # "show_toc_level": 1,
    # "navbar_end": ["components/navbar-links.html"],
    "navbar_persistent": "",
    "logo": {
        "text": "Garyfallidis Research Group",
        "image_light": "_static/images/logos/trident-large.png",
        "image_dark": "_static/images/logos/trident-large.png",
    },
    "navbar_end": ["components/common/navbar.html"],
    "footer_center": ["components/common/footer.html"],
    "footer_start": [],
    "footer_end": [],
}

html_additional_pages = {
    "index": "pages/home.html",
    "about": "pages/about.html",
    "team": "pages/team.html",
    "research": "pages/research.html",
    "teaching": "pages/teaching.html",
    "publications": "pages/publications.html",
    "software": "pages/software.html",
    "career": "pages/career.html",
}

OUTPUT_DIR = "_templates/team"

for filename in glob.glob(os.path.join(OUTPUT_DIR, "*.html")):
    member_name = os.path.splitext(os.path.basename(filename))[0]
    html_additional_pages[f"team/{member_name}"] = f"team/{os.path.basename(filename)}"
