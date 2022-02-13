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
                'partner_image': 'partner_image/unistory_logo.jpeg',
            },
            {
                'username': 'roga',
                'company_name': 'Рога и копыта',
                'descriptions_company': 'рогуем и быкуем',
                'email': 'ayanke@bk.ru',
                'user_type': 'сompany',
                'partner': True,
                'partner_image': 'partner_image/Apple-Logo_CCre4oL.png',
            },
            {
                'username': 'Борода',
                'company_name': 'Борода',
                'descriptions_company': 'Бородуем',
                'email': 'boroda@email.com',
                'user_type': 'сompany',
                'partner': False,
                'partner_image': 'partner_image/nivex_logo.png',
            },
            {
                'username': 'gaz',
                'company_name': 'Газ Ром',
                'descriptions_company': 'Газуем Ромуем',
                'email': 'gas-rom@email.com',
                'user_type': 'сompany',
                'partner': True,
                'partner_image': 'partner_image/newgen_logo_e1E7Vnp.jpeg',
            },
        )
