# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-04-06 12:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(default='')),
                ('is_correct', models.BooleanField(default=False)),
                ('creation_date', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('rating', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.IntegerField(default=0)),
                ('object_id', models.PositiveIntegerField(null=True)),
                ('content_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.TextField(default='')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(default='')),
                ('description', models.TextField(default='')),
                ('creation_date', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('rating', models.IntegerField(default=0)),
                ('profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ask_n_answer.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='tags',
            field=models.ManyToManyField(to='ask_n_answer.Tag'),
        ),
        migrations.AddField(
            model_name='like',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ask_n_answer.Profile'),
        ),
        migrations.AddField(
            model_name='answer',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ask_n_answer.Profile'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ask_n_answer.Question'),
        ),
    ]