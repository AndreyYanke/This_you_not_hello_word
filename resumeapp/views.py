from django.views.generic import DetailView

from resumeapp.forms import ResumeForm
from resumeapp.models import Resume


# TODO исправить ошибку Generic detail view ResumeView must be called with either an object pk or a slug in the URLconf
class ResumeView(DetailView):
    """Резюме для соискателя"""
    model = Resume
    template_name = 'mainapp/index.html'
    success_url = '/'
    form_class = ResumeForm

