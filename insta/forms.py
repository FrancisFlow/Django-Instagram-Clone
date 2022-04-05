from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Image, Profile, Comment


class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].widget=forms.TextInput()
        self.fields['content'].widget.attrs['placeholder']='Comment on this post'

    class Meta:
        model=Comment
        fields=('content',)

class NewProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['user']

class UpdateUserForm(forms.ModelForm):
    email=forms.EmailField(max_length=300, help_text="Requried, email address")
    username=forms.CharField(max_length=40)
    class Meta:
        model=User
        fields=('username', 'email')


class UpdateUserProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields= ['name', 'profile_pic', 'bio']

class NewPostForm(forms.ModelForm):
    class Meta:
        model=Image
        exclude=['posted_by', 'date_posted', 'image_likes', 'user']
        