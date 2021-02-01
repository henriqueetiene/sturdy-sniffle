from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status


class CreateUserTestCase(APITestCase):
    def setUp(self):
        user = User.objects.create_user(username='admin', password='1234')
        self.client.force_login(user)

    def test_create_user(self):
        response = self.client.post('/usuarios/', {'username': 'henrique'})
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)


class ListUsersTestCase(APITestCase):
    def setUp(self):
        user = User.objects.create_user(username='admin', password='1234')
        User.objects.create_user(username='lucas', password='1234')
        User.objects.create_user(username='joao', password='1234')
        User.objects.create_user(username='davi', password='1234')
        self.client.force_login(user)

    def test_list_users(self):
        response = self.client.get('/usuarios/')
        self.assertEquals(len(response.json()['results']), 4)
