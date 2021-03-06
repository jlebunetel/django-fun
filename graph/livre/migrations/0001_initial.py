# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-04 20:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Edge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(max_length=200)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('modification_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entity', models.CharField(max_length=200)),
                ('value', models.TextField()),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('modification_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='edge',
            name='end_node',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='end_node', to='livre.Node'),
        ),
        migrations.AddField(
            model_name='edge',
            name='start_node',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='start_node', to='livre.Node'),
        ),
    ]
