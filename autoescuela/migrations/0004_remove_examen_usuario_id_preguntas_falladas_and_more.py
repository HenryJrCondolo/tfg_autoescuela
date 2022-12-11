# Generated by Django 4.1.3 on 2022-12-10 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autoescuela', '0003_alter_examen_usuario_fecha'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='examen_usuario',
            name='id_preguntas_falladas',
        ),
        migrations.RemoveField(
            model_name='examen_usuario',
            name='respuestas_Usuario',
        ),
        migrations.AddField(
            model_name='examen_usuario',
            name='preguntas_falladas',
            field=models.ManyToManyField(to='autoescuela.pregunta'),
        ),
    ]
