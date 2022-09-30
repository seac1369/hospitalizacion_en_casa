from rest_framework import serializers
from hospitalizacion.models.usuarios import User
from hospitalizacion.models.roles import Roles
from hospitalizacion.serializers.accountSerializer import AccountSerializer


class UserSerializer(serializers.ModelSerializer):
    account = AccountSerializer()

    class Meta:
        model = User
        fields = [
            "id_usuario",
            "numero_identificacion",
            "nombre",
            "apellido",
            "password",
            "telefono",
            "correo",
            "genero",
            "roles_id_roles",
        ]


def create(self, validated_data):
    accountData = validated_data.pop("account")
    userInstance = User.objects.create(**validated_data)
    Roles.objects.create(user=userInstance, **accountData)
    return userInstance


def to_representation(self, obj):
    user = User.objects.get(id=obj.id)
    account = Roles.objects.get(user=obj.id)
    return {
        "id_usuario": user.id_usuario,
        "numero_identificacion": user.numero_identificacion,
        "nombre": user.nombre,
        "apellido": user.apellido,
        "correo": user.correo,
        "roles_id_roles": {
            "id_roles": account.id_roles,
            "rol": account.rol,
        },
    }
