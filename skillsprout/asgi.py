"""
ASGI config for skillsprout project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'skillsprout.settings')

# Update the DATABASES setting to use MySQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'skillssprout',
        'USER': 'kovalsky',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': 3306,
    }
}

application = get_asgi_application()
