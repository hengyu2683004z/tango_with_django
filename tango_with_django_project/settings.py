"""
Django settings for tango_with_django_project project.

<<<<<<< HEAD
Generated by 'django-admin startproject' using Django 4.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-5ymayd6l#9e2ccl3ifz2ku53_^l*awbsiwy94^^wme=!j)!4ri'
=======
Generated by 'django-admin startproject' using Django 1.11.17.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_r+pl)kzm%e!0fnp#xu&ow+$gc^_8+=l2ql%7q-dm#cphlq59_'
>>>>>>> 8a1a396d807343e892f49a2fa7a604835b8f60d5

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rango'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'tango_with_django_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'tango_with_django_project.wsgi.application'


# Database
<<<<<<< HEAD
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
=======
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
>>>>>>> 8a1a396d807343e892f49a2fa7a604835b8f60d5

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
<<<<<<< HEAD
        'NAME': BASE_DIR / 'db.sqlite3',
=======
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
>>>>>>> 8a1a396d807343e892f49a2fa7a604835b8f60d5
    }
}


# Password validation
<<<<<<< HEAD
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators
=======
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators
>>>>>>> 8a1a396d807343e892f49a2fa7a604835b8f60d5

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
<<<<<<< HEAD
# https://docs.djangoproject.com/en/4.0/topics/i18n/
=======
# https://docs.djangoproject.com/en/1.11/topics/i18n/
>>>>>>> 8a1a396d807343e892f49a2fa7a604835b8f60d5

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

<<<<<<< HEAD
=======
USE_L10N = True

>>>>>>> 8a1a396d807343e892f49a2fa7a604835b8f60d5
USE_TZ = True


# Static files (CSS, JavaScript, Images)
<<<<<<< HEAD
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
=======
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
>>>>>>> 8a1a396d807343e892f49a2fa7a604835b8f60d5
