from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView, LoginView
from django.views.generic import TemplateView, CreateView

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


class AspirantRegistration(AuthAfterRegistMixin, CreateView):
    """Регистрация для соискателя"""
    template_name = 'userapp/regist_aspirant.html'
    form_class = AspirantRegisterForm
    initial = {'user_type': User.USER_TYPE_USER}


class UserLogoutView(LogoutView):
    template_name = 'mainapp/index.html'


class UserLoginView(LoginView):
    template_name = 'userapp/authorisation.html'
    success_url = LOGIN_REDIRECT_URL
    form_class = AuthenticationForm
