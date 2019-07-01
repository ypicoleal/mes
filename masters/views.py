from django.shortcuts import render
from material.frontend.views import ModelViewSet
from . import models

# Create your views here.
class OrdenProduccionViewSet(ModelViewSet):
    model = models.OrdenProduccion


class ProductoViewSet(ModelViewSet):
    model = models.Producto


class ColaboradorViewSet(ModelViewSet):
    model = models.Colaborador

class CargoViewSet(ModelViewSet):
    model = models.Cargo

class CausalViewSet(ModelViewSet):
    model = models.Causal