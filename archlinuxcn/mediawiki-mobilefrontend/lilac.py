from lilaclib import *

def pre_build():
  mediawiki_pre_build(
    'MobileFrontend',
    _G.newver,
    'Provides a mobile-friendly view',
    'GPL2',
  )

def post_build():
  mediawiki_post_build()
