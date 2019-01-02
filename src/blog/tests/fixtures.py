from pytest import fixture

from blog.models import Post


@fixture
def post():
    return Post.objects.create(title='LOL title', text='LOL text')
