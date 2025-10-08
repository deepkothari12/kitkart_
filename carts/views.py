from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from store.models import product
from .models import cart, cartitem


def _cart_id(request): ##this is private function 
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart



def add_cart(request , product_id):

    product_from_db = product.objects.get(id = product_id) ##gt the product 

    try :

        Cart = cart.objects.get(
            cart_id = _cart_id(request = request)
            ) ###here we are getting the cart id from the session key

    except cart.DoesNotExist:
        
        Cart = cart.objects.create(
            cart_id = _cart_id(request = request)
            ) ##if cart does not exist then create a new cart 
    Cart.save()

    try:
        cart_item = cartitem.objects.get(
            product = product_from_db,
            cart = cart
        ) ##if the product is already in the cart then increase the quantity 
        if cart_item.quantity < cart_item.product.stock:
            cart_item.quantity += 1
        cart_item.save()

    except cartitem.DoesNotExist:
        cart_item = cartitem.objects.create(
            product = product_from_db,
            quantity = 1,
            cart = Cart
        ) ##if the product is not in the cart then create a new cart item 
        cart_item.save()


    return redirect('cart')

# Create your views here.
def cart(request):
    return render(request = request , template_name = "store/cart.html")
