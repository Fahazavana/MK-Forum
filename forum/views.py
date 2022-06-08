from .forms import PostForm
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Post, PostComment
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# Home page View


class IndexView(ListView):
    """
        Home Page View
    """
    model = Post
    template_name = "forum/index.html"
    context_object_name = "Post"


class ReadPost(DetailView):
    """
        Post reading Post view
    """
    model = Post
    context_object_name = "Post"
    template_name = "forum/post_read.html"


# CREATE Post view
class CreatePost(LoginRequiredMixin, CreateView):
    """
        Post creation view
    """
    template_name = "forum/post_create.html"
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        form.instance.authorPost = self.request.user
        return super().form_valid(form)

# Update post View


class UpdatePost(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
        Update Post View
    """
    template_name = "forum/post_update.html"
    model = Post
    form_class = PostForm

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.authorPost:
            return True
        else:
            return False


class DeletePost(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
        Delete Post View
    """
    model = Post
    context_object_name = "Post"
    template_name = "forum/post_delete.html"
    success_url = reverse_lazy("forum_app:index")

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.authorPost:
            return True
        else:
            return False
