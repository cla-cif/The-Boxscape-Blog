from django.urls import path
from .feeds import LatestPostsFeed
from . import views

# app_name = 'blog'

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('dislike/<slug:slug>', views.PostDislike.as_view(), name='post_dislike'), # noqa
    path('<int:id>/delete', views.comment_delete, name='comment_delete'),
    path('<int:id>/edit-comment/', views.comment_edit, name='comment_edit'),
    path("tag/<slug:slug>/", views.tag, name='tag'),
    path("author/<int:pk>/", views.author_posts, name="author_posts"),
    path('<int:id>/edit-post/', views.post_edit, name='post_edit'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('feed/', LatestPostsFeed(), name='post_feed'),
    path('about', views.AboutView.as_view(), name='about'),
    path('create', views.post_create, name='post_create'),
    # path('create_new', views.PostCreateView.as_view(), name='post_create_new'),
]
