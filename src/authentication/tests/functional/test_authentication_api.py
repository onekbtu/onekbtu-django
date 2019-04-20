from types import MappingProxyType

from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.test import Client
from rest_framework.response import Response


def test_register_201(db, client: Client) -> None:
    data = MappingProxyType(
        {
            'username': 'muslimbeibytuly',
            'email': 'muslimbeibytuly@gmail.com',
            'password': 'Qwerty123'
        }
    )
    response: Response = client.post(path='/api/auth/register/', data=data)
    assert response.status_code == 201
    assert response.data == MappingProxyType(
        {
            'username': 'muslimbeibytuly',
            'email': 'muslimbeibytuly@gmail.com'
        }
    )
    assert get_user_model().objects.count() == 1
    user = get_user_model().objects.last()
    assert user.username == 'muslimbeibytuly'
    assert user.email == 'muslimbeibytuly@gmail.com'


def test_obtain_jwt_token_200(db, client: Client, user: User) -> None:
    data = MappingProxyType(
        {
            'username': 'muslimbeibytuly', 'password': 'Qwerty123'
        }
    )
    response = client.post(path='/api/auth/login/', data=data)
    assert response.data.get('token') is not None
