from userapp.models import User
from database_filling.base_creator import BaseCreator


class UserCreator(BaseCreator):
    """Создает города."""

    def __init__(self):
        self.models = User
        self.data = (
            {
                'email': '',
                'user_type': 'aspirant',
                'username': '',
                'password': '',
                'first_name': '',
                'last_name': '',
            },
            {
                'email': '',
                'user_type': 'aspirant',
                'username': '',
                'password': '',
                'first_name': '',
                'last_name': '',
            },
        )


    def __call__(self):
        super().__call__()
        self.__set_passwords__()


    def __set_passwords__(self):
        for user in self.result:
            user.set_password(user.password)
            user.save()
