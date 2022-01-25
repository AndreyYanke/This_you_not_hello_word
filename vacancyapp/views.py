from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView

from resumeapp.models import ResponseAspirant
from vacancyapp.filters import VacancyFilter
from vacancyapp.forms import VacancyForm
from vacancyapp.models import Vacancy


class CreateVacancyView(LoginRequiredMixin, CreateView):
    """Создание вакансии для компаний"""
    model = Vacancy
    template_name = 'vacancyapp/create.html'
    form_class = VacancyForm
    success_url = reverse_lazy('vacancy:my_vacancies')

    def get_initial(self):
        user = self.request.user
        initial = {'user': user}
        return initial


class UpdateVacancyView(LoginRequiredMixin, UpdateView):
    """Обновление вакансии для компаний"""
    model = Vacancy
    template_name = 'vacancyapp/update.html'
    form_class = VacancyForm
    success_url = reverse_lazy('vacancy:my_vacancies')


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
        context['key_skills'] = Vacancy.objects.get_key_skills(self.kwargs['pk'])

        return context


class VacancyListView(ListView):
    """Отображение вакансий"""
    template_name = 'vacancyapp/vacancies.html'
    paginate_by = 10
    model = Vacancy
    ordering = '-created_at'

    # TODO доработать логику , чтобы вакансии на которые откликались не были доступны
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = VacancyFilter(self.request.GET, queryset=self.get_queryset())
        # context['response'] = ResponseAspirant.objects.filter(user=self.request.user)
        return context


class MyVacanciesListView(LoginRequiredMixin, ListView):
    template_name = 'vacancyapp/my_list_vacancies.html'

    def get_queryset(self):
        return Vacancy.objects.filter_my_resume_or_vacancies(self.request.user.id)
