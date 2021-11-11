# Generated by Django 3.1 on 2021-06-19 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_remove_user_username1'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='userName',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=40),
        ),
    ]