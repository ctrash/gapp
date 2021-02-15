from django.conf import settings 
from django.db import models 
from django.utils import timezone

# Create your models here.

class Kunde(models.Model):
    vorname = models.CharField(max_length=100)
    nachname = models.CharField(max_length=100)		
    straße = models.CharField(max_length=100)
    hausnr = models.IntegerField()
    plz	= models.IntegerField()
    stadt =	models.CharField(max_length=100)
    aufnehmer = models.BooleanField()
    abgeber	= models.BooleanField()
    beförderer = models.BooleanField()

    def __str__(self):
        return self.nachname

class Produkte(models.Model):

    bezeichnung = models.CharField(max_length=100)
    art = models.CharField(max_length=100)
    datum_untersuchung = models.DateField(auto_now=False, auto_now_add=False)
    n = models.FloatField()
    nh4 = models.FloatField()
    p = models.FloatField()
    k = models.FloatField()
    ts = models.FloatField()
    bezugsgröße = models.CharField(max_length=100)

    def __str__(self):
        return self.bezeichnung


class Fahrzeug(models.Model):
    name = models.CharField(max_length=100)
    schlepper = models.CharField(max_length=100)
    fass = models.CharField(max_length=100)
    volumen = models.FloatField()

    def __str__(self):
        return self.name

class Fahrer(models.Model):
    vorname = models.CharField(max_length=100)
    nachname = models.CharField(max_length=100)

    def __str__(self):
        return self.vorname

class Lieferungen(models.Model):
    datum_von = models.DateField(auto_now=False, auto_now_add=False)
    menge = models.FloatField()
    id_produkt = models.ForeignKey(Produkte, related_name='id_produkte',on_delete=models.CASCADE)
    id_fahrer = models.ForeignKey(Fahrer, related_name='id_fahrer',on_delete=models.CASCADE)
    id_fahrzeug = models.ForeignKey(Fahrzeug, related_name='id_fahrzeug',on_delete=models.CASCADE)
    id_aufnehmer = models.ForeignKey(Kunde, related_name='id_aufnehmer',on_delete=models.CASCADE)
    id_abgeber = models.ForeignKey(Kunde, related_name='id_abgeber',on_delete=models.CASCADE)
    id_beförderer = models.ForeignKey(Kunde, related_name='id_beförderer',on_delete=models.CASCADE)

    def __str__(self):
        return str(self.datum_von)
