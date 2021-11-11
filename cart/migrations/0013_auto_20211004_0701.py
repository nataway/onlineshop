# Generated by Django 3.1 on 2021-10-04 01:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0030_remove_order_cart'),
        ('cart', '0012_auto_20211004_0634'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='order',
        ),
        migrations.AddField(
            model_name='cartitem',
            name='order',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.order'),
        ),
    ]