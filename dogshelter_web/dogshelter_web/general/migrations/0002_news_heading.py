# Generated by Django 3.0.4 on 2020-04-07 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='heading',
            field=models.TextField(null=True),
        ),
    ]
