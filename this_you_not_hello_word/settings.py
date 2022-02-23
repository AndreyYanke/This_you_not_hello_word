import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent



# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-mni!%gcsua^8ld4te7kr5gn5e!!c5rc36heiqj3k^(zkqh57b4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_filters',
    'django_extensions',

    'userapp.apps.UserappConfig',
    'vacancyapp.apps.VacancyappConfig',
    'mainapp.apps.MainappConfig',
    'newsapp.apps.NewsappConfig',
    'resumeapp.apps.ResumeappConfig',
    'flower',
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

ROOT_URLCONF = 'this_you_not_hello_word.urls'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.AllowAllUsersModelBackend',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'this_you_not_hello_word.wsgi.application'


# Database

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation


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

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'ru-Ru'

TIME_ZONE = 'Europe/Istanbul'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'

# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, "static"),
# )

STATIC_ROOT = os.path.join(BASE_DIR,'static')

# Default primary key field type

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'userapp.User'

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
LOGIN_URL = '/user/auth/'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


#celery

#smtp
# https://myaccount.google.com/u/1/security?hl=ru
#Ненадежные приложения, у которых есть доступ к аккаунту True
# https://mail.google.com/mail/u/1/#settings/fwdandpop = Включить IMAP True
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'django.celery.redis@gmail.com'
EMAIL_HOST_PASSWORD = 'Qwert123$'


#REDIS related setting
REDIS_HOST = '0.0.0.0'
REDIS_PORT = '6379'
REDIS_URL = f'redis://{REDIS_HOST}:{REDIS_PORT}/0'
CELERY_BROKER_URL =REDIS_URL
CELERY_BROKER_TRANSPORT_OPTIONS ={'visibility_timeout':3600}#таймаут
CELERY_RESULT_BACKEND =REDIS_URL
CELERY_ACCEPT_CONTENT = ['application/json']#заголовки
CELERY_TASK_SERIALIZER = 'json'#задачи в каком формате
CELERY_RESULT_SERIALIZER = 'json'#получаем результат в какком формате

