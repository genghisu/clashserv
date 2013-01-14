from django import template
from django.template import Node, NodeList, Template, Context, Variable, VariableDoesNotExist
from django.template.defaulttags import IfEqualNode

import django_utils.templatetag_helpers as tag_helpers
from django_utils.templatetag_helpers import resolve_variable, copy_context

register = template.Library()

@register.tag(name="toggle_overlay")
def do_toggle_overlay(parser,  token):
    try:
        tag,  link_id,  box_id = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError,  "%r tag requires two arguments" % token.contents.split()[0]
    return ShowOverlay(link_id,  box_id)
    
@register.tag(name="ajax_check_login")
def do_ajax_check_login(parser,  token):
    try:
        tag,  link_id,  box_id = token.split_contents()
        prefix = None
    except ValueError:
        try:
            tag,  link_id,  box_id,  prefix = token.split_contents()
        except ValueError:
            raise template.TemplateSyntaxError,  "%r tag requires two or three arguments" % token.contents.split()[0]
    return ShowOverlay(link_id,  box_id,  prefix)

class ShowOverlay(template.Node):
    """
    link_id - id of the link to attach this ajax event
    box_id - id of the check login box
    """
    
    def __init__(self, link_id,  box_id,  prefix = None):
        self.link_id = link_id
        self.box_id = box_id
        self.prefix = prefix
        
    def render(self,  context):
        link_id = tag_helpers.resolve_variable(self.link_id,  context,  self.link_id)
        if self.prefix:
            prefix = tag_helpers.resolve_variable(self.prefix,  context,  self.prefix)
        else:
            prefix = ''
        unique_id = "%s%s" % (prefix,  link_id)
        
        ajax_script = "<script type='text/javascript'>" + \
                                    '$("#' + str(unique_id) + \
                                    '").overlay();' +\
                                "</script>"
        return_value = "\n" + ajax_script + "\n"
        return return_value
    
@register.tag(name="ajaxify")
def do_ajaxify(parser,  token):
    try:
        tag,  element_id = token.split_contents()
        loading_div = None
    except ValueError:
        try:
            tag,  element_id, loading_div = token.split_contents()
        except ValueError:
            raise template.TemplateSyntaxError,  "%r tag requires one argument" % token.contents.split()[0]
    return Ajaxify(element_id,  loading_div)

class Ajaxify(template.Node):
    """
    div_id - id of div to be replaced
    link_id - id of the link to attach this ajax event
    link - url link to server side socket
    name = name of the generated link
    """
    
    def __init__(self,  element_id,  loading_div = None):
        self.element_id = element_id
        self.loading_div = loading_div
    def render(self,  context):
        if self.loading_div:
            ajax_script = "<script type='text/javascript'>" + \
                                    '$("#' + str(self.element_id) + \
                                    '").ajaxify({' + 'loading_target: ' + "'#" + str(self.loading_div) + "', " + \
                                        "animateOut:{opacity:'0'}, animateIn:{opacity:'1'}, animateOutSpeed:'slow', animateInSpeed:'slow'" +\
                                    '});' + \
                                "</script>"
        else:
            ajax_script = "<script type='text/javascript'>" + \
                                    '$("#' + str(self.element_id) + \
                                    '").ajaxify();' + \
                                "</script>"
        return_value = "\n" + ajax_script + "\n"
        return return_value
    
@register.tag(name="ajax_update")
def do_ajax_update(parser,  token):
    """
    Updates a target div by binding a onclick event to a link which uses jquery.metadata to parse for the target div and data source url
    """
    try:
        args_list = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError,  "%r tag requires one argument" % token.contents.split()[0]
    return AjaxUpdate(args_list[1:])

@register.tag(name="ajax_update_no_effect")
def do_ajax_update_no_effect(parser,  token):
    """
    Updates a target div by binding a onclick event to a link which uses jquery.metadata to parse for the target div and data source url
    """
    try:
        args_list = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError,  "%r tag requires one argument" % token.contents.split()[0]
    return AjaxUpdate(args_list[1:], effect = 'none')

class AjaxUpdate(template.Node):
    """
    link_id - link of the anchor tag to be ajax updated
    """
    
    def __init__(self,  args, effect = 'fade'):
        self.args = args
        self.effect = effect
        
    def render(self,  context):
        link_id = ''
        for arg in self.args:
            link_id = link_id + str(resolve_variable(arg, context, arg))
            
        ajax_script = """<script type='text/javascript'>$("#%s").ajax_update({effect:'%s'});</script>""" % (link_id, self.effect)
        return_value = "\n" + ajax_script + "\n"
        return return_value


@register.tag(name="ajax_update_keyup")
def do_ajax_update_keyup(parser,  token):
    """
    Updates a target div by binding a onclick event to a link which uses jquery.metadata to parse for the target div and data source url
    """
    try:
        tag, target_prefix,  target_suffix = token.split_contents()
    except ValueError:
        try:
            tag, target_suffix = token.split_contents()
            target_prefix = None
        except ValueError:
            raise template.TemplateSyntaxError,  "%r tag requires two or four arguments" % token.contents.split()[0]
    return AjaxUpdateAdvanced(target_prefix,  target_suffix,  'keyup')

class AjaxUpdateAdvanced(template.Node):
    """
    @input_prefix
    @input_suffix
    @target_prefix
    @target_suffix
    @event_mode
    """
    
    def __init__(self, target_prefix,  target_suffix,  event_mode):
        self.target_prefix = target_prefix
        self.target_suffix = target_suffix
        self.event_mode = event_mode
        
    def render(self,  context):
        target_prefix = tag_helpers.resolve_variable(self.target_prefix,  context,  self.target_prefix)
        target_suffix = tag_helpers.resolve_variable(self.target_suffix,  context,  self.target_suffix)
        
        if target_prefix:
            target_id = "%s%s" % (target_prefix,  target_suffix)
        else:
            target_id = target_suffix
            
        ajax_script = "<script type='text/javascript'>$('#%s').ajax_update({action : '%s'});</script>" % (str(target_id), str(self.event_mode))
        return_value = "\n" + ajax_script + "\n"
        return return_value

@register.tag(name="ajax_submit")
def do_ajax_submit(parser,  token):
    try:
        tag,  form_id,  target_id = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError,  "%r tag requires two arguments" % token.contents.split()[0]
    return AjaxSubmit(form_id,  target_id)

class AjaxSubmit(template.Node):
    """
    form_id
    target_id
    """
    
    def __init__(self,  form_id,  target_id):
        self.form_id = form_id
        self.target_id = target_id
        
    def render(self,  context):
        try:
            form_id = Variable(self.form_id)
            form_id = form_id.resolve(context)
        except VariableDoesNotExist:
            form_id = self.form_id
        try:
            target_id = Variable(self.target_id)
            target_id = target_id.resolve(context)
        except VariableDoesNotExist:
            target_id = self.target_id
        ajax_script = "<script type='text/javascript'>" + \
                                    "$('#%s').submit(function() {" % (str(form_id)) + \
                                        "var options = {target: '#%s'};" % (str(target_id)) + \
                                        "$(this).ajaxSubmit(options); return false; });" + \
                                "</script>"
        return_value = "\n" + ajax_script + "\n"
        return return_value
