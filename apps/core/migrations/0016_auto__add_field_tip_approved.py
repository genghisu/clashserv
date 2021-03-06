# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Tip.approved'
        db.add_column('core_tip', 'approved',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

    def backwards(self, orm):
        # Deleting field 'Tip.approved'
        db.delete_column('core_tip', 'approved')

    models = {
        'core.achievement': {
            'Meta': {'object_name': 'Achievement'},
            'crystal_reward': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'exp_reward': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'icon_image': ('django.db.models.fields.TextField', [], {'default': "'-'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'standard_image': ('django.db.models.fields.TextField', [], {'default': "'-'"})
        },
        'core.basebuilding': {
            'Meta': {'ordering': "['name', 'level']", 'object_name': 'BaseBuilding'},
            'build_time': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'cost_type': ('django.db.models.fields.CharField', [], {'default': "'GOLD'", 'max_length': '75'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'elixir_cost': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'elixir_sell_price': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'gold_cost': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'gold_sell_price': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
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
            'standard_image': ('django.db.models.fields.TextField', [], {}),
            'storage': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'townhall_level': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        },
        'core.defensebuilding': {
            'Meta': {'ordering': "['name', 'level']", 'object_name': 'DefenseBuilding'},
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
            'standard_image': ('django.db.models.fields.TextField', [], {}),
            'townhall_level': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        },
        'core.experiencelevel': {
            'Meta': {'object_name': 'ExperienceLevel'},
            'experience': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'core.guide': {
            'Meta': {'object_name': 'Guide'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.GuideCategory']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'icon_image': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
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
            'icon_image': ('django.db.models.fields.TextField', [], {'default': "'-'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'size': ('django.db.models.fields.TextField', [], {}),
            'standard_image': ('django.db.models.fields.TextField', [], {'default': "'-'"})
        },
        'core.rating': {
            'Meta': {'object_name': 'Rating'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rating': ('django.db.models.fields.IntegerField', [], {'default': '5'}),
            'target_model': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'target_name': ('django.db.models.fields.TextField', [], {'default': "''"})
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
        'core.tip': {
            'Meta': {'object_name': 'Tip'},
            'approved': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'target_model': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'target_name': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'tip': ('django.db.models.fields.TextField', [], {'default': "''"})
        },
        'core.totalrating': {
            'Meta': {'object_name': 'TotalRating'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rating_count': ('django.db.models.fields.IntegerField', [], {'default': '10'}),
            'target_model': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'target_name': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'total_rating': ('django.db.models.fields.IntegerField', [], {'default': '50'})
        },
        'core.townhall': {
            'Meta': {'ordering': "['name', 'level']", 'object_name': 'Townhall'},
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
            'townhall_level': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'wall': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'wizard_tower': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'core.unit': {
            'Meta': {'object_name': 'Unit'},
            'barracks_level_required': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'build_time': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'cost_type': ('django.db.models.fields.CharField', [], {'default': "'ELIXIR'", 'max_length': '75'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'dps': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'elixir_cost': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'favorite_target': ('django.db.models.fields.TextField', [], {'default': "'-'"}),
            'gold_cost': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'hit_points': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'hits_air': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hits_ground': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'icon_image': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_flying': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'lab_level_required': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'level': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'living_space': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'range': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'research_cost': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'research_time': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'standard_image': ('django.db.models.fields.TextField', [], {'default': "''"})
        }
    }

    complete_apps = ['core']