# Generated by Django 4.2.6 on 2023-11-24 02:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asistencia', '0003_alter_seccionalumno_seccion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asistencia',
            name='fecha_hora',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='asistencia',
            name='seccion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asistencia.seccion'),
        ),
    ]
