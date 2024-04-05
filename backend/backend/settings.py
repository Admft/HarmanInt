# Import necessary modules and packages
from pathlib import Path  # Used for working with file paths
from datetime import timedelta  # Used for defining timedelta objects
from dotenv import load_dotenv  # Used for loading environment variables
import os  # Used for accessing operating system functionalities

# Load environment variables from .env file
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent  # Base directory of the Django project

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-2tzf6%mvq(xpuvibq=bj(9@!o^k1_5nw(cdjtdywi^a^j-s5o('  # Secret key for Django project

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True  # Enable debug mode for development

ALLOWED_HOSTS = ["*"]  # List of allowed hosts for the Django project

# Django REST Framework settings
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",  # JWT authentication for accessing API endpoints
    ),
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",  # Default permission class - requires authenticated user for all endpoints
    ],
}

# Simple JWT settings
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=100),  # Lifetime of access token
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),  # Lifetime of refresh token
}

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',  # Django admin app
    'django.contrib.auth',  # Django authentication app
    'django.contrib.contenttypes',  # Django content types app
    'django.contrib.sessions',  # Django sessions app
    'django.contrib.messages',  # Django messages app
    'django.contrib.staticfiles',  # Django static files app
    "api",  # Custom app for API
    "rest_framework",  # Django REST Framework
    "corsheaders"  # CORS headers support
]

# Middleware classes
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',  # Security middleware
    'django.contrib.sessions.middleware.SessionMiddleware',  # Sessions middleware
    'django.middleware.common.CommonMiddleware',  # Common middleware
    'django.middleware.csrf.CsrfViewMiddleware',  # CSRF middleware
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Authentication middleware
    'django.contrib.messages.middleware.MessageMiddleware',  # Messages middleware
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # Clickjacking middleware
    "corsheaders.middleware.CorsMiddleware",  # CORS middleware
]

ROOT_URLCONF = 'backend.urls'  # Root URL configuration

# Template settings
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

WSGI_APPLICATION = 'backend.wsgi.application'  # WSGI application configuration

# Database configuration
DATABASES = {
    'default': {
        "ENGINE": 'django.db.backends.postgresql',  # SQLite database engine
        "NAME": os.getenv("DB_NAME"),  # Database name
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PWD"),
        "HOST": os.getenv("DB_HOST"),
        "PORT": os.getenv("DB_PORT"),
    }
}

# Password validation settings
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',  # Similarity validator
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',  # Minimum length validator
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',  # Common password validator
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',  # Numeric password validator
    },
]

# Internationalization settings
LANGUAGE_CODE = 'en-us'  # Language code
TIME_ZONE = 'UTC'  # Time zone
USE_I18N = True  # Enable internationalization
USE_TZ = True  # Use timezone

# Static files settings
STATIC_URL = 'static/'  # URL prefix for static files

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'  # Default auto field type

# CORS settings
CORS_ALLOW_ALL_ORIGINS = True  # Allow all origins
CORS_ALLOWS_CREDENTIALS = True  # Allow credentials
