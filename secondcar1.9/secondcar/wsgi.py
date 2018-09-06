"""
WSGI config for secondcar project.

It exposes the WSGI callable as a module-level variable named ``application``.
'''
Author:PSM Team
date:2018/7/30 12:00:00
'''
For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "secondcar.settings")

application = get_wsgi_application()
