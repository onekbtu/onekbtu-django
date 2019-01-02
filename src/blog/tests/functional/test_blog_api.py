from types import MappingProxyType

from blog.models import Post


def test_create_post_201(db, client):
    data = MappingProxyType(
        {
            'title': 'This is TDD',
            'text': 'TDD is important'
        }
    )
    response = client.post(path='/api/posts/', data=data, format='json')
    assert response.status_code == 201
    assert response.data['title'] == data['title']
    assert response.data['text'] == data['text']
    assert Post.objects.count() == 1
    assert Post.objects.last().title == data['title']
    assert Post.objects.last().text == data['text']


def test_list_posts_200(db, client, post):
    response = client.get(path='/api/posts/', format='json')
    assert response.status_code == 200
    assert response.data[0]['title'] == post.title
    assert response.data[0]['text'] == post.text
