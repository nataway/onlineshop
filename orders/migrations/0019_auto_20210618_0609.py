# Generated by Django 3.1 on 2021-06-18 00:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0018_order_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='order',
            name='payment',
        ),
        migrations.RemoveField(
            model_name='order',
            name='shippingaddress',
        ),
    ]