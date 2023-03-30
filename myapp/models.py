from django.db import models
from django.contrib.auth.models import User

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
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default_avatar.png')
