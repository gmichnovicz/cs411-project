# Grabs the site root setup in settings.py
import os
from settings import SITE_ROOT

DEBUG = True
TEMPLATE_DEBUG = DEBUG

# sqlite is the quick an easy development db
DATABASES = {
  'default': {
      'ENGINE': 'django.db.backends.sqlite3',
      'NAME': os.path.join(SITE_ROOT, 'djlocal.db'),
      'USER': '',             # Not used with sqlite3.
      'PASSWORD': '',         # Not used with sqlite3.
      'HOST': '',             # Not used with sqlite3.
      'PORT': '',             # Not used with sqlite3.
  }
}