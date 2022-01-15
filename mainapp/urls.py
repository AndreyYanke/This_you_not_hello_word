from django.urls import path

import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.MainPageView.as_view(), name='main'),
    path('rules/', mainapp.RulesSiteView.as_view(), name='rules'),
]
