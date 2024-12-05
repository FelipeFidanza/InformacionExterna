from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Configura el entorno para usar las configuraciones de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'InfoExterna.settings')

# Crear la aplicación de Celery
app = Celery('InfoExterna')

# Cargar las configuraciones de Celery desde settings.py
app.config_from_object('django.conf:settings', namespace='CELERY')

# Autodiscover tasks.py en todas las apps del proyecto Django
app.autodiscover_tasks()
