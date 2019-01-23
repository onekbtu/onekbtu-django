from types import MappingProxyType

from blog.models import Post


def test_create_post_201(db, client):
    data = MappingProxyType(
        {
            'title': 'This is TDD',
            'content': 'TDD is important'
        }
    )
    response = client.post(path='/api/posts/', data=data, format='json')
    print(response.data)
    assert response.status_code == 201
    assert response.data['title'] == data['title']
    assert response.data['content'] == data['content']
    assert Post.objects.count() == 1
    post = Post.objects.last()
    assert post.title == data['title']
    assert post.content == data['content']
    assert post.id == response.data['id']


def test_list_posts_200(db, client, post):
    response = client.get(path='/api/posts/', format='json')
    assert response.status_code == 200
    assert response.data['results'][0]['id'] == post.id
    assert response.data['results'][0]['title'] == post.title
    assert response.data['results'][0]['content'] == post.content
