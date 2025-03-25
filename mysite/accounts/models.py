from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(upload_to='profile_images', default='default.jpg')
    bio = models.TextField()

    def __str__(self):
        return self.user.username
    


# Create your models here.
