from django.db import models
from django.utils.text import slugify

# Create your models here.

# Publication


class ForumPost(models.Model):
	titlePost = models.CharField(max_length=50, blank=False)
	contentPost = models.TextField(blank=False)
	authorPost = models.CharField(max_length=100, blank=False)
	datePost = models.DateTimeField(auto_now_add=True)
	lastModification = models.DateTimeField(auto_now_add=True)
	slugPost = models.SlugField(blank=True)

	def __str__(self):
		return "{} - {} par {}".format(self.pk, self.titlePost, self.authorPost)

	def save(self, *args, **kwargs):
		if not self.slugPost:
			self.slugPost = slugify(self.pk, self.authorPost, self.titlePost)
		super().save(*args, **kwargs)


class PostComment(models.Model):
	contentComment = models.TextField(max_length=1000, blank=False)
	commentPost = models.ForeignKey(ForumPost, on_delete=models.CASCADE)
	commentedByUser = models.CharField(max_length=100, blank=False)

	def __str__(self):
		return "{}-{} {}".format(self.id, self.commentedByUser, self.commentPost)
