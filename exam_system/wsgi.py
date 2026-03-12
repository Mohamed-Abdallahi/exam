"""
WSGI config for exam_system project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# Charge les parametres Django avant de creer l application WSGI.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'exam_system.settings')

application = get_wsgi_application()
