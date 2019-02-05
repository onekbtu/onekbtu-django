from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Post(models.Model):
    title = models.CharField(max_length=32)
    content = models.TextField(max_length=2048)
    rating = models.IntegerField(default=0)


class Vote(models.Model):
    TYPE_CHOICES = (
        (1, 'like'),
        (-1, 'dislike'),
    )

    post = models.ForeignKey('blog.Post', related_name='votes', on_delete=models.CASCADE)
    user = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)
    type = models.IntegerField(choices=TYPE_CHOICES)

    class Meta:
        unique_together = ('post', 'user')


@receiver(post_save, sender=Vote)
def post_save_vote(sender, instance: Vote, created, **kwargs):
    if created:
        post = instance.post
        post.rating += instance.type
        post.save()
