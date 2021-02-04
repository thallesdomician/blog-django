from django import forms
from .models import Post
from tinymce.widgets import TinyMCE
from tinymce import models as tinymce_models



class PostForm(forms.ModelForm):
    resume = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 10}))
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    class Meta:
        model = Post
        fields = [
            'title',
            'subtitle',
            'header_image',
            'thumbnail_image',
            'resume',
            'content',
            'categories'
        ]
