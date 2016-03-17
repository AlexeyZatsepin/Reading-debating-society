"""
Django settings for Reading debating society project.

Generated by 'django-admin startproject' using Django 1.9.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'd0$qg)yr@)4ni@b6lkfmku!*x2as&7*d&-pdx+g^)t8qdnx*&k'

# SECURITY WARNING: don't run with debug turned on in production!

ALLOWED_HOSTS = []

ON_OPENSHIFT = False
if 'OPENSHIFT_REPO_DIR' in os.environ:
    ON_OPENSHIFT = True

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
    'community',
    'gallery',
    'materials',
    'staticArticles',
    'googlecharts',
    'widget_tweaks',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATE_DIRS = (os.path.join(BASE_DIR, 'templates'),)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'config.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
if ON_OPENSHIFT:
    DEBUG = True
    TEMPLATE_DEBUG = False
    ALLOWED_HOSTS = ['*']
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'new',
            'USER': os.getenv('OPENSHIFT_MYSQL_DB_USERNAME'),
            'PASSWORD': os.getenv('OPENSHIFT_MYSQL_DB_PASSWORD'),
            'HOST': os.getenv('OPENSHIFT_MYSQL_DB_HOST'),
            'PORT': os.getenv('OPENSHIFT_MYSQL_DB_PORT'),
        }
    }
else:
    DEBUG = True
    TEMPLATE_DEBUG = True
    ALLOWED_HOSTS = []
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
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

# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/static/media/'
STATIC_ROOT = os.path.join(BASE_DIR, 'wsgi', 'static')
#MEDIA_ROOT = os.path.join(BASE_DIR, 'wsgi', 'static', 'media')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
MEDIA_ROOT = os.environ.get('OPENSHIFT_REPO_DIR')+'/wsgi/static/media'
#MEDIA_ROOT = os.environ.get('OPENSHIFT_DATA_DIR', '')