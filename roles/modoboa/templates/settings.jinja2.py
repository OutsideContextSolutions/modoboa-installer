# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from logging.handlers import SysLogHandler

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# SECURITY WARNING: keep the secret key file used in production secret!
from .secret_key_generator import SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
ALLOWED_HOSTS += ['{{ domain }}', ]

DEBUG="{{debug | default('False')}}"

ALLOWED_HOSTS = []

SITE_ID = 1

# Security settings

X_FRAME_OPTIONS = "SAMEORIGIN"

# Application definition

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'reversion',
    'ckeditor',
    'ckeditor_uploader',
    'rest_framework',
    'rest_framework.authtoken',
)

# A dedicated place to register Modoboa applications
# Do not delete it.
# Do not change the order.

MODOBOA_APPS = [
{% for app in modoboa_base_apps+modoboa_apps %}
{% if app is string %}
    "{{app|replace('-','_')}}",
{% else %}
    "{{app[1]}}",
{% endif %}
{% endfor %}
]

INSTALLED_APPS += MODOBOA_APPS

AUTH_USER_MODEL = 'core.User'

MIDDLEWARE_CLASSES = (
    'x_forwarded_for.middleware.XForwardedForMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'modoboa.core.middleware.LocalConfigMiddleware',
    'modoboa.lib.middleware.AjaxLoginRedirect',
    'modoboa.lib.middleware.CommonExceptionCatcher',
    'modoboa.lib.middleware.RequestCatcherMiddleware',
)

AUTHENTICATION_BACKENDS = (
    # 'modoboa.lib.authbackends.LDAPBackend',
    # 'modoboa.lib.authbackends.SMTPBackend',
    'django.contrib.auth.backends.ModelBackend',
)

# SMTP authentication
# AUTH_SMTP_SERVER_ADDRESS = 'localhost'
# AUTH_SMTP_SERVER_PORT = 25
# AUTH_SMTP_SECURED_MODE = None  # 'ssl' or 'starttls' are accepted

{% raw %}
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'modoboa.core.context_processors.top_notifications',
            ],
            'debug': False,
        },
    },
]
{% endraw %}

ROOT_URLCONF = 'Settings.urls'

WSGI_APPLICATION = 'Settings.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Halifax'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/sitestatic/'
STATIC_ROOT = os.path.join(BASE_DIR, 'sitestatic')
STATICFILES_DIRS = (
    '/srv/modoboa/env/lib/python2.7/site-packages/modoboa/bower_components',
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Rest framework settings

{% raw %}
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
}
{% endraw %}

# Modoboa settings
#MODOBOA_CUSTOM_LOGO = os.path.join(MEDIA_URL, "custom_logo.png")

#DOVECOT_LOOKUP_PATH = ('/path/to/dovecot', )

MODOBOA_API_URL = 'https://api.modoboa.org/1/'

# django-passwords

PASSWORD_MIN_LENGTH = 8

{% raw %}
PASSWORD_COMPLEXITY = {
    "UPPER": 1,
    "LOWER": 1,
    "DIGITS": 1
}
{% endraw %}

# CKeditor

CKEDITOR_UPLOAD_PATH = "uploads/"

CKEDITOR_IMAGE_BACKEND = "pillow"

CKEDITOR_RESTRICT_BY_USER = True

CKEDITOR_BROWSE_SHOW_DIRS = True

CKEDITOR_ALLOW_NONIMAGE_FILES = False

{% raw %}
CKEDITOR_CONFIGS = {
    'default': {
        'allowedContent': True,
        'toolbar': 'Modoboa',
        'width': None,
        'toolbar_Modoboa': [
            ['Bold', 'Italic', 'Underline'],
            ['JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['BidiLtr', 'BidiRtl', 'Language'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent'],
            ['Undo', 'Redo'],
            ['Link', 'Unlink', 'Anchor', '-', 'Smiley'],
            ['TextColor', 'BGColor', '-', 'Source'],
            ['Font', 'FontSize'],
            ['Image', ],
            ['SpellChecker']
        ],
    },
}
{% endraw %}

# Logging configuration

{% raw %}
LOGGING = {
    'version': 1,
    'formatters': {
        'syslog': {
            'format': '%(name)s: %(levelname)s %(message)s'
        },
    },
    'handlers': {
        'syslog-auth': {
            'class': 'logging.handlers.SysLogHandler',
            'facility': SysLogHandler.LOG_AUTH,
            'formatter': 'syslog'
        },
        'modoboa': {
            'class': 'modoboa.core.loggers.SQLHandler',
        }
    },
    'loggers': {
        'modoboa.auth': {
            'handlers': ['syslog-auth', 'modoboa'],
            'level': 'INFO',
            'propagate': False
        },
        'modoboa.admin': {
            'handlers': ['modoboa'],
            'level': 'INFO',
            'propagate': False
        }
    }
}
{% endraw %}

from modoboa_amavis.settings import *

INSTALLED_APPS += MODOBOA_APPS

DATABASES = (
    'default': dict(
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '{{dbName}}',
        'USER': '{{dbUser}}',
        'PASSWORD': '{{ dbPasswordCommand.stdout }}',
        'HOST': '127.0.0.1',
        'PORT': '5432',
        'ATOMIC_REQUESTS': True,
    ),
    {% if amavis %}
    'amavis': dict(
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '{{amavis.dbName}}',
        'USER': '{{amavis.dbUser}}',
        'PASSWORD': '{{ amavis_dbPasswordCommand.stdout }}',
        'HOST': '127.0.0.1',
        'PORT': '5432',
        'ATOMIC_REQUESTS': True,
    ),
    {% endif %}
)
