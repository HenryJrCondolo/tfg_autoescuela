# Generated by Django 4.1.3 on 2022-11-24 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autoescuela', '0002_rename_temas_tema'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permiso',
            name='tipo_licencia',
            field=models.CharField(max_length=11, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='dni',
            field=models.CharField(max_length=11, primary_key=True, serialize=False, unique=True),
        ),
    ]
