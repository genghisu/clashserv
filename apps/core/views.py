import json
import datetime

import django.http as http
import django.shortcuts as shortcuts
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse

from models import BaseBuilding, DefenseBuilding, Unit, Townhall, Tip, Rating, TotalRating

def add_rating(request):
    target_model = request.POST.get('model', '').lower()
    target_name = request.POST.get('id', '').lower()
    rating = request.POST.get('rating', '').lower()
    errors = []
    
    if target_model.strip() and target_name.strip():
        try:
            cleaned_rating = int(rating)
            rating_object = Rating(target_model = target_model, 
                                   target_name = target_name, 
                                   rating = cleaned_rating)
            rating_object.save()
            
            try:
                total_rating_object = TotalRating.objects.get(target_model = target_model,
                                                              target_name = target_name)
            except ObjectDoesNotExist:
                total_rating_object = TotalRating(target_model = target_model,
                                                  target_name = target_name)
                total_rating_object.save()
            
            total_rating_object.total_rating = total_rating_object.total_rating + cleaned_rating
            total_rating_object.rating_count += 1
            total_rating_object.save()
        except Exception:
            errors.append('INVALID_RATING')
    
    response = {'success':True, 'errors':errors}
    return shortcuts.render_to_response('json.html',
                                         {'response':json.dumps(response)},
                                         context_instance = RequestContext(request),
                                         mimetype = "application/json") 

def add_tip(request):
    target_model = request.POST.get('model', '').lower()
    target_name = request.POST.get('id', '').lower()
    tip = request.POST.get('tip', '').lower()
    errors = []
    
    if target_model.strip() and target_name.strip():
        cleaned_tip = tip.strip()
        tip_object = Tip(target_model = target_model, 
                         target_name = target_name, 
                         tip = cleaned_tip)
        tip_object.save()
    
    response = {'success':True, 'errors':errors}
    return shortcuts.render_to_response('json.html',
                                         {'response':json.dumps(response)},
                                         context_instance = RequestContext(request),
                                         mimetype = "application/json") 

def get_rating(request):
    target_model = request.POST.get('model', '').lower()
    target_name = request.POST.get('id', '').lower()
    errors = []
    
    try:
        total_rating_object = TotalRating.objects.get(target_model = target_model,
                                                      target_name = target_name)
    except ObjectDoesNotExist:
        total_rating_object = TotalRating(target_model = target_model,
                                          target_name = target_name)
        total_rating_object.save()
    
    total_rating = int(total_rating_object.total_rating/total_rating_object.rating_count)
    
    response = {'rating':total_rating, 'errors':errors}
    return shortcuts.render_to_response('json.html',
                                         {'response':json.dumps(response)},
                                         context_instance = RequestContext(request),
                                         mimetype = "application/json") 

def get_tips(request):
    errors = []
    target_model = request.POST.get('model', '').lower()
    target_name = request.POST.get('id', '').lower()
    
    tip_objects = Tip.objects.filter(target_model = target_model, target_name = target_name, approved = True).order_by('-date_created')
    tips = [x.tip for x in tip_objects]
    
    response = {'tips':tips, 'errors':errors}
    return shortcuts.render_to_response('json.html',
                                         {'response':json.dumps(response)},
                                         context_instance = RequestContext(request),
                                         mimetype = "application/json")