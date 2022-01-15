from userapp.models import User
from database_filling.user_creator import UserCreator


class CompanyCreator(UserCreator):
    """Создает компании."""

    def __init__(self):
        self.model = User
        self.data = (
            {
                'username': 'Ромашка',
                'company_name': 'Ромашка',
                'descriptions_company': 'ромашкуем',
                'email': 'romashka@email.com',
                'user_type': 'сompany',
                'partner': False,
            },
            {
                'username': 'Рога и копыта',
                'company_name': 'Рога и копыта',
                'descriptions_company': 'рогуем и быкуем',
                'email': 'roga-kopita@email.com',
                'user_type': 'сompany',
                'partner': True,
            },
            {
                'username': 'Борода',
                'company_name': 'Борода',
                'descriptions_company': 'Бородуем',
                'email': 'boroda@email.com',
                'user_type': 'сompany',
                'partner': False,
            },
            {
                'username': 'Газ Ром',
                'company_name': 'Газ Ром',
                'descriptions_company': 'Газуем Ромуем',
                'email': 'gas-rom@email.com',
                'user_type': 'сompany',
                'partner': True,
            },
        )
