from copy import deepcopy

from rest_framework import permissions, status, viewsets
from rest_framework.response import Response

from .models import Post, Vote
from .serializers import PostSerializer, VoteSerializer


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    serializer_class = PostSerializer
    queryset = Post.objects.order_by('-id').all()
    http_method_names = ('post', 'get')

    class Meta:
        model = Post


class VoteViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = VoteSerializer
    http_method_names = ('post',)

    class Meta:
        model = Vote

    def create(self, request, *args, **kwargs):
        data = deepcopy(request.data)
        data['user'] = request.user.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
