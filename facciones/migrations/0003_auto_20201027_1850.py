# Generated by Django 3.1.2 on 2020-10-27 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facciones', '0002_auto_20201027_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='castle',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='uploads/'),
        ),
    ]
