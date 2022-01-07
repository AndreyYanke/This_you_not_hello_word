from django.views.generic import DetailView

from newsapp.models import NewsPost


class NewsPostDetailView(DetailView):
    model = NewsPost
    template_name = 'newsapp/post_news.html'
    context_object_name = 'post'

