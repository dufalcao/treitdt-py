"""
Django settings for ptiAreas project.

Generated by 'django-admin startproject' using Django 3.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
### Alterado
### from pathlib import Path

### Importar o decouple e dj_database_url
import os

from decouple import config, Csv
from dj_database_url import parse as db_url


# Build paths inside the project like this: BASE_DIR / 'subdir'.
### Alterado
### BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
### Apagar a SECRET_KEY pq já está no arquivo de conf .env
# SECRET_KEY = 'django-insecure-2wwsf08&$84_1+#-)lthh2d1mvw0-+n30(f6zr%4(wf3z-@u*a'
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
### Alterado e colocado no .env 
# DEBUG = True
DEBUG = config('DEBUG', default=False, cast=bool)

### Alterado e colocado no .env
# ALLOWED_HOSTS =[]
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default=[], cast=Csv())

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    ### django-gis
    'django.contrib.gis',

    ### Outras apps
    'leaflet',
    'djgeojson',

    ### meus apps
    'core',
    'area',
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

ROOT_URLCONF = 'ptiAreas.urls'

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

WSGI_APPLICATION = 'ptiAreas.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

### Foi configurado no .env
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': config('DATABASE_URL', cast=db_url)
}
DATABASES['default']['ENGINE'] = 'django.contrib.gis.db.backends.postgis'


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
### Incluir o caminho dos arquivos statics
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/img/' #endereço para acessar os arquivos

STATICFILES_DIRS =[
    os.path.join(BASE_DIR, 'static'),
]

MEDIA_ROOT = os.path.join(BASE_DIR, "static/img") #pasta media para abrigar os arquivos dos usuários

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

### DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


### Configuração do Leaflet para colocar o retangulo envovente e alterar o mapa
LEAFLET_CONFIG = {
    'SPATIAL_EXTENT': (
        -54.59805445490457, -25.4343113008193, 
        -54.594507506326565, -25.439069876315845, 
    ),
    'TILES': [('GStreets', 'http://www.google.cn/maps/vt?lyrs=m@189&gl=cn&x={x}&y={y}&z={z}',
               {'attribution': '&copy; Google'}),
              ('GSatellite',
               'http://www.google.cn/maps/vt?lyrs=s@189&gl=cn&x={x}&y={y}&z={z}',
               {'attribution': '&copy; Google'})]
}
