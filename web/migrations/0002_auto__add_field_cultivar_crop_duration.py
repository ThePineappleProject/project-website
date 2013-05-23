# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Cultivar.crop_duration'
        db.add_column(u'web_cultivar', 'crop_duration',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Cultivar.crop_duration'
        db.delete_column(u'web_cultivar', 'crop_duration')


    models = {
        u'web.cultivar': {
            'Meta': {'object_name': 'Cultivar'},
            'crop_duration': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
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