from userapp.models import User
from database_filling.user_creator import UserCreator


class AdminCreator(UserCreator):
    """Создает города."""

    def __init__(self):
        self.models = User
        self.data = (
            {
                'email': 'email@email.com',
                'user_type': 'aspirant',
                'username': 'admin',
                'is_superuser': True,
                'is_staff': True,
                'is_active': True,
            },
        )
