# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'DayStepData'
        db.create_table('fitapp_daystepdata', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dispatch.Patient'])),
            ('steps', self.gf('django.db.models.fields.IntegerField')()),
            ('date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('fitapp', ['DayStepData'])

        # Adding unique constraint on 'DayStepData', fields ['user', 'date']
        db.create_unique('fitapp_daystepdata', ['user_id', 'date'])

        # Adding model 'AriaData'
        db.create_table('fitapp_ariadata', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dispatch.Patient'])),
            ('body_weight', self.gf('django.db.models.fields.DecimalField')(max_digits=4, decimal_places=1)),
            ('body_fat', self.gf('django.db.models.fields.DecimalField')(max_digits=3, decimal_places=1)),
            ('bmi', self.gf('django.db.models.fields.DecimalField')(max_digits=3, decimal_places=1)),
            ('date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('fitapp', ['AriaData'])

        # Adding model 'MinuteStepData'
        db.create_table('fitapp_minutestepdata', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dispatch.Patient'])),
            ('steps', self.gf('django.db.models.fields.IntegerField')()),
            ('day', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fitapp.DayStepData'])),
            ('time', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('fitapp', ['MinuteStepData'])

        # Adding unique constraint on 'MinuteStepData', fields ['user', 'time']
        db.create_unique('fitapp_minutestepdata', ['user_id', 'time'])


        # Changing field 'UserFitbit.user'
        db.alter_column('fitapp_userfitbit', 'user_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dispatch.Patient'], unique=True))

        # Changing field 'TimeSeriesData.user'
        db.alter_column('fitapp_timeseriesdata', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dispatch.Patient']))

    def backwards(self, orm):
        # Removing unique constraint on 'MinuteStepData', fields ['user', 'time']
        db.delete_unique('fitapp_minutestepdata', ['user_id', 'time'])

        # Removing unique constraint on 'DayStepData', fields ['user', 'date']
        db.delete_unique('fitapp_daystepdata', ['user_id', 'date'])

        # Deleting model 'DayStepData'
        db.delete_table('fitapp_daystepdata')

        # Deleting model 'AriaData'
        db.delete_table('fitapp_ariadata')

        # Deleting model 'MinuteStepData'
        db.delete_table('fitapp_minutestepdata')


        # Changing field 'UserFitbit.user'
        db.alter_column('fitapp_userfitbit', 'user_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True))

        # Changing field 'TimeSeriesData.user'
        db.alter_column('fitapp_timeseriesdata', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User']))

    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'dispatch.patient': {
            'Meta': {'object_name': 'Patient'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '127'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '127'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'practitioner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'fitapp.ariadata': {
            'Meta': {'object_name': 'AriaData'},
            'bmi': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '1'}),
            'body_fat': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '1'}),
            'body_weight': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '1'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dispatch.Patient']"})
        },
        'fitapp.daystepdata': {
            'Meta': {'unique_together': "(('user', 'date'),)", 'object_name': 'DayStepData'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'steps': ('django.db.models.fields.IntegerField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dispatch.Patient']"})
        },
        'fitapp.minutestepdata': {
            'Meta': {'unique_together': "(('user', 'time'),)", 'object_name': 'MinuteStepData'},
            'day': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fitapp.DayStepData']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'steps': ('django.db.models.fields.IntegerField', [], {}),
            'time': ('django.db.models.fields.DateField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dispatch.Patient']"})
        },
        'fitapp.timeseriesdata': {
            'Meta': {'unique_together': "(('user', 'resource_type', 'date'),)", 'object_name': 'TimeSeriesData'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'resource_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fitapp.TimeSeriesDataType']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dispatch.Patient']"}),
            'value': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '32', 'null': 'True'})
        },
        'fitapp.timeseriesdatatype': {
            'Meta': {'ordering': "['category', 'resource']", 'unique_together': "(('category', 'resource'),)", 'object_name': 'TimeSeriesDataType'},
            'category': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'resource': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'fitapp.userfitbit': {
            'Meta': {'object_name': 'UserFitbit'},
            'auth_secret': ('django.db.models.fields.TextField', [], {}),
            'auth_token': ('django.db.models.fields.TextField', [], {}),
            'fitbit_user': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dispatch.Patient']", 'unique': 'True'})
        }
    }

    complete_apps = ['fitapp']