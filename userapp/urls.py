from django.urls import path

import userapp.views as userapp

app_name = 'userapp'

urlpatterns = [
    path('', userapp.FirstPageRegistration.as_view(), name='type_user'),
    path('aspirant/', userapp.AspirantRegistration.as_view(), name='aspirant'),
    path('company/', userapp.CompanyRegistration.as_view(), name='company'),
]
