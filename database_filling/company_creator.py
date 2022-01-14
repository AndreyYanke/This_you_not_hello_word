from userapp.models import User
from database_filling.user_creator import UserCreator


class CompanyCreator(UserCreator):
    """Создает компании."""

    def __init__(self):
        self.models = User
        self.data = (
            {
                'username': 'Ромашка',
                'password': 'Password123',
                'company_name': 'Ромашка',
                'descriptions_company': 'ромашкуем',
                'email': 'romashka@email.com',
                'user_type': 'сompany',
                'partner': False,
            },
            {
                'username': 'Рога и копыта',
                'password': 'Password123',
                'company_name': 'Рога и копыта',
                'descriptions_company': 'рогуем и быкуем',
                'email': 'roga-kopita@email.com',
                'user_type': 'сompany',
                'partner': True,
            },
        )
