from rest_framework import permissions, viewsets

from blog.models import Post
from blog.serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    http_method_names = ('post', 'get')

    class Meta:
        model = Post
