from django.db import models
from django.urls import reverse

from resumeapp.managers import ResumeOrVacancyManager
from this_you_not_hello_word import config
from this_you_not_hello_word.models import TrackableUpdateCreateModel
from userapp.models import User, City
from vacancyapp.models import KeySkill, Vacancy


class Resume(TrackableUpdateCreateModel):
    WORK_SCHEDULE_TYPE_USER_FULL = config.WORK_SCHEDULE_TYPE_USER_FULL
    WORK_SCHEDULE_TYPE_USER_REPLACEABLE = config.WORK_SCHEDULE_TYPE_USER_REPLACEABLE
    WORK_SCHEDULE_TYPE_USER_FLEXIBLE = config.WORK_SCHEDULE_TYPE_USER_FLEXIBLE
    WORK_SCHEDULE_TYPE_USER_REMOTE = config.WORK_SCHEDULE_TYPE_USER_REMOTE
    WORK_SCHEDULE_TYPE_USER_SHIFT = config.WORK_SCHEDULE_TYPE_USER_SHIFT

    STATUS_CHOICES_WORK_SCHEDULE = config.STATUS_CHOICES_WORK_SCHEDULE

    BUSYNESS_TYPE_USER_FULL_EMLOYMENT = config.BUSYNESS_TYPE_USER_FULL_EMLOYMENT
    BUSYNESS_TYPE_USER_PART_TIME_EMPLOYMENT = config.BUSYNESS_TYPE_USER_PART_TIME_EMPLOYMENT
    BUSYNESSTYPE_USER_PROJECT_WORK = config.BUSYNESSTYPE_USER_PROJECT_WORK
    BUSYNESS_TYPE_USER_VOLUNTEERING = config.BUSYNESS_TYPE_USER_VOLUNTEERING
    BUSYNESS_TYPE_USER_INTERNSHIP = config.BUSYNESS_TYPE_USER_INTERNSHIP

    STATUS_CHOICES_BUSYNESS = config.STATUS_CHOICES_BUSYNESS

    SEX_M = config.SEX_M
    SEX_F = config.SEX_F

    STATUS_SEX = config.STATUS_SEX

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Соискатель', null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True, verbose_name='Город проживания')
    work_experiences = models.ManyToManyField('Work_expirience', verbose_name='Опыт работы',
                                              related_name='work_experiences', blank=True)
    education = models.ManyToManyField('Education', verbose_name='Образование, дополнительные курсы',
                                       related_name='educations', blank=True)
    citizenship = models.ForeignKey('Citizenship', verbose_name='Гражданство', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=64, verbose_name='Имя пользователя')
    last_name = models.CharField(max_length=64, verbose_name='Фамилия пользователя')
    photo = models.ImageField(upload_to='resume_image', blank=True, null=True)
    sex = models.CharField(max_length=9, choices=STATUS_SEX, verbose_name='Пол')
    age = models.PositiveSmallIntegerField(default=18)
    contact_info = models.CharField(max_length=300, verbose_name='Контактная информация')
    ready_to_move = models.BooleanField(default=True, verbose_name='Готов к перезду')
    position = models.CharField(max_length=64, verbose_name='Желаемая должность')
    salary = models.PositiveIntegerField(blank=True, null=True, verbose_name='Желаемая зарплата')
    work_schedule = models.CharField(max_length=20, choices=STATUS_CHOICES_WORK_SCHEDULE, verbose_name='График работы',
                                     blank=True, null=True)
    busyness = models.CharField(max_length=64, choices=STATUS_CHOICES_BUSYNESS, verbose_name='Тип занятости',
                                blank=True, null=True)
    about_myself = models.TextField(blank=True, null=True, verbose_name='Описание')
    is_publish = models.BooleanField(default=False, verbose_name='Опубликованное резюме')
    draft = models.BooleanField(default=False, verbose_name='Черновик')
    key_skills = models.ManyToManyField(KeySkill, verbose_name='Ключевые навыки', blank=True,
                                        related_name='skills_in_resume')

    objects = ResumeOrVacancyManager()

    class Meta:
        verbose_name = 'Резюме'
        verbose_name_plural = 'Резюме'

    def get_absolute_url(self):
        url = reverse('resume:detail', args=[self.id])
        return url

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
    LEVEL_OF_EDUCATION_PRIMARY = config.LEVEL_OF_EDUCATION_PRIMARY
    LEVEL_OF_EDUCATION_SECONDARY = config.LEVEL_OF_EDUCATION_SECONDARY
    LEVEL_OF_EDUCATION_HIGHER = config.LEVEL_OF_EDUCATION_HIGHER

    STATUS_CHOICES_LEVEL_OF_EDUCATION = config.STATUS_CHOICES_LEVEL_OF_EDUCATION

    level = models.CharField(max_length=30, choices=STATUS_CHOICES_LEVEL_OF_EDUCATION, null=True,
                             verbose_name='Уровень образования')
    institution = models.CharField(max_length=124, verbose_name='Учебное учреждение', blank=True, null=True)
    faculty = models.CharField(max_length=64, verbose_name='Факультет', blank=True, null=True)
    specialisation = models.CharField(max_length=64, verbose_name='Специализация', blank=True, null=True)
    year_of_completion = models.PositiveIntegerField(verbose_name='Год окончания', blank=True, null=True)
    image_sertiificate = models.ImageField(upload_to='resume_sertiificate', blank=True, null=True)

    class Meta:
        verbose_name = 'Образование'
        verbose_name_plural = 'Образование'

    def __str__(self):
        if self.institution and self.specialisation and self.year_of_completion:
            return f'{self.institution}: {self.specialisation} | {self.year_of_completion}'
        elif self.institution and self.specialisation:
            return f'{self.institution}: {self.specialisation}'
        elif self.institution:
            return f'{self.institution} | обучение не окончено'
        else:
            return f'Образование отсутствует'


class Citizenship(models.Model):
    country = models.CharField(max_length=124, verbose_name='Гражданство', blank=True, null=True)

    class Meta:
        verbose_name = 'Гражданство'
        verbose_name_plural = 'Гражданство'

    def __str__(self):
        return f'{self.country}'


class ResponseAspirant(TrackableUpdateCreateModel):
    RESPONSE_STATUS = config.RESPONSE_STATUS

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Соискатель',
        null=True)
    selected_vacancy = models.ForeignKey(
        Vacancy,
        on_delete=models.CASCADE,
        verbose_name='Выбранные вакансии',
        related_name='selected_vacancy', null=True)
    cover_letter = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=30, choices=RESPONSE_STATUS, default=RESPONSE_STATUS[0][0], null=True,
                              verbose_name='Статус отклика на вакансию')
    quantity_response = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Отклики соискателей'
        verbose_name_plural = 'Отклики соискателей'

    def __str__(self):
        return f'{self.user} | {self.selected_vacancy}'

class ResponseCompany(TrackableUpdateCreateModel):
    RESPONSE_STATUS = config.RESPONSE_STATUS

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Работодатель',
        null=True)
    selected_resume = models.ForeignKey(
        Resume,
        on_delete=models.CASCADE,
        verbose_name='Выбранные резюме',
        related_name='selected_resume', null=True)
    status = models.CharField(max_length=30, choices=RESPONSE_STATUS ,default=RESPONSE_STATUS[0][0], null=True, verbose_name='Статус отклика на резюме')
    quantity_response = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Отклики работодателей'
        verbose_name_plural = 'Отклики работодателей'

    def __str__(self):
        return f'{self.user} | {self.selected_resume}'

class FollowerAspirant(TrackableUpdateCreateModel):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Соискатель',
        null=True)
    vacancy = models.ForeignKey(
        Vacancy,
        on_delete=models.CASCADE,
        verbose_name='Выбранные вакансии',null=True)

    resume = models.ForeignKey(
        Resume,
        on_delete=models.CASCADE,
        verbose_name='Выбранные резюме',null=True)

    class Meta:
        verbose_name = 'Подписка соискателя'
        verbose_name_plural = 'Подписки соискателей'

    def __str__(self):
        return f'{self.user} | {self.vacancy}'