from .defaultSettings import *

ALLOWED_HOSTS += ['{{ domain }}', ]
DEBUG="{{debug | default('False')}}"

MODOBOA_APPS += [
    {% for app in modoboa_apps %}
        {# If app is a list, use 0 for requirements and 1 for installed name #}
        {% if type(app) is str %}
    "{{app|replace('-','_')}}",
        {% else %}
    "{{app[1]}}",
        {% endif %}
    {% endfor %}
]

INSTALLED_APPS += MODOBOA_APPS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '{{dbName}}',
        'USER': '{{dbUser}}',
        'PASSWORD': '{{ dbPasswordCommand.stdout }}',
        'HOST': '127.0.0.1',
        'PORT': '5432',
        'ATOMIC_REQUESTS': True,
    },
    {% if amavis % }
    'amavis': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '{{amavis.dbName}}',
        'USER': '{{amavis.dbUser}}',
        'PASSWORD': '{{ amavis.dbPasswordCommand.stdout }}',
        'HOST': '127.0.0.1',
        'PORT': '5432',
        'ATOMIC_REQUESTS': True,
    },
    {% endif %}
}

