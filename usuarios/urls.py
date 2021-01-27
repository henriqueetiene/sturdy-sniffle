from django.urls import path, include
from rest_framework import routers

from .views import UsuarioList, UsuarioDetail

urlpatterns = [
    path('', UsuarioList.as_view()),
    path('<int:pk>', UsuarioDetail.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
