from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

from resumeapp.forms import ResumeForm
from resumeapp.models import Resume


class CreateResumeView(CreateView):
    """Создание резюме для соискателя"""
    model = Resume
    template_name = 'resumeapp/resume_page.html'
    success_url = '/'
    form_class = ResumeForm

class  UpdateResumeView(UpdateView):
    """Обновление резюме для соискателя"""
    model = Resume
    template_name = 'resumeapp/resume_page.html'
    success_url = '/'
    form_class = ResumeForm

class DeleteResumeView(DeleteView):
    """Удаление резюме для соискателя"""
    model = Resume
    template_name = 'mainapp/index.html'


class ResumeDetailView(DetailView):
    """Резюме для соискателя"""
    model = Resume
    template_name = 'resumeapp/resume_page.html'
    context_object_name = 'post'


