#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os
import sys
from pathlib import Path

sys.path.append(os.curdir)
from djangocong_data import *


AUTHOR = "Rencontres Django"
SITENAME = "DjangoCong 2019 à Marseille"
SITEDESCRIPTION = """Djangocong est une conférence communautaire et itinérante
reconduite annuellement depuis 2010 autour du framework web Django."""
SITEURL = "/2019"

MOBILE_MENU_BANNER = "images/office.jpg"

PATH = "content"

TIMEZONE = "Europe/Paris"

DEFAULT_LANG = "fr"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
SOCIAL = (("You can add links in your config file", "#"), ("Another social link", "#"))

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"

THEME = "theme"
THEME_STATIC_DIR = ""

PLUGIN_PATHS = ["plugins"]
PLUGINS = []

# STATIC_PATHS = ["extra"]

# EXTRA_PATH_METADATA = {
#     "extra/favicon.ico": {"path": "favicon.ico"},
#     "extra/apple_touch_icon.png": {"path": "apple_touch_icon.png"},
# }
