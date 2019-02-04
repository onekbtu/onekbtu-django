from django.contrib.auth import get_user_model
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=32)
    content = models.TextField(max_length=2000)

    @property
    def rating(self):
        qs = self.votes.all().aggregate(rating=models.Sum('type'))
        return qs['rating']


class Vote(models.Model):
    post = models.ForeignKey(Post, related_name='votes', on_delete=models.CASCADE)
    user = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)

    type = models.IntegerField(
        choices=(
            (1, 'like'),
            (-1, 'dislike'),
        )
    )
