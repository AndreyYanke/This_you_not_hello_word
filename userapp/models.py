from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField
from django.db import models


from this_you_not_hello_word.models import TrackableUpdateCreateModel


class User(AbstractUser):
    """Класс описывает пользователя"""

    USER_TYPE_USER = 'aspirant'
    USER_TYPE_COMPANY = 'сompany'

    TYPE_CHOICES = ((USER_TYPE_USER, 'Соискатель'), (USER_TYPE_COMPANY, 'Компания'))

    user_type = models.CharField(max_length=64, choices=TYPE_CHOICES, verbose_name='Тип пользователя')
    email = models.EmailField(max_length=64, unique=True, blank=False, verbose_name='Email')
    descriptions_company = models.TextField(blank=True, null=True, verbose_name='Карточка компании')
    # is_publish_descriptions = models.BooleanField(default=False, verbose_name='Опубликованная карточка компании')
    company_name = models.CharField(max_length=64, blank=True, null=True, verbose_name='Название компании')
    activation_key = models.CharField(max_length=128, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата и время изменения')
    partner = models.BooleanField(default=False, verbose_name='партнер')
    partner_image = models.ImageField(upload_to='partner_image', blank=True, null=True)
    city = models.ForeignKey('City', on_delete=models.CASCADE, blank=True, null=True, verbose_name='Город')
    phone_number = models.CharField(max_length= 18, blank=True, null=True, verbose_name='Номер телефона')

    REQUIRED_FIELDS = ['user_type', 'email']

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        if self.company_name:
            return self.company_name
        elif self.first_name and self.last_name:
            return f"{self.last_name} {self.first_name}"
        else:
            return self.username


class City(TrackableUpdateCreateModel):

    name = models.CharField(max_length=100, null=True)
    country = CountryField(null=True)

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def __str__(self):
        return self.name
