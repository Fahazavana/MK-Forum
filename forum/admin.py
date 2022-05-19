from django.contrib import admin
from .models import ForumPost, PostComment

# Register your models here.
admin.site.register(ForumPost)
admin.site.register(PostComment)
