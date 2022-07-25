from django.test import TestCase, Client
from users.models import User
from .models import Post, Comment, Author


class PostTest(TestCase):
    """Testing class for posts"""
    def test_post_create_validation_failed(self):
        """This test checks the validation process and message by entering an empty post"""
        res = self.client.post('/create', {'title': '', 'body': ''})
        assert b'This field is required' in res.content