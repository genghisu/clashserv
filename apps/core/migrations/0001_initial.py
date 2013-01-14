# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Lottery'
        db.create_table('core_lottery', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')()),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('has_power_draw', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('primary_draws_count', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('primary_draws_min', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('primary_draws_max', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('power_draw_min', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('power_draw_max', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('core', ['Lottery'])

        # Adding model 'State'
        db.create_table('core_state', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')()),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('core', ['State'])

        # Adding model 'StateLottery'
        db.create_table('core_statelottery', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('state', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.State'])),
            ('lottery', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Lottery'])),
        ))
        db.send_create_signal('core', ['StateLottery'])

        # Adding model 'Drawing'
        db.create_table('core_drawing', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('completed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('numbers', self.gf('django.db.models.fields.TextField')()),
            ('lottery', self.gf('django.db.models.fields.related.ForeignKey')(related_name='drawings', to=orm['core.Lottery'])),
        ))
        db.send_create_signal('core', ['Drawing'])

    def backwards(self, orm):
        # Deleting model 'Lottery'
        db.delete_table('core_lottery')

        # Deleting model 'State'
        db.delete_table('core_state')

        # Deleting model 'StateLottery'
        db.delete_table('core_statelottery')

        # Deleting model 'Drawing'
        db.delete_table('core_drawing')

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