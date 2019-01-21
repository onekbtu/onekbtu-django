from django.contrib.auth.models import User


def test_obtain_jwt_token_200(db, client):
    User.objects.create_user(username='muslimbeibytuly', email='muslimbeibytuly@gmail.com', password='Qwerty123')
    assert User.objects.count() == 1
    data = {
        'username': 'muslimbeibytuly',
        'password': 'Qwerty123'
    }
    response = client.post('/api/auth/login/', data)
    assert response.data.get('token') is not None
