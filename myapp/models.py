from django.db import models
from django.contrib.auth.models import User
from django.utils.deconstruct import deconstructible
import os, base64, uuid

@deconstructible
class UniqueFilename:
    """
    Enforce unique upload file names.
    Usage:
    class MyModel(models.Model):
        file = ImageField(upload_to=unique_filename("path/to/upload/dir"))
    """
    def __init__(self, path):
        self.path = path
    def __call__(self, instance, filename):
        name, ext = os.path.splitext(filename)
        name = base64.urlsafe_b64encode(uuid.uuid4().bytes).decode('utf-8').replace('=', '')
        return os.path.join(self.path, f"{name}{ext}")

unique_filename = UniqueFilename("avatars/")


class Video(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    url = models.URLField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField('Tag', related_name='taged_videos', blank=True)
    likes = models.ManyToManyField(User, related_name='liked_videos', blank=True)

    def __str__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)
    def __str__(self):
        return self.name

class UserAvatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=unique_filename)
    def __str__(self):
        return self.avatar.name
