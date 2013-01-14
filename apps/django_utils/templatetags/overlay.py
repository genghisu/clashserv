from django import template
from django.template import Node, NodeList, Template, Context, Variable, VariableDoesNotExist
from django.template.defaulttags import IfEqualNode

from django_utils.templatetag_helpers import resolve_variable, copy_context

register = template.Library()

@register.tag(name="overlay")
def do_add_overlay(parser,  token):
    try:
        args_list = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError,  "%r tag requires one or two arguments" % token.contents.split()[0]
    return AddOverlay(args_list[1:])

class AddOverlay(template.Node):
    def __init__(self,  args):
        self.args_list = args
        
    def render(self,  context):
        link_id = ''
        for arg in self.args_list:
            link_id = link_id + str(resolve_variable(arg, context, arg))
        
        ajax_script = """<script type='text/javascript'>$("#%s").overlay({expose: {color: '#333', loadSpeed: 200, opacity: 0.9}});</script>""" % (link_id)
        return_value = "\n" + ajax_script + "\n"
        return return_value
        
@register.tag(name="close_onclick")
def do_close_onclick(parser,  token):
    try:
        tag,  box_id = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError,  "%r tag requires one argument" % token.contents.split()[0]
    return CloseOnClick(box_id)

class CloseOnClick(template.Node):
    """
    link_id - id of the link to attach this ajax event
    box_id - id of the check login box
    """
    
    def __init__(self,  box_id):
        self.box_id = box_id
        
    def render(self,  context):
        ajax_script = """<script type='text/javascript'>$("#%(box_id)s").bind("click", function() {close_box('%(box_id)s');});</script>""" \
                            % ({'box_id':self.box_id})
        return_value = "\n" + ajax_script + "\n"
        return return_value