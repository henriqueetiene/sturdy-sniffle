from django.urls import path, include
from rest_framework import routers

from .views import UserList, UserDetail

urlpatterns = [
    path('', UserList.as_view()),
    path('<int:pk>', UserDetail.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
