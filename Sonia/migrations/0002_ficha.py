# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2019-05-15 21:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sonia', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ficha',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=120)),
                ('comienzo', models.DateTimeField(auto_now_add=True)),
                ('contrato', models.FileField(blank=True, null=True, upload_to=b'')),
            ],
            options={
                'verbose_name': 'Ficha',
                'verbose_name_plural': 'Ficha',
            },
        ),
    ]