from django.urls import path
from . import views

# app_name = 'blog'

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('dislike/<slug:slug>', views.PostDislike.as_view(), name='post_dislike'), # noqa
    path("tag/<slug:slug>/", views.tag, name='tag'),
    path("author/<int:pk>/", views.author_posts, name="author_posts"),
    path('<slug:slug>/share/', views.PostShare.as_view(), name="post_share"),
    path('<int:id>/edit/', views.edit, name='post_edit'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('about', views.AboutView.as_view(), name='about'),
    path('create', views.create, name='create'),
]
