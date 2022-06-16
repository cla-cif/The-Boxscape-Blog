from django.urls import path
from . import views

# app_name = 'blog'

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('dislike/<slug:slug>', views.PostDislike.as_view(), name='post_dislike'),
    path('<slug:slug>/share/', views.PostShare.as_view(), name="post_share"),
]
