from django import template
from django.template import Node, NodeList, Template, Context, Variable, VariableDoesNotExist
from django.template.defaulttags import IfEqualNode
from django.template import TemplateSyntaxError

from django_utils.templatetag_helpers import resolve_variable

register = template.Library()

@register.tag(name="static_with")
def do_static_with(parser, token):
    """
    Adds a value to the context (inside of this block) for caching and easy
    access.

    For example::

        {% with person.some_sql_method as total %}
            {{ total }} object{{ total|pluralize }}
        {% endwith %}
    """
    bits = list(token.split_contents())
    if not "as" in bits:
        raise TemplateSyntaxError("%r expected format is 'static_value, dynamic_value as name'" % bits)
    split = bits.index("as")
    var_list = bits[1:split]
    name_list = bits[split+1:]
    nodelist = parser.parse(('endstatic_with',))
    parser.delete_first_token()
    return StaticWithNode(var_list, name_list, nodelist)

class StaticWithNode(Node):
    def __init__(self, var_list, name_list, nodelist):
        self.var_list = var_list
        self.name_list = name_list
        self.nodelist = nodelist

    def __repr__(self):
        return "<StaticWithNode>"

    def render(self, context):
        val = ''
        for arg in self.var_list:
            val = val + str(resolve_variable(arg, context, arg))
        name = ''
        for arg in self.name_list:
            name = name + arg
        
        context.push()
        context[name] = val
        output = self.nodelist.render(context)
        context.pop()
        return output
        
@register.tag(name="update_context")
def do_update_context(parser,  token):
    try:
        args_list = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError, "%r tag requires one or more arguments" % token.contents.split()[0]
    
    if not "as" in args_list:
        raise template.TemplateSyntaxError, "%r has malformed arguments" % tag_name
    
    split = args_list.index("as")
    var_list = args_list[1:split]
    name_list = args_list[split + 1:]
    return UpdateContextNode(var_list, name_list)

class UpdateContextNode(template.Node):
    def __init__(self,  var_list,  name_list):
        self.var_list = var_list
        self.name_list = name_list
        
    def render(self,  context):
        val = ''
        for arg in self.var_list:
            val = val + str(resolve_variable(arg, context, arg))
        name = ''
        for arg in self.name_list:
            name = name + str(resolve_variable(arg, context, arg))
        context[name] = val
        return ''
