from django.contrib.auth import get_user_model
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=32)
    content = models.TextField(max_length=2048)

    @property
    def rating(self):
        qs = self.votes.all().aggregate(rating=models.Sum('type'))
        return qs['rating'] or 0


class Vote(models.Model):
    TYPE_CHOICES = (
        (1, 'like'),
        (-1, 'dislike'),
    )

    post = models.ForeignKey('blog.Post', related_name='votes', on_delete=models.CASCADE)
    user = models.ForeignKey(to=get_user_model(), related_name='votes', on_delete=models.CASCADE)
    type = models.IntegerField(choices=TYPE_CHOICES)
