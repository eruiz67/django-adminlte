# Generated by Django 2.2.10 on 2021-07-22 04:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20210722_0352'),
    ]

    operations = [
        migrations.AddField(
            model_name='workermodel',
            name='area',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='workers', to='app.AreaModel', verbose_name='Area'),
        ),
        migrations.AddField(
            model_name='workermodel',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='workers', to='app.DepartmentModel', verbose_name='Departamento'),
        ),
    ]