from datetime import date
from tokenize import group
from django import forms

class Wedding(forms.Form):
    name = forms.CharField(max_length=60)
    fecha = forms.DateField()
    precio = forms.FloatField()

class Corpo(forms.Form):
    empresa = forms.CharField(max_length=60)
    dia = forms.DateField()
    costo = forms.FloatField()

class Tourism(forms.Form):
    group = forms.CharField(max_length=60)
    date = forms.DateField()
    price = forms.FloatField()