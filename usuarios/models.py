from django.db import models


class Usuario(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ["nome"]
