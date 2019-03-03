import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
AWS_S3_ACCESS_KEY_ID='AKIAITGWJK6BWS4WJ4FA' 
AWS_S3_SECRET_ACCESS_KEY='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'
# AWS_S3_SECURE_URLS = False       
# AWS_QUERYSTRING_AUTH = False 
STATIC_ROOT = 'static'
STATIC_URL = 'https://s3.ap-south-1.amazonaws.com/oryxrating/static/'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
MEIDA_ROOT = 'media'
MEDIA_URL = 'https://s3.ap-south-1.amazonaws.com/oryxrating/media/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# STATIC_URL = '/static/'
# MEDIA_URL = '/media/'



SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 's3euaut-0%)(o#dz+v_p2ro*x!%+)pk&%-epkvmo2ts=q7kyb_')

DEBUG = True

SECURE_CONTENT_TYPE_NOSNIFF = True

SECURE_BROWSER_XSS_FILTER = True

SECURE_SSL_REDIRECT = True

SESSION_COOKIE_SECURE = True

CSRF_COOKIE_SECURE = True

ALLOWED_HOSTS = [
    '127.0.0.1',
    'oryxrating.herokuapp.com',
]


# Heroku: Update database configuration from $DATABASE_URL.
import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES = {'default': dj_database_url.config(conn_max_age=500)}
DATABASES['default'].update(db_from_env)



INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'productapi',
    'signup',
    'login',
    'profiles',
    'home',
    'storages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Oryx.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR,],
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

WSGI_APPLICATION = 'Oryx.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         # 'NAME': os.path.join(BASE_DIR, 'OryxDB'),
#         'NAME': 'oryxdb',
#         'USER' : 'root',
#         'PASSWORD': '#@Ineedaxessmysql12@#',
#         'HOST': '127.0.0.1',
#         'PORT': '3306',
#     }
# }


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

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
    ]
}


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_URL = '/media/'


# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES = {'default': dj_database_url.config(conn_max_age=500)}
DATABASES['default'].update(db_from_env)