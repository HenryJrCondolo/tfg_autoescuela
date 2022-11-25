# Generated by Django 4.1.3 on 2022-11-24 19:35

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Examen',
            fields=[
                ('id_Examen', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_Examen', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Permiso',
            fields=[
                ('tipo_licencia', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.TextField()),
                ('precio', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Temas',
            fields=[
                ('id_Tema', models.AutoField(primary_key=True, serialize=False)),
                ('tema', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('dni', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('fecha_nacimiento', models.DateField()),
                ('direccion', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=9)),
                ('email', models.EmailField(max_length=254)),
                ('fecha_matriculacion', models.DateField()),
                ('fecha_salida', models.DateField(blank=True, default=None, null=True)),
                ('permiso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autoescuela.permiso')),
            ],
        ),
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id_Pregunta', models.AutoField(primary_key=True, serialize=False)),
                ('pregunta', models.TextField()),
                ('respuesta_Falsa_1', models.TextField()),
                ('respuesta_Falsa_2', models.TextField()),
                ('respuesta_Correcta', models.TextField()),
                ('imagen_pregunta', models.ImageField(blank=True, null=True, upload_to='preguntas')),
                ('descripcion_adicional', models.TextField(blank=True, null=True)),
                ('permiso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autoescuela.permiso')),
                ('tema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autoescuela.temas')),
            ],
        ),
        migrations.CreateModel(
            name='Examen_Usuario',
            fields=[
                ('id_Examen_Usuario', models.AutoField(primary_key=True, serialize=False)),
                ('respuestas_Usuario', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), size=None)),
                ('aprobado', models.BooleanField(default=False)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('examen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autoescuela.examen')),
                ('preguntas_falladas', models.ManyToManyField(to='autoescuela.pregunta')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autoescuela.usuario')),
            ],
        ),
        migrations.AddField(
            model_name='examen',
            name='preguntas',
            field=models.ManyToManyField(to='autoescuela.pregunta'),
        ),
    ]