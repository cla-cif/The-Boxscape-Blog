from django import template
from django.contrib.auth.models import User
from django.db.models import Count
from ..models import Post, Author, Comment

register = template.Library()


@register.simple_tag()
def total_posts():
    return Post.objects.filter(status='pub').count()


@register.simple_tag()
def total_authors():
    result = (Author.objects
              .values('user')
              .annotate(count=Count('user'))
              .order_by()
              )
    return len(result)


# @register.simple_tag()
# def total_authors():
#     return Author.objects.all().count()


@register.simple_tag()
def total_users():
    return User.objects.count()


@register.simple_tag()
def total_comments():
    return Comment.objects.filter(approved=True).count()


@register.inclusion_tag('latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.objects.filter(status='pub').order_by('-published')[:count]  # noqa
    return {'latest_posts': latest_posts}


@register.simple_tag()
def get_most_commented_posts(count=5):
    return Post.objects.annotate(
        total_comments=Count('comments')
    ).order_by('-total_comments')[:count]
