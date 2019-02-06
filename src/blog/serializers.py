from rest_framework import serializers

from blog.models import Post, Vote


class PostSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    rating = serializers.IntegerField(read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'rating',)


class VoteSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    type = serializers.IntegerField(required=True)
    user = serializers.HiddenField(
        write_only=True,
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Vote
        fields = ('id', 'post', 'user', 'type')

    def validate_type(self, type):
        if type not in (-1, 1):
            raise serializers.ValidationError('Invalid vote type')
        return type

    def create(self, validated_data):
        vote, created = Vote.objects.get_or_create(**validated_data)
        if not created:
            vote.delete()
            return vote
        return vote
