from django.db import models

from this_you_not_hello_word.models import TrackableUpdateCreateModel
from userapp.models import User, City


class Resume(TrackableUpdateCreateModel):
    WORK_SCHEDULE_TYPE_USER_FULL = 'full_time'
    WORK_SCHEDULE_TYPE_USER_REPLACEABLE = 'replaceable'
    WORK_SCHEDULE_TYPE_USER_FLEXIBLE = 'flexible'
    WORK_SCHEDULE_TYPE_USER_REMOTE = 'remote'
    WORK_SCHEDULE_TYPE_USER_SHIFT = 'remote'

    BUSYNESS_TYPE_USER_FULL_EMLOYMENT = 'full employment'
    BUSYNESS_TYPE_USER_PART_TIME_EMPLOYMENT = ' part-time employment'
    BUSYNESSTYPE_USER_PROJECT_WORK = ' project work'
    BUSYNESS_TYPE_USER_VOLUNTEERING = 'volunteering'
    BUSYNESS_TYPE_USER_INTERNSHIP = ' internship'

    SEX_M = 'man'
    SEX_F = 'woman'

    STATUS_CHOICES_WORK_SCHEDULE = (
        (WORK_SCHEDULE_TYPE_USER_FULL, 'полный день'),
        (WORK_SCHEDULE_TYPE_USER_REPLACEABLE, 'сменный график'),
        (WORK_SCHEDULE_TYPE_USER_FLEXIBLE, 'гибкий работа'),
        (WORK_SCHEDULE_TYPE_USER_REMOTE, 'удаленная работа'),
        (WORK_SCHEDULE_TYPE_USER_SHIFT, 'вахтовый метод'),
    )

    STATUS_CHOICES_BUSYNESS = (
        (BUSYNESS_TYPE_USER_FULL_EMLOYMENT, 'полная занятость  '),
        (BUSYNESS_TYPE_USER_PART_TIME_EMPLOYMENT, 'частичная занятость'),
        (BUSYNESSTYPE_USER_PROJECT_WORK, 'проектная работа'),
        (BUSYNESS_TYPE_USER_VOLUNTEERING, 'волонтерство '),
        (BUSYNESS_TYPE_USER_INTERNSHIP, 'стажировка'),
    )

    STATUS_SEX = (
        (SEX_M, 'мужской'),
        (SEX_F, 'женский'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Соискатель', null=True)
    first_name = models.CharField(max_length=64, verbose_name='Имя пользователя')
    last_name = models.CharField(max_length=64, verbose_name='Фамилия пользователя')
    photo = models.ImageField(upload_to='resume_image', blank=True, null=True)
    sex = models.CharField(max_length=9, choices=STATUS_SEX, verbose_name='Пол')
    age = models.PositiveSmallIntegerField()
    contact_info = models.CharField(max_length=300, verbose_name='Контактная информация')
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='Город проживания')
    ready_to_move = models.BooleanField(default=True, verbose_name='Готов к перезду')
    position = models.CharField(max_length=64, verbose_name='Желаемая должность')
    salary = models.PositiveIntegerField(blank=True, null=True, verbose_name='Желаемая зарплата')
    work_schedule = models.CharField(max_length=20, choices=STATUS_CHOICES_WORK_SCHEDULE, verbose_name='График работы',
                                     blank=True, null=True)
    busyness = models.CharField(max_length=64, choices=STATUS_CHOICES_BUSYNESS, verbose_name='Тип занятости',
                                blank=True, null=True)
    work_experiences = models.ForeignKey('Work_expirience', on_delete=models.CASCADE, verbose_name='Опыт работы')

    about_myself = models.TextField(blank=True, null=True, verbose_name='Описание')
    is_publish = models.BooleanField(default=True, verbose_name='Опубликованное резюме')

    # TODO создать отдельную модель
    education = models.CharField(max_length=1024, verbose_name='Образование, дополнительные курсы')

    # TODO создать отдельную модель
    citizenship = models.CharField(max_length=64, verbose_name='Гражданство')

    class Meta:
        verbose_name = 'Резюме'
        verbose_name_plural = 'Резюме'

    def __str__(self):
        return f'{self.position}'


class Work_expirience(models.Model):
    start_of_work = models.DateField(blank=True, null=True)
    end_of_work = models.DateField(blank=True, null=True)
    organisation = models.CharField(max_length=64, verbose_name='Организация в которой работал')
    position = models.CharField(max_length=64, verbose_name='Должность')
    duties = models.TextField(blank=True, null=True, verbose_name='Обязанности')

    class Meta:
        verbose_name = 'Опыт работы'
        verbose_name_plural = 'Опыт работы'

    def __str__(self):
        if self.end_of_work:
            return f'{self.organisation}: {self.start_of_work} - {self.end_of_work}'
        else:
            return f'{self.organisation}: {self.start_of_work}'
