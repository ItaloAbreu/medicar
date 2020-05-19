# Generated by Django 3.0.6 on 2020-05-18 22:43

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_medico'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.DateField()),
                ('horarios', django.contrib.postgres.fields.ArrayField(base_field=models.TimeField(), size=None)),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Medico')),
            ],
        ),
    ]