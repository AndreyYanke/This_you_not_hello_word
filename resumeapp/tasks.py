from celery.loaders import app
from django.core.mail import send_mail

from resumeapp.models import FollowerAspirant
from this_you_not_hello_word.celery import app


@app.task  # Обязательно обвернуть функцию
def send_beat_email():  # не передаем рез
    # попросить email
    for contact in FollowerAspirant.objects.all():
        send_mail(
            'На вашу вакансию подписались',
            f'Имя подписчика {contact.user} наименование вакансии {contact.vacancy.name}',
            'django.celery.redis@gmail.com',
            [contact.user.email],
            fail_silently=False
        )


@app.task  # Обязательно обвернуть функцию
def send_response_email(user, text_message, email):  # не передаем рез
    # попросить email
    # for contact in FollowerAspirant.objects.all():
    send_mail('На вашу вакансию откликнулися', f'пользователь:  {user} '
                                               f'\n сопровождающее письмо: {text_message}',
              'django.celery.redis@gmail.com',
              [email], fail_silently=False)
