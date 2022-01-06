from django.db import models

from this_you_not_hello_word.models import TrackableUpdateCreateModel
from userapp.models import User, City


class Vacancy(TrackableUpdateCreateModel):
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Компания')
    is_active = models.BooleanField(default=True, verbose_name='Активная вакансия')
    salary_from = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Зарплата от', blank=True, null=True)
    salary_to = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Зарплата до', blank=True, null=True)
    address = models.CharField(max_length=255, verbose_name='Адрес', blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='Город')

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'

    def __str__(self):
        return self.name
