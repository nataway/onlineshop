# Generated by Django 3.1 on 2021-10-04 00:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0030_remove_order_cart'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cart', '0010_auto_20211004_0605'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='order',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.order'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
