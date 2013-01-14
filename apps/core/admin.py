import models
from django.contrib import admin


class BaseBuildingAdmin(admin.ModelAdmin):
    list_display = ('name', 'level', 'size', 'cost_type', 'gold_cost', 'elixir_cost', 'gold_sell_price', 'elixir_sell_price',  'build_time', 'hit_points', 'production_type', 'production', 'storage', 'living_space', 'queue_size', 'townhall_level')
    
class DefenseBuildingAdmin(admin.ModelAdmin):
    list_display = ('name', 'level', 'size', 'cost_type', 'gold_cost', 'elixir_cost', 'gold_sell_price', 'elixir_sell_price', 'build_time', 'hit_points', 'dps', 'min_range', 'max_range', 'townhall_level')
    ordering = ('name', 'level')
    
class UnitAdmin(admin.ModelAdmin):
    list_display = ('name', 'level', 'cost_type', 'gold_cost', 'elixir_cost', 'build_time', 'hit_points', 'dps', 'favorite_target')
    ordering = ('name', 'level')
    
class ObstacleAdmin(admin.ModelAdmin):
    list_display = ('name', 'size', 'gold_cost', 'elixir_cost', 'build_time', 'cost_type')
    ordering = ('name', 'size')
    
class GuideAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'icon_image', 'standard_image')
    ordering = ('name', 'category', 'order')

class TownhallAdmin(admin.ModelAdmin):
    list_display = ('name', 'level', 'gold_cost', 'build_time', 'hit_points', 'gold_mine', 'elixir_extractor', 'gold_storage',
                    'elixir_storage', 'cannon', 'archer_tower', 'wall', 'mortar', 'bomb', 'spring_trap', 'air_defense', 'wizard_tower', 'giant_bomb', 'hidden_tesla',
                    'army_camp', 'barracks', 'laboratory', 'spell_factory')

class ExperienceLevelAdmin(admin.ModelAdmin):
     list_display = ('level', 'experience')
     ordering = ('level', )

class AchievementAdmin(admin.ModelAdmin):
    list_display = ('name', 'level', 'exp_reward', 'crystal_reward')
    ordering = ('name', 'level')
    
admin.site.register(models.BaseBuilding, BaseBuildingAdmin)
admin.site.register(models.DefenseBuilding, DefenseBuildingAdmin)
admin.site.register(models.Unit, UnitAdmin)
admin.site.register(models.Townhall, TownhallAdmin)
admin.site.register(models.Obstacle, ObstacleAdmin)
admin.site.register(models.Spell)
admin.site.register(models.GuideCategory)
admin.site.register(models.Guide, GuideAdmin)
admin.site.register(models.ExperienceLevel, ExperienceLevelAdmin)
admin.site.register(models.Achievement)
admin.site.register(models.Tip)
admin.site.register(models.Rating)
admin.site.register(models.TotalRating)