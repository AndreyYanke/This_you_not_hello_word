from django.views.generic import TemplateView

from newsapp.models import NewsPost
from userapp.models import User


class MainPageView(TemplateView):
    """Класс, который полностью разворачивает главную страницу"""
    template_name = 'mainapp/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_company_partners'] = User.objects.filter(is_partner=True)
        context['list_news'] = NewsPost.objects.filter(is_active=True).order_by('-created_at')
        context['user'] = self.request.user
        return context


class RulesSiteView(TemplateView):
    """Класс, который переносит на страницу с полной редакцией правил портала"""
    template_name = 'mainapp/rules.html'
