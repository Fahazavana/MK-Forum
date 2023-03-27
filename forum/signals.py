from django.db.models.signals import post_save,pre_save
from django.contrib.auth.models import User
from django.dispatch.dispatcher import receiver
from .models import PostComment, Post
import mdtex2html



@receiver(pre_save, sender=Post,dispatch_uid="post_md_to_html")
def create_html_post(sender, instance,**kwargs):
    """
        Generate the pocessed MarkDown Html
    """
    print(instance.contentPost)
    instance.contentPostHTML = mdtex2html.convert(instance.contentPost)
    #instance.save()

@receiver(pre_save, sender=PostComment,dispatch_uid="postcomment_md_to_html")
def create_html_post(sender, instance,**kwargs):
    """
        Generate the pocessed MarkDown Html
    """
    instance.contentCommentHTML = mdtex2html.convert(instance.contentComment)
