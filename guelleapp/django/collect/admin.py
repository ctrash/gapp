from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Kunde, Produkte, Fahrer, Fahrzeug, Lieferungen

admin.site.register(Kunde)
admin.site.register(Produkte)
admin.site.register(Fahrzeug)
admin.site.register(Fahrer)
admin.site.register(Lieferungen)



