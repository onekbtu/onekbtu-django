from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from blog.views import PostViewSet

router = routers.DefaultRouter()
router.register('posts', PostViewSet, basename='posts-viewset')

urlpatterns = (
    url(r'', include(router.urls)),
)
