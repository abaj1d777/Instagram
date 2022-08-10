from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from .serializers import *
from .models import *

class Posts(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSer

class Medias(generics.ListCreateAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaSer

class MediaGet(generics.RetrieveAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaSer

class UserQosh(generics.CreateAPIView):
    model = User.objects.all()
    serializer_class = UserSerializers

class UserGetUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
        queryset =User.objects.all()
        serializer_class = UserSerializers


class ConnectionListCreate(generics.ListCreateAPIView):
    queryset = Connection.objects.all()
    serializer_class = ConnectionSer
    def get_queryset(self):
        queryset = []
        ism = self.request.query_params.get('user_ism')
        if ism is not None:
            p1 = Profil.objects.get(username=ism)
            queryset = Connection.objects.filter(user_id=p1)
        f_ism = self.request.query_params.get('following_ism')
        if f_ism is not None:
            p1 = Profil.objects.get(username=f_ism)
            queryset = Connection.objects.filter(following_id=p1)
        return queryset

class ConnectionGetDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Connection.objects.all()
    serializer_class = ConnectionSerializers
    def perform_destroy(self, instance):
        p1 = Profil.objects.get(username="abdumajid")
        if instance.following_id == p1 or instance.user_id == p1:
            instance.delete()
        return Response(instance)


class Posts(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSer
    def perform_create(self, serializer):
        p1 = Profile.objects.get(user= self.request.user)
        serializer.save(profile=p1)
    def get_queryset(self):
        ism = self.request.query_params.get("username")
        if ism in None:
            p1 =Profil.objects.get(username= ism)
            p2 = Profil.objects.get(user = self.request.user)
            connection  =Connection.objects.filter(following_id=p1,user_id=p2)
            if p1.public  == True or len(connection)>0:
                queryset = Post.objects.filter(profile_in = 'connects_following_id')
class Media(generics.ListCreateAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaSer


class Media(generics.RetrieveAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaSer



