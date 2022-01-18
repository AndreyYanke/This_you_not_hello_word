from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView

from newsapp.models import NewsPost
from this_you_not_hello_word.settings import LOGIN_REDIRECT_URL
from userapp.models import User


class MainPageView(TemplateView):
    """Класс, который полностью разворачивает главную страницу"""
    # form_class = AuthenticationForm
    template_name = 'mainapp/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_company_partners'] = User.objects.filter(partner=True)
        context['list_news'] = NewsPost.objects.filter(is_active=True).values('pk', 'title').order_by('-created_at')[:5]
        return context

class UserLogoutView(LogoutView):
    template_name = 'mainapp/index.html'


class RulesSiteView(TemplateView):
    """Класс, который переносит на страницу с полной редакцией правил портала"""
    template_name = 'mainapp/rules.html'
