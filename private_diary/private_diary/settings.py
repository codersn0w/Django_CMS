from .settings_common import *
import os
# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = 'x75pxr2oawo=(=)(y+j^kt5c46r%w!z$cipio9sq66))o+$f6r'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [os.environ.get('ALLOWED_HOSTS')]

STATIC_ROOT = '/usr/share/nginx/html/static'
MEDIA_ROOT = '/usr/share/nginx/html/media'

AWS_SES_ACCESS_KEY_ID = os.environ.get('AWS_SES_ACCESS_KEY_ID')
AWS_SES_SECRET_ACCESS_KEY = os.environ.get('AWS_SES_SECRET_ACCESS_KEY')
EMAIL_BACKEND = 'django_ses.SESBackend'

LOGGING={
    'version':1,
    'disable_existing_loggers': False,
    'loggers':{
        'django':{
            'handlers': ['file'],
            'level': 'INFO',
        },
        'diary':{
            'handlers': ['file'],
            'level': 'INFO',
        },
    },

    'handlers':{
        'file':{
            'level': 'INFO',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/django.log'),
            'formatter': 'prod',
            'when': 'D',
            'interval': 1,
            'backupCount': 7,
        },
    },

    'formatters':{
        'prod':{
            'format': '\t'.join([
                '%(asctime)s',
                '[%(levelname)s]',
                '%(pathname)s(Line:%(lineno)d)',
                '%(message)s'
            ])
        },
    }
}
