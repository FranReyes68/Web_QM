"""
//////////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                                      //
//                         Proyecto:	Sitio WEB para Tecnología QuickMatch C.A.                       // 
//                         Fecha:		Septiembre de 2023                                              //
//                         Autor:		Francisco Reyes ©                                               //
//                         Archivo:		settings.py                                                     //
//																										//
//////////////////////////////////////////////////////////////////////////////////////////////////////////
"""

"""
Configuraciones de Django para Proyecto QM.

Para más información, consulte este sitio:
https://docs.djangoproject.com/en/4.2/topics/settings/

Para obtener la Lista Completa de Configuraciones y sus Valores, consulte:
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

from django.contrib.messages import constants as mensajes_de_error


# Cree rutas dentro del Proyecto de esta manera: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Configuraciones de Desarrollo de inicio rápido: No aptas para Producción
# Consulte: https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# ADVERTENCIA DE SEGURIDAD: ¡Mantenga en Secreto la Clave Secreta empleada en Producción!
SECRET_KEY = 'django-insecure-_=@_%cc7v#-t2u2!re^d6=lz5_r@m5scd4m@7uo!1i0$*7k4f^'

# ADVERTENCIA DE SEGURIDAD: ¡No ejecute con la Depuración Activada en Producción!
# True = Desarrollo
# False = Producción
DEBUG = True

ALLOWED_HOSTS = []


# Definición de Aplicaciones:

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ProyectoWebApp',
    'servicios',
    'blog',
    'contacto',
    'tienda',
    'carro',
    'autenticacion',
    'crispy_forms',
    'crispy_bootstrap4',
    'pedidos',
]

# Registro de Bootstrap Versión 4:

CRISPY_TEMPLATE_PACK='bootstrap4'


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ProyectoWeb.urls'

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
                'carro.context_processor.importe_total_carro',
            ],
        },
    },
]

WSGI_APPLICATION = 'ProyectoWeb.wsgi.application'


# Base de Datos
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Validación de Contraseñas
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


# Internacionalizaciión
# https://docs.djangoproject.com/en/4.2/topics/i18n/

#LANGUAGE_CODE = 'en-us'	# Establece el Idioma Inglés con Zona Horaria "us" en el Administrador Django.

LANGUAGE_CODE = 'es-VE'		# Establece el Idioma Español con Zona Horaria "eu" en el Administrador Django.

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Ubicación de Archivos "Static" (Static files: CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

MEDIA_URL= '/media/'

MEDIA_ROOT= BASE_DIR / 'media'

# Tipo de Campo de Clave Principal Predeterminado
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Configuración de Correo Electrónico:

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

EMAIL_HOST = "smtp.gmail.com"

EMAIL_USE_TLS = True

EMAIL_PORT = 587

EMAIL_HOST_USER = "sitio.web.qm@gmail.com"

EMAIL_HOST_PASSWORD = "dvmykmktudblhyrf"


# Mensajes de Error:

MESSAGE_TAGS={

    mensajes_de_error.DEBUG: 'debug',
    mensajes_de_error.INFO: 'info',
    mensajes_de_error.SUCCESS: 'success',
    mensajes_de_error.WARNING: 'warning',
    mensajes_de_error.ERROR: 'danger',
}