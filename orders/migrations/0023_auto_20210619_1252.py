# Generated by Django 3.1 on 2021-06-19 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0022_auto_20210619_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='shipCost',
            field=models.DecimalField(decimal_places=2, default=0.04, max_digits=10),
        ),
    ]
