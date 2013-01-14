from optparse import make_option
import sys
import json
import csv
from os.path import join,  dirname,  normpath
import datetime

from django.conf import settings
from django.core import management
from django.core.management.base import BaseCommand
from django.test.utils import get_runner
from django.core.exceptions import ObjectDoesNotExist

from core.models import BaseBuilding, DefenseBuilding, Unit, Townhall, Obstacle, Spell, Achievement, ExperienceLevel, Guide

def calculate_build_time(days, hours, minutes):
    return 60 * 24 * days + 60 * hours + minutes

class Command(BaseCommand):
    help = 'Load initial Clash data.'
    args = []
    
    requires_model_validation = True
    
    def export_data(self):
        data = {}
        
        base_data = {'base_buildings':BaseBuilding.objects.all(),
                     'defense_buildings':DefenseBuilding.objects.all(),
                     'units':Unit.objects.all(),
                     'townhall':Townhall.objects.all(),
                     'obstacle':Obstacle.objects.all(),
                     'achievement':Achievement.objects.all(),
                     'experience_level':ExperienceLevel.objects.all(),
                     'gameplay_guides':Guide.objects.filter(category__name = 'Gameplay'),
                     'strategy_guides':Guide.objects.filter(category__name = 'Strategy')}
        
        for k, v in base_data.items():
            data_group = k
            object_names = [object.full_name() for object in v]
            object_details = {}
            unique_names = []
            for object in v:
                object_details[object.full_name()] = object.as_dict()
                unique_names = object.unique_names()
            data[data_group] = {'names':object_names, 'details':object_details, 'unique_names':unique_names}
        final_data = {'data':data}
        
        PROJECT_ROOT = join(dirname(normpath(__file__)), '..')
        DATA_DIR = join(PROJECT_ROOT, '../../../data')
        OUTPUT_FILE = join(DATA_DIR, 'data.json')
        
        with open(OUTPUT_FILE, 'w+') as file:
            file.write(json.dumps(final_data))
    
    def load_townhall(self):        
        PROJECT_ROOT = join(dirname(normpath(__file__)), '..')
        DATA_DIR = join(PROJECT_ROOT, '../../../data')
        TARGET_CSV = join(DATA_DIR, 'townhall_levels.csv')
        
        townhall_fields = ["Name",
                           "AttackCost",
                           "Troop Housing",
                           "Elixir Storage",
                           "Gold Storage",
                           "Elixir Pump",
                           "Gold Mine",
                           "Barrack",
                           "Cannon",
                           "Wall",
                           "Archer Tower",
                           "Wizard Tower",
                           "Air Defense",
                           "Mortar",
                           "Alliance Castle",
                           "Ejector",
                           "Superbomb",
                           "Mine",
                           "Worker Building",
                           "Laboratory",
                           "Communications mast",
                           "Tesla Tower",
                           "Spell Forge"]
                
        with open(TARGET_CSV, 'rb') as units_file:
            reader = csv.reader(units_file)
            counter = 1
            current_name = ''
            current_level = 1
            current_army_camp = 0
            current_elixir_storage = 0
            current_gold_storage = 0
            current_elixir_pump = 0
            current_gold_mine = 0
            current_barracks = 0
            current_cannon = 0
            current_wall = 0
            current_archer_tower = 0
            current_wizard_tower = 0
            current_air_defense = 0
            current_mortar = 0
            current_clan_castle = 0
            current_super_bomb = 0
            current_bomb = 0
            current_builder_shut = 0
            current_laboratory = 0
            current_tesla_tower = 0
            current_spell_forge = 0
            for row in reader:
                if counter >= 3:
                    current_army_camp = row[2] if row[2] else current_army_camp
                    current_elixir_storage = row[3] if row[3] else current_elixir_storage
                    current_gold_storage = row[4] if row[4] else current_gold_storage
                    current_elixir_pump = row[5] if row[5] else current_elixir_pump
                    current_gold_mine = row[6] if row[6] else current_gold_mine
                    current_barracks = row[7] if row[7] else current_barracks
                    current_cannon = row[8] if row[8] else current_cannon
                    current_wall = row[9] if row[9] else current_wall
                    current_archer_tower = row[10] if row[10] else current_archer_tower
                    current_wizard_tower = row[11] if row[11] else current_wizard_tower
                    current_air_defense = row[12] if row[12] else current_air_defense
                    current_mortar = row[13] if row[13] else current_mortar
                    current_clan_castle = row[14] if row[14] else current_clan_castle
                    current_super_bomb = row[16] if row[16] else current_super_bomb
                    current_bomb = row[17] if row[17] else current_bomb
                    current_builders_hut = row[18] if row[18] else current_builders_hut
                    current_laboratory = row[19] if row[19] else current_laboratory
                    current_tesla_tower = row[21] if row[21] else current_tesla_tower
                    current_spell_forge = row[22] if row[22] else current_spell_forge
                    try:
                        townhall_object = Townhall.objects.get(level = current_level)
                        townhall_object.army_camp = current_army_camp
                        townhall_object.elixir_storage = current_elixir_storage
                        townhall_object.gold_storage = current_gold_storage
                        townhall_object.elixir_extractor = current_elixir_pump
                        townhall_object.gold_mine = current_gold_mine
                        townhall_object.barracks = current_barracks
                        townhall_object.cannon = current_cannon
                        townhall_object.wall = current_wall
                        townhall_object.archer_tower = current_archer_tower
                        townhall_object.wizard_tower = current_wizard_tower
                        townhall_object.air_defense = current_air_defense
                        townhall_object.mortar = current_mortar
                        townhall_object.clan_castle = current_clan_castle
                        townhall_object.giant_bomb = current_super_bomb
                        townhall_object.bomb = current_bomb
                        townhall_object.builders_hut = current_builders_hut
                        townhall_object.laboratory = current_laboratory
                        townhall_object.hidden_tesla = current_tesla_tower
                        townhall_object.spell_factory = current_spell_forge
                        townhall_object.save()
                    except ObjectDoesNotExist:
                        townhall_object = None
                    current_level = current_level + 1
                counter = counter + 1
    
    def load_text(self):
        self.texts = {}
        PROJECT_ROOT = join(dirname(normpath(__file__)), '..')
        DATA_DIR = join(PROJECT_ROOT, '../../../data')
        TARGET_CSV = join(DATA_DIR, 'texts.csv')
        
        with open(TARGET_CSV, 'rb') as units_file:
            reader = csv.reader(units_file)
            counter = 1
            current_name = ''
            current_level = 1
            for row in reader:
                if counter >= 3:
                    key = row[0]
                    text = row[1]
                    self.texts[key] = text
                counter = counter + 1
        print self.texts
    
    def load_experience_levels(self):
        PROJECT_ROOT = join(dirname(normpath(__file__)), '..')
        DATA_DIR = join(PROJECT_ROOT, '../../../data')
        TARGET_CSV = join(DATA_DIR, 'experience_levels.csv')
        
        with open(TARGET_CSV, 'rb') as units_file:
            reader = csv.reader(units_file)
            counter = 1
            current_level = 1
            for row in reader:
                if counter >= 3:
                    try:
                        level_object = ExperienceLevel.objects.get(level = row[0])
                        level_object.experience = row[1]
                        level_object.save()
                    except ObjectDoesNotExist:
                        level_object = ExperienceLevel(level = row[0],
                                                       experience = row[1])
                        level_object.save()
                    current_level = current_level + 1
                counter = counter + 1
                
    def load_achievements(self):
        PROJECT_ROOT = join(dirname(normpath(__file__)), '..')
        DATA_DIR = join(PROJECT_ROOT, '../../../data')
        TARGET_CSV = join(DATA_DIR, 'achievements.csv')
        
        with open(TARGET_CSV, 'rb') as units_file:
            reader = csv.reader(units_file)
            counter = 1
            current_name = ''
            current_level = 1
            for row in reader:
                if counter >= 3:
                    base_title = row[2]
                    base_description = row[3]
                    base_count = row[5]
                    exp = row[7]
                    crystal = row[8]
                    if base_title and base_description:
                        title = self.texts.get(base_title)
                        description = self.texts.get(base_description).replace('<number>', base_count)
                        if base_title == current_name:
                            current_level = current_level + 1
                        else:
                            current_level = 1
                            current_name = base_title
                        print "%s - %s" % (title, description)
                        try:
                            achievement_object = Achievement.objects.get(name = title, level = current_level)
                        except ObjectDoesNotExist:
                            achievement_object = Achievement(name = title,
                                                             description = description,
                                                             level = current_level,
                                                             exp_reward = exp,
                                                             crystal_reward = crystal)
                            achievement_object.save()
                            
                counter = counter + 1
 
    def load_units(self):
        PROJECT_ROOT = join(dirname(normpath(__file__)), '..')
        DATA_DIR = join(PROJECT_ROOT, '../../../data')
        TARGET_CSV = join(DATA_DIR, 'characters.csv')
        UNIT_FIELDS = ["Name",
                       "TID",
                       "SWF",
                       "HousingSpace",
                       "BarrackLevel",
                       "LaboratoryLevel",
                       "Speed",
                       "Hitpoints",
                       "TrainingTime",
                       "TrainingResource",
                       "TrainingCost",
                       "UpgradeTimeH",
                       "UpgradeResource",
                       "UpgradeCost",
                       "AttackRange",
                       "AttackSpeed",
                       "Damage",
                       "PreferedTargetDamageMod",
                       "DamageRadius",
                       "IconSWF",
                       "IconExportName",
                       "BigPicture"
                       ,"Projectile",
                       "PreferedTargetBuilding",
                       "DeployEffect","AttackEffect","HitEffect","IsFlying","AirTargets","GroundTargets","AttackCount","DieEffect","Animation"]
        UNIT_NAME_MAPPINGS = {'Balloon Goblin':'Balloon',
                              'PEKKA':'P.E.K.K.A'}
        
        UNIT_NAMES = []
        with open(TARGET_CSV, 'rb') as units_file:
            reader = csv.reader(units_file)
            counter = 1
            current_name = ''
            current_level = 1
            for row in reader:
                if counter >= 3:
                    name = row[0]
                    if name == '':
                        current_level = current_level + 1
                    else:
                        UNIT_NAMES.append(name)
                        current_name = name
                        current_level = 1
                        housing_space = row[3]
                        barracks_level = row[4]
                        lab_level = row[5]
                        training_time = row[8]
                        training_resource = row[9]
                        upgrade_resource = row[12]
                        attack_range = row[14]
                        attack_speed = row[15]
                    hitpoints = row[7]
                    training_cost = row[10]
                    upgrade_time = row[11]
                    upgrade_cost = row[13] if row[13] else 0
                    attack_damage = row[16]
                
                    if current_name in UNIT_NAME_MAPPINGS.keys():
                        mapping_name = UNIT_NAME_MAPPINGS.get(current_name)
                    else:
                        mapping_name = current_name
                    
                    try:
                        unit_object = Unit.objects.get(name__iexact = mapping_name.lower(), level = current_level)
                    except ObjectDoesNotExist:
                        unit_object = None
                    
                    if unit_object:
                        print unit_object
                        print [housing_space, barracks_level, lab_level, training_time, training_cost, upgrade_cost, upgrade_time, hitpoints, attack_damage]
                        unit_object.living_space = housing_space
                        unit_object.barracks_level_required = barracks_level
                        unit_object.lab_level_required = lab_level
                        unit_object.build_time = training_time
                        unit_object.elixir_cost = training_cost
                        unit_object.research_cost = upgrade_cost
                        unit_object.research_time = upgrade_time
                        unit_object.hit_points = hitpoints
                        unit_object.dps = attack_damage
                        unit_object.save()
                    else:
                        print "%s not found" % (mapping_name)
                counter = counter + 1
                    
        print UNIT_NAMES
        
    def load_buildings(self):
        PROJECT_ROOT = join(dirname(normpath(__file__)), '..')
        DATA_DIR = join(PROJECT_ROOT, '../../../data')
        BUILDINGS_CSV = join(DATA_DIR, 'buildings.csv')
        
        BUILDINGS_FIELDS = ["Name",
                            "TID",
                            "InfoTID",
                            "BuildingClass",
                            "SWF",
                            "ExportName",
                            "ExportNameNpc",
                            "ExportNameConstruction",
                            "BuildTimeD",
                            "BuildTimeH",
                            "BuildTimeM",
                            "BuildResource",
                            "BuildCost",
                            "TownHallLevel",
                            "Width",
                            "Height",
                            "Icon",
                            "ExportNameBuildAnim",
                            "MaxStoredGold",
                            "MaxStoredElixir",
                            "Bunker",
                            "HousingSpace",
                            "ProducesResource",
                            "ResourcePerHour",
                            "ResourceMax",
                            "UnitProduction",
                            "UpgradesUnits",
                            "Hitpoints",
                            "RegenTime",
                            "AttackRange",
                            "AttackSpeed",
                            "Damage",
                            "DestroyEffect",
                            "AttackEffect",
                            "HitEffect",
                            "Projectile",
                            "ExportNameDamaged",
                            "BuildingW",
                            "BuildingH",
                            "ExportNameBase",
                            "ExportNameBaseNpc",
                            "AirTargets",
                            "GroundTargets",
                            "MinAttackRange",
                            "DamageRadius",
                            "PushBack",
                            "PickUpEffect",
                            "PlacingEffect",
                            "CanNotSellLast",
                            "DefenderCharacter",
                            "DefenderCount",
                            "DefenderZ",
                            "DestructionXP",
                            "Locked",
                            "Hidden",
                            "TriggerRadius",
                            "ExportNameTriggered",
                            "AppearEffect",
                            "ForgesSpells"]
        BUILDINGS_FIELDTYPES = ['String', 'String', 'String', 'String', 'String', 'String', 'String', 'String', 'int', 'int', 'int', 'String', 'int', 'int', 'int', 'int', 'String', 'String', 'int', 'int', 'boolean', 'int', 'String', 'int', 'int', 'int', 'boolean', 'int', 'int', 'int', 'int', 'int', 'String', 'String', 'String', 'String', 'String', 'int', 'int', 'String', 'String', 'boolean', 'boolean', 'int', 'int', 'boolean', 'String', 'String', 'boolean', 'String', 'int', 'int', 'int', 'Boolean', 'Boolean', 'int', 'String', 'String', 'boolean']
        
#        for i in range(0, len(BUILDINGS_FIELDS)):
#            print (i, BUILDINGS_FIELDS[i], BUILDINGS_FIELDTYPES[i])
        
        BUILDING_NAMES = ['Troop Housing', 
                          'Town Hall', 
                          'Elixir Pump', 
                          'Elixir Storage',
                          'Gold Mine',
                          'Gold Storage', 
                          'Barrack', 
                          'Laboratory',
                          'Cannon', 
                         'Archer Tower',
                         'Wall', 
                         'Wizard Tower',
                         'Air Defense',
                          'Mortar', 
                          'Alliance Castle', 
                          'Worker Building', 
                          'Communications mast', 
                          'Goblin main building',
                           'Goblin hut',
                            'Tesla Tower', 
                            'Spell Forge']
        
        BUILDING_NAMES_MAPPING = {'Troop Housing':'Army Camp',
                                  'Elixir Pump':'Elixir Collector',
                                  'Spell Forge':'Spell Factory',
                                  'Worker Building':"Builder's Hut",
                                  'Alliance Castle':'Clan Castle',
                                  'Barrack':'Barracks',
                                  'Tesla Tower':'Hidden Tesla'}
        
        with open(BUILDINGS_CSV, 'rb') as buildings_file:
            reader = csv.reader(buildings_file)
            counter = 1
            current_name = ''
            current_level = 1
            for row in reader:
                if counter >= 3:
                    name = row[0]
                    if name == '':
                        current_level = current_level + 1
                    else:
                        BUILDING_NAMES.append(name)
                        current_name = name
                        current_level = 1
                        build_resource = row[11]
                        attack_range = row[29]
                        attack_speed = row[30]
                        damage_radius = row[44]
                        min_attack_range = row[43]
                    buildtime_days = int(row[8]) if row[8] else 0
                    buildtime_hours = int(row[9]) if row[9] else 0
                    buildtime_minutes = int(row[10]) if row[10] else 0
                    build_cost = row[12]
                    townhall_level = row[13] if row[13] else 0
                    max_gold_storage = row[18]
                    max_elixir_storage = row[19]
                    bunker = row[20]
                    housing_space = row[21]
                    resource_per_hour = row[23]
                    resource_max = row[24]
                    hitpoints = row[27]
                    resource_production = row[22]
                    unit_production = row[25]
                    
                    attack_damage = row[31]
                    pushback = row[45]
                    
                    if current_name in BUILDING_NAMES_MAPPING.keys():
                        mapping_name = BUILDING_NAMES_MAPPING.get(current_name)
                    else:
                        mapping_name = current_name
                    
                    object_type = 'None'
                    if mapping_name.lower() == 'town hall':
                        building_object = Townhall.objects.get(level = current_level)
                        object_type = 'Townhall'
                    else:
                        try:
                            building_object = BaseBuilding.objects.get(name__iexact = mapping_name.lower(), level = current_level)
                            object_type = 'Base'
                        except ObjectDoesNotExist:
                            try:
                                building_object = DefenseBuilding.objects.get(name__iexact = mapping_name.lower(), level = current_level)
                                object_type = 'Defense'
                            except ObjectDoesNotExist:
                                building_object = None
                    
                    if not building_object:
                        print "%s - %s (NOT FOUND)" % (current_name.strip(), str(current_level))
                    else:
                        print mapping_name
                        building_object.build_time = calculate_build_time(buildtime_days, buildtime_hours, buildtime_minutes)
                        building_object.hit_points = hitpoints
                        if build_resource == 'Gold':
                            building_object.cost_type = 'GOLD'
                            building_object.gold_cost = build_cost
                        elif build_resource == 'Elixir':
                            building_object.cost_type = 'ELIXIR'
                            building_object.elixir_cost = build_cost
                        building_object.townhall_level = townhall_level
                        if object_type == 'Defense':
                            if mapping_name.lower() == 'wall':
                                pass
                            else:
                                building_object.dps = attack_damage
                                building_object.max_range = int(attack_range)/100
                        elif object_type == 'Base':
                            if mapping_name.lower() == 'gold mine':
                                building_object.production_type = 'GOLD'
                                building_object.production = resource_per_hour
                                building_object.storage = resource_max
                            elif mapping_name.lower() == 'elixir collector':
                                building_object.production_type = 'ELIXIR'
                                building_object.production = resource_per_hour
                                building_object.storage = resource_max
                            elif mapping_name.lower() == 'army camp':
                                building_object.living_space = housing_space
                            elif mapping_name.lower() == 'gold storage':
                                building_object.storage = max_gold_storage
                            elif mapping_name.lower() == 'elixir storage':
                                building_object.storage = max_elixir_storage
                            elif mapping_name.lower() == 'barracks':
                                building_object.queue_size = unit_production
                        print building_object.__dict__
                        building_object.save()
                counter = counter + 1
                
    def handle(self, *test_labels, **options):
        #self.load_townhall()
        self.export_data()
        #self.load_experience_levels()
        #self.load_text()
        #self.load_achievements()
        #self.load_units()
        #self.load_buildings()