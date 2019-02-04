from django.contrib import admin

from blog.models import Post, Vote

admin.site.register(Post)
admin.site.register(Vote)
