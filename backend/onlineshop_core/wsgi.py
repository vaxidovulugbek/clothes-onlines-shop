"""
WSGI config for onlineshop_core project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
from onlineshop_core.settings import MEDIA_ROOT

from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'onlineshop_core.settings')

application = get_wsgi_application()
application = WhiteNoise(application, root=MEDIA_ROOT)
application.add_files(MEDIA_ROOT, prefix="more-files/")

