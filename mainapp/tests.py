from http import HTTPStatus

from django.contrib import auth
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

        self.client.login(username='Vasy123', password='111333222qwe')
        response = self.client.get('/')
        self.assertFalse(response.context['user'].is_anonymous)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_logout_user(self):

        self.client.login(username='Vasy123', password='111333222qwe')
        self.client.logout()
        response = self.client.get('/')
        self.assertEqual(response.status_code, HTTPStatus.OK)
        user = auth.get_user(self.client)
        self.assertTrue(user.is_anonymous)
from django.test import TestCase

# Create your tests here.
