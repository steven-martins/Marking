# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('result', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('file', models.ImageField(max_length=150, upload_to='picture/%Y/%m/%d')),
                ('title', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('marks', models.ManyToManyField(to=settings.AUTH_USER_MODEL, through='marks.Mark', related_name='project_marks_student')),
                ('members', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('pictures', models.ManyToManyField(to='marks.Picture', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('title', models.CharField(max_length=200)),
                ('detail', models.CharField(max_length=250, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('login', models.CharField(serialize=False, max_length=10, primary_key=True)),
                ('last_connection', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Timeslot',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('title', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='project',
            name='timeslot',
            field=models.ForeignKey(to='marks.Timeslot', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mark',
            name='project',
            field=models.ForeignKey(to='marks.Project'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mark',
            name='question',
            field=models.ForeignKey(to='marks.Question'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mark',
            name='student',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
