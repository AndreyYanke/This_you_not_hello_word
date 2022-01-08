from django.urls import path

import newsapp.views as newsapp

app_name = 'newsapp'

urlpatterns = [
    path('<int:pk>/', newsapp.NewsPostDetailView.as_view(), name='detail_news')
]
