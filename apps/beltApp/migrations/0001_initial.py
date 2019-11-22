# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-22 16:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('description', models.TextField()),
                ('age', models.IntegerField(null=True)),
                ('breed', models.CharField(max_length=45)),
                ('species', models.CharField(max_length=45)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=45)),
                ('lastName', models.CharField(max_length=45)),
                ('email', models.CharField(max_length=45)),
                ('password', models.CharField(max_length=255)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='pet',
            name='favorites',
            field=models.ManyToManyField(related_name='usersThatFavorite', to='beltApp.User'),
        ),
        migrations.AddField(
            model_name='pet',
            name='submitted',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userThatSubmitted', to='beltApp.User'),
        ),
    ]
