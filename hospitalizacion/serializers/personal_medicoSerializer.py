from hospitalizacion.models.personal_medico import Personal
from rest_framework import serializers


class PersonalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personal
        fields = [
            "identificacion_funcionario",
            "especialidad",
            "registro",
        ]
