# Generated by Django 2.2.10 on 2021-07-20 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personmodel',
            name='identification',
            field=models.CharField(max_length=11, unique=True, verbose_name='Carnet'),
        ),
    ]
