import os
from pathlib import Path
from dotenv import load_dotenv
from decouple import config

# Загружаем переменные из .env файла
load_dotenv()

# Базовая директория проекта
BASE_DIR = Path(__file__).resolve().parent.parent

# Безопасный ключ
SECRET_KEY = config('SECRET_KEY', default='your-secret-key')

# Режим отладки
DEBUG = config('DEBUG', default=True, cast=bool)

ALLOWED_HOSTS = []

# Приложения
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'catalog',  # Ваше приложение
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

ROOT_URLCONF = 'myproject.urls'  # Замените 'myproject' на имя вашей папки с urls.py

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # Оставьте пустым для app-specific шаблонов
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

WSGI_APPLICATION = 'myproject.wsgi.application'  # Замените 'myproject' на имя вашей папки с wsgi.py

# База данных
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
        'USER': config('POSTGRES_USER', default='myuser'),
        'PASSWORD': config('POSTGRES_PASSWORD', default='mypassword'),
        'HOST': config('DB_HOST', default='db'),  # 'db' для Docker, 'localhost' для локального
        'PORT': config('DB_PORT', default='5432'),
    }
}

# Пароли
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

# Локализация
LANGUAGE_CODE = 'ru-ru'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Статические файлы
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Media files (user-uploaded files)
MEDIA_URL = '/http://127.0.0.1:8000/media/image.jpg/'  # URL prefix for media files
MEDIA_ROOT = BASE_DIR / 'media'  # Directory where media files are stored (create this folder if it doesn't exist)

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Отладочный print (удалите после тестирования)
print("POSTGRES_DB:", os.environ.get('POSTGRES_DB'))
print("Env loaded:", load_dotenv())



