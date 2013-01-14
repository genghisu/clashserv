# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Drawing.jackpot'
        db.add_column('core_drawing', 'jackpot',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Lottery.current_jackpot'
        db.add_column('core_lottery', 'current_jackpot',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

    def backwards(self, orm):
        # Deleting field 'Drawing.jackpot'
        db.delete_column('core_drawing', 'jackpot')

        # Deleting field 'Lottery.current_jackpot'
        db.delete_column('core_lottery', 'current_jackpot')

    models = {
        'core.drawing': {
            'Meta': {'object_name': 'Drawing'},
            'completed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jackpot': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'lottery': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'drawings'", 'to': "orm['core.Lottery']"}),
            'numbers': ('django.db.models.fields.TextField', [], {})
        },
        'core.lottery': {
            'Meta': {'object_name': 'Lottery'},
            'current_jackpot': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'has_power_draw': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'next_draw_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 5, 1, 0, 0)', 'blank': 'True'}),
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