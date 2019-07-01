from django.urls import include, path
from django.views import generic
from . import views

urlpatterns = [
    path('', generic.RedirectView.as_view(url='./ordenproduccion/', permanent=False), name="index"),
    path('ordenproduccion/', include(views.OrdenProduccionViewSet().urls), name='ordenproduccion'),
    path('producto/', include(views.ProductoViewSet().urls), name='producto'),
    path('colaborador/', include(views.ColaboradorViewSet().urls), name='colaborador'),
    path('cargo/', include(views.CargoViewSet().urls), name='cargo'),
    path('causal/', include(views.CausalViewSet().urls), name='causal'),
]