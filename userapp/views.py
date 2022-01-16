from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView, LoginView
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, DetailView

from this_you_not_hello_word.settings import LOGIN_REDIRECT_URL
from userapp.forms import AspirantRegisterForm, CompanyRegisterForm
from userapp.mixins import AuthAfterRegistMixin
from userapp.models import User


class FirstPageRegistration(TemplateView):
    """Страница с выбором типа пользователя для дальнейшей регистрации"""
    template_name = 'userapp/first_page_registration.html'


class CompanyRegistration(AuthAfterRegistMixin, CreateView):

    """Регистрация для компании"""
    template_name = 'userapp/regist_company.html'
    form_class = CompanyRegisterForm
    initial = {'user_type': User.USER_TYPE_COMPANY}
    success_url = LOGIN_REDIRECT_URL


class CompanyUpdateView(AuthAfterRegistMixin, UpdateView):
    model = User
    form_class = CompanyRegisterForm
    template_name = 'userapp/update_company.html'
    success_url = reverse_lazy('main:main')


class CompanyDeleteView(AuthAfterRegistMixin, DeleteView):
    model = User
    template_name = 'userapp/update_company.html'
    success_url = reverse_lazy('main:main')


class CompanyDetailView(AuthAfterRegistMixin, DetailView):
    model = User
    template_name = 'userapp/company.html'
    success_url = reverse_lazy('main:main')


class AspirantRegistration(AuthAfterRegistMixin, CreateView):

    """Регистрация для соискателя"""
    template_name = 'userapp/regist_aspirant.html'
    form_class = AspirantRegisterForm
    initial = {'user_type': User.USER_TYPE_USER}
    success_url = reverse_lazy('main:main')


class UserLogoutView(LogoutView):
    template_name = 'mainapp/index.html'


class UserLoginView(LoginView):
    template_name = 'userapp/authorisation.html'
    form_class = AuthenticationForm

    def get_success_url(self):
        if self.request.user.user_type == User.USER_TYPE_USER:
            url = reverse_lazy('vacancy:list')
        elif self.request.user.user_type == User.USER_TYPE_COMPANY:
            url = reverse_lazy('resume:list')
        else:
            url = LOGIN_REDIRECT_URL
        return url
