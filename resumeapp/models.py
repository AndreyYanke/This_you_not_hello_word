from django.db import models

from this_you_not_hello_word.models import TrackableUpdateCreateModel
from userapp.models import User, City


class Resume(TrackableUpdateCreateModel):
    READY_TO_MOVE_YES = 1
    READY_TO_MOVE_NO = 2
    BUSYNESS_TYPE_USER_FULL = 1
    BUSYNESS_TYPE_USER_PARTLY = 2
    BUSYNESS_TYPE_USER_DISTANT = 3
    SEX_M = 1
    SEX_F = 2

    STATUS_CHOICES_READY_TO_MOVE = (
        (READY_TO_MOVE_NO, 'нет'),
        (READY_TO_MOVE_YES, 'да'),
    )

    STATUS_CHOICES = (
        (BUSYNESS_TYPE_USER_FULL, 'полный рабочий день'),
        (BUSYNESS_TYPE_USER_PARTLY, 'частичная занятость'),
        (BUSYNESS_TYPE_USER_DISTANT, 'удаленная работа'),
    )
    STATUS_SEX = (
        (SEX_M, 'мужской'),
        (SEX_F, 'женский'),
    )

    photo = models.ImageField(upload_to='This_you_not_hello_word1/static/img/img_the_applicant', blank=True, null=True)
    sex = models.IntegerField(choices=STATUS_SEX, verbose_name='Пол')
    contact_info = models.CharField(max_length=128, verbose_name='Контактная информация')
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='Город проживания')
    citizenship = models.CharField(max_length=64, verbose_name='Гражданство')
    ready_to_move = models.IntegerField(choices=STATUS_CHOICES_READY_TO_MOVE, default=READY_TO_MOVE_NO,
                                        verbose_name='Готов к перезду')
    position = models.CharField(max_length=64, verbose_name='Желаемая должность')
    salary = models.DecimalField(max_digits=15, decimal_places=1, blank=True, null=True,
                                 verbose_name='Желаемая зарплата')
    busyness = models.IntegerField(choices=STATUS_CHOICES, default=BUSYNESS_TYPE_USER_FULL, verbose_name='Занятость',
                                   blank=True, null=True)
    work_schedule = models.CharField(max_length=64, verbose_name='График работы', blank=True, null=True)
    travel_time_to_work = models.CharField(max_length=64, verbose_name='Желательное время в пути до работы', blank=True,
                                           null=True)
    work_experiences = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True,
                                           verbose_name='Опыт работы')
    description = models.TextField(verbose_name='Описание')
    is_active = models.BooleanField(default=True, verbose_name='Активное резюме')

    class Meta:
        verbose_name = 'Резюме'
        verbose_name_plural = 'Резюме'

    def __str__(self):
        return f'{User.first_name} | {User.last_name}'
