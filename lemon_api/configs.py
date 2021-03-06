import os
from pathlib import Path
import environ

BASE_DIR = Path(__file__).resolve().parent.parent

environment = environ.Env(
    SECRET_KEY=(str, 'key'),
    ENVIRONMENT=(str, 'local'),
    DB_NAME=(str, 'iguzman'),
    DB_USER=(str, 'iguzman'),
    DB_PASSWORD=(str, 'iguzman'),
    EMAIL_HOST_USER=(str, 'john@doe.com'),
    EMAIL_HOST_PASSWORD=(str, 'password')
)

SERVER_APP_FOLDER_NAME = 'lemon-api'

environ.Env.read_env()


SECRET_KEY = environment('SECRET_KEY')
ENVIRONMENT = environment('ENVIRONMENT')
DB_NAME = environment('DB_NAME')
DB_USER = environment('DB_USER')
DB_PASSWORD = environment('DB_PASSWORD')
EMAIL_HOST_USER = environment('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = environment('EMAIL_HOST_PASSWORD')


class Common:
    SECRET_KEY = SECRET_KEY
    SITE_HEADER = 'Limon News'
    INDEX_TITLE = 'CMS'
    SITE_TITLE = 'CMS'
    API_DNS = 'http://127.0.0.1:8000/'
    API_URL = '{}v1/'.format(API_DNS)
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_USE_TLS = True
    EMAIL_PORT = 587
    DEBUG = True
    ALLOWED_HOSTS = ['*']
    JWT_ACCESS_EXPIRATION_MINUTES = 300
    JWT_REFRESH_EXPIRATION_MINUTES = 600
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': DB_NAME,
            'USER': DB_USER,
            'PASSWORD': DB_PASSWORD,
            'HOST': '127.0.0.1',
            'PORT': '5432'
        }
    }
    EMAIL_HOST_USER = EMAIL_HOST_USER
    EMAIL_HOST_PASSWORD = EMAIL_HOST_PASSWORD
    ENVIRONMENT = ENVIRONMENT


class LOCAL(Common):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
        }
    }
    WEB_APP_URL = 'http://127.0.0.1:3000/'
    MEDIA_ROOT=os.path.join(BASE_DIR, 'media')


class STAGING(Common):
    API_DNS = 'https://api.limon.iguzman.com.mx/'
    WEB_APP_URL = 'https://limon.iguzman.com.mx/'
    MEDIA_ROOT='/var/www/static/staging/{}/media'.format(SERVER_APP_FOLDER_NAME)

class MASTER(Common):
    DEBUG = False
    JWT_ACCESS_EXPIRATION_MINUTES = 15
    JWT_REFRESH_EXPIRATION_MINUTES = 30
    API_DNS = 'https://api.limon.news/'
    WEB_APP_URL = 'https://www.limon.news/'
    MEDIA_ROOT='/var/www/static/master/{}/media'.format(SERVER_APP_FOLDER_NAME)

if ENVIRONMENT == 'staging':
    env = STAGING
elif ENVIRONMENT == 'master':
    env = MASTER
else:
    env = LOCAL
