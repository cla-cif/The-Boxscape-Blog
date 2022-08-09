from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse, BadHeaderError
from django.core.mail import send_mail
from django.views.generic import TemplateView, DeleteView
from django.db.models import Count
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Post, Comment, Author
from .forms import CommentForm, PostForm, EditPostForm, EditCommentForm, ContactForm  # noqa


# ABOUT THE BLOG
class AboutView(TemplateView):
    template_name = "./about.html"


# LIST VIEW
class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status='pub')
    template_name = "list.html"
    paginate_by = 9


# DETAIL VIEW
class PostDetail(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status='pub')
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("created")
        # display number of approved comments
        number_comments = len(comments)
        # fetch post by similarity
        post_tags_ids = post.tags.values_list('id', flat=False)
        similar_posts = Post.objects.filter(tags__in=post_tags_ids)
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
                "number_comments": number_comments,
                "commented": False,
                "liked": liked,
                "disliked": disliked,
                "comment_form": CommentForm(),
                "similar_posts": similar_posts
            },
        )

    def post(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status='pub')
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("created")
        # display number of approved comments
        number_comments = len(comments)
        # retrieving post by similarity
        post_tags_ids = post.tags.values_list('id', flat=True)
        print(post_tags_ids)
        similar_posts = Post.objects.filter(tags__in=post_tags_ids)
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
                "number_comments": number_comments,
                "comment_form": comment_form,
                "liked": liked,
                "disliked": disliked,
                "similar_posts": similar_posts
            },
        )


# ALL POSTS UNDER THE SAME TAG
def tag(request, slug):
    post = Post.objects.filter(tags__slug=slug)
    return render(request, 'list.html', {"post_list": post, "tag": slug})


# ALL POSTS FROM THE SAME AUTHOR
def author_posts(request, pk):
    author = User.objects.get(pk=pk)
    post = Post.objects.filter(author=author)
    return render(request, 'list.html', {'post_list': post, "author": author})


# POST LIKE
class PostLike(View):

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


# POST DISLIKE
class PostDislike(View):

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.dislikes.filter(id=request.user.id).exists():
            post.dislikes.remove(request.user)
        else:
            post.dislikes.add(request.user)
        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


# POST CREATE
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
            post = Post()
            post.author = request.user
            # remove special chars and set to lowercase for better SEO
            post.slug = '-'.join(form.cleaned_data.get('title')
                                 .replace("'", '').replace('-', '')
                                 .split(' '))
            post.slug = post.slug.lower()
            post.title = form.cleaned_data.get('title')
            tags = form.cleaned_data.get('tags')
            post.list_image = form.cleaned_data.get('list_image')
            post.excerpt = form.cleaned_data.get('excerpt')
            post.body = form.cleaned_data.get('body')
            post.save()
            post_author = Author(name=request.user.first_name,
                                 user=request.user)
            post_author.save()
            for t in tags:
                post.tags.add(t.lower())
        else:
            form = PostForm(request.POST, request.FILES)
            return render(request, 'post_create.html', {
                'form': form,
                'created': False,
            })
    return render(request, "post_create.html", {
        'form': form,
        'created': True,
    })


# POST EDIT
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
        else:
            form = EditPostForm(request.POST or None, instance=post)
            return render(request, 'post_edit.html', {
                'form': form,
                'edited': False,
                'post': post,
            })
        context = {'form': form, 'edited': True, 'post': post}
    return render(request, "post_edit.html", context)


# POST DELETE
class TestView(DeleteView):

    model = Post
    success_url = reverse_lazy('home')
    template_name = "post_create.html"


# COMMENT EDIT
def comment_edit(request, id):
    comment = get_object_or_404(Comment, pk=id)
    form = EditCommentForm(request.POST or None, instance=comment)
    context = {'form': form, 'edited': False, 'comment': comment}
    if request.method == 'GET':
        return render(
            request,
            "comment_edit.html", context)
    if request.method == 'POST':
        form = CommentForm(request.POST or None, instance=comment)
        if form.is_valid():
            comment.approved = False
            form.save()
        context = {'form': form, 'edited': True, 'comment': comment}
    return render(request, "comment_edit.html", context)


# COMMENT DELETE
def comment_delete(request, id, *args):
    if request.method == 'POST':
        comment = get_object_or_404(Comment, pk=id)
        comment.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


# CONTACT FORM
def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Contact us"
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())
        try:
            send_mail(subject, message, 'the.boxscape.blog@gmail.com',
                      ['the.boxscape.blog@gmail.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        messages.success(request, "Message sent.")
        return redirect('home')
    form = ContactForm()
    return render(request, "contact_us.html", {'form': form})
