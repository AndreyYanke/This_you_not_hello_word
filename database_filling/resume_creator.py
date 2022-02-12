import random


from database_filling.base_creator import BaseCreator
#
#
from resumeapp.models import Resume


class ResumeCreator(BaseCreator):
    """Создает резюме."""

    def __init__(self, users, cities, citizenships):
        self.cities = cities
        self.users = users
        self.citizenships = citizenships
        self.model = Resume
        self.data = (
            {
                'city': self.cities[random.randint(0, len(self.cities)-1)],
                'user': self.users[random.randint(0, len(self.users)-1)],
                'citizenship': self.citizenships[random.randint(0, len(self.citizenships)-1)],
            },
        )
