import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'this_you_not_hello_word.settings')
# celery -A this_you_not_hello_word worker -l info
app = Celery('this_you_not_hello_word')#Имя проекта get settings from settings
app.config_from_object('django.conf:settings',namespace='CELERY')#namespace
app.autodiscover_tasks()#Автоматом подцеплять наши задачи(tasks)


app.conf.beat_schedule = {
    'send-spam-every-1-minute':{
        'task':'resumeapp.tasks.send_beat_email',
        'schedule': crontab(minute='*/1'),
    }
}