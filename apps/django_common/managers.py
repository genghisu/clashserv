"""
Managers that may be inherited by custom model managers to provide commonly
used additional functionality such as sorting. 
"""

import datetime

from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.conf import settings

from django_utils.sql_helpers import sql_str

class BaseObjectsManager(models.Manager):
    """
    Custom manager class that provides get_sorted_objects.
    """
    def get_sorted_objects(self, option):
        """
        Returns a QuerySet of self.model sorted by option.
        
        Currently depends on django_multivoting and django_comments.
        """
        from django_multivoting.models import Vote, Popularity
        from django_comments.models import Comment
        
        model = self.model
        model_opts = model._meta
        content_type = ContentType.objects.get_for_model(model)
        today = datetime.date(1,  1,  1).today()
        last_week = today - datetime.timedelta(days = 7)
        model_table = model_opts.db_table
        date = sql_str(last_week.isoformat())
        
        current_vals = {}
        current_vals['date'] = date
        current_vals['vote_table'] = Vote._meta.db_table
        current_vals['model_content_type'] = content_type.id
        current_vals['model_table'] = model_table
        current_vals['comment_table'] = Comment._meta.db_table
        current_vals['popularity_table'] = Popularity._meta.db_table
        
        if option == 'most_active':
            order_select_clause = {'vote_count' : \
                                   """SELECT COUNT(*) FROM %(vote_table)s 
                                    WHERE %(vote_table)s.content_type_id = %(model_content_type)s
                                    AND %(vote_table)s.object_id = %(model_table)s.id
                                    AND %(vote_table)s.date_created > %(date)s""" % current_vals}
            order_by_clause = '-vote_count'
        elif option == 'most_discussed':
            order_select_clause = {'comment_count' : \
                                   """SELECT COUNT(*) FROM %(comment_table)s 
                                   WHERE %(comment_table)s.content_type_id = %(model_content_type)s
                                   AND %(comment_table)s.object_id = %(model_table)s.id 
                                   AND %(comment_table)s.date_modified > %(date)s""" % current_vals}
            order_by_clause = '-comment_count'
        elif option == 'highest_rated':
            order_select_clause = {'popularity' : \
                                   """SELECT popularity FROM %(popularity_table)s 
                                    WHERE %(popularity_table)s.content_type_id = %(model_content_type)s
                                    AND %(popularity_table)s.object_id = %(model_table)s.id""" % current_vals}
            order_by_clause = '-popularity'
        elif option == 'featured':
            objects = model.objects.all().order_by('-date_created')
            return objects
            order_by_clause = '-vote_count'
        elif option == 'most_recent':
            objects = model.objects.all().order_by('-date_created')
            return objects
                            
        objects = model.objects.all().extra(select = order_select_clause)
        objects = objects.extra(order_by = [order_by_clause])
        return objects
        
class LimitingManager(models.Manager):
    """
    Custom manager class that provides can_add.
    """
    def can_add(self, user, count = None):
        """
        Returns True if the user can create new instances of self.model, else return False.
        """
        today = datetime.datetime.now()
        yesterday = today - datetime.timedelta(days = 1)
        daily_count = self.model.objects.filter(user = user, date_created__gt = yesterday).count()
        if settings.DEBUG:
            return True
        if daily_count >= (count or settings.MAX_POSTS_PER_DAY):
            return False
        else:
            return True