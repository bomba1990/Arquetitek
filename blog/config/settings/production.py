import dj_database_url
import raven

from .base import *

DEBUG = False

COMPRESS_ENABLED = True

COMPRESS_OFFLINE = True

DATABASES = {'default': dj_database_url.config(conn_max_age=600)}


ALLOWED_HOSTS = ['192.168.2.169',"arquetitek.com"]

INSTALLED_APPS += (
    'raven.contrib.django.raven_compat',
)

RAVEN_CONFIG = {
    'dsn': 'https://f6a5164b658843d4991a513d395986bc:96c5bb69788d463a835f56a6038a431e@sentry.io/218182',
    # If you are using git, you can also automatically configure the
    # release based on the git info.
    'release': raven.fetch_git_sha(os.path.dirname(BASE_DIR)),
}