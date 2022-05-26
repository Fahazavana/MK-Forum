from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Posts, PostComment
from .forms import postForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Home page View


class indexView(ListView):
    model = Posts
    template_name = "forum/index.html"
    context_object_name = "posts"

#READ Post View

class readPost(DetailView):
    model = Posts
    context_object_name = "post"
    template_name = "forum/post_read.html"


# CREATE Post view
class createPost(LoginRequiredMixin, CreateView):
    template_name = "forum/post_create.html"
    model = Posts
    form_class = postForm

    def form_valid(self, form):
        form.instance.authorPost = self.request.user
        return super().form_valid(form)

# Update post View


class updatePost(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "forum/post_update.html"
    model = Posts
    form_class = postForm

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.authorPost:
            return True
        else:
            return False


# Delete Post View

class deletePost(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Posts
    context_object_name = "post"
    template_name = "forum/post_delete.html"
    success_url = reverse_lazy("forum_app:index")

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.authorPost:
            return True
        else:
            return False
