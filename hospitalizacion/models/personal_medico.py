from django.db import models
from .usuarios import User


class Personal(models.Model):
    identificacion_funcionario = models.IntegerField(primary_key=True)
    especialidad = models.CharField("Especialidad", max_length=40)
    registro = models.CharField("Registro", max_length=40)
    usuarios_id_usuario = models.ForeignKey(
        User, related_name="usuario", on_delete=models.CASCADE
    )
