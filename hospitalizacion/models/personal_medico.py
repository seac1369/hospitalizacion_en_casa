from django.db import models
from .usuarios import User


class Personal(models.Model):
    identificacion_funcionario = models.IntegerField(primary_key=True)
    especialidad = models.TextField("Especialidad", max_length=40)
    registro = models.TextField("Registro", max_length=40)
    usuarios_id_usuario = models.ForeignKey(
        User, related_name="personal", on_delete=models.CASCADE
    )
