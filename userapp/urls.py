from django.urls import path

import userapp.views as userapp

app_name = 'userapp'

urlpatterns = [
    path('type_user/', userapp.FirstPageRegistration.as_view(), name='type_user'),
    path('aspirant/', userapp.AspirantRegistration.as_view(), name='regist_aspirant'),
    path('company/', userapp.CompanyRegistration.as_view(), name='regist_company'),
    path('logout/', userapp.UserLogoutView.as_view(), name='logout'),
    path('auth/', userapp.UserLoginView.as_view(), name='auth'),
    # path('delete/<int:pk>/', userapp.CompanyDeleteView.as_view(), name='delete'),
    path('update/<int:pk>/', userapp.ProfileUpdateView.as_view(), name='update'),
    path('<int:pk>/', userapp.CompanyDetailView.as_view(), name='user'),
]
