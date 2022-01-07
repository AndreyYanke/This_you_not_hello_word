from http import HTTPStatus

from django.contrib import auth
from django.test.client import Client

from django.test import TestCase


class TestMainPageForAnon(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_main_page_rules(self):
        response = self.client.get('/rules/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

        response = self.client.get('/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

        user = auth.get_user(self.client)
        self.assertTrue(user.is_anonymous)



