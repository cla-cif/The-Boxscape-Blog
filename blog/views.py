from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post


# def post_list(request):
#     posts = Post.objects.all()
#     return render(request,
#                   'list.html',
#                   {'posts': posts})


# def post_detail(request, year, month, day, post):
#     post = get_object_or_404(Post, slug=post,
#                              status='Published',
#                              publish__year=year,
#                              publish__month=month,
#                              publish__day=day)
#     return render(request,
#                   'detail.html',
#                   {'post': post})

class PostList(generic.ListView):
    model = Post
    # queryset = Post.objects.filter(status='published')
    queryset = Post.objects.all()
    template_name = "list.html"
    paginate_by = 6


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("created")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                # "comment_form": CommentForm()
            },
        )
