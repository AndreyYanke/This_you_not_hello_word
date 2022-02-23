from django.core.management.base import BaseCommand
from mixer.backend.django import mixer

from resumeapp.models import Resume
from vacancyapp.models import Vacancy


class Command(BaseCommand):
    def handle(self, *args, **options):
        # User.objects.create_superuser(username='nikolay',user_type='aspirant',email='isp06@mail.ru',password='1')
        # User.objects.create_superuser(username='nikolay1',user_type='сompany',email='glamur-greek@mail.ru',password='1')
        for i in range(5):
            mixer.blend(Resume)
            mixer.blend(Vacancy)
