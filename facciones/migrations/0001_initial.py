# Generated by Django 3.1.2 on 2020-10-26 00:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Castle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Faction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faction_name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='', verbose_name='uploads/')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=150)),
                ('fullname', models.CharField(max_length=100)),
                ('lastlogin', models.DateTimeField()),
                ('apikey', models.CharField(max_length=100)),
                ('castle', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='facciones.castle')),
                ('faction', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='facciones.faction')),
            ],
        ),
        migrations.CreateModel(
            name='ScoreHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.TextField()),
                ('score', models.IntegerField()),
                ('date', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facciones.user')),
            ],
        ),
    ]
