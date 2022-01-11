from django.urls import path

from resumeapp.views import CreateResumeView, UpdateResumeView, DeleteResumeView, ResumeDetailView

app_name = 'resumeapp'

urlpatterns = [
    path('', CreateResumeView.as_view(), name='resume'),
    path('', UpdateResumeView.as_view(), name='resume'),
    path('', DeleteResumeView.as_view(), name='resume'),
    path('', ResumeDetailView.as_view(), name='resume'),
]
