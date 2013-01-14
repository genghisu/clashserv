# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'BaseBuilding'
        db.create_table('core_basebuilding', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')()),
            ('level', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('size', self.gf('django.db.models.fields.TextField')()),
            ('icon_image', self.gf('django.db.models.fields.TextField')()),
            ('standard_image', self.gf('django.db.models.fields.TextField')()),
            ('cost_type', self.gf('django.db.models.fields.CharField')(default='GOLD', max_length=75)),
            ('elixir_cost', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('gold_cost', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('build_time', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('hit_points', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('elixir_sell_price', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('gold_sell_price', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('production_type', self.gf('django.db.models.fields.CharField')(default='NONE', max_length=75)),
            ('production', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('gold_storage', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('elixir_storage', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('living_space', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('queue_size', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('core', ['BaseBuilding'])

        # Adding model 'DefenseBuilding'
        db.create_table('core_defensebuilding', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')()),
            ('level', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('size', self.gf('django.db.models.fields.TextField')()),
            ('icon_image', self.gf('django.db.models.fields.TextField')()),
            ('standard_image', self.gf('django.db.models.fields.TextField')()),
            ('cost_type', self.gf('django.db.models.fields.CharField')(default='GOLD', max_length=75)),
            ('elixir_cost', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('gold_cost', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('build_time', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('hit_points', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('elixir_sell_price', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('gold_sell_price', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('dps', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('min_range', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('max_range', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('hits_ground', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('hits_air', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('single_use', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('core', ['DefenseBuilding'])

        # Adding model 'Unit'
        db.create_table('core_unit', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')()),
            ('level', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('image', self.gf('django.db.models.fields.TextField')()),
            ('cost_type', self.gf('django.db.models.fields.CharField')(default='ELIXIR', max_length=75)),
            ('elixir_cost', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('gold_cost', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('build_time', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('living_space', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('research_cost', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('research_time', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('lab_level_required', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('hit_points', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('dps', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('range', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('hits_ground', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('hits_air', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_flying', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('core', ['Unit'])

        # Adding model 'Townhall'
        db.create_table('core_townhall', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')()),
            ('level', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('size', self.gf('django.db.models.fields.TextField')()),
            ('icon_image', self.gf('django.db.models.fields.TextField')()),
            ('standard_image', self.gf('django.db.models.fields.TextField')()),
            ('cost_type', self.gf('django.db.models.fields.CharField')(default='GOLD', max_length=75)),
            ('elixir_cost', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('gold_cost', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('build_time', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('hit_points', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('elixir_sell_price', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('gold_sell_price', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('gold_mine', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('elixir_extractor', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('gold_storage', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('elixir_storage', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('builders_hut', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('cannon', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('archer_tower', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('mortar', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('wall', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('bomb', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('air_defense', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('spring_trap', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('wizard_tower', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('giant_bomb', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('hidden_tesla', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('army_camp', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('barracks', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('laboratory', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('spell_factory', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('core', ['Townhall'])

        # Adding model 'Obstacle'
        db.create_table('core_obstacle', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')()),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('size', self.gf('django.db.models.fields.TextField')()),
            ('cost_type', self.gf('django.db.models.fields.CharField')(default='GOLD', max_length=75)),
            ('gold_cost', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('elixir_cost', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('build_time', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('core', ['Obstacle'])

        # Adding model 'Spell'
        db.create_table('core_spell', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')()),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('cost_type', self.gf('django.db.models.fields.CharField')(default='ELIXIR', max_length=75)),
            ('gold_cost', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('elixir_cost', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('core', ['Spell'])

        # Adding model 'GuideCategory'
        db.create_table('core_guidecategory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')()),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('core', ['GuideCategory'])

        # Adding model 'Guide'
        db.create_table('core_guide', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.GuideCategory'])),
            ('name', self.gf('django.db.models.fields.TextField')()),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('sections', self.gf('django.db.models.fields.TextField')()),
            ('icon_image', self.gf('django.db.models.fields.TextField')()),
            ('standard_image', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('core', ['Guide'])

    def backwards(self, orm):
        # Deleting model 'BaseBuilding'
        db.delete_table('core_basebuilding')

        # Deleting model 'DefenseBuilding'
        db.delete_table('core_defensebuilding')

        # Deleting model 'Unit'
        db.delete_table('core_unit')

        # Deleting model 'Townhall'
        db.delete_table('core_townhall')

        # Deleting model 'Obstacle'
        db.delete_table('core_obstacle')

        # Deleting model 'Spell'
        db.delete_table('core_spell')

        # Deleting model 'GuideCategory'
        db.delete_table('core_guidecategory')

        # Deleting model 'Guide'
        db.delete_table('core_guide')

    models = {
        'core.basebuilding': {
            'Meta': {'object_name': 'BaseBuilding'},
            'build_time': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'cost_type': ('django.db.models.fields.CharField', [], {'default': "'GOLD'", 'max_length': '75'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'elixir_cost': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'elixir_sell_price': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'elixir_storage': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'gold_cost': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'gold_sell_price': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'gold_storage': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'hit_points': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'icon_image': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'living_space': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'production': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'production_type': ('django.db.models.fields.CharField', [], {'default': "'NONE'", 'max_length': '75'}),
            'queue_size': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'size': ('django.db.models.fields.TextField', [], {}),
            'standard_image': ('django.db.models.fields.TextField', [], {})
        },
        'core.defensebuilding': {
            'Meta': {'object_name': 'DefenseBuilding'},
            'build_time': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'cost_type': ('django.db.models.fields.CharField', [], {'default': "'GOLD'", 'max_length': '75'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'dps': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'elixir_cost': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'elixir_sell_price': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'gold_cost': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'gold_sell_price': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'hit_points': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'hits_air': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hits_ground': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'icon_image': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'max_range': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'min_range': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'single_use': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'size': ('django.db.models.fields.TextField', [], {}),
            'standard_image': ('django.db.models.fields.TextField', [], {})
        },
        'core.guide': {
            'Meta': {'object_name': 'Guide'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.GuideCategory']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'icon_image': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'sections': ('django.db.models.fields.TextField', [], {}),
            'standard_image': ('django.db.models.fields.TextField', [], {})
        },
        'core.guidecategory': {
            'Meta': {'object_name': 'GuideCategory'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {})
        },
        'core.obstacle': {
            'Meta': {'object_name': 'Obstacle'},
            'build_time': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'cost_type': ('django.db.models.fields.CharField', [], {'default': "'GOLD'", 'max_length': '75'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'elixir_cost': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'gold_cost': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'size': ('django.db.models.fields.TextField', [], {})
        },
        'core.spell': {
            'Meta': {'object_name': 'Spell'},
            'cost_type': ('django.db.models.fields.CharField', [], {'default': "'ELIXIR'", 'max_length': '75'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'elixir_cost': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'gold_cost': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {})
        },
        'core.townhall': {
            'Meta': {'object_name': 'Townhall'},
            'air_defense': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'archer_tower': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'army_camp': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'barracks': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'bomb': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'build_time': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'builders_hut': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'cannon': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'cost_type': ('django.db.models.fields.CharField', [], {'default': "'GOLD'", 'max_length': '75'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'elixir_cost': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'elixir_extractor': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'elixir_sell_price': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'elixir_storage': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'giant_bomb': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'gold_cost': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'gold_mine': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'gold_sell_price': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'gold_storage': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'hidden_tesla': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'hit_points': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'icon_image': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'laboratory': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'level': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'mortar': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'size': ('django.db.models.fields.TextField', [], {}),
            'spell_factory': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'spring_trap': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'standard_image': ('django.db.models.fields.TextField', [], {}),
            'wall': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'wizard_tower': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'core.unit': {
            'Meta': {'object_name': 'Unit'},
            'build_time': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'cost_type': ('django.db.models.fields.CharField', [], {'default': "'ELIXIR'", 'max_length': '75'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'dps': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'elixir_cost': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'gold_cost': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'hit_points': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'hits_air': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hits_ground': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.TextField', [], {}),
            'is_flying': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'lab_level_required': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'level': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'living_space': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'range': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'research_cost': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'research_time': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['core']