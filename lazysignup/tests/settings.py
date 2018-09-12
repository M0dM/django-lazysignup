import os

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}

INSTALLED_APPS = (
    'lazysignup',
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',
)

SITE_ID = 1

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "lazysignup.backends.LazySignupBackend",
)

MIDDLEWARE_CLASSES = [
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.auth.middleware.SessionAuthenticationMiddleware",
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                "django.template.context_processors.i18n",
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                "django.template.context_processors.tz",
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

LAZYSIGNUP_USER_AGENT_BLACKLIST = [
    "^search",
]

LAZYSIGNUP_USER_MODEL = 'auth.User'
AUTH_USER_MODEL = 'auth.User'

SECRET_KEY = 'non-empty-key'
DEBUG = True

STATIC_URL = '/static/'
ALLOWED_HOSTS = [
    'testserver'
]
