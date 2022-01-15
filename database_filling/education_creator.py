from userapp.models import Education
from database_filling.base_creator import BaseCreator


class EducationCreator(BaseCreator):
    """Создает образование."""

    def __init__(self):
        self.model = Education
        self.data = (
            {
                '': '',
            },
        )
