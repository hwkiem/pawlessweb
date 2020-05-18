from django.db import models
from django.contrib.auth.models import User
from core.face_recognition import get_encoding, mock
import base64
import pickle
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    prof_enc = models.BinaryField(default=bytes("hello world", 'utf-8'))

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save()
