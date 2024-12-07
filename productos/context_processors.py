# Contador de productos del carrito
from .models import Carrito, models
from django.contrib.auth.models import User

def carrito_contador(request):
    if request.user.is_authenticated:
        # Obtén los items del carrito para el usuario autenticado
        carrito_items_count = Carrito.objects.filter(usuario=request.user).aggregate(total=models.Sum('cantidad'))['total'] or 0
    else:
        # Si el usuario no está autenticado, muestra 0
        carrito_items_count = 0
    return {
        'carrito_items_count': carrito_items_count
    }
