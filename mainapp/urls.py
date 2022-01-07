from django.urls import path

import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.main_page, name='main'),
    path('rules/', mainapp.rules_site, name='rules')
]
