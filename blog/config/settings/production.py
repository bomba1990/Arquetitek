import dj_database_url

from .base import *

DEBUG = False

COMPRESS_ENABLED = True

COMPRESS_OFFLINE = True

DATABASES = {'default': dj_database_url.config(conn_max_age=600)}
