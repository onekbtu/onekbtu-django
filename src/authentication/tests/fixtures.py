from types import MappingProxyType

from django.contrib.auth import get_user_model
from pytest import fixture
from rest_framework.test import APIClient


@fixture
def user():
    return get_user_model().objects.create_user(
        username='muslimbeibytuly',
        email='muslimbeibytuly@gmail.com',
        password='Qwerty123'
    )


@fixture
def client_with_token(client):
    get_user_model().objects.create_user(
        username='russiandoll',
        email='russiandoll@mail.ru',
        password='Qwerty123'
    )
    data = MappingProxyType(
        {
            'username': 'russiandoll',
            'password': 'Qwerty123'
        }
    )
    response = client.post(path='/api/auth/login/', data=data, format='json')
    token = response.data['token']
    authenticated_client = APIClient()
    authenticated_client.credentials(
        HTTP_AUTHORIZATION='JWT {}'.format(token)
    )
    return authenticated_client
