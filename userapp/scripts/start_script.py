import random

from database_filling.vacancy_creator import VacancyCreator
from database_filling.city_creator import CityCreator
from database_filling.company_creator import CompanyCreator
from database_filling.key_skill_creator import KeySkillsCreator
from database_filling.admin_creator import AdminCreator
from database_filling.user_creator import UserCreator


def run():
    user = UserCreator()
    user()

    admin = AdminCreator()
    admin()

    companies = CompanyCreator()
    companies()

    cities = CityCreator()
    cities()

    key_skills = KeySkillsCreator()
    key_skills()

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