from django.views.generic import TemplateView, CreateView

from userapp.forms import AspirantRegisterForm, CompanyRegisterForm
from userapp.models import User


class FirstPageRegistration(TemplateView):
    """Страница с выбором типа пользователя для дальнейшей регистрации"""
    template_name = 'userapp/first_page_registration.html'


class CompanyRegistration(CreateView):
    """Регистрация для компании"""
    template_name = 'userapp/regist_company.html'
    success_url = '/'
    form_class = CompanyRegisterForm
    initial = {'user_type': User.USER_TYPE_COMPANY}


class AspirantRegistration(CreateView):
    """Регистрация для соискателя"""
    template_name = 'userapp/regist_aspirant.html'
    success_url = '/'
    form_class = AspirantRegisterForm
    initial = {'user_type': User.USER_TYPE_USER}



