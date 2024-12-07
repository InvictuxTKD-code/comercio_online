from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Carrito, models
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Sum
# Create your views here.

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/lista_productos.html', {'productos': productos})

def index(request):
    return render(request, 'productos/index.html')

# def agregar_al_carrito(request, producto_id):
#     producto = get_object_or_404(Producto, id=producto_id)
#     carrito_item, created = Carrito.objects.get_or_create(producto=producto)
#     if not created:
#         carrito_item.cantidad += 1
#     carrito_item.save()
#     return redirect('productos/carrito.html')

@login_required
def ver_carrito(request):
    carrito_items = Carrito.objects.filter(usuario=request.user)
    total = sum(item.producto.precio * item.cantidad for item in carrito_items)
    
    return render(request, 'productos/carrito.html', {
        'carrito_items': carrito_items,
        'total': total,
    })

# Vista para agregar al carrito
@login_required
def agregar_al_carrito(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    
    # Comprobar si el carrito del usuario ya contiene este producto
    carrito, created = Carrito.objects.get_or_create(
        producto=producto,
        usuario=request.user,  # Asociar el carrito con el usuario logueado
    )
    
    # Si el producto ya estaba en el carrito, aumentamos la cantidad
    if not created:
        carrito.cantidad += 1
        carrito.save()
    
    # Mensaje de éxito
    # Redirigir a una página de éxito con el nombre del producto
    return redirect('ver_carrito')  # Redirige a la página de carrito

@login_required
def actualizar_cantidad(request, item_id):
    item = Carrito.objects.get(id=item_id)
    action = request.POST.get('action')  # Obtener si el botón presionado fue "increase" o "decrease"
    
    if action == 'increase':
        if item.cantidad < item.producto.stock:  # Asegurarse de que no se exceda el stock
            item.cantidad += 1
            item.save()
    elif action == 'decrease':
        if item.cantidad > 1:  # Asegurarse de que no baje de 1
            item.cantidad -= 1
            item.save()
    
    return redirect('ver_carrito')


def eliminar_del_carrito(request, carrito_id):
    try:
        # Buscar el item del carrito con el id proporcionado
        carrito_item = Carrito.objects.get(id=carrito_id)
        # Eliminar el item del carrito
        carrito_item.delete()
    except Carrito.DoesNotExist:
        # Si el producto no existe en el carrito, no hacemos nada
        pass
    # Redirigir al carrito después de eliminar el producto
    return redirect('ver_carrito')

