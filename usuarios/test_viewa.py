from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status


class CreateUserTestCase(APITestCase):
    def setUp(self):
        user = User.objects.create_superuser(username='admin', password='1234')
        self.client.force_login(user=user)

    def test_create_user(self):
        response = self.client.post('/usuarios/', {'username': 'henrique'})
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)