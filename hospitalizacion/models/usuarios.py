from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)
from django.contrib.auth.hashers import make_password


class UserManager(BaseUserManager):
    def create_user(self, numero_identificacion, password=None):
        """
        Creates and saves a user with the given username and password.
        """
        if not numero_identificacion:
            raise ValueError("Users must have an numero_identificacion")
        user = self.model(numero_identificacion=numero_identificacion)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, numero_identificacion, password):
        """
        Creates and saves a superuser with the given username and password.
        """
        user = self.create_user(
            numero_identificacion=numero_identificacion,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    id_usuario = models.IntegerField(primary_key=True)
    numero_identificacion = models.CharField(
        "Numero_identificacion", max_length=15, unique=True
    )
    nombre = models.CharField("Nombre", max_length=30)
    apellido = models.CharField("Apellido", max_length=30)
    password = models.CharField("Password", max_length=30)
    telefono = models.CharField("Telefono", max_length=30)
    correo = models.EmailField("Correo", max_length=100)
    genero = models.CharField("Genero", max_length=30)
    rol = models.CharField("Genero", max_length=30)

    def save(self, **kwargs):
        some_salt = "mMUj0DrIK6vgtdIYepkIxN"
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)

    objects = UserManager()
    USERNAME_FIELD = "numero_identificacion"
