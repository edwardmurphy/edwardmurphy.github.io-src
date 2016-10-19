# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Edward Murphy'
SITENAME = u'ad astra per aspera'
SITEURL = 'https://edwardmurphy.github.io'
THEME = "/home/emurphy/pelican-themes/blueidea"

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Flipboard', 'https://flipboard.com/@emurphy711'))


# Social widget
SOCIAL = (('GitHub', 'https://github.com/edwardmurphy'),
          ('LinkedIn', 'https://www.linkedin.com/in/edward-murphy-000b002'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Fix no valid files in content? No, needed python-markdown (not just pip markdown)
#MARKUP = ('rst', 'md', 'html')

# Category settings
USE_FOLDER_AS_CATEGORY = False
#DEFAULT_CATEGORY = 'Misc'

# Static paths
STATIC_PATHS = ['images', 'pdfs']
