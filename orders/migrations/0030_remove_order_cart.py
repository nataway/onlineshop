# Generated by Django 3.1 on 2021-10-04 00:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0029_auto_20211001_2141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='cart',
        ),
    ]
