"""
Django settings for vrms project.

Generated by 'django-admin startproject' using Django 4.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

import secretkeys

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = secretkeys.django_secret_key

KHALTI_API_KEY = secretkeys.khati_secret_key

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = ['testserver']
# ALLOWED_HOSTS=['127.0.0.1', '0.0.0.0']
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '0.0.0.0']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'base',
    'widget_tweaks',
    'tailwind',
    'theme',
    'django_browser_reload',
    'ckeditor'
    
]

TAILWIND_APP_NAME = 'theme'


INTERNAL_IPS = [
    "127.0.0.1",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django_browser_reload.middleware.BrowserReloadMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'vrms.urls'

# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.host.django.DjangoTemplates',
#         'DIRS': [os.path.join(BASE_DIR, 'templates')],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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


WSGI_APPLICATION = 'vrms.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.allowed.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.allowed.mysql',
#         'NAME': 'vrms',
#         'USER': 'root',
#         'PASSWORD': secretkeys.xamp_root_key,
#         'HOST': '127.0.0.1',
#         'PORT': '3306',
#     }
# }
# Server: sql5.freemysqlhosting.net
# Name: sql5698900
# Username: sql5698900
# Password: WJNp13d9lr
# Port number: 3306

# DATABASES = {
#     'default': {
#         # 'ENGINE': 'django.db.allowed.mysql',
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'vrms2',
#         'USER': 'root',
#         'PASSWORD': 'W7301@jqir#',
#         'HOST': '127.0.0.1',
#         'PORT': '3306',
#     }
# }

# Password: UZVUxmCPmdU
# sql302.infinityfree.com
# DB: if0_36366018_py
# User: if0_36366018


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        # 'ENGINE': 'mysql.connector.django',
        
        'NAME': 'databaseBS',
        'USER': 'admin',
        'PASSWORD': 'adminadmin',
        'HOST': 'datatbaseap.ct2a642y2s2b.us-west-1.rds.amazonaws.com',
        'PORT': '3306',  # Custom port for MySQL service
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'base/static')
]
LOGIN_URL = 'login'
# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

CKEDITOR_BASEPATH = "/static/ckeditor/ckeditor/"
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

NPM_BIN_PATH = "C:/Program Files/nodejs/npm.cmd"

from django.contrib.messages import constants as messages

MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}

EMAIL_BACKEND = 'django.core.mail.host.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'sakss.hi19@gmail.com'
EMAIL_HOST_PASSWORD = "nhgbejnvgkrkpndg"
EMAIL_PORT = 587


CKEDITOR_CONFIGS = {
    'awesome_ckeditor': {
        'toolbar': 'full',
        'height': 300,
        'width': 960,
    },
    'awesome_ckeditor2': {
        'toolbar': 'full',
        'height': 300,
        'width': 770,
    },
}
