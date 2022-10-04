# Generated by Django 4.1.1 on 2022-10-03 23:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                ("id_usuario", models.IntegerField(primary_key=True, serialize=False)),
                (
                    "numero_identificacion",
                    models.CharField(
                        max_length=15, unique=True, verbose_name="Numero_identificacion"
                    ),
                ),
                ("nombre", models.CharField(max_length=30, verbose_name="Nombre")),
                ("apellido", models.CharField(max_length=30, verbose_name="Apellido")),
                ("password", models.CharField(max_length=30, verbose_name="Password")),
                ("telefono", models.CharField(max_length=30, verbose_name="Telefono")),
                ("correo", models.EmailField(max_length=100, verbose_name="Correo")),
                ("genero", models.CharField(max_length=30, verbose_name="Genero")),
                ("rol", models.CharField(max_length=30, verbose_name="Genero")),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Personal",
            fields=[
                (
                    "identificacion_funcionario",
                    models.IntegerField(primary_key=True, serialize=False),
                ),
                (
                    "especialidad",
                    models.CharField(max_length=40, verbose_name="Especialidad"),
                ),
                ("registro", models.CharField(max_length=40, verbose_name="Registro")),
                (
                    "usuarios_id_usuario",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="usuario",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
