from django.test import TestCase

from .models import Usuario


class UsuarioTestCase(TestCase):
    def setUp(self):
        Usuario.objects.create(nome="adao")
        Usuario.objects.create(nome="barbara")

    def test_ordering_names(self):
        usuarios = Usuario.objects.all()
        self.assertEquals('adao', usuarios[0].nome)
        self.assertEquals('barbara', usuarios[1].nome)
