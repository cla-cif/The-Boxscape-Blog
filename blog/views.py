from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post


# def post_list(request):
#     posts = Post.published.all()
#     return render(request,
#                   'blog/post/list.html',
#                   {'posts:posts'})


# def post_detail(request, year, month, day, post):
#     post = get_object_or_404(Post, slug=post,
#                              status='published',
#                              publish__year=year,
#                              publish__month=month,
#                              publish__day=day)
#     return render(request,
#                   'blog/post/detail.html',
#                   {'post': post})


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status='Published').order_by("-created")
    template_name = "list.html"
    paginate_by = 6
