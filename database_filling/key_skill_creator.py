from vacancyapp.models import KeySkill
from database_filling.base_creator import BaseCreator


class KeySkillsCreator(BaseCreator):
    '''Создает скилы.'''

    def __init__(self):
        self.models = KeySkill
        self.data = (
            {
                'name': 'Python',
            },
            {
                'name': 'Django Framework',
            },
            {
                'name': 'MongoDB',
            },
            {
                'name': 'Обучение',
            },
            {
                'name': 'Git',
            },
            {
                'name': 'Linux',
            },
            {
                'name': 'JavaScript',
            },
            {
                'name': 'HTML',
            },
        )
