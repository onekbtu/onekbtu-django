from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token

from authentication.views import RegisterAPIView

urlpatterns = (
    path(route='auth/login/', view=obtain_jwt_token),
    path(route='auth/register/', view=RegisterAPIView.as_view())
)
