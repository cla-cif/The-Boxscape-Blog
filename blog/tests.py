from django.test import TestCase, Client, SimpleTestCase
import unittest
from django.urls import reverse, resolve
from .models import Post
from .views import PostList


class TestModels(TestCase):
    def test_model_str(self):
        title = Post.objects.create(title="This is the blog title")
        self.assertEqual(str(title), "This is the blog title")


# class TestBlogUrls(SimpleTestCase):
    
#     def test_home_url_is_resolved(self):
#         url = reverse('home')
#         self.assertEquals(resolve(url).func.view_class, PostList)




