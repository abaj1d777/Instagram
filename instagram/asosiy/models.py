from django.db import models
from userapp.models import *



class Post(models.Model):
    matn = models.CharField(max_length=200,blank=True)
    vaqt = models.DateField(auto_now_add=True)
    profil= models.ForeignKey(Profil,on_delete=models.CASCADE)
    joy = models.CharField(max_length=200)
    def __str__(self):
        return self.matn[:30]

class Media(models.Model):
    fayl = models.FileField()
    post_id = models.ForeignKey(Post,on_delete=models.CASCADE,related_name="postegi_rasimlar")

class Like(models.Model):
    profile = models.ForeignKey(Profil,on_delete=models.CASCADE,related_name="profil_liklar")
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name="post_likar")



class Comment(models.Model):
    profile = models.ForeignKey(Profil,on_delete=models.CASCADE)
    matn = models.CharField(max_length=300)
    sana = models.DateField(auto_now_add=True)
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name="post_comment")
    asosiy_comment = models.ForeignKey("self",on_delete=models.CASCADE,null= True)

class Comment_like(models.Model):
    comment= models.ForeignKey(Comment,on_delete=models.CASCADE,related_name="comment_liklar")
    profil = models.ForeignKey(Profil,on_delete=models.CASCADE)

class Xabar(models.Model):
    vaxt = models.DateTimeField()
    matn = models.CharField(max_length=200)
    jonatuvchi = models.ForeignKey(Profil,on_delete=models.CASCADE,related_name="jonatuvchi_xabar")
    qabul = models.ForeignKey(Profil,on_delete=models.CASCADE,related_name="qabul_xabar")
    def __str__(self):
        return self.matn[:30]

class Reaktisya(models.Model):
    xabar = models.ForeignKey(Xabar,on_delete=models.CASCADE)
    profile = models.ForeignKey(Profil,on_delete=models.CASCADE)
    reaktsiya = models.CharField(max_length=200)