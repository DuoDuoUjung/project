from pathlib import Path
import os
import sys

# 基本設置
BASE_DIR = str(Path(__file__).resolve().parent.parent)
SECRET_KEY = 'your-secret-key'
DEBUG = True
ALLOWED_HOSTS = []

# 已安裝應用程式
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'friends_app',  # 新增的好友應用程式
    'other_app',# 暫放課程用的
    'teach_app',
    'test_app',
]

# 中介軟體
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Django-project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # 確認這裡包含 templates 資料夾
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

WSGI_APPLICATION = 'Django-project.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# settings.py
AUTH_USER_MODEL = 'friends_app.CustomUser'


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

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'debug.log',
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


LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),  # 確保這一行指向你的 static 資料夾
]
LOGIN_REDIRECT_URL = '/friends/'


# 在 settings.py 中設置
STATIC_URL = '/static/'
MEDIA_URL = '/media/'  # 媒體文件在 URL 中的訪問路徑
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # 媒體文件的實際存放路徑

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FLASK_SERVICE_DIR = os.path.join(BASE_DIR, '../Flask_service')
sys.path.append(FLASK_SERVICE_DIR)