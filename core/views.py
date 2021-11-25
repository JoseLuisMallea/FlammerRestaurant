from django.shortcuts import redirect, render, reverse
from rest_framework.response import Response
from .models import Usuario
from core.serializers import UsuarioSerializers
# Create your views here.

usuario = Usuario.objects.all()
correo1 = "juan@tecnico.cl"

def index(request):
    return render(request, "core/index.html")

def tecnico(request):
    return render(request, "core/tecnico.html")

def chef(request):
    return render(request, "core/chef.html")

def administrador(request):
    return render(request, "core/administrador.html")


