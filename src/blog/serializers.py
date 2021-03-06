from bleach import clean
from rest_framework import serializers

from blog.constants import MARKDOWN_ATTRS, MARKDOWN_TAGS
from blog.models import Post, Vote


class PostSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    rating = serializers.ReadOnlyField()
    vote = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'rating', 'vote')

    def validate_content(self, content):
        content = clean(
            content,
            tags=MARKDOWN_TAGS,
            attributes=MARKDOWN_ATTRS,
        )
        return content

    def get_vote(self, post) -> int:
        user = self.context['request'].user
        return getattr(
            Vote.objects.filter(post=post, user=user).last(),
            'vote_value',
            0
        ) if user.is_authenticated else 0


class VoteSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    vote_value = serializers.IntegerField(required=True)
    user = serializers.HiddenField(
        write_only=True,
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Vote
        fields = ('id', 'post', 'user', 'vote_value')

    def validate_vote_value(self, value: int) -> int:
        if value not in (-1, 1):
            raise serializers.ValidationError('Invalid vote vote_value')
        return value

    def create(self, validated_data) -> Vote:
        vote, created = Vote.objects.get_or_create(**validated_data)
        if not created:
            vote.delete()
        else:
            Vote.objects.filter(
                post=validated_data['post'],
                user=validated_data['user']
            ).exclude(id=vote.id).delete()
        return vote
