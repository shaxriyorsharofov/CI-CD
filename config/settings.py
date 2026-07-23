"""Django blog loyihasining asosiy sozlamalari.

Ushbu faylda loyiha ma'lumotlar bazasi, ulangan ilovalar, shablonlar,
xavfsizlik kalitlari hamda statik fayllar sozlamalari joylashgan.
"""
import os
from pathlib import Path

# Loyihaning ildiz papkasi yo'li (BASE_DIR)
BASE_DIR = Path(__file__).resolve().parent.parent

# Xavfsizlik kaliti (production'da atrof-muhit o'zgaruvchisidan olinadi)
SECRET_KEY = os.environ.get(
    'SECRET_KEY',
    'django-insecure-default-key-change-in-production-1234567890'
)

# Debug rejimi (production'da False bo'lishi kerak)
DEBUG = os.environ.get('DEBUG', 'True') == 'True'

ALLOWED_HOSTS = ['*']

# O'rnatilgan Django ilovalari
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Bizning ilova
    'blog.apps.BlogConfig',
]

# Oraliq dasturlar (Middleware)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

# Shablonlar (HTML templates) sozlamasi
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

# Ma'lumotlar bazasi sozlamalari (Standart SQLite3)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Parol murakkabligini tekshirish
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

# Til va vaqt mintaqasi sozlamalari
LANGUAGE_CODE = 'uz-uz'

TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True

USE_TZ = True

# Statik fayllar (CSS, JavaScript, rasmlar)
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
