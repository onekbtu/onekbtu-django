from types import MappingProxyType

from django.contrib.auth import get_user_model
from rest_framework.exceptions import ErrorDetail

from blog.models import Post, Vote


def test_create_post_201(db, client):
    data = MappingProxyType(
        {
            'title': 'This is TDD',
            'content': 'TDD is important'
        }
    )
    response = client.post(path='/api/posts/', data=data, format='json')
    assert response.status_code == 201
    assert response.data['title'] == data['title']
    assert response.data['content'] == data['content']
    assert Post.objects.count() == 1
    post = Post.objects.last()
    assert post.title == data['title']
    assert post.content == data['content']
    assert post.id == response.data['id']


def test_create_post_sanitize_201(db, client):
    data = MappingProxyType(
        {
            'title': 'This is TDD',
            'content': 'Hello from xss :D <script>alert("hi")</script><img src="google.com">',
        }
    )
    expected_content = 'Hello from xss :D &lt;script&gt;alert("hi")&lt;/script&gt;<img src="google.com">'
    response = client.post(path='/api/posts/', data=data, format='json')
    assert response.status_code == 201
    assert response.data['title'] == data['title']
    assert response.data['content'] == expected_content
    assert Post.objects.count() == 1
    post = Post.objects.last()
    assert post.title == data['title']
    assert post.content == expected_content
    assert post.id == response.data['id']


def test_list_posts_200(db, client, post):
    response = client.get(path='/api/posts/', format='json')
    assert response.status_code == 200
    assert response.data['results'][0]['id'] == post.id
    assert response.data['results'][0]['title'] == post.title
    assert response.data['results'][0]['content'] == post.content
    assert response.data['results'][0]['rating'] == 0
    assert response.data['results'][0]['vote'] == 0


def test_like_201(db, client_with_token, post):
    data = MappingProxyType(
        {
            'post': post.id,
            'vote_value': 1
        }
    )
    assert Post.objects.last().rating == 0
    response = client_with_token.post(path='/api/votes/', data=data, format='json')
    assert response.status_code == 201
    assert response.data == {
        'id': 1,
        'post': Post.objects.last().id,
        'vote_value': 1
    }
    assert Vote.objects.count() == 1
    assert Post.objects.count() == 1
    assert Post.objects.last().rating == 1


def test_delete_vote_201(db, client_with_token, post):
    Vote.objects.create(user=get_user_model().objects.last(), post=post, vote_value=1)
    assert Vote.objects.count() == 1
    assert Post.objects.last().rating == 1
    data = MappingProxyType(
        {
            'post': post.id,
            'vote_value': 1
        }
    )
    response = client_with_token.post(path='/api/votes/', data=data, format='json')
    assert response.status_code == 201
    assert response.data == {
        'id': None,
        'post': post.id,
        'vote_value': 1
    }
    assert Vote.objects.count() == 0
    assert Post.objects.last().rating == 0


def test_dislike_201(db, client_with_token, post):
    Vote.objects.create(user=get_user_model().objects.last(), post=post, vote_value=1)
    assert Vote.objects.count() == 1
    assert Post.objects.last().rating == 1
    data = MappingProxyType(
        {
            'post': post.id,
            'vote_value': -1
        }
    )
    response = client_with_token.post(path='/api/votes/', data=data, format='json')
    assert response.status_code == 201
    assert response.data == {
        'id': Vote.objects.last().id,
        'post': post.id,
        'vote_value': -1
    }
    assert Vote.objects.count() == 1
    assert Post.objects.last().rating == -1


def test_create_vote_400_incorrect_vote_value(db, client_with_token, post):
    data = MappingProxyType(
        {
            'post': post.id,
            'vote_value': 2
        }
    )
    response = client_with_token.post(path='/api/votes/', data=data, format='json')
    assert response.status_code == 400
    assert response.data['vote_value'] == [ErrorDetail(string='Invalid vote vote_value', code='invalid')]
