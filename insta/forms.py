from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Image, Profile, Comment


class CommentForm(forms.ModleForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].widget=forms.TextInput()
        self.fields['content'].widget.attrs['placeholder']='Comment on this post'

    class Meta:
        modle=Comment
        fileds=('content',)