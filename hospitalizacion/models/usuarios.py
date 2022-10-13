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
    numero_identificacion = models.TextField(
        "Numero_identificacion", max_length=40, unique=True
    )
    nombre = models.TextField("Nombre", max_length=40)
    apellido = models.TextField("Apellido", max_length=40)
    password = models.TextField("Password", max_length=40)
    telefono = models.TextField("Telefono", max_length=40)
    correo = models.EmailField("Correo", max_length=100)
    genero = models.TextField("Genero", max_length=40)
    rol = models.TextField("Genero", max_length=40)

    def save(self, **kwargs):
        some_salt = "mMUj0DrIK6vgtdIYepkIxN"
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)

    objects = UserManager()
    USERNAME_FIELD = "numero_identificacion"
