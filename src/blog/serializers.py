from rest_framework import serializers

from blog.models import Post, Vote


class PostSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'rating', )


class VoteSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Vote
        fields = ('id', 'post', 'user',)
