from userapp.models import Work_expirience
from database_filling.base_creator import BaseCreator


class Work_expirienceCreator(BaseCreator):
    """Создает опыт работы."""

    def __init__(self):
        self.model = Work_expirience
        self.data = (
            {
                '': '',
            },
        )
