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
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True, verbose_name='Город проживания')
    work_experiences = models.ForeignKey('Work_expirience', on_delete=models.CASCADE, verbose_name='Опыт работы')
    education = models.ForeignKey('Education', verbose_name='Образование, дополнительные курсы',
                                  on_delete=models.CASCADE)
    citizenship = models.ForeignKey('Citizenship', verbose_name='Гражданство', on_delete=models.CASCADE)

    first_name = models.CharField(max_length=64, verbose_name='Имя пользователя')
    last_name = models.CharField(max_length=64, verbose_name='Фамилия пользователя')
    photo = models.ImageField(upload_to='resume_image', blank=True, null=True)
    sex = models.CharField(max_length=9, choices=STATUS_SEX, verbose_name='Пол')
    age = models.PositiveSmallIntegerField()
    contact_info = models.CharField(max_length=300, verbose_name='Контактная информация')
    ready_to_move = models.BooleanField(default=True, verbose_name='Готов к перезду')
    position = models.CharField(max_length=64, verbose_name='Желаемая должность')
    salary = models.PositiveIntegerField(blank=True, null=True, verbose_name='Желаемая зарплата')
    work_schedule = models.CharField(max_length=20, choices=STATUS_CHOICES_WORK_SCHEDULE, verbose_name='График работы',
                                     blank=True, null=True)
    busyness = models.CharField(max_length=64, choices=STATUS_CHOICES_BUSYNESS, verbose_name='Тип занятости',
                                blank=True, null=True)
    about_myself = models.TextField(blank=True, null=True, verbose_name='Описание')
    is_publish = models.BooleanField(default=True, verbose_name='Опубликованное резюме')

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


class Education(models.Model):
    LEVEL_OF_EDUCATION_PRIMARY = 'primary'
    LEVEL_OF_EDUCATION_SECONDARY = 'secondary'
    LEVEL_OF_EDUCATION_HIGHER = 'higher'

    STATUS_CHOICES_LEVEL_OF_EDUCATION = (
        (LEVEL_OF_EDUCATION_PRIMARY, 'начальное образование'),
        (LEVEL_OF_EDUCATION_SECONDARY, 'среднее образование'),
        (LEVEL_OF_EDUCATION_HIGHER, 'высшее образование'),
    )

    level = models.CharField(max_length=30, choices= STATUS_CHOICES_LEVEL_OF_EDUCATION, null=True, verbose_name='Уровень образования')
    institution = models.CharField(max_length=124, verbose_name='Учебное учреждение', blank=True, null=True)
    faculty = models.CharField(max_length=64, verbose_name='Факультет', blank=True, null=True)
    specialisation = models.CharField(max_length=64, verbose_name='Специализация', blank=True, null=True)
    year_of_completion = models.PositiveIntegerField(verbose_name='Год окончания', blank=True, null=True)
    image_sertiificate = models.ImageField(upload_to='resume_sertiificate', blank=True, null=True)

    class Meta:
        verbose_name = 'Образование'
        verbose_name_plural = 'Образование'

    def __str__(self):
        if self.institution:
            return f'{self.institution}: {self.specialisation} | {self.year_of_completion}'
        else:
            return f'Образование отсутствует'


class Citizenship(models.Model):
    country = models.CharField(max_length=124, verbose_name='Гражданство', blank=True, null=True)

    class Meta:
        verbose_name = 'Гражданство'
        verbose_name_plural = 'Гражданство'

    def __str__(self):
        return f'{self.country}'
