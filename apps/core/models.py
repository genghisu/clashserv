from django.db import models
import datetime
from django_extensions.db.fields import CreationDateTimeField, ModificationDateTimeField

class Building(models.Model):
    name = models.TextField()
    level = models.IntegerField(default = 1)
    description = models.TextField()
    size = models.TextField()
    icon_image = models.TextField()
    standard_image = models.TextField()
    
    cost_type = models.CharField(choices = (('ELIXIR', 'ELIXIR'),
                                            ('GOLD', 'GOLD'),
                                            ('GEMS', 'GEMS'),
                                            ('BOTH', 'BOTH')),
                                            max_length = 75,
                                            default = 'GOLD')
    elixir_cost = models.IntegerField(default = 0)
    gold_cost = models.IntegerField(default = 0)
    build_time = models.IntegerField(default = 0)
    hit_points = models.IntegerField(default = 0)
    elixir_sell_price = models.IntegerField(default = 0)
    gold_sell_price = models.IntegerField(default = 0)
    townhall_level = models.IntegerField(default = 1)
    
    class Meta:
        abstract = True
        ordering = ["name", "level"]
        
class BaseBuilding(Building):
    production_type = models.CharField(choices = (('NONE', 'NONE'),
                                                  ('ELIXIR', 'ELIXIR'),
                                                  ('GOLD', 'GOLD'),
                                                  ('BOTH', 'BOTH')),
                                                  max_length = 75,
                                                  default = 'NONE')
    production = models.IntegerField(default = 0)
    storage = models.IntegerField(default = 0)
    
    living_space = models.IntegerField(default = 0)
    queue_size = models.IntegerField(default = 0)
    
    def get_relevant_stats(self):
        stats = 'BASE'
        
        if self.name.lower() in ['gold mine', 'elixir collector']:
            stats = 'PRODUCTION'
        elif self.name.lower() in ['gold storage', 'elixir storage']:
            stats = 'STORAGE'
        elif self.name.lower() in ['army camp']: 
            stats = 'CAMP'
        elif self.name.lower() in ['barracks']:
            stats = 'BARRACKS'
            
        return stats
            
    def full_name(self):
        return "%s - %s" % (self.name, str(self.level))
    
    def unique_names(self):
        return sorted(list(set([x.full_name() for x in BaseBuilding.objects.filter(level = 1).order_by('name')])))
    
    def as_dict(self):
        return {'name':self.name,
                'level':str(self.level),
                'description':self.description,
                'size':self.size,
                'icon_image':self.icon_image,
                'standard_image':self.standard_image,
                'cost_type':self.cost_type,
                'elixir_cost':self.elixir_cost,
                'gold_cost':self.gold_cost,
                'build_time':self.build_time,
                'hit_points':self.hit_points,
                'elixir_sell_price':self.elixir_sell_price,
                'gold_sell_price':self.gold_sell_price,
                'townhall_level':self.townhall_level,
                'production_type':self.production_type,
                'production':self.production,
                'storage':self.storage,
                'living_space':self.living_space,
                'queue_size':self.queue_size,
                'relevant_stats':self.get_relevant_stats()}
        
    def __unicode__(self):
        return "%s - %s" % (self.name, str(self.level))
    
class DefenseBuilding(Building):
    dps = models.IntegerField(default = 0)
    min_range = models.IntegerField(default = 0)
    max_range = models.IntegerField(default = 0)
    hits_ground = models.BooleanField(default = False)
    hits_air = models.BooleanField(default = False)
    single_use = models.BooleanField(default = False)
    
    def full_name(self):
        return "%s - %s" % (self.name, str(self.level))
    
    def unique_names(self):
        return sorted(list(set([x.full_name() for x in DefenseBuilding.objects.filter(level = 1).order_by('name')])))
    
    def as_dict(self):
        return {'name':self.name,
                'level':str(self.level),
                'description':self.description,
                'size':self.size,
                'icon_image':self.icon_image,
                'standard_image':self.standard_image,
                'cost_type':self.cost_type,
                'elixir_cost':self.elixir_cost,
                'gold_cost':self.gold_cost,
                'build_time':self.build_time,
                'hit_points':self.hit_points,
                'elixir_sell_price':self.elixir_sell_price,
                'gold_sell_price':self.gold_sell_price,
                'townhall_level':self.townhall_level,
                'dps':self.dps,
                'min_range':self.min_range,
                'max_range':self.max_range,
                'hits_ground':str(self.hits_ground),
                'hits_air':str(self.hits_air),
                'single_use':str(self.single_use),
                'relevant_stats':'DEFENSE'}
        
    def __unicode__(self):
        return "%s - %s" % (self.name, str(self.level))

class Unit(models.Model):
    name = models.TextField()
    level = models.IntegerField(default = 1)
    description = models.TextField() 
    icon_image = models.TextField(default = '')
    standard_image = models.TextField(default = '')
    
    cost_type = models.CharField(choices = (('ELIXIR', 'ELIXIR'),
                                            ('GOLD', 'GOLD'),
                                            ('BOTH', 'BOTH')),
                                            max_length = 75,
                                            default = 'ELIXIR')
    elixir_cost = models.IntegerField(default = 0)
    gold_cost = models.IntegerField(default = 0)
    build_time = models.IntegerField(default = 0)
    living_space = models.IntegerField(default = 0)
    barracks_level_required = models.IntegerField(default = 0)
    
    research_cost = models.IntegerField(default = 0)
    research_time = models.IntegerField(default = 0)
    lab_level_required = models.IntegerField(default = 0)
                                             
    hit_points = models.IntegerField(default = 0)
    dps = models.IntegerField(default = 0)
    range = models.IntegerField(default = 0)
    hits_ground = models.BooleanField(default = False)
    hits_air = models.BooleanField(default = False)
    is_flying = models.BooleanField(default = False)
    favorite_target = models.TextField(default = '-')
    
    def full_name(self):
        return "%s - %s" % (self.name, str(self.level))
    
    def unique_names(self):
        return sorted(list(set([x.full_name() for x in Unit.objects.filter(level = 1).order_by('barracks_level_required')])))
    
    def as_dict(self):
        return {'name':self.name,
                'level':str(self.level),
                'description':self.description,
                'icon_image':self.icon_image,
                'standard_image':self.standard_image,
                'cost_type':self.cost_type,
                'elixir_cost':self.elixir_cost,
                'gold_cost':self.gold_cost,
                'build_time':self.build_time,
                'living_space':self.living_space,
                'barracks_level_required':self.barracks_level_required,
                'research_cost':self.research_cost,
                'research_time':self.research_time,
                'lab_level_required':self.lab_level_required,
                'hit_points':self.hit_points,
                'dps':self.dps,
                'range':self.range,
                'hits_ground':self.hits_ground,
                'hits_air':self.hits_air,
                'is_flying':self.is_flying,
                'favorite_target':self.favorite_target,
                'relevant_stats':'UNIT',
                }
        
    def __unicode__(self):
        return "%s - %s" % (self.name, str(self.level))

class Townhall(Building):
    gold_mine = models.IntegerField(default = 0)
    elixir_extractor = models.IntegerField(default = 0)
    gold_storage = models.IntegerField(default = 0)
    elixir_storage = models.IntegerField(default = 0)
    builders_hut = models.IntegerField(default = 0)
    cannon = models.IntegerField(default = 0)
    archer_tower = models.IntegerField(default = 0)
    mortar = models.IntegerField(default = 0)
    wall = models.IntegerField(default = 0)
    bomb = models.IntegerField(default = 0)
    air_defense = models.IntegerField(default = 0)
    spring_trap = models.IntegerField(default = 0)
    wizard_tower = models.IntegerField(default = 0)
    giant_bomb = models.IntegerField(default = 0)
    hidden_tesla = models.IntegerField(default = 0)
    army_camp = models.IntegerField(default = 0)
    barracks = models.IntegerField(default = 0)
    laboratory = models.IntegerField(default = 0)
    spell_factory = models.IntegerField(default = 0)
    
    def full_name(self):
        return "%s - %s" % (self.name, str(self.level))
    
    def unique_names(self):
        return sorted(list(set([x.name for x in Townhall.objects.all()])))
    
    def as_dict(self):
        return {'name':self.name,
                'level':str(self.level),
                'description':self.description,
                'size':self.size,
                'icon_image':self.icon_image,
                'standard_image':self.standard_image,
                'cost_type':self.cost_type,
                'elixir_cost':self.elixir_cost,
                'gold_cost':self.gold_cost,
                'build_time':self.build_time,
                'hit_points':self.hit_points,
                'elixir_sell_price':self.elixir_sell_price,
                'gold_sell_price':self.gold_sell_price,
                'townhall_level':self.townhall_level,
                'gold_mine':str(self.gold_mine),
                'elixir_extractor':str(self.elixir_extractor),
                'gold_storage':str(self.gold_storage),
                'elixir_storage':str(self.elixir_storage),
                'builders_hut':str(self.builders_hut),
                'cannon':str(self.cannon),
                'archer_tower':str(self.archer_tower),
                'mortar':str(self.mortar),
                'wall':str(self.wall),
                'bomb':str(self.bomb),
                'air_defense':str(self.air_defense),
                'spring_trap':str(self.spring_trap),
                'wizard_tower':str(self.wizard_tower),
                'giant_bomb':str(self.giant_bomb),
                'hidden_tesla':str(self.hidden_tesla),
                'army_camp':str(self.army_camp),
                'barracks':str(self.barracks),
                'laboratory':str(self.laboratory),
                'spell_factory':str(self.spell_factory)
                }
    def __unicode__(self):
        return "%s - %s" % (self.name, str(self.level))

class Obstacle(models.Model):
    name = models.TextField()
    description = models.TextField()
    size = models.TextField()
    icon_image = models.TextField(default = '-')
    standard_image = models.TextField(default = '-')
    
    cost_type = models.CharField(choices = (('ELIXIR', 'ELIXIR'),
                                            ('GOLD', 'GOLD'),
                                            ('BOTH', 'BOTH')),
                                            max_length = 75,
                                            default = 'GOLD')
    gold_cost = models.IntegerField(default = 0)
    elixir_cost = models.IntegerField(default = 0)
    build_time = models.IntegerField(default = 0)
    
    def full_name(self):
        return self.name
    
    def unique_names(self):
        return list(set([x.name for x in Obstacle.objects.all()]))
    
    def as_dict(self):
        return {'name':self.name,
                'description':self.description,
                'size':self.size,
                'icon_image':self.icon_image,
                'standard_image':self.standard_image,
                'cost_type':self.cost_type,
                'gold_cost':self.gold_cost,
                'elixir_cost':self.elixir_cost,
                'build_time':self.build_time
                }
        
    def __unicode__(self):
        return "%s" % (self.name)

class Spell(models.Model):
    name = models.TextField()
    description = models.TextField()
    cost_type = models.CharField(choices = (('ELIXIR', 'ELIXIR'),
                                            ('GOLD', 'GOLD'),
                                            ('BOTH', 'BOTH')),
                                            max_length = 75,
                                            default = 'ELIXIR')
    gold_cost = models.IntegerField(default = 0)
    elixir_cost = models.IntegerField(default = 0)
    
class GuideCategory(models.Model):
    name = models.TextField()
    description = models.TextField()
    
    def __unicode__(self):
        return "%s" % (self.name)
    
class Guide(models.Model):
    category = models.ForeignKey(GuideCategory)
    name = models.TextField()
    description = models.TextField()
    sections = models.TextField()
    icon_image = models.TextField()
    standard_image = models.TextField()
    order = models.IntegerField(default = 1)
    
    def full_name(self):
        return self.name
    
    def unique_names(self):
        return []
    
    def parse_sections(self):
        parts = self.sections.split('-----')
        final_sections = []
        for part in parts:
            if part.strip().startswith('Image:'):
                final_sections.append(['IMAGE', part.strip().split('Image:')[1].strip()])
            else:
                final_sections.append(['TEXT', part.strip()])
        return final_sections
    
    def as_dict(self):
        return {'category':self.category.name,
                'name':self.name,
                'description':self.description,
                'sections':self.parse_sections(),
                'icon_image':self.icon_image,
                'standard_image':self.standard_image,
                'order':self.order
                }
        
    def __unicode__(self):
        return "%s - %s" % (self.category.name, self.name)

class Achievement(models.Model):
    name = models.TextField(default = '')
    level = models.IntegerField(default = 0)
    description = models.TextField(default = '')
    exp_reward = models.IntegerField(default = 0)
    crystal_reward = models.IntegerField(default = 0)
    icon_image = models.TextField(default = '-')
    standard_image = models.TextField(default = '-')
    
    def full_name(self):
        return "%s - %s" % (self.name, str(self.level))
    
    def unique_names(self):
        return list(set([x.name for x in Achievement.objects.all()]))
    
    def as_dict(self):
        return {'name':self.name,
                'level':self.level,
                'description':self.description,
                'exp_reward':self.exp_reward,
                'crystal_reward':self.crystal_reward,
                'icon_image':self.icon_image,
                'standard_image':self.standard_image,
                }
        
    def __unicode__(self):
        return "%s - %s" % (self.name, self.description)
    
class ExperienceLevel(models.Model):
    level = models.IntegerField(default = 0)
    experience = models.IntegerField(default = 0)
    
    def full_name(self):
        return "%s" % (str(self.level))
    
    def unique_names(self):
        return []
    
    def as_dict(self):
        return {'level':str(self.level),
                'experience':str(self.experience)
                }

class Tip(models.Model):
    target_model = models.TextField(default = "")
    target_name = models.TextField(default = "")
    tip = models.TextField(default = "")
    
    approved = models.BooleanField(default = False)
    date_created = CreationDateTimeField()
    date_modified = ModificationDateTimeField()
    
class Rating(models.Model):
    target_model = models.TextField(default = "")
    target_name = models.TextField(default = "")
    rating = models.IntegerField(default = 5)
    date_created = CreationDateTimeField()
    date_modified = ModificationDateTimeField()
    
class TotalRating(models.Model):
    target_model = models.TextField(default = "")
    target_name = models.TextField(default = "")
    total_rating = models.IntegerField(default = 50)
    rating_count = models.IntegerField(default = 10)