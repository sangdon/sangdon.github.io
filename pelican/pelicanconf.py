#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Sangdon Park'
SITENAME = u'Sangdon Park'
#SITEURL = 'http://localhost:8000'
SITEURL = 'http://cis.upenn.edu/~sangdonp'

PATH = 'content'
STATIC_PATHS = ['articles', 'pages', 'images']

# output dir
OUTPUT_PATH = '../'

# favicon
FAVICON = 'images/upenn-shield-simple.png'

# theme setups
THEME = 'themes/pelican-themes/pelican-bootstrap3-sangdon'
BOOTSTRAP_THEME = 'cosmo-sangdon'
#PYGMENTS_STYLE = 'darkly'
HIDE_SIDEBAR = True
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

TIMEZONE = 'EST'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
