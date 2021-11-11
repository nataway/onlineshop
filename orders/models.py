# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from shop.models import Product
from accounts.models import User
from payment.models import PaymentModel , ShippingAddress
# from cart.models import Cart


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    payment = models.ForeignKey(PaymentModel, on_delete=models.CASCADE, null=True)
    shippingAddress = models.ForeignKey(ShippingAddress, on_delete=models.CASCADE, null=True)
    # cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
    isDelivered = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    isPaid = models.BooleanField(default=False)
    # shipCost = models.DecimalField( max_digits=10,decimal_places=2, null = True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return ' {} '.format(self.id)


class OrderItem(models.Model):
    order = models.ForeignKey(Order,
    related_name='items',
    on_delete=models.CASCADE,
    )
    product = models.ForeignKey(Product,
    related_name='products',
    on_delete=models.CASCADE,
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity