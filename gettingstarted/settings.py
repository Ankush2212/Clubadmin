"""
Django settings for gettingstarted project.

Generated by 'django-admin startproject' using Django 2.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import django_heroku
import dj_database_url


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'CHANGE_ME!!!! (P.S. the SECRET_KEY environment variable will be used, if set, instead).'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS =  ['stark-dusk-77176.herokuapp.com', '.herokuapp.com']
ALLOWED_HOSTS =  ['*']



# Application definition
#,  'anymail'
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'hello',
	 'intercom'
]
PREPEND_WWW = True
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

INTERCOM_APPID = "bb2tjtrb"
#INTERCOM_SECURE_KEY = "your security_code"
ROOT_URLCONF = 'gettingstarted.urls'

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

WSGI_APPLICATION = 'gettingstarted.wsgi.application'

# DATABASES = {
    # 'default': {
        # 'ENGINE': 'django.db.backends.postgresql_psycopg2',
		# 'NAME': os.path.join('test'),
    # },
   # 'OPTIONS': {
        # 'timeout': 50,
    # }
# }

# DATABASES = {
 
 # 'default': {
        # 'ENGINE': 'django.db.backends.postgresql_psycopg2',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        # 'NAME': 'test',  # Or path to database file if using sqlite3.
        # 'USER': 'postgres',  # Not used with sqlite3.
        # 'PASSWORD': '',  # Not used with sqlite3.
        # 'HOST': '',  # Set to empty string for localhost. Not used with sqlite3.
        # 'PORT': '',  # Set to empty string for default. Not used with sqlite3. 
 # }

# }

DATABASES = {
    'default': dj_database_url.config()
}

db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(db_from_env)
DATABASES['default'] =  dj_database_url.config()
DATABASES['default']['ENGINE'] = 'django.db.backends.postgresql_psycopg2'
DATABASES['default']['NAME'] = 'test'
#DATABASES['default']['CONN_MAX_AGE'] = 500
# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

# DATABASES = {
    # 'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # },
   # 'OPTIONS': {
        # 'timeout': 50,
    # }
# }

# # add this

# db_from_env = dj_database_url.config()
# DATABASES['default'].update(db_from_env)
# #DATABASES['default']['ENGINE'] = 'django.db.backends.postgresql_psycopg2'
# DATABASES['default']['CONN_MAX_AGE'] = 500
# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators
# Honor the 'X-Forwarded-Proto' header for request.is_secure() 
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'
# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)
django_heroku.settings(locals())
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(PROJECT_ROOT, 'hello.log'),
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
             'propagate': True,
         },
     },
 }






MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')
MEDIA_URL = '/media/'





EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 465
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
# #smtp changes
# EMAIL_BACKEND = 'django_smtp_ssl.SSLEmailBackend'
# MAILER_EMAIL_BACKEND = EMAIL_BACKEND
# EMAIL_BACKEND = 'django_mailgun.MailgunBackend'
# MAILGUN_ACCESS_KEY = 'key-72442c5f7222d9e4ee790c61b0da37ba'
# MAILGUN_SERVER_NAME = 'sandbox8d00a0060a5c4befbd280ae759883df7.mailgun.org'

# ANYMAIL = {
    # # (exact settings here depend on your ESP...)
    # "MAILGUN_API_KEY": 'key-72442c5f7222d9e4ee790c61b0da37ba',
    # "MAILGUN_SENDER_DOMAIN": ' sandbox8d00a0060a5c4befbd280ae759883df7.mailgun.org',  # your Mailgun domain, if needed
# }
# EMAIL_BACKEND = "anymail.backends.mailgun.EmailBackend"  # or sendgrid.EmailBackend, or...
# DEFAULT_FROM_EMAIL = "kalpana@codenomad.net"  # if you don't already have this in settings