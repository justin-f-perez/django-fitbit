# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    # Since the user model for UserFitbit is allowed to be user set, the app
    # that contains the model must be migrated before this.
    required_app = settings.USERFITBIT_USER_MODEL.split('.')[0]

    dependencies = [
        (required_app, '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeSeriesData',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('value', models.CharField(null=True, default=None, max_length=32)),
                ('intraday', models.BooleanField(default=False)),
            ],
            options={
                'get_latest_by': 'date',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TimeSeriesDataType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('category', models.IntegerField(choices=[(0, 'foods'), (1, 'activities'), (2, 'sleep'), (3, 'body')])),
                ('resource', models.CharField(max_length=128)),
                ('intraday_support', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['category', 'resource'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserFitbit',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('fitbit_user', models.CharField(max_length=32, unique=True)),
                ('auth_token', models.TextField()),
                ('auth_secret', models.TextField()),
                ('user', models.OneToOneField(to=settings.USERFITBIT_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='timeseriesdatatype',
            unique_together=set([('category', 'resource')]),
        ),
        migrations.AddField(
            model_name='timeseriesdata',
            name='resource_type',
            field=models.ForeignKey(to='fitapp.TimeSeriesDataType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='timeseriesdata',
            name='user',
            field=models.ForeignKey(to=settings.USERFITBIT_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='timeseriesdata',
            unique_together=set([('user', 'resource_type', 'date', 'intraday')]),
        ),
    ]
