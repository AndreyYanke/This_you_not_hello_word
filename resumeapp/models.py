from django.db import models

from this_you_not_hello_word.models import TrackableUpdateCreateModel
from userapp.models import User, City


class Resume(TrackableUpdateCreateModel):

    BUSYNESS_TYPE_USER_FULL = 'full_time'
    BUSYNESS_TYPE_USER_PARTLY = 'partly'
    BUSYNESS_TYPE_USER_REMOTE = 'remote'
    SEX_M = 'man'
    SEX_F = 'woman'


    STATUS_CHOICES = (
        (BUSYNESS_TYPE_USER_FULL, 'полный рабочий день'),
        (BUSYNESS_TYPE_USER_PARTLY, 'частичная занятость'),
        (BUSYNESS_TYPE_USER_REMOTE, 'удаленная работа'),
    )
    STATUS_SEX = (
        (SEX_M, 'мужской'),
        (SEX_F, 'женский'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Соискатель', null=True)
    first_name = models.CharField(max_length=64, verbose_name='Имя пользователя')
    last_name = models.CharField(max_length=64,  verbose_name='Фамилия пользователя')
    photo = models.ImageField(upload_to='this_you_not_hello_word/static/img/img_the_applicant', blank=True, null=True)
    sex = models.CharField(max_length=9, choices=STATUS_SEX, verbose_name='Пол')
    age = models.PositiveSmallIntegerField()
    contact_info = models.CharField(max_length=300, verbose_name='Контактная информация')
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='Город проживания')
    ready_to_move = models.BooleanField(default=True, verbose_name='Готов к перезду')
    position = models.CharField(max_length=64, verbose_name='Желаемая должность')
    salary = models.PositiveIntegerField(blank=True, null=True, verbose_name='Желаемая зарплата')
    busyness = models.CharField(max_length=20, choices=STATUS_CHOICES, default=BUSYNESS_TYPE_USER_FULL, verbose_name='Занятость',
                                   blank=True, null=True)
    about_myself = models.TextField(blank=True, null=True, verbose_name='Описание')
    is_publish = models.BooleanField(default=True, verbose_name='Опубликованное резюме')


    #TODO добавить на choices
    work_schedule = models.CharField(max_length=64, verbose_name='График работы', blank=True, null=True)

    # TODO создать отдельную модель
    education= models.CharField(max_length=1024, verbose_name='Образование, дополнительные курсы')

    # TODO создать отдельную модель
    citizenship = models.CharField(max_length=64, verbose_name='Гражданство')


    # TODO создать отдельную модель
    work_experiences = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True,
                                           verbose_name='Опыт работы')


    class Meta:
        verbose_name = 'Резюме'
        verbose_name_plural = 'Резюме'

    def __str__(self):
        return  f'{self.user.first_name} {self.user.last_name}'

# class Work_expirience():
#     resume = models.ForeignKey(Resume, on_delete=models.CASCADE, verbose_name='')