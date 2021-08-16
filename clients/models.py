from django.contrib.auth.models import User
from django.db import models
from russian_fields import INNBusinessField, KPPField, OGRNField


class KPP(KPPField):
    def from_db_value(self, value, expression, connection, context=None):
        return super().from_db_value(value, expression, connection, context)


class OGRN(OGRNField):
    def from_db_value(self, value, expression, connection, context=None):
        return super().from_db_value(value, expression, connection, context)


class INNB(INNBusinessField):
    def from_db_value(self, value, expression, connection, context=None):
        return super().from_db_value(value, expression, connection, context)


class City(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Client(models.Model):
    city = models.ForeignKey('City', models.PROTECT, related_name='clients')
    company_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    inn = INNB()
    kpp = KPP()
    ogrn = OGRN()
    email = models.EmailField(max_length=255)
    # Для российских номеров длина 12 символов
    phone_number = models.CharField(max_length=12)
    site_url = models.URLField()

    def __str__(self):
        return self.company_name
