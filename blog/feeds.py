from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from django.utils.feedgenerator import Atom1Feed
from django.urls import reverse_lazy, reverse
from .models import Post


class LatestPostsFeed(Feed):
    title = 'The Boxscape Blog'
    link = reverse_lazy('home')
    description = 'Check the new posts from The Boxscape blog'

    def items(self):
        return Post.objects.filter(status='pub').order_by('-published')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.body, 30)

    def item_link(self, item):
        return reverse('post_detail', args=[item.slug])


class atomFeed(Feed):
    feed_type = Atom1Feed
