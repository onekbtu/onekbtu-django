from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=32)
    content = models.TextField(max_length=128)
    rating = models.IntegerField(default=0)


class Vote(models.Model):
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    type = models.IntegerField(choices=(
        (1, 'like'),
        (-1, 'dislike'),
    ))

    class Meta:
        unique_together = ('post', 'user')
