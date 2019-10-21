"""
Django settings for valhalla project.

Generated by 'django-admin startproject' using Django 2.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TRUE_LIST = ('true', 'True', 'TRUE', '1')

PRINT_ENVS = os.getenv('PRINT_ENVS', 'false') in TRUE_LIST
PRINT_ENVS_ONLY = os.getenv('PRINT_ENVS_ONLY', 'false') in TRUE_LIST

def getenv(var, default):
    env = os.getenv(var, default)
    if PRINT_ENVS:
        if PRINT_ENVS_ONLY:
            if env != default:
                print('{var}={value}'.format(var=var, value=env))
        else:
            print('{var}={value}'.format(var=var, value=env))
    return env

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'b_d*xx*i(+m@@(2fkag@x+87xgpzjzferh&38gpvrgabpqk-=e'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

DEFAULT_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'active_link',
    'rest_framework',
    'rest_framework.authtoken',
]

PROJECT_APPS = [
    'dashboard.apps.DashboardConfig',
    'api.apps.ApiConfig',
]

INSTALLED_APPS = DEFAULT_APPS + THIRD_PARTY_APPS + PROJECT_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'crowdrest.backend.CrowdRestBackend'
)

# Crowd configuration
AUTH_CROWD_ALWAYS_UPDATE_USER = getenv('AUTH_CROWD_ALWAYS_UPDATE_USER', 'true') in TRUE_LIST
AUTH_CROWD_ALWAYS_UPDATE_GROUPS = getenv('AUTH_CROWD_ALWAYS_UPDATE_GROUPS', 'true') in TRUE_LIST
AUTH_CROWD_CREATE_GROUPS = getenv('AUTH_CROWD_CREATE_GROUPS', 'true') in TRUE_LIST
AUTH_CROWD_STAFF_GROUP = getenv('AUTH_CROWD_STAFF_GROUP', 'ongoing')
AUTH_CROWD_SUPERUSER_GROUP = getenv('AUTH_CROWD_SUPERUSER_GROUP', 'ongoing-admin')
AUTH_CROWD_APPLICATION_USER = getenv('AUTH_CROWD_APPLICATION_USER', 'atlas-api')
AUTH_CROWD_APPLICATION_PASSWORD = getenv('AUTH_CROWD_APPLICATION_PASSWORD', 'atlas')
AUTH_CROWD_SERVER_REST_URI = getenv('AUTH_CROWD_SERVER_REST_URI', 'http://crowd.b2w')

ROOT_URLCONF = 'valhalla.urls'

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
                'dashboard.processors.profile',
            ],
        },
    },
]

WSGI_APPLICATION = 'valhalla.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'pt_BR'

TIME_ZONE = 'America/Sao_Paulo'

DATETIME_FORMAT = 'd/m/y H:i:s'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Log Configuration

LOG_DIR = getenv('APPLICATION_LOG_DIR', BASE_DIR)
LOG_HANDLER = 'console'
LOG_LEVEL = getenv('APPLICATION_LOG_LEVEL', 'DEBUG')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'crowdrest': {
            'handlers': [LOG_HANDLER, ],
            'level': LOG_LEVEL,
        },
    }
}

#  Rest Framework

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    )
}