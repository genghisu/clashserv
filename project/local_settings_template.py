from settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'lottserv',
        'USER': 'lottserv',
        'PASSWORD': 'lottserv',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}