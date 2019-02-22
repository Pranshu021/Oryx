from django.db import models
from django.contrib.auth.models import User

class UserInfo(models.Model):
    Userinfo = models.OneToOneField(User, on_delete=models.CASCADE, related_name='info', null="True")
    ratings_given = models.IntegerField(default=0, blank=False)
    profile_pic = models.ImageField(blank=True, upload_to='')
