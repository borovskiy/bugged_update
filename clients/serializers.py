from rest_framework import serializers
from .models import City, Client


class ClientSerializer(serializers.ModelSerializer):
    city = serializers.PrimaryKeyRelatedField(queryset=City.objects.all())
    inn = serializers.IntegerField()
    kpp = serializers.IntegerField()
    ogrn = serializers.IntegerField()

    class Meta:
        fields = ('id', 'city', 'company_name', 'address', 'inn', 'kpp', 'ogrn', 'email', 'phone_number', 'site_url',)
        model = Client
