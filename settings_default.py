from os import path

# Set PROJECT_ROOT to the dir of the current file
PROJECT_ROOT = path.dirname(__file__)

# DJANGO_PROJECT: the short project name
# (defaults to the basename of PROJECT_ROOT)
DJANGO_PROJECT = path.basename(PROJECT_ROOT.rstrip('/'))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = path.join(PROJECT_ROOT, 'static', 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/static/media/'

# staticfiles
STATIC_ROOT = path.join(PROJECT_ROOT, 'static', 'apps')
STATIC_URL = '/static/apps/'
STATICFILES_DIRS = [
    ('global', path.join(PROJECT_ROOT, 'static', 'global')),
]

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

MIDDLEWARE_CLASSES = [
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

TEMPLATE_CONTEXT_PROCESSORS = [
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.core.context_processors.static',
    # 'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
]

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    path.join(PROJECT_ROOT, 'templates')
)


INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.staticfiles',
    'django_extensions',
    'debug_toolbar',
    'raven.contrib.django',
    'south',
    'djcelery',
    'devserver',
    'sorl.thumbnail'
]


# App-specific settings
""" django-celery """
import djcelery
djcelery.setup_loader()


""" django-devserver """
DEVSERVER_MODULES = (
    # 'devserver.modules.sql.SQLRealTimeModule',
    'devserver.modules.sql.SQLSummaryModule',
    'devserver.modules.profile.ProfileSummaryModule',

    # Modules not enabled by default
    # 'devserver.modules.ajax.AjaxDumpModule',
    # 'devserver.modules.profile.MemoryUseModule',
    # 'devserver.modules.cache.CacheSummaryModule',
    # 'devserver.modules.profile.LineProfilerModule',
)

# DEVSERVER_TRUNCATE_SQL = False


""" sorl-thumbnail """
# This makes a huge difference in image serving performance
THUMBNAIL_QUALITY = 85

# To use redis, uncomment
# THUMBNAIL_KVSTORE = 'sorl.thumbnail.kvstores.redis_kvstore.KVStore'
# THUMBNAIL_REDIS_DB etc. (see docs)

# To use GraphicsMagic (better quality, performance, memory management) instead, uncomment
# THUMBNAIL_ENGINE = 'sorl.thumbnail.engines.convert_engine.Engine'
# Uncomment below to use the superior GraphicsMagick (make sure you install it!)
# THUMBNAIL_CONVERT = 'gm convert'
