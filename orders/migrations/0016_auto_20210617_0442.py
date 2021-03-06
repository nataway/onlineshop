# Generated by Django 3.1 on 2021-06-16 23:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0004_auto_20210617_0442'),
        ('orders', '0015_remove_order_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='payment.paymentmodel'),
        ),
        migrations.AddField(
            model_name='order',
            name='shippingadd',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='payment.shippingaddress'),
        ),
    ]
