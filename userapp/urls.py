from django.urls import path

import userapp.views as userapp

app_name = 'userapp'

urlpatterns = [
    path('type_user/', userapp.FirstPageRegistration.as_view(), name='type_user'),
    path('aspirant/', userapp.AspirantRegistration.as_view(), name='regist_aspirant'),
    path('company/', userapp.CompanyRegistration.as_view(), name='regist_company'),
    path('logout/', userapp.UserLogoutView.as_view(), name='logout'),
    path('auth/', userapp.UserLoginView.as_view(), name='auth'),
]
