from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from taggit.models import Tag
from .models import Post
from .forms import CommentForm, EmailPostForm

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
    # queryset = Post.objects.filter(status='published') not working!!
    queryset = Post.objects.all()
    template_name = "list.html"
    paginate_by = 6


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.all()
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
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):

        queryset = Post.objects.all()
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("created")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )


class PostLike(View):

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class PostShare(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, slug=slug)
        sent = False

        if request.method == 'POST':
            form = EmailPostForm(request.POST)
            if form.is_valid():
                # form fields passed validation
                cd = form.cleaned_data
                post_url = request.build_absolute_uri(post.get_absolute_url())
                subject = f"{cd['name']} recommends you read "\
                          f"{post.title}"
                message = f"Read {post.title} at {post_url}\n\n" \
                          f"{cd['name']}\'s comments: {cd['comments']}"
                send_mail(subject, message, 'the.boxscape.blog@gmail.com', [cd['to']])
                sent = True
        else:
            form = EmailPostForm()
        return render(request, "share.html",
                      {'post': post, 'form': form, 'sent': sent})
