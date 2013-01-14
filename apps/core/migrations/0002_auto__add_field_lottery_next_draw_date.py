# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Lottery.next_draw_date'
        db.add_column('core_lottery', 'next_draw_date',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 4, 29, 0, 0), blank=True),
                      keep_default=False)

    def backwards(self, orm):
        # Deleting field 'Lottery.next_draw_date'
        db.delete_column('core_lottery', 'next_draw_date')

    models = {
        'core.drawing': {
            'Meta': {'object_name': 'Drawing'},
            'completed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lottery': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'drawings'", 'to': "orm['core.Lottery']"}),
            'numbers': ('django.db.models.fields.TextField', [], {})
        },
        'core.lottery': {
            'Meta': {'object_name': 'Lottery'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'has_power_draw': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'next_draw_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 4, 29, 0, 0)', 'blank': 'True'}),
            'power_draw_max': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'power_draw_min': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'primary_draws_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'primary_draws_max': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'primary_draws_min': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'core.state': {
            'Meta': {'object_name': 'State'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lotteries': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['core.Lottery']", 'through': "orm['core.StateLottery']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.TextField', [], {})
        },
        'core.statelottery': {
            'Meta': {'object_name': 'StateLottery'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lottery': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Lottery']"}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.State']"})
        }
    }

    complete_apps = ['core']