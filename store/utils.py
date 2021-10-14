from .models import *
import json


def get_cart(request):
    cart = None
    if 'cart' in (cookies := request.COOKIES):
        cart = json.loads(cookies['cart'])
    return cart


def get_cart_total(request):
    total = 0
    if (cart := get_cart(request)):
        for id in cart:
            total += cart[id]['quantity']
    return total


def get_cart_items(request):
    items = []
    if (cart := get_cart(request)):
        for id in cart:
            product = Product.objects.get(pk=id)
            item = {
                'id': product.id,
                'imageURL': product.imageURL,
                'name': product.name,
                'price': product.price,
                'quantity': cart[id]['quantity'],
                'total': product.price * cart[id]['quantity'],
            }
            items.append(item)
    return items


def get_cart_amount(request):
    amount = 0
    if (cart := get_cart(request)):
        for id in cart:
            product = Product.objects.get(pk=id)
            amount += product.price * cart[id]['quantity']
    return amount
