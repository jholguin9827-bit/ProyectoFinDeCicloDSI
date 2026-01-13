from pathlib import Path
import os
import dj_database_url  # Para usar la URL de Postgres en Render

BASE_DIR = Path(__file__).resolve().parent.parent

# ----------------------
# Seguridad
# ----------------------
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-temp-key')  # Usa variable de entorno en producción
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# Permitir tu dominio Render
ALLOWED_HOSTS = ['proyectofindeciclodsi.onrender.com']  # Cambia según tu URL
# Para pruebas temporales puedes usar ALLOWED_HOSTS = ['*']

# ----------------------
# Aplicaciones
# ----------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core.apps.CoreConfig',
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

ROOT_URLCONF = 'DSI_Matriculas.urls'

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

WSGI_APPLICATION = 'DSI_Matriculas.wsgi.application'

# ----------------------
# Base de datos
# ----------------------
# Render proporciona DATABASE_URL, dj_database_url lo convierte en config de Django
DATABASES = {
    'default': dj_database_url.config(
        default='postgres://postgres:Postgres123@localhost:5432/MatriculasBD',
        conn_max_age=600
    )
}

# ----------------------
# Password validation
# ----------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# ----------------------
# Internacionalización
# ----------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ----------------------
# Archivos estáticos
# ----------------------
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # Necesario en producción
