# Generated by Django 3.1.2 on 2020-10-27 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facciones', '0005_auto_20201027_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='apikey',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
