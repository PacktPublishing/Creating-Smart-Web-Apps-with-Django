from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from blog.models import Blogpost

# Create your tests here.


class BlogpostViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='foobar'
        )

        Blogpost.objects.create(title='test post 1', user=self.user, body='this is a test post')
        Blogpost.objects.create(title='test post 2', user=self.user, body='this is another test post')

        self.client = Client()
        self.url = reverse('posts')

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

        data = response.context_data['posts']

        self.assertEqual(len(data), 2)
        self.assertEqual(data[0], {
            'id': 1,
            'title': 'test post 1',
            'author': self.user.username,
        })
        self.assertEqual(data[1], {
            'id': 2,
            'title': 'test post 2',
            'author': self.user.username,
        })
