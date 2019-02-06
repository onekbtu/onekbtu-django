from bleach import clean
from rest_framework import serializers

from blog.constants import MARKDOWN_ATTRS, MARKDOWN_TAGS
from blog.models import Post, Vote


class PostSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    rating = serializers.IntegerField(read_only=True)
    vote = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'rating', 'vote',)

    def validate_content(self, content):
        content = clean(
            content,
            tags=MARKDOWN_TAGS,
            attributes=MARKDOWN_ATTRS,
        )
        return content

    def get_vote(self, post):
        user = self.context['request'].user
        if not user or not user.is_authenticated:
            return 0
        vote = Vote.objects.filter(user=user, post=post)
        if len(vote) > 0:
            return vote[len(vote)-1].type
        return 0


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
