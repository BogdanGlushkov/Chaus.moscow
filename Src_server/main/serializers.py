from rest_framework import serializers
from .models import GuestList


class GuestSerializer(serializers.Serializer):
    name = serializers.CharField('ФИО', max_length=255)
    email = serializers.CharField('Почта', max_length=255)
    phone = serializers.CharField('Телефон', max_length=20)
    promo = serializers.CharField('Промокод', max_length=20, null=True, blank=True)

    def create(self, validated_data):
        return GuestList.objects.create(**validated_data)







