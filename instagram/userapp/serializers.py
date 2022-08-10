from .models import *
from rest_framework import serializers

class ProfilrSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profil
        fields = "__all__"

class ConnectionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Connection
        fields = "__all__"