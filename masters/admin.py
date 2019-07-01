from import_export.admin import ImportExportActionModelAdmin
from django.contrib import admin
from .models import OrdenProduccion, Producto, Colaborador, Cargo, Causal

# Register your models here.
@admin.register(OrdenProduccion)
class OrdenAdmin(ImportExportActionModelAdmin):
    pass

@admin.register(Producto)
class ProductoAdmin(ImportExportActionModelAdmin):
    pass

@admin.register(Colaborador)
class ColaboradorAdmin(ImportExportActionModelAdmin):
    pass

@admin.register(Cargo)
class CargoAdmin(ImportExportActionModelAdmin):
    pass

@admin.register(Causal)
class CausalAdmin(ImportExportActionModelAdmin):
    pass