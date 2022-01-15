from django.urls import path

import newsapp.views as newsapp

app_name = 'newsapp'

urlpatterns = [
    path('<int:pk>/', newsapp.NewsPostDetailView.as_view(), name='detail_news'),
    path('all_news/', newsapp.NewsPostListView.as_view(), name='list_news')
]
