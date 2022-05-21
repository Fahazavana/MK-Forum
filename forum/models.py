from django.db import models
from users.models import User
from django.utils.text import slugify

# Create your models here.

# Post models


class Posts(models.Model):
	titlePost = models.CharField(max_length=50, blank=False)
	contentPost = models.TextField(blank=False)
	authorPost = models.ForeignKey(User, on_delete=models.CASCADE)
	datePost = models.DateTimeField(auto_now=True)
	lastModificationPost = models.DateTimeField(auto_now=True)
	slugPost = models.SlugField(blank=True)

	def __str__(self):
		return "{} - {} par {}".format(self.pk, self.titlePost, self.authorPost)

	def save(self, *args, **kwargs):
		if not self.slugPost:
			self.slugPost = slugify(self.pk, self.authorPost)
		super().save(*args, **kwargs)


class PostComment(models.Model):
	contentComment = models.TextField(max_length=1000, blank=False)
	commentPost = models.ForeignKey(Posts, on_delete=models.CASCADE)
	commentAuthor = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return "{}-{} {}".format(self.id, self.commentedByUser, self.commentPost)
