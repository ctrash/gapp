from django.forms import ModelForm, TextInput, Select
from django import forms

from .models import Fahrer, Lieferungen, Kunde

class FahrerForm(forms.ModelForm):

    class Meta:
        model = Fahrer
        fields = ('vorname', 'nachname',)
        labels = {
            "vorname": "VORNAME Title",
        }
        widgets = {
              "vorname": TextInput(attrs={'class': 'form-control', 'placeholder':'Vorname'}),
              "nachname": TextInput(attrs={'class': 'form-control', 'placeholder':'Nachname'})
        }

class Lieferform(forms.ModelForm):

    class Meta:
        model = Lieferungen
        fields = ('datum_von', 'menge','id_fahrer','id_fahrzeug','id_produkt','id_aufnehmer','id_abgeber','id_beförderer')
        labels = {
            
        }
        widgets = {
            "datum_von": TextInput(attrs={'class': 'form-control', 'placeholder':'',"readonly":"true"}),
            "menge": TextInput(attrs={'class': 'form-control', 'placeholder':''}),
            "id_fahrer": Select(attrs={'class': 'selectpicker', 'data-live-search':'false', 'data-max-options':'1'}),
            "id_fahrzeug": Select(attrs={'class': 'selectpicker', 'data-live-search':'false', 'data-max-options':'1'}),            
            "id_produkt": Select(attrs={'class': 'selectpicker', 'data-live-search':'false', 'data-max-options':'1'}),
            "id_aufnehmer": Select(attrs={'class': 'selectpicker', 'data-live-search':'false', 'data-max-options':'1'}),
            "id_abgeber": Select(attrs={'class': 'selectpicker', 'data-live-search':'false', 'data-max-options':'1'}),
            "id_beförderer":  Select(attrs={'class': 'selectpicker', 'data-live-search':'false', 'data-max-options':'1'}),
            #"id_beförderer": ModelChoiceField(queryset=Kunde.objects.all()),

        }