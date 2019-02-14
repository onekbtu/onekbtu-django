import os
from datetime import timedelta
from types import MappingProxyType

import environ
from corsheaders.defaults import default_headers, default_methods

env = environ.Env(
    DEBUG=(bool, True),
    SECRET_KEY=(str, 'ee9a4958-1881-4e2f-97bc-e347562ddb58'),
    DATABASE_URL=(str, 'psql://admin:pass@db:5432/onekbtu')
)

environ.Env.read_env()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = env('SECRET_KEY')

DEBUG = env('DEBUG')

ALLOWED_HOSTS = ('*',)

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'corsheaders',

    'authentication',
    'blog'
)

MIDDLEWARE = (
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware'
)

ROOT_URLCONF = 'core.urls'

TEMPLATES = (
    MappingProxyType(
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': (),
            'APP_DIRS': True,
            'OPTIONS': MappingProxyType(
                {
                    'context_processors': (
                        'django.template.context_processors.debug',
                        'django.template.context_processors.request',
                        'django.contrib.auth.context_processors.auth',
                        'django.contrib.messages.context_processors.messages',
                    )
                }
            ),
        }
    ),
)

WSGI_APPLICATION = 'core.wsgi.application'

DATABASES = MappingProxyType(
    {
        'default': env.db()
    }
)

AUTH_PASSWORD_VALIDATORS = (
    MappingProxyType(
        {
            'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'
        }
    ),
    MappingProxyType(
        {
            'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'
        }
    ),
    MappingProxyType(
        {
            'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'
        }
    ),
    MappingProxyType(
        {
            'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'
        }
    ),
)

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

REST_FRAMEWORK = MappingProxyType(
    {
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        ),
        'DEFAULT_PERMISSION_CLASSES': (
            'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
        ),
        'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
        'PAGE_SIZE': 20
    }
)

CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_METHODS = default_methods

CORS_ALLOW_HEADERS = default_headers

CORS_ALLOW_CREDENTIALS = True

JWT_AUTH = MappingProxyType(
    {
        'JWT_AUTH_HEADER_PREFIX': 'JWT',

        'JWT_ENCODE_HANDLER': 'rest_framework_jwt.utils.jwt_encode_handler',

        'JWT_DECODE_HANDLER': 'rest_framework_jwt.utils.jwt_decode_handler',

        'JWT_PAYLOAD_HANDLER': 'rest_framework_jwt.utils.jwt_payload_handler',

        'JWT_PAYLOAD_GET_USER_ID_HANDLER': 'rest_framework_jwt.utils.jwt_get_user_id_from_payload_handler',

        'JWT_RESPONSE_PAYLOAD_HANDLER': 'rest_framework_jwt.utils.jwt_response_payload_handler',

        'JWT_ALLOW_REFRESH': False,

        'JWT_EXPIRATION_DELTA': timedelta(weeks=5215),

        'JWT_REFRESH_EXPIRATION_DELTA': timedelta(weeks=5215)
    }
)
