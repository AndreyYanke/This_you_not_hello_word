from userapp.models import User
from database_filling.base_creator import BaseCreator


class UserCreator(BaseCreator):
    """Создает пользователя."""

    def __init__(self):
        self.model = User
        self.data = (
            {
                'email': 'nick@email.com',
                'user_type': 'aspirant',
                'username': 'nick',
                'first_name': 'nick',
                'last_name': 'nick',
                'partner_image': 'partner_image/dfa0b1b5f53005eac0d8985eef9f72a4.jpg',
            },
        )


    def __call__(self):
        super().__call__()
        self.__set_passwords__()


    def __set_passwords__(self):
        self.password = 'Password123'
        for user in self.result:
            user.set_password(self.password)
            user.save()
