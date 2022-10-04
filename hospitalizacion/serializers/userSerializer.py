from rest_framework import serializers
from hospitalizacion.models.usuarios import User
from hospitalizacion.models.personal_medico import Personal
from hospitalizacion.serializers.personal_medicoSerializer import PersonalSerializer


class UserSerializer(serializers.ModelSerializer):
    account = PersonalSerializer()

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
            "rol",
        ]

    def create(self, validated_data):
        accountData = validated_data.pop("account")
        userInstance = User.objects.create(**validated_data)
        Personal.objects.create(user=userInstance, **accountData)
        return userInstance

    def to_representation(self, obj):
        usuario = User.objects.get(id=obj.id)
        # personal = Personal.objects.get(user=obj.id)
        return {
            "id_usuario": usuario.id_usuario,
            "numero_identificacion": usuario.numero_identificacion,
            "nombre": usuario.nombre,
            "apellido": usuario.apellido,
            "password": usuario.password,
            "telefono": usuario.telefono,
            "correo": usuario.correo,
            "genero": usuario.genero,
            "rol": usuario.rol,
            # "account": {
            #   "identificacion_funcionario": personal.identificacion_funcionario,
            #   "especialidad": personal.especialidad,
            #    "registro": personal.registro,
            #    "isActive": personal.isActive,
            # },
        }
