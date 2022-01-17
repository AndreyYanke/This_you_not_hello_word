from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView

from vacancyapp.filters import VacancyFilter
from vacancyapp.forms import VacancyForm
from vacancyapp.models import Vacancy, KeySkill
from this_you_not_hello_word.settings import LOGIN_REDIRECT_URL


class CreateVacancyView(LoginRequiredMixin, CreateView):
    """Создание вакансии для компаний"""
    model = Vacancy
    template_name = 'vacancyapp/create.html'
    form_class = VacancyForm
    success_url = reverse_lazy('main:main')


class UpdateVacancyView(LoginRequiredMixin, UpdateView):
    """Обновление вакансии для компаний"""
    model = Vacancy
    template_name = 'vacancyapp/update.html'
    form_class = VacancyForm


class DeleteVacancyView(DeleteView):
    """Удаление вакансии для компаний"""
    model = Vacancy
    template_name = 'vacancyapp/update.html'
    success_url = reverse_lazy('main:main')


class VacancyDetailView(LoginRequiredMixin, DetailView):
    """Вакансия для компаний"""
    model = Vacancy
    template_name = 'vacancyapp/vacancy.html'
    context_object_name = 'vacancy'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['city'] = Vacancy.objects.get(pk=self.kwargs['pk']).city
        context['key_skills'] = Vacancy.objects.get(pk=self.kwargs['pk']).key_skills.select_related()

        return context


class VacancyListView(ListView):
    """Отображение вакансий"""
    template_name = 'vacancyapp/vacancies.html'
    paginate_by = 10
    model = Vacancy
    ordering = '-created_at'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = VacancyFilter(self.request.GET, queryset=self.get_queryset())
        return context
