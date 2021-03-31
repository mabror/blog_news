import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = 'mzrv+=49v_=rx6ho#gh(k9=)(!mzlyk*ynv+3bh8yfmdhrmlg9'


DEBUG = True

ALLOWED_HOSTS = []


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'news_blog',
        'PASSWORD': 'Qwerty123$',
        'HOST': '127.0.0.1',
        'USER': 'news_blog'
    }
}