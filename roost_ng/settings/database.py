import os

from . import config, paths

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# local sqlite database for dev
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(paths.BASE_DIR, 'db.sqlite3'),
    }
}

# database settings from config; may override above definition.
if 'databases' in config.config:
    DATABASES.update(config.config['databases'])
