from django.contrib import admin
from .models import appsecObservation, vaptObservation, vaptPlugin, scrObservation

# Register your models here.
@admin.register(appsecObservation)
class appsecObs(admin.ModelAdmin):
    list_filter = ('criticality',)

@admin.register(vaptObservation)
class vaptObs(admin.ModelAdmin):
    list_filter = ('criticality',)

@admin.register(scrObservation)
class scrObs(admin.ModelAdmin):
    list_filter = ('criticality',)

admin.site.register(vaptPlugin)
