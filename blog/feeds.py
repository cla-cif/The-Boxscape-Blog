from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from django.urls import reverse_lazy, reverse
from .models import Post


class LatestPostsFeed(Feed):
    title = 'The Boxscape Blog'
    link = reverse_lazy('blog:home')
    description = 'Check the new posts from The Boxscape blog'

    def items(self):
        return Post.objects.filter(status='pub')[:5]
        # return Post.objects.order_by('-published')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.body, 30)



    # def items(self):
    #     # return Post.objects.filter(status='pub').order_by('-published')[:5]
    #     return Post.objects.all()

    # def item_title(self, item):
    #     return item.title

    # def item_description(self, item):
    #     return truncatewords(item.body, 30)

    # def item_link(self, item):
    #     return reverse('list.html', args=[item.pk])
