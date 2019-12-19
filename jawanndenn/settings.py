"""
Django settings for jawanndenn project.

Generated by 'django-admin startproject' using Django 2.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import copy
import os

from django.utils.log import DEFAULT_LOGGING
from jawanndenn import DEFAULT_MAX_POLLS, DEFAULT_MAX_VOTES_PER_POLL

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['JAWANNDENN_SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('JAWANNDENN_DEBUG', 'False') == 'True'

ALLOWED_HOSTS = os.environ.get('JAWANNDENN_ALLOWED_HOSTS', ','.join([
    '127.0.0.1',
    '0.0.0.0',
    'localhost',
])).split(',')

_USE_POSTGRES = 'JAWANNDENN_SQLITE_FILE' not in os.environ


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'jawanndenn',
]

if _USE_POSTGRES:
    INSTALLED_APPS += [
        'django_probes',  # management command "wait_for_database"
    ]

MIDDLEWARE = [
    'jawanndenn.middleware.set_remote_addr_to_x_forwarded_for',

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'jawanndenn.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'jawanndenn', 'static'),
        ],
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

WSGI_APPLICATION = 'jawanndenn.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

if _USE_POSTGRES:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ['JAWANNDENN_POSTGRES_NAME'],
            'USER': os.environ['JAWANNDENN_POSTGRES_USER'],
            'PASSWORD': os.environ['JAWANNDENN_POSTGRES_PASSWORD'],
            'HOST': os.environ['JAWANNDENN_POSTGRES_HOST'],
            'PORT': os.environ['JAWANNDENN_POSTGRES_PORT'],
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.environ['JAWANNDENN_SQLITE_FILE'],
        }
    }


# Logging
# https://docs.djangoproject.com/en/2.2/ref/settings/#std:setting-LOGGING

LOGGING = copy.copy(DEFAULT_LOGGING)
LOGGING['handlers']['console']['filters'].remove('require_debug_true')
if not DEBUG:
    LOGGING['handlers']['console']['level'] = 'ERROR'


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',  # noqa: E501
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',  # noqa: E501
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',  # noqa: E501
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',  # noqa: E501
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Settings specific to jawanndenn

JAWANNDENN_URL_PREFIX = os.environ.get('JAWANNDENN_URL_PREFIX', '').strip('/')

if JAWANNDENN_URL_PREFIX != '':
    JAWANNDENN_URL_PREFIX = '/' + JAWANNDENN_URL_PREFIX

JAWANNDENN_MAX_POLLS = int(os.environ.get(
    'JAWANNDENN_MAX_POLLS', str(DEFAULT_MAX_POLLS)))
JAWANNDENN_MAX_VOTES_PER_POLL = int(os.environ.get(
    'JAWANNDENN_MAX_VOTES_PER_POLL', str(DEFAULT_MAX_VOTES_PER_POLL)))


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = JAWANNDENN_URL_PREFIX + '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'jawanndenn', 'static'),
]
