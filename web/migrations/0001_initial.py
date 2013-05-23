# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Plant'
        db.create_table(u'web_plant', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'web', ['Plant'])

        # Adding model 'Cultivar'
        db.create_table(u'web_cultivar', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('plant', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.Plant'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('temp_low', self.gf('django.db.models.fields.FloatField')()),
            ('temp_high', self.gf('django.db.models.fields.FloatField')()),
            ('elevation_low', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('elevation_high', self.gf('django.db.models.fields.IntegerField')()),
            ('soil_type', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('ph_low', self.gf('django.db.models.fields.FloatField')()),
            ('ph_high', self.gf('django.db.models.fields.FloatField')()),
            ('sunlight', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('precipitation_low', self.gf('django.db.models.fields.IntegerField')()),
            ('precipitation_high', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'web', ['Cultivar'])


    def backwards(self, orm):
        # Deleting model 'Plant'
        db.delete_table(u'web_plant')

        # Deleting model 'Cultivar'
        db.delete_table(u'web_cultivar')


    models = {
        u'web.cultivar': {
            'Meta': {'object_name': 'Cultivar'},
            'elevation_high': ('django.db.models.fields.IntegerField', [], {}),
            'elevation_low': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'ph_high': ('django.db.models.fields.FloatField', [], {}),
            'ph_low': ('django.db.models.fields.FloatField', [], {}),
            'plant': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['web.Plant']"}),
            'precipitation_high': ('django.db.models.fields.IntegerField', [], {}),
            'precipitation_low': ('django.db.models.fields.IntegerField', [], {}),
            'soil_type': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'sunlight': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'temp_high': ('django.db.models.fields.FloatField', [], {}),
            'temp_low': ('django.db.models.fields.FloatField', [], {})
        },
        u'web.plant': {
            'Meta': {'object_name': 'Plant'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['web']