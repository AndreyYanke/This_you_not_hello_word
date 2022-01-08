from django.urls import path

import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.MainPageView.as_view(), name='main'),
    path('rules/', mainapp.RulesSiteView.as_view(), name='rules'),
    path('logout/', mainapp.UserLogoutView.as_view(), name='logout'),
    path('', mainapp.main_page, name='main')
]
