from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from django.urls import reverse_lazy
from .models import Post


class LatestPostsFeed(Feed):
    title = 'The Boxscape Blog'
    link = reverse_lazy('blog:post_list')
    description = 'Check the new posts from The Boxscape blog'

    def items(self):
        return Post.objects.filter(status='pub')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.body, 30)
