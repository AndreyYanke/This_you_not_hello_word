from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, FormView

from newsapp.models import NewsPost
from this_you_not_hello_word.settings import LOGIN_REDIRECT_URL
from userapp.models import User


class MainPageView(FormView):
    """Класс, который полностью разворачивает главную страницу"""
    form_class = AuthenticationForm
    template_name = 'mainapp/index.html'
    success_url = LOGIN_REDIRECT_URL

    """В случае, если POST (авторизация)"""
    def form_valid(self, form):
        auth.login(self.request, form.get_user())
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_company_partners'] = User.objects.filter(is_partner=True)
        context['list_news'] = NewsPost.objects.filter(is_active=True).order_by('-created_at')
        context['user'] = self.request.user
        return context


class UserLogoutView(LogoutView):
    template_name = 'mainapp/index.html'


class RulesSiteView(TemplateView):
    """Класс, который переносит на страницу с полной редакцией правил портала"""
    template_name = 'mainapp/rules.html'
