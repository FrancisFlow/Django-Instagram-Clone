from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
import cloudinary
from tinymce.models import HTMLField
# Create your models here.

class Image(models.Model):
    image=CloudinaryField('image')
    image_name=models.CharField(max_length=50)
    image_caption=models.CharField(max_length=255)
    date_posted= models.DateTimeField(auto_now_add=True)
    image_likes=models.IntegerField(default=0, blank=True)
    posted_by=models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    @classmethod
    def get_images(cls):
        return cls.objects.all()

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    profile_pic=CloudinaryField('image')
    bio=models.CharField(blank=True, max_length=200, null=True)
    name=models.CharField(blank=True, max_length=40)
    def __str__(self):
        return f'{self.user.username} profile'
    
    def search_profile(cls, name):
        return cls.objects.filter(user_username__icontains=name).all()
    def save_profile(self):
        self.save()
    def delete_profile(self):
        self.delete()

    def update_bio(self, new_bio):
        self.bio=new_bio
        self.save()
    def update_image(self, user_id, new_image):
        user=User.objects.get(id=user_id)
        self.photo=new_image
        self.save()

class Comment(models.Model):
    user=models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="comments")
    post=models.ForeignKey(Image, on_delete=models.CASCADE, related_name="comments")
    content=HTMLField()
    date_posted=models.DateTimeField(auto_now_add=True)

    @classmethod
    def get_comments(cls, id):
        return cls.objects.filter(image_id=id)