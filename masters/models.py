from django.db import models

# Create your models here.
class OrdenProduccion(models.Model):

    producto = models.ForeignKey("Producto", on_delete=models.CASCADE)
    descripcion = models.TextField("Descripcion")
    numero_lote = models.CharField("Numero de lote", max_length=50)
    cantidad = models.IntegerField("Cantidad a fabricar")
    fecha_inicio = models.DateField("Fecha de inicio", auto_now=False, auto_now_add=False)
    fecha_fin = models.DateField("Fecha de Entrega", auto_now=False, auto_now_add=False)
    codigo_pedido = models.CharField("Codigo de pedido", max_length=50)
    caducidad = models.DateField("Caducidad", auto_now=False, auto_now_add=False)

    class Meta:
        verbose_name = "Orden de Produccion"
        verbose_name_plural = "Ordenes de Produccion"

    def __str__(self):
        return self.descripcion

class Producto(models.Model):

    codigo = models.CharField("Codigo", max_length=50)
    descripcion = models.TextField("Descripcion")
    
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return self.codigo

class Colaborador(models.Model):

    nombre = models.CharField("Nombre completo", max_length=50)
    cedula = models.CharField("Cedula", max_length=50)
    codigo = models.CharField("Codigo interno", max_length=50)
    cargo = models.ForeignKey("Cargo", verbose_name="Cargo", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Colaborador"
        verbose_name_plural = "Colaboradores"

    def __str__(self):
        return self.nombre

class Cargo(models.Model):

    nombre = models.CharField("Nombre del cargo", max_length=50)
    descripcion = models.CharField("Descripcion", max_length=50)
    causales = models.ManyToManyField("Causal", verbose_name="Causales")

    class Meta:
        verbose_name = "Cargo"
        verbose_name_plural = "Cargos"

    def __str__(self):
        return self.nombre

class Causal(models.Model):

    nombre = models.CharField("Nombre", max_length=50)
    descripcion = models.CharField("Descripcion", max_length=50)

    class Meta:
        verbose_name = "Causal"
        verbose_name_plural = "Causales"

    def __str__(self):
        return self.nombre
