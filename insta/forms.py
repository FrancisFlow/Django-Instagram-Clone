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
        fields=('content',)

class NewProfileForm(forms.ModleForm):
    class Meta:
        model=Profile
        exclude=['user']

class UpdateUserForm(forms.ModleForm):
    email=forms.EmailField(max_length=300, help_text="Requried, email address")
    class Meta:
        model=User
        fields=('username', 'email')


class UpdateUserProfileForm(forms.ModleForm):
    class Meta:
        model=Profile
        fields= ['name', 'profile_photo', 'bio']
        
