from django import template
from django.db.models import Count, Case, When, Value
from ..models import Post, Comment

register = template.Library()


# @register.simple_tag()
# def total_comments():
#     return Comment.objects.aggregate(approved=Count(Case(
#         When(approved==True,
#              then=Value(1)))))

# @register.simple_tag()
# def total_comments():
#     return Post.comments.objects.filter(comment__approved=True).count()


# @register.simple_tag()
# def total_comments():
#     return Post.objects.aggregate(
#         approved=Count(Case(When(Comment.approved is True, then=Value(1)))))


@register.simple_tag()
def total_posts():
    return Post.objects.filter(status='pub').count()


@register.simple_tag()
def total_users():
    return Post.author.count()


@register.inclusion_tag('latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.objects.filter(status='pub').order_by('-published')[:count]
    return {'latest_posts': latest_posts}


@register.simple_tag()
def get_most_commented_posts(count=5):
    return Post.objects.annotate(
        total_comments=Count('comments')
    ).order_by('-total_comments')[:count]