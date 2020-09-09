from django.contrib import admin
from .models import appsecObservation, vaptObservation, vaptPlugin

# Register your models here.
@admin.register(appsecObservation)
class appsecObs(admin.ModelAdmin):
    list_filter = ('criticality',)

@admin.register(vaptObservation)
class appsecObs(admin.ModelAdmin):
    list_filter = ('criticality',)

admin.site.register(vaptPlugin)