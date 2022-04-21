"""
WSGI config for GTV_VST project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os, sys
sys.path.append('Gestion_visiteur/GTV_VST')

sys.path.append('/venv/Lib/site-packages')

#exec(open("/venv/Scripts/activate").read(), {'__file__': "/venv/Scripts/activate"})

#sys.path.append('/venv/core/core')

#sys.path.append('/venv/lib/python3.6/site-packages')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GTV_VST.settings')

application = get_wsgi_application()
