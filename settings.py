"""
Django settings for cryptofolio project.

Generated by 'django-admin startproject' using Django 1.11.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SECRET_KEY = os.environ['SECRET_KEY']

DEBUG = False
ALLOWED_HOSTS = [
    # local testing
    '0.0.0.0',
    '127.0.0.1',
    'localhost',
    # production
    'cryptofolio.herokuapp.com'
]

# Application definition

STATICFILES_FINDERS = (
   'django.contrib.staticfiles.finders.FileSystemFinder',
   'django.contrib.staticfiles.finders.AppDirectoriesFinder',
   'djangobower.finders.BowerFinder',
)

INSTALLED_APPS = [
    'cryptofolio.apps.CryptofolioConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_nvd3',
    'djangobower',
    'encrypted_model_fields',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'cryptofolio/templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'wsgi.application'

# redirect to home after login
LOGIN_REDIRECT_URL = 'home'
LOGIN_URL = 'login'

# password reset email backend
EMAIL_BACKEND = 'sendgrid_backend.SendgridBackend'
DEFAULT_FROM_EMAIL = 'no-reply@cryptofol.io'
SERVER_EMAIL = 'system@cryptofol.io'
SENDGRID_API_KEY = os.environ['SENDGRID_API_KEY']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ['DB_NAME'],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASSWORD'],
        'HOST': os.environ['DB_HOST'],
        'PORT': os.environ['DB_PORT'],
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME':
        'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Europe/Zagreb'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS=(
    os.path.join(BASE_DIR, 'cryptofolio/static'),
)
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

BOWER_INSTALLED_APPS = (
    'd3#3.3.13',
    'nvd3#1.7.1',
    'popper.js#1.12.5',
    'jquery#3.2.1',
    'bootstrap#4.0.0-alpha.6',
)

BOWER_COMPONENTS_ROOT = os.path.join(BASE_DIR, 'components')
BOWER_PATH = '/usr/local/bin/bower'

FIELD_ENCRYPTION_KEY = os.environ['FIELD_ENCRYPTION_KEY']

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# ADMINS = (('msantl', 'msantl.ck@gmail.com'),)

