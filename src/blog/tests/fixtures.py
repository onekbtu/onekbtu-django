from django.contrib.auth.models import User
from pytest import fixture

from ..models import Post


@fixture
def post():
    return Post.objects.create(title='LOL title', content='LOL content')
