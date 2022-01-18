from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView

from resumeapp import services
from resumeapp.filters import ResumeFilter
from resumeapp.forms import ResumeForm
from resumeapp.models import Resume
from this_you_not_hello_word import config


class ListResumeView(LoginRequiredMixin, ListView):
    """Отображение всех резюме"""
    model = Resume
    template_name = 'resumeapp/all_resume.html'
    form_class = ResumeForm
    paginate_by = 10
    ordering = '-created_at'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['config'] = config
        context['filter'] = ResumeFilter(self.request.GET, queryset=self.get_queryset())
        return context


class CreateResumeView(LoginRequiredMixin, CreateView):
    """Создание резюме для соискателя"""
    model = Resume
    template_name = 'resumeapp/resume_create.html'
    form_class = ResumeForm
    success_url = reverse_lazy('resume:my_resume')

    def get_initial(self):
        user = self.request.user
        initial = {'user': user}
        return initial


class UpdateResumeView(LoginRequiredMixin, UpdateView):
    """Обновление резюме для соискателя"""
    model = Resume
    template_name = 'resumeapp/resume_update.html'
    form_class = ResumeForm


class DeleteResumeView(LoginRequiredMixin, DeleteView):
    """Удаление резюме для соискателя"""
    model = Resume
    template_name = 'resumeapp/resume_update.html'
    success_url = reverse_lazy('resume:my_resume')


class ResumeDetailView(LoginRequiredMixin, DetailView):
    """Резюме для соискателя"""
    model = Resume
    template_name = 'resumeapp/resume_page.html'
    context_object_name = 'resume'

    def get_context_data(self, **kwargs):
        resume = self.get_object()
        context = super().get_context_data(**kwargs)

        context['work_experiences'] = resume.work_experiences.select_related()
        context['educations'] = resume.education.select_related()
        context['education_level'] = services.get_level_education_rus_languange(context['educations'])
        context['sex'] = services.get_sex_rus_languange(resume)
        context['busyness'] = services.get_busyness_rus_languange(resume)
        context['work_schedule'] = services.get_work_schedule_rus_languange(resume)
        context['key_skills'] = Resume.objects.get_key_skills(self.kwargs['pk'])
        return context


class MyResumeListView(LoginRequiredMixin, ListView):
    template_name = 'resumeapp/my_list_resume.html'

    def get_queryset(self):
        return Resume.objects.filter_my_resume_or_vacancies(self.request.user.id)
