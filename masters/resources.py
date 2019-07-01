from import_export import resources
from .models import OrdenProduccion

class OrdenResource(resources.ModelResource):

    class Meta:
        model = OrdenProduccion