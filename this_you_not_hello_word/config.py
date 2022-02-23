
WORK_SCHEDULE_TYPE_USER_FULL = 'full time'
WORK_SCHEDULE_TYPE_USER_REPLACEABLE = 'replaceable'
WORK_SCHEDULE_TYPE_USER_FLEXIBLE = 'flexible'
WORK_SCHEDULE_TYPE_USER_REMOTE = 'remote'
WORK_SCHEDULE_TYPE_USER_SHIFT = 'remote'

STATUS_CHOICES_WORK_SCHEDULE = (
    (WORK_SCHEDULE_TYPE_USER_FULL, 'полный день'),
    (WORK_SCHEDULE_TYPE_USER_REPLACEABLE, 'сменный график'),
    (WORK_SCHEDULE_TYPE_USER_FLEXIBLE, 'гибкий график'),
    (WORK_SCHEDULE_TYPE_USER_REMOTE, 'удаленная работа'),
    (WORK_SCHEDULE_TYPE_USER_SHIFT, 'вахтовый метод'),
)


BUSYNESS_TYPE_USER_FULL_EMLOYMENT = 'full employment'
BUSYNESS_TYPE_USER_PART_TIME_EMPLOYMENT = 'part-time employment'
BUSYNESSTYPE_USER_PROJECT_WORK = 'project work'
BUSYNESS_TYPE_USER_VOLUNTEERING = 'volunteering'
BUSYNESS_TYPE_USER_INTERNSHIP = 'internship'

STATUS_CHOICES_BUSYNESS = (
    (BUSYNESS_TYPE_USER_FULL_EMLOYMENT, 'полная занятость'),
    (BUSYNESS_TYPE_USER_PART_TIME_EMPLOYMENT, 'частичная занятость'),
    (BUSYNESSTYPE_USER_PROJECT_WORK, 'проектная работа'),
    (BUSYNESS_TYPE_USER_VOLUNTEERING, 'волонтерство'),
    (BUSYNESS_TYPE_USER_INTERNSHIP, 'стажировка'),
)


SEX_M = 'man'
SEX_F = 'woman'

STATUS_SEX = (
    (SEX_M, 'мужской'),
    (SEX_F, 'женский'),
)


LEVEL_OF_EDUCATION_PRIMARY = 'primary'
LEVEL_OF_EDUCATION_SECONDARY = 'secondary'
LEVEL_OF_EDUCATION_HIGHER = 'higher'

STATUS_CHOICES_LEVEL_OF_EDUCATION = (
    (LEVEL_OF_EDUCATION_PRIMARY, 'начальное образование'),
    (LEVEL_OF_EDUCATION_SECONDARY, 'среднее образование'),
    (LEVEL_OF_EDUCATION_HIGHER, 'высшее образование'),
)

RESPONSE_STATUS_UNDER_CONSIDERATION = 'на рассмотрении'
RESPONSE_STATUS_YES = 'да'
RESPONSE_STATUS_NO = 'нет'

RESPONSE_STATUS = (
    (RESPONSE_STATUS_UNDER_CONSIDERATION, 'на рассмотрении'),
    (RESPONSE_STATUS_YES, 'да'),
    (RESPONSE_STATUS_NO, 'нет'),
)