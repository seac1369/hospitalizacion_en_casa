from hospitalizacion.models.roles import Account
from rest_framework import serializers


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account


fields = ["balance", "lastChangeDate", "isActive"]
