from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='principal'),
    path('productos/', views.lista_productos, name='lista_productos'),
    path('productos/carrito/', views.ver_carrito, name='ver_carrito'),
    path('actualizar_cantidad/<int:item_id>/', views.actualizar_cantidad, name='actualizar_cantidad'),
    path('eliminar_del_carrito/<int:carrito_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
    path('carrito/agregar/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
