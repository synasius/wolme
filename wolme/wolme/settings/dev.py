from .base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'ENABLE_STACKTRACES': True,
}

INTERNAL_IPS = ('127.0.0.1',)

INSTALLED_APPS += (
    'debug_toolbar',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'wolme',
        'USER': 'devel',
        'PASSWORD': '123456',
        'HOST': '',
        'PORT': '',
    }
}

SECRET_KEY = '1x2x@lv07t!b_m-=@dqhpf-!-=zi8dgzosh%7gj^t1y3kb^6f6'
