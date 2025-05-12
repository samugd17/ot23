"""
WSGI config for ot project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
import sys
import traceback
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ot.settings")


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ot.settings')

try:
    application = get_wsgi_application()
except Exception:
    sys.stderr.write("ERROR al iniciar Django:\n")
    traceback.print_exc()

