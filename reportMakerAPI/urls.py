from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'appsec', views.appsecViewSet)		# Web App Sec
router.register(r'network', views.networkViewSet)	# Network Arch 
router.register(r'va', views.vaViewSet)				# Network VAPT
router.register(r'mobsec', views.mobsecViewSet)		# Mobile App Sec

urlpatterns = [
    path('', include(router.urls)),
    path('mnbvcxz/', admin.site.urls),
]
