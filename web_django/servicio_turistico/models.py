from sqlite3 import Date
from tokenize import group
from django.db import models


class Weddings(models.Model):
    name = models.CharField(max_length=60)
    fecha = models.DateField()
    precio = models.FloatField()

class Corporativos(models.Model):
    empresa = models.CharField(max_length=60)
    dia = models.DateField()
    costo = models.FloatField()

class Turismo(models.Model):
    group = models.CharField(max_length=60)
    date = models.DateField()
    price = models.FloatField()