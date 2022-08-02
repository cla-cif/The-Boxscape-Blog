from django.test import TestCase, Client, SimpleTestCase
from django.urls import reverse, resolve
from django.core.exceptions import ValidationError
import unittest
from model_bakery import baker
from pprint import pprint
from .models import Post, Comment
from .views import PostList, PostDetail, post_create, contact_us


class TestPostModel(TestCase):
    def setUp(self):
        self.post = baker.make('Post')
        # pprint(self.post.__dict__)

    def test_post_delete(self):
        pk = self.post.pk
        get_post = Post.objects.get(pk=pk)
        get_post.delete()
        self.assertFalse(Post.objects.filter(pk=pk).exists())

    def test_model(self):
        self.assertIsInstance(self.post, Post)


class TestCommentModel(TestCase):
    def setUp(self):
        self.comment = baker.make('Comment')
        # pprint(self.comment.__dict__)

    def test_comment_delete(self):
        pk = self.comment.pk
        get_comment = Comment.objects.get(pk=pk)
        get_comment.delete()
        self.assertFalse(Comment.objects.filter(pk=pk).exists())

    def test_model(self):
        self.assertIsInstance(self.comment, Comment)


class TestBlogUrls(SimpleTestCase):
    def test_home_url_is_resolved(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func.view_class, PostList)

    def test_postdetail_url_is_resolved(self):
        url = reverse('post_detail', args=[1])
        self.assertEquals(resolve(url).func.view_class, PostDetail)

    def test_postcreate_url_is_resolved(self):
        url = reverse('post_create')
        self.assertEquals(resolve(url).func, post_create)

    def test_contact_url_is_resolved(self):
        url = reverse('contact')
        self.assertEquals(resolve(url).func, contact_us)


class TestBlogViews(TestCase):
    def setUp(self):
        self.client = Client()

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'list.html')

    def test_createpost_view(self):
        response = self.client.get(reverse('post_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_create.html')

    def test_contactus_view(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact_us.html')


class TestUrlValidation(TestCase):
    def test_image_url_validation_failed(self):
        # response = self.client.post('/post_create/', data={'list_image': 'https://www.google.com/'})
        with self.assertRaisesRegex(ValidationError,
                               'Unsupported file extension.',
                               response,
                               'https://www.google.com/')
