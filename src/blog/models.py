from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=32)
    text = models.TextField(max_length=128)
