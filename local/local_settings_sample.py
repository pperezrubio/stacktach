import logging
import os
import sys

#DEBUG=True
STACKTACH_INSTALL_DIR = '/usr/share/stacktach/'
STACKTACH_DEPLOYMENTS_FILE = '/etc/stacktach/stacktach_worker_config.json'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME':   '/var/lib/stacktach/stacktach.db',
        'USER':   '',
        'PASSWORD': '',
        'HOST': '',    # Set to empty string for localhost.
        'PORT': 0,    # Set to empty string for default.
    }
}
