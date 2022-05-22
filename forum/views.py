from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Posts, PostComment

# Home View


class indexView(ListView):
    model = Posts
    template_name = "forum/index.html"
    context_object_name = "posts"


class readPost(DetailView):
    model = Posts
    context_object_name = "posts"
    template_name = "forum/read.html"
