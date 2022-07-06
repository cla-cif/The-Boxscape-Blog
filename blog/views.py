from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.views.generic import TemplateView, CreateView
from taggit.models import Tag
from django.db.models import Count
import cloudinary
from cloudinary.models import CloudinaryField
from cloudinary.forms import cl_init_js_callbacks
from django.contrib.auth.models import User
from .models import Post
from .forms import CommentForm, EmailPostForm, PostForm, EditPostForm


class AboutView(TemplateView):
    template_name = "./about.html"


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status='pub')
    template_name = "list.html"
    paginate_by = 9


def tag(request, slug):
    post = Post.objects.filter(tags__slug=slug)
    return render(request, 'list.html', {"post_list": post, "tag": slug})


def author_posts(request, pk):
    author = User.objects.get(pk=pk)
    post = Post.objects.filter(author=author)
    return render(request, 'list.html', {'post_list': post, "author": author})


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status='pub')
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("created")
        # retrieving post by similarity
        post_tags_ids = post.tags.values_list('id', flat=True)
        similar_posts = Post.objects.filter(tags__in=post_tags_ids)\
            .exclude(id=post.id)
        similar_posts = similar_posts.annotate(same_tags=Count('tags'))\
            .order_by('-same_tags')
        # like and dislike functionality
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
                "comment_form": CommentForm(),
                "similar_posts": similar_posts  # new
            },
        )

    def post(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status='pub')
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("created")
        # retrieving post by similarity
        post_tags_ids = post.tags.values_list('id', flat=True)
        similar_posts = Post.objects.filter(tags__in=post_tags_ids)\
            .exclude(id=post.id)
        similar_posts = similar_posts.annotate(same_tags=Count('tags'))\
            .order_by('-same_tags')
        #  like and dislike functionality
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
                "disliked": disliked,
                "similar_posts": similar_posts
            },
        )


def create(request):
    form = PostForm()
    context = {'form': form, 'created': False, }
    if request.method == 'GET':
        return render(
            request,
            "create_posts.html", context)
    # context = {'form': form, 'created':True}
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = Post()
            post.author = request.user
            post.slug = '-'.join(form.cleaned_data.get('title').split(' '))
            post.title = form.cleaned_data.get('title')
            tags = form.cleaned_data.get('tags')
            # post.image = cloudinary.uploader.upload(request.FILES['file'])
            post.excerpt = form.cleaned_data.get('excerpt')
            post.body = form.cleaned_data.get('body')
            post.save()
            for t in tags:
                post.tags.add(t)

    return render(request, "create_posts.html", {
        'form': form,
        'created': True
    })


def edit(request, id):
    post = get_object_or_404(Post, pk=id)  # to get specific post
    print(post.id)
    form = EditPostForm(request.POST or None, instance=post)
    context = {'form': form, 'edited': False, 'post': post}
    if request.method == 'GET':
        # form = PostForm(request.POST or None, instance=post)
        return render(
            request,
            "edit_posts.html", context)
    if request.method == 'POST':
        form = EditPostForm(request.POST or None, instance=post)
        if form.is_valid():
            post.status = 'dft'
            form.save()
        context = {'form': form, 'edited': True, 'post': post}      
    return render(request, "edit_posts.html", context)


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
