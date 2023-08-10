from django.forms import ModelForm
from django.forms import Textarea, TextInput
from .models import Post, PostComment


class PostForm(ModelForm):
    # overwride default
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['titlePost'].widget.attrs = {
            'class': 'form-control mb-3 mod-input text-white post-title', 'placeholder': "Titre"}
        self.fields['contentPost'].widget.attrs = {
            'class': "form-control mb-3",
            'style': "height: 100px"}

    class Meta:
        model = Post
        fields = ['titlePost', 'contentPost']
        

class CommentForm(ModelForm):
    # overwride default
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['contentComment'].widget.attrs = {
            'class': "form-control mb-3",
            'style': "height: 100px"}

    class Meta:
        model = PostComment
        fields = ['contentComment']

    

