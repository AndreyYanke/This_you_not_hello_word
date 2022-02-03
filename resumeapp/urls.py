from django.urls import path

from resumeapp.views import CreateResumeView, UpdateResumeView, DeleteResumeView, ResumeDetailView, ListResumeView, \
    MyResumeListView, MyResponseListView, AspirantResponseView

app_name = 'resumeapp'

urlpatterns = [
    path('create/', CreateResumeView.as_view(), name='create'),
    path('update/<int:pk>/', UpdateResumeView.as_view(), name='update'),
    path('delete/<int:pk>/', DeleteResumeView.as_view(), name='delete'),
    path('<int:pk>/', ResumeDetailView.as_view(), name='detail'),
    path('', ListResumeView.as_view(), name='list'),
    path('my_resume/', MyResumeListView.as_view(), name='my_resume'),
    path('my_response/<int:pk>/', MyResponseListView.as_view(), name='my_response'),
    path('my_response_add/<int:pk>/', AspirantResponseView.as_view(), name='my_response_add'),
]
