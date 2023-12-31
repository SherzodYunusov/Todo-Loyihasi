# Generated by Django 4.2.1 on 2023-06-22 06:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Aktyor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=50)),
                ('davlat', models.CharField(max_length=50)),
                ('tugulgan_yil', models.DateField()),
                ('jins', models.CharField(choices=[('Erkak', 'Erkak'), ('Ayol', 'Ayol')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Kino',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('janr', models.CharField(max_length=50)),
                ('yil', models.DateField()),
                ('davomiylik', models.DurationField()),
                ('reyting', models.FloatField()),
                ('aktyorlar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.aktyor')),
            ],
        ),
        migrations.CreateModel(
            name='Izoh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matn', models.TextField()),
                ('sana', models.DateField(auto_now_add=True)),
                ('baho', models.PositiveSmallIntegerField()),
                ('kino', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.kino')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
