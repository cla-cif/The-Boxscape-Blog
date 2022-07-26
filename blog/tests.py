from django.test import TestCase, Client
# from users.models import User
from .models import Post, Comment, Author






# TEST NOT WORKING
# class TestModels(TestCase):
#     def test_model_str(self):
#         t = Post.objects.create(title="This is the post title")
#         a = Author.objects.create(user="Jane")
#         c = Comment.objects.create(body="This is the comment body")
#         n = Comment.objects.create(name="John")
#         self.assertEqual(str(t), "This is a title")
#         self.assertEqual(str(a), "This is an author")
#         self.assertEqual(str(c), "This is a comment")
#         self.assertEqual(str(n), "This is a name")

# TEST NOT WORKING
# class PostTest(TestCase):
#     """Testing class for posts"""
#     def test_post_create_validation_failed(self):
#         """This test checks the validation process and message by entering an empty post"""
#         res = self.client.post('/create', {'title': '', 'body': ''})
#         assert b'This field is required' in res.content

