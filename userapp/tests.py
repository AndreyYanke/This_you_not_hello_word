from http import HTTPStatus

from django.test.client import Client
from unittest import TestCase


from userapp.models import User


class TestRegister(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_regist_view_aspirant(self):
        # переходим на сайт с регистрацией для соискателя
        response = self.client.get('/user/aspirant/')
        self.assertTrue(response, HTTPStatus.OK)
        self.assertTrue(response.context['user'].is_anonymous)

        form_data = {'username': 'aspirant1',
                     'password1': '111333222qwe',
                     'password2': '111333222qwe',
                     'email': 'aspirant1@mail.ru',
                     'user_type': User.USER_TYPE_USER}

        response = self.client.post('/user/aspirant/', data=form_data)
        self.assertTrue(response, HTTPStatus.FOUND)

        # после регистрации, нас автоматически авторизируют и redirect на главную страницу
        response = self.client.get('/')
        self.assertTrue(response, HTTPStatus.OK)
        self.assertFalse(response.context['user'].is_anonymous)

    def test_regist_view_company(self):
        response = self.client.get('/user/company/')
        self.assertTrue(response, HTTPStatus.OK)
        self.assertTrue(response.context['user'].is_anonymous)

        form_data = {'user_type': User.USER_TYPE_COMPANY,
                     'username': 'company16',
                     'email': 'company16@mail.ru',
                     'password1': '111333222qwe',
                     'password2': '111333222qwe'}

        # регистрируемя
        response = self.client.post('/user/company/', data=form_data)
        self.assertTrue(response, HTTPStatus.FOUND)

        # после регистрации, нас автоматически авторизируют и redirect на главную страницу
        response = self.client.get('/')
        self.assertTrue(response, HTTPStatus.OK)
        self.assertFalse(response.context['user'].is_anonymous)

    def test_regist_view_wrong(self):
        # проверка на разные пароли при регистрации
        form_data = {'user_type': User.USER_TYPE_COMPANY,
                     'username': 'company17',
                     'email': 'company17@mail.ru',
                     'password1': '111333222qwe',
                     'password2': '436634fdhf'}

        response = self.client.post('/user/company/', data=form_data)
        self.assertTrue(response, HTTPStatus.OK)
        form = response.context['form']
        self.assertFalse(form.is_valid())
        self.assertTrue(self.check_errors_form(form))

        # проверка на уникальность username при регистрации
        form_data['password2'] = '111333222qwe'
        form_data['username'] = 'company16'
        response = self.client.post('/user/company/', data=form_data)
        self.assertTrue(response, HTTPStatus.OK)
        form = response.context['form']
        self.assertFalse(form.is_valid())
        self.assertTrue(self.check_errors_form(form))

        # проверка на уникальность email при регистрации
        form_data['username'] = 'company17'
        form_data['email'] = 'company16@mail.ru'
        response = self.client.post('/user/company/', data=form_data)
        self.assertTrue(response, HTTPStatus.OK)
        form = response.context['form']
        self.assertFalse(form.is_valid())
        self.assertTrue(self.check_errors_form(form))

    def check_errors_form(self, form):
        error_list = ['Пользователь с таким именем уже существует.',
                      'Введенные пароли не совпадают.',
                      'Пользователь с таким Email уже существует.']

        for field, errors in form.errors.items():
            for error in errors:
                if error in error_list:
                    return True
        return False


class AuthorisationTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.user = User.objects.create_user(user_type=User.USER_TYPE_USER,
                                             username='Vasy123',
                                             email='vasy123@mail.ru',
                                             password='111333222qwe',)
        self.user1 = User.objects.create_user(user_type=User.USER_TYPE_USER,
                                              username='Vasy124',
                                              email='vasy124@mail.ru',
                                              password='111333222qwe')

    def test_login_logout_user(self):
        # страница авторизации
        response = self.client.get('/user/auth/')
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTrue(response.context['user'].is_anonymous)

        form_data = {'username': 'Vasy123',
                     'password': '111333222qwe'}

        # логинимся
        response = self.client.post('/user/auth/', data=form_data)
        self.assertTrue(response, HTTPStatus.FOUND)

        # главная с авторизированным пользователем
        response = self.client.get('/')
        self.assertFalse(response.context['user'].is_anonymous)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context['user'], self.user)

        # выходим из системы
        print(response.context['user'])
        response = self.client.get('/user/logout/')
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

        # главная с неавторизированным пользователем
        response = self.client.get('/')
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTrue(response.context['user'].is_anonymous)
