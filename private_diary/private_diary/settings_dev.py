from .settings_common import *
# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = 'x75pxr2oawo=(=)(y+j^kt5c46r%w!z$cipio9sq66))o+$f6r'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

LOGGING={
    'version':1,
    'disable_existing_loggers': False,
    'loggers':{
        'django':{
            'handlers': ['console'],
            'level': 'INFO',
        },
        'diary':{
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    },

    'handlers':{
        'console':{
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'dev'
        },
    },

    'formatters':{
        'dev':{
            'format': '\t'.join([
                '%(asctime)s',
                '[%(levelname)s]',
                '%(pathname)s(Line:%(lineno)d)',
                '%(message)s'
            ])
        },
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')