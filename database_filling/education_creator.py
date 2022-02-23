import random

from resumeapp.models import Education
from database_filling.base_creator import BaseCreator


class EducationCreator(BaseCreator):
    """Создает образование."""

    def __init__(self):
        self.model = Education
        self.data = (
            {
                'level': self.model.STATUS_CHOICES_LEVEL_OF_EDUCATION[
                    random.randint(
                        0, len(self.model.STATUS_CHOICES_LEVEL_OF_EDUCATION)-1
                    )
                ][0],
                'institution': 'ИМЭИ',
                'faculty': 'Финансы и кредит',
                'specialisation': 'экономист',
                'year_of_completion': 2014,
                # 'image_sertiificate':
            },
        )


