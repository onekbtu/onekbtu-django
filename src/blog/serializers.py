from rest_framework import serializers

from blog.models import Post


class PostSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Post
        fields = ('id', 'title', 'content')
