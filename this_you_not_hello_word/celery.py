import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'this_you_not_hello_word.settings')

app = Celery('celery')#Имя проекта get settings from settings
app.config_from_object('django.conf:settings',namespace='CELERY')#namespace
app.autodiscover_tasks()#Автоматом подцеплять наши задачи(tasks)