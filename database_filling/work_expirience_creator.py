from database_filling.base_creator import BaseCreator

from resumeapp.models import Work_expirience


class Work_expirienceCreator(BaseCreator):
    """Создает опыт работы."""

    def __init__(self):
        self.model = Work_expirience
        self.data = (
            {
                'start_of_work': '2018-03-01',
                'end_of_work': '2021-06-01',
                'organisation': 'Газпром',
                'position': 'руководитель',
                'duties': 'составление плана продаж и его своевременная коррекция\n\n '
                          'постановка задач сотрудникам и ежедневный контроль их выполнения\n\n'
                          'помощь сотрудникам в решении конкретных ситуаций, например,'
                          ' периодическое сопровождение их на встречах с ключевыми клиентами\n\n'
                          'организацию мероприятий по обучению менеджеров и поддержанию их высокого уровня мотивации\n\n'
                          'контроль поступления оплаты от клиентов (совместно с бухгалтерией), '
                          'при необходимости принятие мер для её своевременного получения',
            },
        )

