from hospitalizacion.models.roles import Roles
from rest_framework import serializers


class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = ["id_-roles", "rol"]
