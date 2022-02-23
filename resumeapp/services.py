from this_you_not_hello_word import config


# функция для получения уровня образования на русском языке
def get_level_education_rus_languange(educations):
    level_view = None
    for education in educations:
        for level in config.STATUS_CHOICES_LEVEL_OF_EDUCATION:
            if education.level == level[0]:
                level_view = level[1]
            elif education.level == level[0]:
                level_view = level[1]
            elif education.level == level[0]:
                level_view = level[1]
        return level_view


# функция для получения пола на русском языке
def get_sex_rus_languange(resume):
    return [status[1] for status in config.STATUS_SEX if status[0] == resume.sex][0]


# функция для получения графика работы на русском языке
def get_work_schedule_rus_languange(resume):
    return [status[1] for status in config.STATUS_CHOICES_WORK_SCHEDULE if status[0] == resume.work_schedule][0]


# функция для получения типа занятости на русском языке
def get_busyness_rus_languange(resume):
    return [status[1] for status in config.STATUS_CHOICES_BUSYNESS if status[0] == resume.busyness][0]
