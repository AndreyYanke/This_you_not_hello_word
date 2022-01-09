from django.views.generic import TemplateView, CreateView

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



