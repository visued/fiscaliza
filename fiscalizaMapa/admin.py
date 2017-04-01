from django.contrib import admin
from .models import Incidente
from leaflet.admin import LeafletGeoAdmin

# Register your models here.

class IncidenteAdmin(LeafletGeoAdmin):
    list_display = ['assunto']
admin.site.register(Incidente, IncidenteAdmin)
