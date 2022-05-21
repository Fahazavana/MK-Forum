from django.contrib import admin
from .models import Posts, PostComment

# Register your models here.
admin.site.register(Posts)
admin.site.register(PostComment)
