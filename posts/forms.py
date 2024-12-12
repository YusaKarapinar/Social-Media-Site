from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    image = forms.ImageField(
        widget=forms.ClearableFileInput(),
        required=False
    )

    class Meta:
        model = Post
        fields = ['content', 'image']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
