from django.db import models


def sum_all(*args):
    return sum((x for x in args))


class Post(models.Model):
    title = models.CharField(max_length=32)
    text = models.TextField(max_length=128)
