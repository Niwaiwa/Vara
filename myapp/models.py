from django.db import models
from django.contrib.auth.models import User


def unique_filename(path):
    """
    Enforce unique upload file names.
    Usage:
    class MyModel(models.Model):
        file = ImageField(upload_to=unique_filename("path/to/upload/dir"))
    """
    import os, base64, uuid
    def _func(instance, filename):
        name, ext = os.path.splitext(filename)
        name = base64.urlsafe_b64encode(uuid.uuid4().bytes).decode('utf-8').replace('=', '')
        return os.path.join(path, f"{name}{ext}")
    return _func


class Video(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    url = models.URLField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class TagVideo(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)

class VideoLike(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class UserAvatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=unique_filename('avatars/'), default='avatars/default_avatar.png')
    def __str__(self):
        return self.avatar.name
