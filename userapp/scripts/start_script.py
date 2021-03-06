import random

from database_filling.news_creator import NewsPostCreator
from database_filling.vacancy_creator import VacancyCreator
from database_filling.city_creator import CityCreator
from database_filling.company_creator import CompanyCreator
from database_filling.key_skill_creator import KeySkillsCreator
from database_filling.admin_creator import AdminCreator
from database_filling.user_creator import UserCreator
from database_filling.education_creator import EducationCreator
from database_filling.resume_creator import ResumeCreator
from database_filling.work_expirience_creator import Work_expirienceCreator
from database_filling.citizenship_creator import CitizenshipCreator


def run():
    users = UserCreator()
    users()

    admin = AdminCreator()
    admin()

    companies = CompanyCreator()
    companies()

    cities = CityCreator()
    cities()

    key_skills = KeySkillsCreator()
    key_skills()

    news = NewsPostCreator()
    news()


    vacancies = VacancyCreator(
        users = companies.result,
        cities = cities.result,
    )
    vacancies()

    for vacancy in vacancies.result:
        skills = set()
        for _ in range(4):
            skills.add(key_skills.result[random.randint(
                0,
                len(key_skills.result)-1,
            )])

        vacancy.key_skills.add(*skills)


    citizenships = CitizenshipCreator()
    citizenships()

    work_experiences = Work_expirienceCreator()
    work_experiences()

    #
    # education = EducationCreator()
    # education()

    resumes = ResumeCreator(
        users = users.result,
        cities = cities.result,
        citizenships = citizenships.result,
        # work_experiences = work_experiences.result,
        # education = education.result,
    )
    resumes()

    for  resumes in resumes.result:
        skills = set()
        for _ in range(4):
            skills.add(key_skills.result[random.randint(
                0,
                len(key_skills.result)-1,
            )])

        resumes.key_skills.add(*skills)
