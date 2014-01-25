from .base import *

# Heroku settings
import dj_database_url
DATABASES['default'] = dj_database_url.config()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Django settings
ALLOWED_HOSTS = [
    'wolme.herokuapp.com',
]

SITE_ID = 2
PROTOCOL = 'https'

MIDDLEWARE_CLASSES = (
    'core.middleware.SSLRedirectMiddleware',
) + MIDDLEWARE_CLASSES

########## Rest framework
REST_FRAMEWORK.update({
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
    ),
})

########## STORAGE CONFIGURATION
# See: http://django-storages.readthedocs.org/en/latest/index.html
INSTALLED_APPS += (
    'storages',
    'gunicorn',
)

# See: http://django-storages.readthedocs.org/en/latest/backends/amazon-S3.html#settings
STATICFILES_STORAGE = DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

from S3 import CallingFormat
# See: http://django-storages.readthedocs.org/en/latest/backends/amazon-S3.html#settings
AWS_CALLING_FORMAT = CallingFormat.SUBDOMAIN

# See: http://django-storages.readthedocs.org/en/latest/backends/amazon-S3.html#settings
AWS_ACCESS_KEY_ID = environ.get('AWS_ACCESS_KEY_ID', '')
AWS_SECRET_ACCESS_KEY = environ.get('AWS_SECRET_ACCESS_KEY', '')
AWS_STORAGE_BUCKET_NAME = environ.get('AWS_STORAGE_BUCKET_NAME', '')
AWS_AUTO_CREATE_BUCKET = True
AWS_QUERYSTRING_AUTH = False

# AWS cache settings, don't change unless you know what you're doing:
AWS_EXPIREY = 60 * 60 * 24 * 7
AWS_HEADERS = {
    'Cache-Control': 'max-age=%d, s-maxage=%d, must-revalidate' % (AWS_EXPIREY, AWS_EXPIREY)
}

# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = 'https://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
########## END STORAGE CONFIGURATION
