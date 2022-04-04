from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
import cloudinary
# Create your models here.

class Image(models.Model):
    image=CloudinaryField('image')
    image_name=models.CharField(max_length=50)
    image_caption=models.CharField(max_length=255)
    date_posted= models.DateTimeField(auto_now_add=True)
    image_likes=models.IntegerField(default=0, blank=True)
    # posted_by=models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    @classmethod
    def get_images(cls):
        return cls.objects.all()