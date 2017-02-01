# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-10 09:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('itv', '0003_centros'),
    ]

    operations = [
        migrations.CreateModel(
            name='resultado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resultado', models.IntegerField(default=0)),
                ('vehiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vehiculo', to='itv.vehiculo')),
                ('centro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='centro', to='itv.centros')),
            ],
        ),
    ]
