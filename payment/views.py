# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, reverse

# Create your views here.
from paypal.standard.forms import PayPalPaymentsForm
from orders.models import Order
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from orders.models import Order
from shop.models import Product
from accounts.models import User
from django.db import models
from decimal import *
from .models import Review, ShippingAddress, PaymentModel

def add_save(request):
    shippingaddress = ShippingAddress.objects.create(order=request.order)
    shippingaddress.address = request.POST['address']
    shippingaddress.postal_code = request.POST['zip']
    shippingaddress.country = request.POST['country']
    shippingaddress.state = request.POST['state']
    shippingaddress.save()

def add_review(request, id_product):
    product = get_object_or_404(Product, id=id_product)
    user=request.user
    review = Review.objects.create(product=product, user=user)
    review.save()
    # review.name = user.first_name
    review.rating = request.POST['rating']
    review.comment = request.POST['comment']
    review.save()
    reviews = product.review_set.all()
    return render(
        request,
        'shop/product/detail.html',
        {'product': product,
        'reviews': reviews
        }
    )
def create_payment(request, name):
    # payment.name = name
    payment = PaymentModel.objects.create(name=name)
    return payment

def create_shipment(request, address,postal_code,country,state):
    shippingaddress = ShippingAddress.objects.create(address = address,postal_code = postal_code,country = country,state = state)
    # shippingaddress.address = address
    # shippingaddress.postal_code = postal_code
    # shippingaddress.country = country
    # shippingaddress.state = state
    return shippingaddress
