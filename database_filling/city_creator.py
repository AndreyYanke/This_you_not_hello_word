from database_filling.base_creator import BaseCreator
from userapp.models import City


class CityCreator(BaseCreator):
    """Создает города."""

    def __init__(self):
        self.model = City
        self.data = (
            {
                'name': 'Saint-Petersburg',
                'country': 'Russia',
            },
            {
                'name': 'Moscow',
                'country': 'Russia',
            },
        )
