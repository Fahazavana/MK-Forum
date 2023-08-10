from django.contrib import admin
from .models import Post, PostComment,Reaction,ReactionComment

# Register your models here.
admin.site.register(Post)
admin.site.register(PostComment)
admin.site.register(Reaction)
admin.site.register(ReactionComment)
