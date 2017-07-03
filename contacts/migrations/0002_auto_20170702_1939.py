# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-02 18:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'ordering': ['-name']},
        ),
        migrations.AddField(
            model_name='contact',
            name='image',
            field=models.ImageField(default='images/noimages.jpg', upload_to='images'),
        ),
    ]