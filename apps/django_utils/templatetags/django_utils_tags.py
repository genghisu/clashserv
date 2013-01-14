from django import template
from django.template import Node, NodeList, Template, Context, Variable, VariableDoesNotExist, TemplateSyntaxError
from django.template.defaulttags import IfEqualNode
import datetime

from django_utils.templatetag_helpers import resolve_variable, copy_context

register = template.Library()

def yearsince(value):
    """Formats a date as the years since the date."""
    now = datetime.datetime.now()
    if value:
        return now.year - value.year
    else:
        return ''
yearsince.is_safe = False

register.filter(yearsince)

@register.tag(name="add_query_params")
def do_toggle_overlay(parser,  token):
    bits = list(token.split_contents())
    if not "to" in bits:
        raise TemplateSyntaxError("%r expected format is 'param1,value1, ... paramN,valueN to url'" % bits)
    split = bits.index("to")
    param_list = bits[1:split-1:2]
    val_list = bits[2:split:2]
    if not len(param_list) == len(val_list):
        raise TemplateSyntaxError("%r expected format is 'param1,value1, ... paramN,valueN to url'" % bits)
    url = bits[-1]
    return AddQueryParams(param_list, val_list, url, nodelist)
    
class AddQueryParams(Node):
    def __init__(self, param_list, val_list, url, nodelist):
        self.param_list = param_list
        self.val_list = val_list
        self.url = url
        self.nodelist = nodelist

    def __repr__(self):
        return "<StaticWithNode>"

    def render(self, context):
        from itertools import izip
        
        query_tokens = ['&%s=%s' % (k, v) for k, v in izip(self.param_list, self.val_list)]
        if '?' in self.url:
            final_url = self.url + ''.join(query_tokens)
        else:
            final_url = self.url + '?' + ''.join(query_tokens)[1:]
            
        return str(final_url)
