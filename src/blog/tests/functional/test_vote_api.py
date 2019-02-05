from django.contrib.auth.models import User
from rest_framework.test import APITestCase

from blog.models import Post, Vote


class VoteViewTest(APITestCase):

    def setUp(self):
        self.client.post(
            path='/api/posts/',
            data={
                'title': 'this is test post',
                'content': 'this is test post content',
            },
        )
        self.user = User.objects.create_user('user1', 'user1@mail.ru', 'Pas$w0rd')
        response = self.client.post('/api/auth/login/', {'username': 'user1', 'password': 'Pas$w0rd'})
        token = response.data.get('token')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)

    def test_create_vote_201(self):
        response = self.client.post(
            path='/api/votes/',
            data={
                'post': 1,
                'type': 1,
            },
        )
        self.assertEqual(response.status_code, 201)
        self.assertTrue(Vote.objects.exists())

    def test_create_vote_invalid_post_400(self):
        response = self.client.post(
            path='/api/votes/',
            data={
                'post': 'asdas',
                'type': '2',
            },
            format='json',
        )
        self.assertEqual(response.status_code, 400)

    def test_create_vote_invalid_type_400(self):
        response = self.client.post(
            path='/api/votes/',
            data={
                'post': 5,
                'type': 2,
            },
            format='json',
        )
        self.assertEqual(response.status_code, 400)

    def test_post_rating(self):
        response = self.client.post(
            path='/api/votes/',
            data={
                'post': 1,
                'type': 1,
            },
            format='json',
        )
        self.assertEqual(response.status_code, 201)

        post = Post.objects.get(pk=1)
        self.assertEqual(post.rating, 1)

        response = self.client.post(
            path='/api/votes/',
            data={
                'post': 1,
                'type': -1,
            },
            format='json',
        )
        print(response.content)
        self.assertEqual(response.status_code, 201)

        post = Post.objects.get(pk=1)
        self.assertEqual(post.rating, 0)
