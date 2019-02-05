from django.contrib.auth.models import User
from factory.django import DjangoModelFactory


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    @classmethod
    def create_user(cls):
        return User.objects.create_user(
            username='muslimbeibytuly',
            password='Qwerty123'
        )
