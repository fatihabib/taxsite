import os
from pathlib import Path

# ------------------------------
# Base Directory
# ------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# ------------------------------
# Secret Key
# ------------------------------
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "replace-this-with-a-random-key")

# ------------------------------
# Debug & Allowed Hosts
# ------------------------------
DEBUG = os.environ.get("DJANGO_DEBUG", "False") == "True"
ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS", "*").split(",")

# ------------------------------
# Installed Apps
# ------------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'siteapp',
]

# ------------------------------
# Middleware
# ------------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # serve static files in production
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ------------------------------
# URL Configuration
# ------------------------------
ROOT_URLCONF = 'taxsite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'siteapp' / 'templates'],
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

WSGI_APPLICATION = 'taxsite.wsgi.application'

# ------------------------------
# Database
if os.environ.get("DATABASE_URL"):
    import importlib

    dj_database_url = importlib.import_module("dj_database_url")
    DATABASES = {
        "default": dj_database_url.config(conn_max_age=600, ssl_require=True)
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

# ------------------------------
# Password Validation
# ------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ------------------------------
# Internationalization
# ------------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Africa/Lagos'
USE_I18N = True
USE_TZ = True

# ------------------------------
# Static Files
# ------------------------------
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / "staticfiles"  # for production
STATICFILES_DIRS = [BASE_DIR / "static"]  # optional local static files
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
# settings.py

# ------------------------------
# Media Files
# ------------------------------
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# ------------------------------
# Default Primary Key
# ------------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
