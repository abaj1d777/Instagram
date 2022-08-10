from app1.views import *
from userapp.views import *
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from django.contrib import admin
from django.urls import path
from rest_framework import permissions
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView)

sxema_view = get_sxema_view(
   openapi.Info(
      title="Spotify Api",
      default_version='v1',
      description="Test description",
      contact=openapi.Contact("Abdumajid Muhammadov. Email:<amuhammadov719@gmail.com>"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',sxema_view.with_url('swagger', cache_timeout=0), name='swagger-doc'),
    path('users/', UserQosh.as_view()),
    path('user/<int:pk>/', UserGetUpdateDelete.as_view()),
    path('profils/', Profils.as_view()),
    path('profil/<int:pk>/', ProfilGet.as_view()),
    path('connections/', Connections.as_view()),
    path('connection/<int:pk>/', ConnectionDelete.as_view()),
    path('posts/', Posts.as_view()),
    path('medias/', Medias.as_view()),
    path('media/<int:pk>/', MediaGet.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_juft_ol'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_yangila '),
]
