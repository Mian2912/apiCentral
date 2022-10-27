from .base import *

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'apidb',
        'USER': 'root',
        'PASSWORD': 'academyjava',
        'HOST':'localhost',
        'PORT': 3306
    }
}


STATIC_URL = 'static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.child('media')