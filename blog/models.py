from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.http import HttpResponseRedirect
from cloudinary.models import CloudinaryField
from taggit.managers import TaggableManager
from .validators import validate_url


class Author(models.Model):
    name = models.CharField(max_length=80)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}(author)"


class Post(models.Model):
    STATUS = (
        ('dft', 'Draft'),
        ('pub', 'Published'),
    )
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=200,
                            unique_for_date='published', blank=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts")
    tags = TaggableManager(
        help_text="We suggest to use no more than 3 tags to improve search results")  # noqa
    featured_image = CloudinaryField(
        'image', default='placeholder')  # upld from admin site
    list_image = models.CharField(blank=True, null=True, max_length=200,
                                  validators=[validate_url],
                                  help_text="Paste here a link ending with .jpg .gif .png",  # noqa
                                  verbose_name="Image")  # upld from blog
    excerpt = models.TextField(blank=True)
    body = models.TextField(blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    published = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, choices=STATUS, default='dft')
    likes = models.ManyToManyField(User,
                                   related_name='blogpost_like', blank=True)
    dislikes = models.ManyToManyField(User,
                                      related_name='blogpost_dislike',
                                      blank=True)

    class Meta:
        ordering = ["-published"]

    def approved_comments(self):
        comments = Comment.objects.filter(approved=True).filter(post=self.id)
        return len(comments)

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()

    def number_of_dislikes(self):
        return self.dislikes.count()

    def get_absolute_url(self):
        return HttpResponseRedirect(reverse('post_detail', args=[self.slug]))


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField(blank=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ["created"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
