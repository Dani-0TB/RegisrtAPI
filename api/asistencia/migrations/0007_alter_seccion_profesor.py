# Generated by Django 4.2.6 on 2023-12-11 20:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asistencia', '0006_asistencia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seccion',
            name='profesor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asistencia.profesor'),
        ),
    ]
