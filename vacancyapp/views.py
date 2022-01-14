from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView

from vacancyapp.forms import VacancyForm
from vacancyapp.models import Vacancy, KeySkill
from this_you_not_hello_word.settings import LOGIN_REDIRECT_URL


class CreateVacancyView(LoginRequiredMixin, CreateView):
    """Создание вакансии для компаний"""
    model = Vacancy
    template_name = 'vacancyapp/create.html'
    success_url = '/'
    form_class = VacancyForm
    login_url = LOGIN_REDIRECT_URL


class UpdateVacancyView(LoginRequiredMixin, UpdateView):
    """Обновление вакансии для компаний"""
    model = Vacancy
    template_name = 'vacancyapp/update.html'
    success_url = '/'
    form_class = VacancyForm
    login_url = LOGIN_REDIRECT_URL


class DeleteVacancyView(LoginRequiredMixin, DeleteView):
    """Удаление вакансии для компаний"""
    model = Vacancy
    template_name = 'mainapp/index.html'
    login_url = LOGIN_REDIRECT_URL


class VacancyDetailView(LoginRequiredMixin, DetailView):
    """Вакансия для компаний"""
    model = Vacancy
    template_name = 'vacancyapp/vacancy.html'
    context_object_name = 'vacancy'
    login_url = LOGIN_REDIRECT_URL

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['city'] = Vacancy.objects.get(pk=self.kwargs['pk']).city
        context['key_skills'] = Vacancy.objects.get(pk=self.kwargs['pk']).key_skills.select_related()

        return context


class VacancyListView(ListView):
    """Отображение вакансий"""
    model = Vacancy
    template_name = 'vacancyapp/vacancies.html'
    paginate_by = 10
