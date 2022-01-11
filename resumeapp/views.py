from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

from resumeapp.forms import ResumeForm
from resumeapp.models import Resume, Work_expirience
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
        context = super().get_context_data(**kwargs)
        context['work_experiences'] = Work_expirience.objects.filter(resume=self.kwargs['pk']).select_related()
        return context
