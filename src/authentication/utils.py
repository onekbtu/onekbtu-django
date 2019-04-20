from datetime import datetime

from django.contrib.auth.models import User
from rest_framework_jwt.compat import get_username
from rest_framework_jwt.settings import api_settings


def jwt_payload_handler(user: User):
    return {
        'username': get_username(user),
        'exp': datetime.utcnow() + api_settings.JWT_EXPIRATION_DELTA
    }
