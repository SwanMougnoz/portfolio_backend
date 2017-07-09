from portfolio_backend.settings.common import *

DEBUG = True

ALLOWED_HOSTS = [u'0.0.0.0']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'portfolio',
        'USER': 'portfolio',
        'PASSWORD': 'portfolio',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = os.path.join(BASE_DIR, 'var/emails')
