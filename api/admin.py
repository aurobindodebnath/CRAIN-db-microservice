from django.contrib import admin
from .models import allObservations
# Register your models here.
@admin.register(allObservations)
class Observ(admin.ModelAdmin):
    list_filter = ('ptype',)