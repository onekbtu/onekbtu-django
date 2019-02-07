from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase

from blog.models import Post, Vote


class VoteViewTest(APITestCase):

    def setUp(self):
        self.client.post(
            path='/api/posts/',
            data={
                'title': 'this is test post',
                'content': 'this is test post content'
            },
        )
        self.user = get_user_model().objects.create_user(username='user1', password='Pas$w0rd')
        response = self.client.post(
            '/api/auth/login/',
            {
                'username': 'user1',
                'password': 'Pas$w0rd'
            }
        )
        token = response.data.get('token')
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token)

    def test_create_vote_201(self):
        response = self.client.post(
            path='/api/votes/',
            data={
                'post': Post.objects.last().id,
                'vote_value': 1
            },
        )
        self.assertEqual(response.status_code, 201)
        self.assertTrue(Vote.objects.exists())

    def test_create_vote_invalid_post_400(self):
        response = self.client.post(
            path='/api/votes/',
            data={
                'post': 'asdas',
                'vote_value': '2',
            },
            format='json',
        )
        self.assertEqual(response.status_code, 400)

    def test_create_vote_invalid_vote_value_400(self):
        response = self.client.post(
            path='/api/votes/',
            data={
                'post': 5,
                'vote_value': 2,
            },
            format='json'
        )
        self.assertEqual(response.status_code, 400)

    def test_post_rating_201(self):
        response = self.client.post(
            path='/api/votes/',
            data={
                'post': Post.objects.last().id,
                'vote_value': 1
            },
            format='json'
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Post.objects.last().rating, 1)

        response = self.client.post(
            path='/api/votes/',
            data={
                'post': Post.objects.last().id,
                'vote_value': -1
            },
            format='json'
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Post.objects.last().rating, -1)
