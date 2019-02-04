from django.urls import include, path
from rest_framework import routers

from blog.views import PostViewSet, VoteViewSet

router = routers.DefaultRouter()
router.register('posts', PostViewSet, basename='posts-viewset')
router.register('votes', VoteViewSet, basename='votes-viewset')

urlpatterns = (
    path('', include(router.urls)),
)
