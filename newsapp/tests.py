from http import HTTPStatus

from django.contrib import auth
from django.test.client import Client

from django.test import TestCase

from newsapp.models import NewsPost


class TestDetailNewsPost(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.news_post = NewsPost.objects.create(title='Web-development', description='Раз-два-три')

    def test_detail_news_post_for_anon(self):
        response = self.client.get(f'/news/{self.news_post.pk}/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

        response = self.client.get('/news/4/')
        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)

        response = self.client.get('/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

        user = auth.get_user(self.client)
        self.assertTrue(user.is_anonymous)
