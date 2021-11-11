# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect, reverse
from .models import *
from cart.models import Cart, CartItem
from accounts.models import Profile
# from ShippingAddress.models import ShippingAddress
from payment.models import ShippingAddress ,PaymentModel
from shop.models import Product
from django.contrib.auth.decorators import login_required
from shop.views import product_list
from payment.views import create_payment, create_shipment
from decimal import Decimal
# Create your views here.


def order_save(request):
    user = request.user
    cart = Cart.objects.get(user = user)
    address = request.POST['address']
    postal_code = request.POST['zip']
    country = request.POST['country']
    state = request.POST['state']
    name = request.POST['payment']
    payment = create_payment(request, name)
    payment.save()
    shippingaddress = create_shipment(request, address,postal_code,country,state)
    shippingaddress.save()
    
    # order.shopCost = cart.get_shipcost()
    order = Order.objects.create(user=user,payment = payment ,shippingAddress = shippingaddress)
    
    order.total = cart.get_total_cost()
    for item in cart.items.all():
        # order.total = item.price * item.quantity
        product = item.product
        quantity = item.quantity
        price = item.price
        orderItem = OrderItem.objects.create(order = order, product = product, price = price, quantity = quantity)
        product.stock -= quantity
        product.save()
        orderItem.save()
        cart.items.remove(item)
    order.save()
    return product_list(request)

def order_create(request):
    user = request.user
    profile = get_object_or_404(Profile, user=request.user)
    cart = Cart.objects.get(user = request.user)
    
    return render(request, 'orders/order_list.html', {'cart': cart, 'profile': profile})


@login_required
def my_order(request):
    user = request.user
    orders = user.order_set.all() 
    return render(
        request, 
        'orders/my_order.html', 
        {
            'orders': orders,
            'user': user,
        }
    )
    
def order_detail(request, id):
    user = request.user
    order = Order.objects.get(id=id)
    # cart = Cart.objects.get(user = user)
    # orderItems = orderItems.objects.get(order = order)
    # payment = PaymentModel.objects.get(order=order)
    # shippingaddress = ShippingAddress.objects.get(order=order)
    payment = order.payment
    shippingaddress = order.shippingAddress
    items = order.items.all()
    return render(
        request,
        'orders/my_order_detail.html',
        {
            'items': items,
            'order': order,
            # 'orderItems' : orderItems,
            # 'cart' : cart,
            'payment': payment,
            'shippingaddress': shippingaddress
        }
    )

