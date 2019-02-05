from types import MappingProxyType

from django.contrib.auth.models import User


def test_register_201(db, client):
    data = MappingProxyType(
        {
            'username': 'muslimbeibytuly',
            'email': 'muslimbeibytuly@gmail.com',
            'password': 'Qwerty123'
        }
    )
    response = client.post('/api/auth/register/', data)
    assert response.status_code == 201
    assert response.data == MappingProxyType(
        {
            'username': 'muslimbeibytuly',
            'email': 'muslimbeibytuly@gmail.com'
        }
    )
    assert User.objects.count() == 1
    user = User.objects.last()
    assert user.username == 'muslimbeibytuly'
    assert user.email == 'muslimbeibytuly@gmail.com'


def test_obtain_jwt_token_200(db, client, user):
    data = MappingProxyType(
        {
            'username': 'muslimbeibytuly',
            'password': 'Qwerty123'
        }
    )
    response = client.post('/api/auth/login/', data)
    assert response.data.get('token') is not None
