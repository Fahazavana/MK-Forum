from django.db import models
from users.models import User
from django.urls import reverse

# Create your models here.

# Post models


class Post(models.Model):
    titlePost = models.CharField(max_length=50, blank=False)
    contentPost = models.TextField(blank=False)
    authorPost = models.ForeignKey(User, on_delete=models.CASCADE)
    datePost = models.DateTimeField(auto_now=True)
    lastModificationPost = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} - {} par {}".format(self.pk, self.titlePost, self.authorPost)

    def get_absolute_url(self):
        return reverse("forum_app:read", kwargs={'pk': self.pk})


class PostComment(models.Model):
    contentComment = models.TextField(max_length=1000, blank=False)
    commentPost = models.ForeignKey(Post, on_delete=models.CASCADE)
    commentAuthor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "{}-{} {}".format(self.id, self.commentedByUser, self.commentPost)

class Reaction(models.Model):
    up = models.IntegerField(default=0)
    down = models.IntegerField(default=0)
    reactedPost = models.ForeignKey(Post, on_delete=models.RESTRICT)
    reactionAuthor = models.ForeignKey(User, on_delete=models.CASCADE)
    reactionDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Reaction de {} sur {}".format(self.voteAuthor, self.votedPost)