from django.db import models
from django.urls import reverse

from resumeapp.managers import ResumeOrVacancyManager
from this_you_not_hello_word.models import TrackableUpdateCreateModel
from userapp.models import User, City
from this_you_not_hello_word import config


class KeySkill(TrackableUpdateCreateModel):
    name = models.CharField(max_length=255, verbose_name='Название', db_index=True)

    class Meta:
        verbose_name = 'Ключевой навык'
        verbose_name_plural = 'Ключевые навыки'

    def __str__(self):
        return self.name


class Vacancy(TrackableUpdateCreateModel):
    WORK_SCHEDULE_TYPE_USER_FULL = config.WORK_SCHEDULE_TYPE_USER_FULL
    WORK_SCHEDULE_TYPE_USER_REPLACEABLE = config.WORK_SCHEDULE_TYPE_USER_REPLACEABLE
    WORK_SCHEDULE_TYPE_USER_FLEXIBLE = config.WORK_SCHEDULE_TYPE_USER_FLEXIBLE
    WORK_SCHEDULE_TYPE_USER_REMOTE = config.WORK_SCHEDULE_TYPE_USER_REMOTE
    WORK_SCHEDULE_TYPE_USER_SHIFT = config.WORK_SCHEDULE_TYPE_USER_SHIFT

    STATUS_CHOICES_WORK_SCHEDULE = config.STATUS_CHOICES_WORK_SCHEDULE

    name = models.CharField(max_length=255, verbose_name='Название', db_index=True)
    description = models.TextField(verbose_name='Описание')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Компания')
    is_active = models.BooleanField(default=True, verbose_name='Активная вакансия')
    salary_from = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Зарплата от', blank=True, null=True)
    salary_to = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Зарплата до', blank=True, null=True)
    address = models.CharField(max_length=255, verbose_name='Адрес', blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='Город', related_name='city')
    required_experience_from = models.PositiveSmallIntegerField(verbose_name='Минимальный трудовой стаж', blank=True, null=True)
    required_experience_to = models.PositiveSmallIntegerField(verbose_name='Максимальный трудовой стаж', blank=True, null=True)
    work_schedule = models.CharField(max_length=64, choices=STATUS_CHOICES_WORK_SCHEDULE, verbose_name='Занятость', blank=True, null=True)
    key_skills = models.ManyToManyField(KeySkill, verbose_name='Ключевые навыки', blank=True, related_name='skills')

    objects = ResumeOrVacancyManager()

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'

    def get_absolute_url(self):
        url = reverse('vacancy:detail', args=[self.id])
        return url

    def __str__(self):
        return self.name
