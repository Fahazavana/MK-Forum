from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Posts, PostComment

# Home View
class indexView(TemplateView):
    model = Posts
    template_name = "forum/index.html"
    context_object_name="posts"