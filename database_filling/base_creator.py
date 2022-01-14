from abc import ABCMeta, abstractmethod


class BaseCreator(metaclass=ABCMeta):
    """Конструктор для создателей."""

    @abstractmethod
    def __init__(self):
        pass

    def __call__(self):
        self.get_or_create()


    def get_or_create(self):
        self.result = list()
        for object in self.data:
            self.result.append(self.models.objects.get_or_create(**object)[0])
