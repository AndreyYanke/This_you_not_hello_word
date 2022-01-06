from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UnicodeUsernameValidator, UserManager
from django.db import models


class UserType(models.Model):
    """Класс описывающий модель типа пользователя"""
    name = models.CharField(max_length=64, blank=False, null=False, verbose_name='Название типа пользователя')
    description = models.CharField(max_length=256, blank=True, verbose_name='Описание типа пользователя')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата и время изменения')


class User(AbstractBaseUser, PermissionsMixin):
    """Класс описывает пользователя"""
    username_validator = UnicodeUsernameValidator()

    user_type = models.ForeignKey(UserType, on_delete=models.CASCADE, verbose_name='Тип пользователя')
    username = models.CharField(max_length=64, unique=True, validators=[username_validator])
    first_name = models.CharField(max_length=64, blank=True, null=False, verbose_name='Имя пользователя')
    last_name = models.CharField(max_length=64, blank=True, null=False, verbose_name='Фамилия пользователя')
    email = models.EmailField(max_length=64, unique=True, blank=False, verbose_name='Email')
    descriptions_company = models.TextField(blank=True, null=True, verbose_name='Описание компании')
    company_name = models.CharField(max_length=64, blank=True, null=True, verbose_name='Название компании')
    is_staff = models.BooleanField(default=False, verbose_name='Модератор')
    is_active = models.BooleanField(default=True, verbose_name='Активный пользователь')
    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_expires = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата и время изменения')

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['user_type_id', 'email']

    objects = UserManager()
