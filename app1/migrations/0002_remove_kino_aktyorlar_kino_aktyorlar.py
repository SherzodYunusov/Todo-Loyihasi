# Generated by Django 4.2.1 on 2023-06-22 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kino',
            name='aktyorlar',
        ),
        migrations.AddField(
            model_name='kino',
            name='aktyorlar',
            field=models.ManyToManyField(to='app1.aktyor'),
        ),
    ]
