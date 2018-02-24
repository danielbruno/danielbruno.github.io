#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Daniel Bruno'
SITENAME = u'Daniel Bruno'
SITEURL = 'http://dbruno.org'
THEME = 'Flex'
PATH = 'content'
SITESUBTITLE = "Systems Engineer and Open Source Enthusiast"
BROWSER_COLOR = '#333'
ROBOTS = 'index, follow'

PLUGIN_PATHS = ['plugins']
PLUGINS = ['tipue_search']

THEME = 'themes/Flex'

DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'authors', 'archives', 'search'))

# ADD_THIS_ID = 'ra-XYZ'
DISQUS_SITENAME = 'danielbruno'
GOOGLE_ANALYTICS = 'UA-73073002-1'
GOOGLE_TAG_MANAGER = 'GTM-5SCDNJ4'

TIMEZONE = 'Africa/Johannesburg'
DEFAULT_LANG = u'en'
OG_LOCALE = u'en_US'

SITELOGO = u'/theme/img/danielbruno-avatar.png'
FAVICON = u'/theme/img/favicon.ico'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa'
}

# Blogroll
# LINKS = (('RPM Packages', 'https://src.fedoraproject.org/user/dbruno'),
#          ('Fedora', 'https://src.fedoraproject.org/user/dbruno'),
#          ('', 'http://jinja.pocoo.org/'),
#          ('Home', '#'),)

# Social widget
SOCIAL = (('github', 'https://github.com/danielbruno'),
          ('linkedin', 'https://linkedin.com/in/danielbrunos'),
          ('twitter', 'https://twitter.com/danielbrunos'),
          ('rss', 'http://dbruno.org/feeds/all.atom.xml'),)

DEFAULT_PAGINATION = 13

# Github Profile
GITHUB_URL = 'http://github.com/danielbruno'

USE_LESS = True

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
