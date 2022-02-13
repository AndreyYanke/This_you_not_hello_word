import random

from database_filling.base_creator import BaseCreator
from resumeapp.models import Resume


class ResumeCreator(BaseCreator):
    """Создает резюме."""

    def __init__(self, users, cities, citizenships):
        self.cities = cities
        self.users = users
        self.citizenships = citizenships
        # self.work_experiences = work_experiences
        # self.education = education
        self.model = Resume
        self.data = (
            {
                'city': self.cities[random.randint(0, len(self.cities) - 1)],
                'user': self.users[random.randint(0, len(self.users) - 1)],
                'citizenship': self.citizenships[random.randint(0, len(self.citizenships) - 1)],
                # 'work_experiences': self.work_experiences[random.randint(0, len(self.work_experiences) - 1)],
                # 'education':self.education[random.randint(0, len(self.education) - 1)],
                'first_name': 'Андрей',
                'last_name': 'Иванов',
                'sex': self.model.SEX_M,
                'age': '32',
                'contact_info': 'ayanke@bk.ru',
                'ready_to_move': True,
                'position': 'программист',
                'salary': 100000,
                'work_schedule': self.model.STATUS_CHOICES_WORK_SCHEDULE[
                    random.randint(
                        0, len(self.model.STATUS_CHOICES_WORK_SCHEDULE) - 1
                    )
                ][0],
                'busyness': self.model.STATUS_CHOICES_BUSYNESS[
                    random.randint(
                        0, len(self.model.STATUS_CHOICES_BUSYNESS) - 1
                    )
                ][0],
                'about_myself': 'Пунктуальный, Креативный, Желание разбираться во всём новом',
                'is_publish': True,

            },
            {
                'city': self.cities[random.randint(0, len(self.cities) - 1)],
                'user': self.users[random.randint(0, len(self.users) - 1)],
                'citizenship': self.citizenships[random.randint(0, len(self.citizenships) - 1)],
                # 'work_experiences': self.work_experiences[random.randint(0, len(self.work_experiences) - 1)],
                # 'education':self.education[random.randint(0, len(self.education) - 1)],
                'first_name': 'Андрей',
                'last_name': 'Иванов',
                'sex': self.model.SEX_M,
                'age': '32',
                'contact_info': 'ayanke@bk.ru',
                'ready_to_move': True,
                'position': 'web developer',
                'salary': 100000,
                'work_schedule': self.model.STATUS_CHOICES_WORK_SCHEDULE[
                    random.randint(
                        0, len(self.model.STATUS_CHOICES_WORK_SCHEDULE) - 1
                    )
                ][0],
                'busyness': self.model.STATUS_CHOICES_BUSYNESS[
                    random.randint(
                        0, len(self.model.STATUS_CHOICES_BUSYNESS) - 1
                    )
                ][0],
                'about_myself': 'Пунктуальный, Креативный, Желание разбираться во всём новом',
                'is_publish': False,
                'draft': True,
            },
        )

