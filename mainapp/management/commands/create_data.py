from django.core.management.base import BaseCommand

from userapp.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        User.objects.create_superuser('nikolay', 'admin@mail.ru', '1')
