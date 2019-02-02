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
        user = request.user
        try:
            type = int(request.data.get('type'))
            post_pk = int(request.data.get('post'))
            if type != -1 and type != 1:
                return Response({
                    'errors': [
                        'Vote type must be either 1 or -1'
                    ]},
                    status=status.HTTP_405_METHOD_NOT_ALLOWED,
                )
            post = Post.objects.get(pk=post_pk)
            vote = Vote.objects.filter(post=post, user=user)

            if not len(vote):
                vote = Vote.objects.create(post=post, user=user, type=type)
            else:
                vote = vote[0]
                post.rating -= vote.type
                vote.type = type

            post.rating += vote.type

            post.save()
            vote.save()

            return Response({'rating': post.rating}, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({}, status=status.HTTP_400_BAD_REQUEST)
