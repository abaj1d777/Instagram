from rest_framework import serializers

from .models import *


class XabarSerializers(serializers.ModelSerializer):
    class Meta:
        model = Xabar
        fields = "__all__"

class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"

class MediaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = "__all__"

class LikeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"

class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

class ReaksiyaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Reaktisya
        fields = "__all__"

class CommentLikeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment_like
        fields = "__all__"

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        filds = "__all__"


class ProfilSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profil
        filds = "__all__"

class ConnectionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Connection
        filds = "__all__"