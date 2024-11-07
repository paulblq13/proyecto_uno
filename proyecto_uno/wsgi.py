"""
WSGI config for proyecto_uno project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
#==HEROKU STATICS==
from dj_static import Cling
#==HEROKU STATICS==
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise
from proyecto_uno.settings import BASE_DIR

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyecto_uno.settings')

application = get_wsgi_application()
#application = WhiteNoise(application, root=os.path.join(BASE_DIR, 'staticfiles'))
application = Cling(get_wsgi_application())

