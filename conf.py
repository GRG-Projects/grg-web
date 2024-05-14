# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'GRG'
copyright = '2024, GRG'
author = 'GRG'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "grg_sphinx_theme"

html_static_path = ['_static']

html_theme_options = {
  "secondary_sidebar_items": ["page-toc"],
  "show_toc_level": 1,
  # "announcement": "Here's a <a href='https://pydata.org'>PyData Announcement!</a>",
  "navbar_center": ["components/navbar-links.html"],
  "navbar_links": [
     {
        "name": "Docs",
        "children": [
          {
            "name": "Overview",
            "url": "https://docs.dipy.org/stable",
            "link_type": "inter"
          },
          {
            "name": "Tutorials",
            "url": "https://docs.dipy.org/stable/examples_built/index",
            "link_type": "inter"
          },
          {
            "name": "Recipes",
            "url": "https://docs.dipy.org/stable/recipes",
            "link_type": "inter"
          },
          {
            "name": "CLI / Workflows",
            "url": "https://docs.dipy.org/stable/interfaces/index",
            "link_type": "inter"
          },
          {
            "name": "API",
            "url": "https://docs.dipy.org/stable/reference/index",
            "link_type": "inter"
          },
          {
            "name": "CLI API",
            "url": "https://docs.dipy.org/stable/reference_cmd/index",
            "link_type": "inter"
          }
        ]
     },
     {
        "name": "Workshops",
        "sections": [
          {
            "name": "Latest",
            "children": [
              {
                "name": "DIPY Workshop 2024",
                "url": "https://workshop.dipy.org/workshops/dipy-workshop-2024",
                "link_type": "external"
              }
            ]
          },
          {
            "name": "Past",
            "children": [
              {
                "name": "DIPY Workshop 2023",
                "url": "https://workshop.dipy.org/workshops/dipy-workshop-2023",
                "link_type": "external"
              },
              {
                "name": "DIPY Workshop 2022",
                "url": "https://workshop.dipy.org/workshops/dipy-workshop-2022",
                "link_type": "external"
              },
              {
                "name": "DIPY Workshop 2021",
                "url": "https://workshop.dipy.org/workshops/dipy-workshop-2021",
                "link_type": "external"
              },
              {
                "name": "DIPY Workshop 2020",
                "url": "https://workshop.dipy.org/workshops/dipy-workshop-2020",
                "link_type": "external"
              },
              {
                "name": "DIPY Workshop 2019",
                "url": "https://workshop.dipy.org/workshops/dipy-workshop-2019",
                "link_type": "external"
              },
            ]
          }
        ],
     },
     {
        "name": "Community",
        "sections": [
            {
              "name": "News",
              "children": [
                  {
                    "name": "Calendar",
                    "url": "calendar",
                  },
                  {
                    "name": "Newsletters",
                    "url": "https://mail.python.org/mailman3/lists/dipy.python.org/",
                    "link_type": "external"
                  },
                  {
                    "name": "Blog",
                    "url": "blog"
                  },
                  {
                    "name": "Youtube",
                    "url": "https://www.youtube.com/c/diffusionimaginginpython",
                    "link_type": "external"
                  }
              ]
            },
            {
              "name": "Help",
              "children": [
                  {
                    "name": "Live Chat (Gitter)",
                    "url": "https://app.gitter.im/#/room/%23dipy_dipy:gitter.im",
                    "link_type": "external"
                  },
                  {
                    "name": "Github Discussions",
                    "url": "https://github.com/dipy/dipy/discussions",
                    "link_type": "external"
                  }
              ]
            }
          ]
     },
     {
        "name": "About",
        "children": [
          {
            "name": "Team",
            "url": "team",
          },
          {
            "name": "FAQ",
            "url": "https://docs.dipy.org/stable/faq",
            "link_type": "inter"
          },
          {
            "name": "Mission Statement",
            "url": "https://docs.dipy.org/stable/user_guide/mission",
            "link_type": "inter"
          },
          {
            "name": "Releases",
            "url": "https://docs.dipy.org/stable/stateoftheart",
            "link_type": "inter"
          },
          {
            "name": "Cite",
            "url": "https://docs.dipy.org/stable/cite",
            "link_type": "inter"
          },
          {
            "name": "Glossary",
            "url": "https://docs.dipy.org/stable/glossary",
            "link_type": "inter"
          },
        ]
     },
  ],
  # To remove search icon
  "navbar_persistent": "",
  "icon_links": [
    {
      "name": "GitHub",
      "url": "https://github.com/dipy",
      "icon": "fa-brands fa-github"
    },
    {
      "name": "Twitter/X",
      "url": "https://twitter.com/dipymri",
      "icon": "fa-brands fa-twitter"
    },
    {
      "name": "YouTube",
      "url": "https://www.youtube.com/c/diffusionimaginginpython",
      "icon": "fa-brands fa-youtube"
    },
    {
      "name": "LinkedIn",
      "url": "https://www.linkedin.com/company/dipy/",
      "icon": "fa-brands fa-linkedin"
    },
  ],
  "logo": {
    "image_dark": "_static/images/logos/dipy-logo.png",
    "alt_text": "DIPY",
  },
  # "footer_start": ["components/footer-sign-up.html"],
  # "footer_signup_data": {
  #   "heading": "Never miss an update from us!",
  #   "sub_heading": "Don't worry! we are not going to spam you."
  # },
  # "footer_end": ["components/footer-sections.html"],
  # "footer_links": [
  #   {
  #     "title": "About",
  #     "links": [
  #       {
  #         "name": "Developers",
  #         "link": "team"
  #       },
  #       {
  #         "name": "Support",
  #         "link": "https://github.com/dipy/dipy/discussions",
  #         "link_type": "external"
  #       },
  #       {
  #         "name": "Download",
  #         "link": "https://docs.dipy.org/stable/user_guide/installation",
  #         "link_type": "inter"
  #       },
  #       {
  #         "name": "Get Started",
  #         "link": "https://docs.dipy.org/stable/",
  #         "link_type": "inter"
  #       },
  #       {
  #         "name": "Tutorials",
  #         "link": "https://docs.dipy.org/stable/examples_built/index",
  #         "link_type": "inter"
  #       },
  #       {
  #         "name": "Videos",
  #         "link": "https://www.youtube.com/c/diffusionimaginginpython",
  #         "link_type": "external"
  #       },
  #     ]
  #   }, {
  #     "title": "Friends",
  #     "links": [
  #       {
  #         "name": "Nipy Projects",
  #         "link": "https://nipy.org/",
  #         "link_type": "external"
  #       },
  #       {
  #         "name": "FURY",
  #         "link": "https://fury.gl/",
  #         "link_type": "external"
  #       },
  #       {
  #         "name": "Nibabel",
  #         "link": "https://nipy.org/nibabel",
  #         "link_type": "external"
  #       },
  #       {
  #         "name": "Tortoise",
  #         "link": "https://tortoise.nibib.nih.gov/",
  #         "link_type": "external"
  #       },
  #     ]
  #   }, {
  #     "title": "Support",
  #     "links": [
  #       {
  #         "name": "The department of Intelligent Systems Engineering of Indiana University",
  #         "link": "https://engineering.indiana.edu/",
  #         "link_type": "external"
  #       },
  #       {
  #         "name": "The National Institute of Biomedical Imaging and Bioengineering, NIH",
  #         "link": "https://www.nibib.nih.gov/",
  #         "link_type": "external"
  #       },
  #       {
  #         "name": "The Gordon and Betty Moore Foundation and the Alfred P. Sloan Foundation, through the University of Washington eScience Institute Data Science Environment",
  #         "link": "https://escience.washington.edu/tag/alfred-p-sloan-foundation/",
  #         "link_type": "external"
  #       },
  #       {
  #         "name": "Google supported DIPY through the Google Summer of Code Program during multiple Summer (2015-2024)",
  #         "link": "https://summerofcode.withgoogle.com/",
  #         "link_type": "external"
  #       },
  #     ]
  #   }
  # ],
  # "footer_copyright": "Copyright 2008-2023, DIPY developers. Created using Grg Sphinx Theme and PyData Sphinx Theme.",
  # "github_project": "dipy",
  # "github_repo": "dipy",
  # "github_teams": [{
  #     "value": "core-dev",
  #     "label": "Core Developers"
  # }],
  # "contributors_details": contributors,
#   "subscribe_callback": "subscriptionClick"
}

# html_additional_pages = {'index': 'home.html'}