from django.urls import path

from resumeapp.views import ResumeView

app_name = 'resumeapp'

urlpatterns = [
    path('', ResumeView.as_view(), name='resume'),
]
