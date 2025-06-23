# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# VSCode code spell check settings
# cSpell:enableCompoundWords

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import datetime as dt
import os
import packaging.version
import sphinx_rtd_theme    # type: ignore

project = "NOAA GFDL Documentation"
copyright = f"{dt.datetime.now().year}, NOAA GFDL"
author = "NOAA GFDL"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
extensions = [
    "sphinx.ext.intersphinx",
    "sphinx_rtd_theme",
]

# Additional Sphinx templates
templates_path = ["_templates"]

# Options for HTML output ----------------------------------------------------
html_title = "NOAA GFDL Documentation"
html_logo = "_static/NOAA_logo_header.png"
html_favicon = "_static/favicon.ico"
html_theme = "sphinx_rtd_theme"
html_show_copyright = False

html_baseurl = os.environ.get("READTHEDOCS_CANONICAL_URL",
                              "https://docs.gfdl.noaa.gov/")

html_static_path = [
    "_static",
]

html_css_files = [
    "css/theme_overrides.css",
]

html_context = {    # type: ignore
    "display_github": True,
    "github_user": "underwoo",
    "github_repo": "noaa-gfdl",
    "github_version": "main",
    "conf_py_path": "/docs/",
    "show_sphinx": False,
    "project_home_url": "https://www.gfdl.noaa.gov/",
    "project_home_name": "NOAA Geophysical Fluid Dynamics Laboratory",
    "noaa_footer_links": {
        "Protecting Your Privacy": "https://www.noaa.gov/protecting-your-privacy",
        "FOIA": "https://www.noaa.gov/information-technology/foia",
        "Information Quality": "https://www.noaa.gov/organization/information-technology/policy-oversight/information-quality",
        "Accessibility": "https://www.noaa.gov/accessibility",
        "Guidance": "https://www.noaa.gov/guidance",
        "Budget & Performance": "https://www.noaa.gov/budget-finance-performance",
        "Disclaimer": "https://www.noaa.gov/disclaimer",
        "EEO": "https://www.noaa.gov/inclusion-and-civil-rights",
        "No-Fear Act": "https://www.noaa.gov/organization/inclusion-and-civil-rights/no-fear-act",
        "USA.gov": "https://www.usa.gov/",
        "Ready.gov": "https://www.ready.gov/",
    }
}

# RTD theme options ----------------------------------------------------------
# https://sphinx-rtd-theme.readthedocs.io/en/stable/configuring.html
html_theme_options = {   # type: ignore
    "collapse_navigation": False,
    "sticky_navigation": True,
    "navigation_depth": 4,
    "style_external_links": True,
    "style_nav_header_background": "#efefef",
    "logo_only": True,
    "version_selector": True,
    "language_selector": True,
    "vcs_pageview_mode": "blob",
    "includehidden": True,
}

if (packaging.version.Version(sphinx_rtd_theme.__version__) >=
    packaging.version.Version("2.1.0")):
    html_theme_options["flyout_display"] = "hidden"

# Sphinx Intersphinx configuration -------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html
intersphinx_mapping = {
    "fre-cli": ("https://noaa-gfdl.readthedocs.io/projects/fre-cli/en/latest", None),
}

# Sphinx defaults to automatically resolve *unresolved* labels using all your
# Intersphinx mappings. This behavior has unintended side-effects, namely that
# documentations local references can suddenly resolve to an external location.
#
# See also:
# https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html#confval-intersphinx_disabled_reftypes
intersphinx_disabled_reftypes = ["*"]
