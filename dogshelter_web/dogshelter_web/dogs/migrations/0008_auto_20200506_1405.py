# Generated by Django 3.0.4 on 2020-05-06 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dogs', '0007_auto_20200506_1359'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dog',
            options={'verbose_name': 'Kutyák'},
        ),
        migrations.AlterModelOptions(
            name='dogimages',
            options={'verbose_name': 'Képek kutyáról'},
        ),
        migrations.AlterField(
            model_name='dog',
            name='income_date',
            field=models.DateField(verbose_name='Felvételi dátum'),
        ),
    ]
