from django.views.generic import DetailView, ListView

from newsapp.models import NewsPost


class NewsPostDetailView(DetailView):
    model = NewsPost
    template_name = 'newsapp/post_news.html'
    context_object_name = 'post'


class NewsPostListView(ListView):
    model = NewsPost
    template_name = 'newsapp/all_post_news.html'
    paginate_by = 10
