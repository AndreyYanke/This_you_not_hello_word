from django.db import models


class ResumeOrVacancyManager(models.Manager):

    def get_key_skills(self, obj_id):
        key_skills = self.get(pk=obj_id).key_skills.select_related()
        return key_skills

    def filter_my_resume_or_vacancies(self, user_id):
        return self.filter(user=user_id)
