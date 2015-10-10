#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Dmitry Ogurtsov'
SITENAME = u'Dmitry Ogurtsov'
SITEURL = ''

PATH = 'content'
STATIC_PATHS = ['attached', 'downloads']
# ARTICLE_PATHS = ['blog']
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{slug}.html'
ARTICLE_URL = 'blog/{date:%Y}/{slug}.html'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (('GitHub', 'https://github.com/ogurtsov'),
    ('5Pointers', 'http://5pointers.com/'),
    ('UpWork', 'https://www.upwork.com/freelancers/~01f5159861ce9e4c0f'),
    ('Guru', 'http://www.guru.com/freelancers/dmitry-ogurtsov'))


DEFAULT_PAGINATION = 10

THEME = "themes/default/"

DISQUS_SITENAME = "ogurtsovgithubio"

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
