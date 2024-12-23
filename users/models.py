from django.conf import settings
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='following_profiles', blank=True)  # 팔로워
    followings = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='follower_profiles', blank=True)  # 팔로우

    def __str__(self):
        return self.user.username

