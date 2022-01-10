from http import HTTPStatus

from django.test.client import Client

from django.test import TestCase

from userapp.models import User


class TestMainPage(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.user = User.objects.create_user(username='Vasy123',
                                             password='111333222qwe',
                                             email='vasy123@mail.ru',
                                             user_type='aspirant')

    def test_main_page_rules(self):
        response = self.client.get('/rules/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

        response = self.client.get('/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_login_user(self):
        # главная без логина
        response = self.client.get('/')
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTrue(response.context['user'].is_anonymous)

        # логинимся
        self.client.login(username='Vasy123', password='111333222qwe')

        # главная с авторизированным пользователем
        response = self.client.get('/')
        self.assertFalse(response.context['user'].is_anonymous)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context['user'], self.user)

    def test_logout_user(self):
        # логинимся
        self.client.login(username='Vasy123', password='111333222qwe')
        response = self.client.get('/')
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertFalse(response.context['user'].is_anonymous)
        self.assertEqual(response.context['user'], self.user)

        # выходим из системы
        response = self.client.get('/logout/')
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

        response = self.client.get('/')
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTrue(response.context['user'].is_anonymous)
