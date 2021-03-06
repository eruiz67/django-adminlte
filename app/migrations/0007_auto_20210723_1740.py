# Generated by Django 2.2.10 on 2021-07-23 17:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0006_personmodel_identification_image_front'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personmodel',
            name='identification_image_front',
            field=models.FileField(blank=True, null=True, upload_to='app_person_identification_image_front', verbose_name='Foto carnet frontal'),
        ),
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='fecha creación')),
                ('write_date', models.DateTimeField(auto_now=True, null=True, verbose_name='última modificación')),
                ('active', models.BooleanField(default=True, verbose_name='Activo?')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Nombre')),
                ('description', models.TextField(blank=True, max_length=500, null=True, verbose_name='Descripción')),
                ('create_uid', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='creado por')),
                ('write_uid', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='modificado por')),
            ],
            options={
                'verbose_name': 'Categoría',
                'verbose_name_plural': 'Categorías',
                'db_table': 'app_category',
                'managed': True,
            },
        ),
    ]
