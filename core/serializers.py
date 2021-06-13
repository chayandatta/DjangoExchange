from rest_framework import serializers
from .models import ExchangeModel


class DjangoExchangeApi(serializers.ModelSerializer):
    class Meta:
        model = ExchangeModel
