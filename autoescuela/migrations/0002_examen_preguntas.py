# Generated by Django 4.1.3 on 2022-12-07 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autoescuela', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='examen',
            name='preguntas',
            field=models.ManyToManyField(to='autoescuela.pregunta'),
        ),
    ]
