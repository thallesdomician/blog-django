from django import forms
from .models import Post

from django.utils.translation import gettext as _



class PostForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'id': 'editor'}), label=_('Content'))
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
