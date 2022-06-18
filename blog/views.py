from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from taggit.models import Tag
from .models import Post
from .forms import CommentForm, EmailPostForm


# class PostList(generic.ListView):
#     model = Post
#     queryset = Post.objects.all()
#     template_name = "list.html"
#     paginate_by = 8


# PLAYGROUND #

class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.all()
    template_name = "list.html"
    paginate_by = 8

    
def tag(request, slug):
    post = Post.objects.filter(tags__slug=slug)
    return render(request, 'list.html', {"post_list": post, "tag": slug})


# class PostList(generic.ListView):
#     model = Post
#     queryset = Post.objects.all()
#     template_name = "list.html"
#     paginate_by = 8
#     queryset = object_list.filter(tags__in=[tag])
#     def get_queryset(self):
#         return Book.objects.filter(title__icontains='war')[:5]+
# 
        

# # TAG FUNCIONALITY #

# def post_list(request, tag_slug=None):
#     object_list = Post.objects.all()
#     tag = None
#     if tag_slug:
#         tag = get_object_or_404(Tag, slug=tag_slug)
#         object_list = object_list.filter(tags__in=[tag])
#     return render(
#         request,
#         "list.html",
#         {
#          'post': post, 
#          'tag': tag
#         }
#     )

# END PLAYGROUND #

class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("created")
        liked = False
        disliked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        if post.dislikes.filter(id=self.request.user.id).exists():
            disliked = True
        
        return render(
            request,
            "detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "disliked": disliked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):

        queryset = Post.objects.all()
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("created")
        liked = False
        disliked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        if post.dislikes.filter(id=self.request.user.id).exists():
            disliked = True

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
                "liked": liked,
                "disliked": disliked
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


class PostDislike(View):

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.dislikes.filter(id=request.user.id).exists():
            post.dislikes.remove(request.user)
        else:
            post.dislikes.add(request.user)

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
