from django.db import models
from django.contrib.auth.models import User


class Profil(models.Model):
    ism = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    rasim = models.URLField()
    bio = models.CharField(max_length=200,blank=True)
    public = models.BooleanField(default=True)
    def __str__(self):
        return self.ism


class Connection(models.Model):
    user_id =models.ForeignKey(Profil,on_delete=models.CASCADE,related_name="followerlar")
    following_id = models.ForeignKey(Profil,on_delete=models.CASCADE,related_name="following")