# Test bulletin_board app.

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from .models import Post

class PostModelTest(TestCase):

    def setUp(self):
        Post.objects.create(title="Test Post", content="This is a test post.")

    def test_post_creation(self):
        post = Post.objects.get(id=1)
        self.assertEqual(post.title, "Test Post")
        self.assertEqual(post.content, "This is a test post.")

class PostViewTest(TestCase):

    def setUp(self):
        self.post = Post.objects.create(title="Test Post", content="This is a test post.")

    def test_post_list_view(self):
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Post")

    def test_post_detail_view(self):
        response = self.client.get(reverse('post_detail', args=[self.post.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Post")
        self.assertContains(response, "This is a test post")
