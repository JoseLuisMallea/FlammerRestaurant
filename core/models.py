from django.db import models

# Create your models here.

class Usuario(models.Model):
    idUsuario = models.IntegerField(primary_key=True, verbose_name="idUsuario")
    correo = models.CharField(max_length=50, verbose_name="correo")
    password = models.CharField(max_length=50, verbose_name="password")
    class Meta:
        verbose_name="usuario",
        verbose_name_plural = "usuarios",
        ordering = ["idUsuario"]

        def __str__(self):
            return self.correo