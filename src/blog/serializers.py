from rest_framework import serializers

from blog.models import Post, Vote


class PostSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'rating', )


class VoteSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = Vote
        fields = ('id', 'post', 'user', 'type')

    def create(self, validated_data):
        """
        creates vote
        if vote exists, updates it
        """
        validated_data['user'] = self.context.get('request').user

        Vote.objects.filter(user=validated_data['user'], post=validated_data['post']).delete()
        vote = Vote.objects.get_or_create(**validated_data)[0]
        return self.update(vote, validated_data)

    def update(self, instance, validated_data):
        instance.type = validated_data.get('type', instance.type)
        instance.save()
        return instance
