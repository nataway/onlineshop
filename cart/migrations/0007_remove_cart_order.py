# Generated by Django 3.1 on 2021-06-18 01:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0006_cart_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='order',
        ),
    ]
