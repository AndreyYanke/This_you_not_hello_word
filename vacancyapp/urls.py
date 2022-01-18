from django.urls import path

from vacancyapp import views

app_name = 'vacancyapp'

urlpatterns = [
    path('create/', views.CreateVacancyView.as_view(), name='create'),
    path('update/<int:pk>/', views.UpdateVacancyView.as_view(), name='update'),
    path('delete/<int:pk>/', views.DeleteVacancyView.as_view(), name='delete'),
    path('<int:pk>/', views.VacancyDetailView.as_view(), name='detail'),
    path('', views.VacancyListView.as_view(), name='list'),
    path('my_vacancies/', views.MyVacanciesListView.as_view(), name='my_vacancies'),
]
