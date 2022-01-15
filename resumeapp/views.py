from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

from resumeapp.forms import ResumeForm
from resumeapp.models import Resume
from this_you_not_hello_word import config
from this_you_not_hello_word.settings import LOGIN_REDIRECT_URL


class CreateResumeView(CreateView):
    """Создание резюме для соискателя"""
    model = Resume
    template_name = 'resumeapp/resume_page.html'
    success_url = '/'
    form_class = ResumeForm


class UpdateResumeView(UpdateView):
    """Обновление резюме для соискателя"""
    model = Resume
    template_name = 'resumeapp/resume_page.html'
    success_url = '/'
    form_class = ResumeForm


class DeleteResumeView(DeleteView):
    """Удаление резюме для соискателя"""
    model = Resume
    template_name = 'mainapp/index.html'


class ResumeDetailView(LoginRequiredMixin, DetailView):
    """Резюме для соискателя"""
    model = Resume
    template_name = 'resumeapp/resume_page.html'
    context_object_name = 'resume'
    login_url = LOGIN_REDIRECT_URL


    def get_context_data(self, **kwargs):
        resume = self.get_object()
        context = super().get_context_data(**kwargs)

        context['work_experiences'] = resume.work_experiences.select_related()
        context['educations'] = resume.education.select_related()

        context['sex'] = [status[1] for status in config.STATUS_SEX if status[0] == resume.sex][0]
        context['busyness'] = [status[1] for status in config.STATUS_CHOICES_BUSYNESS if status[0] == resume.busyness][0]
        context['work_schedule'] = [status[1] for status in config.STATUS_CHOICES_WORK_SCHEDULE if
                                    status[0] == resume.work_schedule][0]

        return context




