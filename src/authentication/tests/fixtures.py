from types import MappingProxyType

from pytest import fixture
from rest_framework.test import APIClient

from authentication.tests.factories import UserFactory


@fixture
def client_with_token(client):
    UserFactory.create_user()
    data = MappingProxyType(
        {
            'username': 'muslimbeibytuly',
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
