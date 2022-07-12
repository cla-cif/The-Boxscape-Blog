from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.core.mail import send_mail
from django.views.generic import TemplateView, CreateView, DeleteView
from taggit.models import Tag
from django.db.models import Count
import cloudinary
from cloudinary.models import CloudinaryField
from cloudinary.forms import cl_init_js_callbacks
from django.contrib.auth.models import User
from .models import Post, Comment
from .forms import CommentForm, PostForm, EditPostForm, EditCommentForm


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
        # create comment
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


def post_create(request):
    form = PostForm()
    context = {'form': form, 'created': False, }
    if request.method == 'GET':
        return render(
            request,
            "post_create.html", context)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            post.author = request.user
            post.slug = '-'.join(form.cleaned_data.get('title').split(' '))
            post.title = form.cleaned_data.get('title')
            tags = form.cleaned_data.get('tags')
            # post.image = cloudinary.uploader.upload(request.FILES['featured_image'])
            post.excerpt = form.cleaned_data.get('excerpt')
            post.body = form.cleaned_data.get('body')
            post.save()
            for t in tags:
                post.tags.add(t)

    return render(request, "post_create.html", {
        'form': form,
        'created': True
    })


def post_edit(request, id):
    post = get_object_or_404(Post, pk=id)
    form = EditPostForm(request.POST or None, instance=post)
    context = {'form': form, 'edited': False, 'post': post}
    if request.method == 'GET':
        return render(
            request,
            "post_edit.html", context)
    if request.method == 'POST':
        form = EditPostForm(request.POST or None, instance=post)
        if form.is_valid():
            post.status = 'dft'
            form.save()
        context = {'form': form, 'edited': True, 'post': post}
    return render(request, "post_edit.html", context)


def comment_edit(request, id):
    comment = get_object_or_404(Comment, pk=id)
    edit_form = EditCommentForm(request.POST or None, instance=comment)
    if request.method == 'GET':
        context = {'edit_form': edit_form, 'comment': comment}
        print(edit_form)
        return render(request, 'detail.html', context)
    if request.method == 'POST':
        comment = get_object_or_404(Comment, pk=id)
        if edit_form.is_valid():
            edit_form.save()
        context = {'edit_form': edit_form, 'comment': comment}
        return render(request, 'detail.html', context)
        
    
def comment_delete(request, id):
    if request.method == 'POST':
        comment = get_object_or_404(Comment, pk=id)
        comment.delete()
    return HttpResponseRedirect('post_detail')


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



class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'featured_image', 'excerpt', 'body']
    template_name = "post_create.html"