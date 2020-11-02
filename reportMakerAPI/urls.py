from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'appsec', views.appsecViewSet)
router.register(r'scr', views.scrViewSet)
router.register(r'va', views.vaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('mnbvcxz/', admin.site.urls),
    path('va-elliot/', views.sendVAPTObs),
    path('fill/appsec/', views.fillObservationsAppsec),
    path('fill/va/', views.fillObservationsVA),
    path('fill/scr/', views.fillObservationsSCR),
]
