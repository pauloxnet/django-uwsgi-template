from {{project_name}}.settings.base import *  # noqa
from {{project_name}}.settings.secret import *  # noqa

HOST = BASE_HOST_URL
ALLOWED_HOSTS = (HOST,)

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': DATABASES_DEFAULT_NAME or '{{project_name}}',
        'USER': DATABASES_DEFAULT_USER or '{{project_name}}',
        'PASSWORD': DATABASES_DEFAULT_PASSWORD or '',
        'HOST': DATABASES_DEFAULT_HOST or '127.0.0.1',
        'PORT': DATABASES_DEFAULT_PORT or '5432',
    }
}

# Email Settings
# https://docs.djangoproject.com/en/2.1/topics/email/

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = EMAIL_HOST or ''
# EMAIL_PORT = EMAIL_PORT or 465
# EMAIL_HOST_USER = EMAIL_HOST_USER or ''
# EMAIL_HOST_PASSWORD = EMAIL_HOST_PASSWORD or ''
# EMAIL_USE_SSL = EMAIL_USE_SSL or False
# EMAIL_USE_TLS = EMAIL_USE_SSL or False

# Debug

DEBUG = False
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG  # noqa

# Assets

# STATIC_DEBUG = False

# Sites
# https://docs.djangoproject.com/en/2.1/ref/contrib/sites/

# SITE_ID = 1

# Fab commands configuration

WORKING_DIR = 'www/{{project_name}}'
HOST_USER = ''
HOST_IP = ''
HOST_PORT = '22'

# Deployment

SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'  # Default: 'SAMEORIGIN'

# HTTPS
# https://docs.djangoproject.com/en/dev/howto/deployment/checklist/#https

# CSRF_COOKIE_SECURE = True
# SECURE_SSL_REDIRECT = True
# SESSION_COOKIE_SECURE = True

# Performance optimizations
# https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/#performance-optimizations

# CONN_MAX_AGE = None
