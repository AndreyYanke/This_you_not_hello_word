from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, FormView

from userapp.models import User


class MainPageView(TemplateView):
    """Класс, который полностью разворачивает главную страницу"""
    template_name = 'mainapp/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_company_partners'] = User.objects.filter(is_partner=True)
        return context


class RulesSiteView(TemplateView):
    """Класс, который переносит на страницу с полной редакцией правил портала"""
    template_name = 'mainapp/rules.html'
