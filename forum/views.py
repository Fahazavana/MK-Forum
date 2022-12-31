from .forms import PostForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Post, PostComment, Reaction
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        Reaction = {'up': context['Post'].reaction_set.filter(up=1).count(
        ), 'down': context['Post'].reaction_set.filter(down=1).count()}
        context['Reaction'] = Reaction
        return context


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

# Adding reaction


@login_required
def reactOnPost(request, pk, reactionType):
    if request.method == "GET":
        post = Post.objects.get(pk=pk)
        try:
            reaction = post.reaction_set.get(
                reactedPost=pk, reactionAuthor=request.user)
            if (reactionType == 'up'):
                if (reaction.up == 0):
                    reaction.up = 1
                    if (reaction.down == 1):
                        reaction.down = 0
                elif (reaction.up == 1):
                    reaction.up = 0
            elif (reactionType == 'down'):
                if (reaction.down == 0):
                    reaction.down = 1
                    if (reaction.up == 1):
                        reaction.up = 0
                elif (reaction.down == 1):
                    reaction.down = 0
            reaction.save()

        #New Reaction
        except Reaction.DoesNotExist:
            if reactionType == "up":
                up, down = 1, 0
            elif vreactionType == "down":
                up, down = 0, 1
            reaction = Reaction(reactedPost=post, up=up,
                                down=down, reactionAuthor=request.user)
            reaction.save()
    return redirect("forum_app:read", pk)


@login_required
def commentPost(request, pk):
    if request.method == "POST":
        comment = request.POST['commentaire']
        if len(comment) > 0:
            author = request.user
            post = Post.objects.get(pk=pk)
            newcomment = PostComment(
                contentComment=comment, commentPost=post, commentAuthor=author)
            newcomment.save()
            return redirect("forum_app:read", pk)
        else:
            messages.warning(request, "Votre commentaire est vide!")
            return redirect("forum_app:read", pk)
    return redirect("forum_app:read", pk)
