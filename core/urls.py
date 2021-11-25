from django.urls import path
from .views import index, administrador, chef, tecnico

urlpatterns = [
    path('', index, verbose_name="index"),
    path('administrador', administrador, verbose_name="administrador"),
    path('chef', chef, verbose_name="chef"),
    path('tecnico', tecnico, verbose_name="tecnico")
]