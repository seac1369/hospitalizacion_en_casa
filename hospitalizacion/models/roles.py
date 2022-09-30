from django.db import models


class Roles(models.Model):
    id_roles = models.AutoField(primary_key=True)
    rol = models.CharField("Rol", max_length=30)
