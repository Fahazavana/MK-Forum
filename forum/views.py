from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from .models import Posts, PostComment
from .forms import postForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Home page View


class indexView(ListView):
    model = Posts
    template_name = "forum/index.html"
    context_object_name = "posts"

#READ Post View

class readPost(DetailView):
    model = Posts
    context_object_name = "posts"
    template_name = "forum/read.html"


class createPost(LoginRequiredMixin, CreateView):
    template_name = "forum/post_cu.html"
    model = Posts
    form_class = postForm

    def form_valid(self, form):
        form.instance.authorPost = self.request.user
        return super().form_valid(form)
