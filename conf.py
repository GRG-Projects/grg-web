# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import glob
import os
import shutil
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

# The suffix of source filenames.
source_suffix = ".rst"

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "pydata_sphinx_theme"

templates_path = ["_templates"]
html_static_path = ["_static"]

html_js_files = [
    "js/carousel.js",
    "js/splide.js",
    "js/search.js",
    "js/pagination.js",
    "js/publications.js",
    "js/modal.js",
]

html_style = "css/main.css"

# Load multiple TOML files
toml_files = ["context/others.toml", "context/publications.toml", "context/team.toml"]
config = {}

for toml_file in toml_files:
    with open(toml_file, "rb") as f:
        config.update(tomllib.load(f))

html_context = {
    "journal_slides": config["journal_slides"],
    "team_director": config["team_director"],
    "team_staff": config["team_staff"],
    "team_current": config["team_current"],
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


def generate_team_pages():
    TOML_FILE = "context/team.toml"
    TEMPLATE_FILE = "_templates/components/team_template/team_template.html"
    OUTPUT_DIR = "_templates/team"

    # Clear the output directory
    if os.path.exists(OUTPUT_DIR):
        for filename in os.listdir(OUTPUT_DIR):
            file_path = os.path.join(OUTPUT_DIR, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f"Failed to delete {file_path}. Reason: {e}")
    else:
        os.makedirs(OUTPUT_DIR)

    # Read the team.toml file
    with open(TOML_FILE, "rb") as f:
        team_data = tomllib.load(f)

    # Read the template file
    with open(TEMPLATE_FILE, "r") as f:
        template_content = f.read()

    # List of all team collections we want to process
    collections = ["team_director", "team_staff", "team_current", "team_alumni"]

    # Loop through each collection
    for collection in collections:
        if collection in team_data:
            for member in team_data[collection]:
                member_name = member["name"].lower().replace(" ", "_")
                output_file = f"{member_name}.html"

                member_html = template_content.replace("{{ collection }}", collection)
                member_html = member_html.replace(
                    "{{ member.name }}", member.get("name", "")
                )

                with open(os.path.join(OUTPUT_DIR, output_file), "w") as f:
                    f.write(member_html)


# Generate team pages
generate_team_pages()

# Now populate html_additional_pages
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
