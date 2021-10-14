from django.shortcuts import render
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime
from .models import *
from .utils import *
from .forms import *


def store(request):
    products = Product.objects.all()
    total = get_cart_total(request)
    context = {'products': products, 'total': total}
    return render(request, 'store/store.html', context)


def cart(request):
    items = get_cart_items(request)
    amount = get_cart_amount(request)
    total = get_cart_total(request)
    context = {'items': items, 'amount': amount, 'total': total}
    return render(request, 'store/cart.html', context)


def checkout(request):
    # si está autenticado, le pasamos la dirección de la última compra
    if request.user.is_authenticated:
        try:
            customer = Customer.objects.get(user=request.user)
            details = ShippingAddress.objects.filter(customer=customer).last()
            form = ShippingInfoForm(instance=details)
        except ObjectDoesNotExist:
            form = ShippingInfoForm()
    else:
        form = ShippingInfoForm()

    items = get_cart_items(request)
    amount = get_cart_amount(request)
    total = get_cart_total(request)
    context = {'form': form, 'items': items, 'amount': amount, 'total': total}
    return render(request, 'store/checkout.html', context)


def order(request):
    if request.method == 'POST':
        if (items := get_cart_items(request)):
            if request.user.is_authenticated:
                customer, _ = Customer.objects.get_or_create(user=request.user)
            else:
                customer = None

            order = Order.objects.create(
                customer=customer,
                date=datetime.now,
                transaction=datetime.now().timestamp(),
                completed=True
            )

            data = json.loads(request.body)
            ShippingAddress.objects.create(
                customer=customer,
                order=order,
                name=data['name'],
                address=data['address'],
                city=data['city'],
                country=data['country'],
                zipcode=data['zipcode'],
            )

            for item in items:
                OrderItem.objects.create(
                    order=order,
                    product=Product.objects.get(pk=item['id']),
                    quantity=item['quantity']
                )

            return JsonResponse('Order submitted..', safe=False)
