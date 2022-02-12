# from userapp.models import Citizenship
from database_filling.base_creator import BaseCreator
from resumeapp.models import Citizenship


class CitizenshipCreator(BaseCreator):
    """Создает страны."""

    def __init__(self):
        self.model = Citizenship
        self.data = (
            {
                'country': 'РФ',
            },
        )
