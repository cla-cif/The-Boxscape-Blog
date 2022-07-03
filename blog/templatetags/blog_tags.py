from django import template
from django.db.models import Count
from ..models import Post

register = template.Library()


@register.simple_tag()
def total_posts():
    return Post.objects.filter(status='pub').count()


@register.inclusion_tag('latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.objects.order_by('-published')[:count]
    return {'latest_posts': latest_posts}


@register.simple_tag()
def get_most_commented_posts(count=5):
    return Post.objects.annotate(
        total_comments=Count('comments')
    ).order_by('-total_comments')[:count]