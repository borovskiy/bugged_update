from rest_framework import generics
from rest_framework.exceptions import ValidationError

from .models import Client
from .serializers import ClientSerializer
from .services import telephone_check


class ClientListView(generics.ListCreateAPIView):
    queryset = Client.objects.all().order_by('id')
    serializer_class = ClientSerializer
    filterset_fields = ['city', 'company_name', 'address', 'inn', 'kpp', 'ogrn', 'email', 'phone_number', 'site_url']

    def perform_create(self, serializer):
        if telephone_check(self.request.data['phone_number']) is True:
            return super().perform_create(serializer)
        raise ValidationError('no valid phone')


class ClientView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
