"""
A set of views that provide generic functionality which can
be used for other apps.
"""

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
import django.shortcuts as shortcuts
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist
import django.http as http

import django_utils.request_helpers as request_helpers
from django_community.decorators import UserRequired
from django_reputation.decorators import ReputationRequired
import django_utils.pagination as pagination
from tagging.models import Tag
from django_metatagging.utils import add_tags
    
class ListView(object):
    """
    Renders a list of objects in a paginated and sorted list.
    """
    def __init__(self, model, per_page, ordered = True, moderated = False, template = None):
        self.model = model
        self.per_page = per_page
        self.template = template
        self.ordered = ordered
        self.moderated = moderated
        self.content_type = ContentType.objects.get_for_model(model)
    
    def __call__(self, request, option = 'most_recent'):
        page = request_helpers.get_page(request)
        
        if self.ordered:
            objects = self.model.objects.get_sorted_objects(option)
        else:
            objects = self.model.objects.all()
    
        current_page, page_range = pagination.paginate_queryset(objects, self.per_page, 5, page)
    
        return shortcuts.render_to_response(
                self.template,
                {'current_page':current_page,  
                 'page_range':page_range,  
                 'sort':option}, 
                context_instance = RequestContext(request),
        )

class ContributeView(object):
    """
    Renders a view which contains a form for creating new instances of a model.
    """
    def __init__(self, model, form_builder, redirect_url, template = None):
        self.model = model
        self.form_builder = form_builder
        self.redirect_url = redirect_url
        self.template = template
        self.content_type = ContentType.objects.get_for_model(model)
    
    def call(self, request):
        user = request.user
        ContributeForm = self.form_builder()
        
        if request.POST:
            form = ContributeForm(request.POST,  request.FILES)
            form.user = user
            if form.is_valid():
                object = self.model.objects.add(user, form.cleaned_data)
                if object:
                    tags = add_tags(object, form.cleaned_data['tags'])
                    return http.HttpResponseRedirect(reverse(self.redirect_url,  args=[object.id]))
        else:
            form = ContributeForm()
        return shortcuts.render_to_response(
                    self.template, 
                    {'form':form}, 
                    context_instance = RequestContext(request),
        )
    __call__ = UserRequired(call)
    
class EditView(object):
    """
    Renders a view which allows an object to be edited.
    """
    def __init__(self, model, form_builder, view_url, redirect_url, template = None):
        self.model = model
        self.form_builder = form_builder
        self.view_url = view_url
        self.redirect_url = redirect_url
        self.template = template
        self.content_type = ContentType.objects.get_for_model(model)
        
    def call(self, request, object_id):
        user = request.user
        
        object = get_object_or_404(self.model, id = object_id)
        EditForm = self.form_builder(object)
        
        if request.POST:
            form = EditForm(request.POST,  request.FILES)
            form.user = user
            if form.is_valid():
                self.model.objects.edit(object, user = user, data = form.cleaned_data)
                return http.HttpResponseRedirect(reverse(self.redirect_url,  args=[object_id]))
        else:
            form = EditForm()
        
        return shortcuts.render_to_response(
                    self.template,
                    {'node':object,  
                     'model':self.content_type.model,
                     'object_url': reverse(self.view_url,  args=[object_id]),
                     'form':form}, 
                    context_instance = RequestContext(request),
        )
    __call__ = ReputationRequired(call, 'edit_content')

def content_redirect_by_id(request,  content_type,  id):
    """
    Redirects to the appropriate view based on content_type and id.  Allows for 
    {% url content-redirect-by-id content_type object_id %} which can be used
    for all content types and objects.
    """
    content_type_object = ContentType.objects.get(id = content_type)
    model_class = content_type_object.model_class()
    
    reverse_target = "%s-%s-%s" % (content_type_object.app_label.replace('_', '-'), 'view', content_type_object.model)
    redirect_url = reverse(reverse_target, args=[int(id)])
    return http.HttpResponseRedirect(redirect_url)

def content_list_redirect(request, content_type):
    """
    Redirects to the appropriate object list based on content_type and id.  Allows 
    for {% url content-list-redirect content_type object_id %} which can be used
    for all content types and objects.
    """
    content_type_object = ContentType.objects.get(id = content_type)
    model_class = content_type_object.model_class()
    
    reverse_target = "%s-%s-%s" % (content_type_object.app_label.replace('_', '-'), 'list', content_type_object.model)
    redirect_url = reverse(reverse_target, args=['most_recent'])
    return http.HttpResponseRedirect(redirect_url)