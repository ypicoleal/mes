from django.apps import AppConfig
from material.frontend.apps import ModuleMixin

class MastersConfig(ModuleMixin, AppConfig):
    verbose_name = "Maestros"
    name = 'masters'
    icon = '<i class="material-icons">table_chart</i>'