# Generated by Django 3.1 on 2021-10-01 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0006_auto_20210618_2234'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paymentmodel',
            name='order',
        ),
        migrations.RemoveField(
            model_name='shippingaddress',
            name='order',
        ),
    ]
