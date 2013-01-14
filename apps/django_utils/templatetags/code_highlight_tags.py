from django import template
from django.template import Node, NodeList, Template, Context, Variable, VariableDoesNotExist
from django.template.loader import render_to_string
from django.template.defaulttags import IfEqualNode

from django_utils.templatetag_helpers import resolve_variable

from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

register = template.Library()

@register.tag(name="highlight_python")
def do_highlight_code(parser, token):
    try:
        tag, code = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError,  "%r tag requires one argument" % token.contents.split()[0]
    return HighlightCode(code)

class HighlightCode(template.Node):
    """
    @code
    """

    def __init__(self,  code):
        self.code = code

    def render(self,  context):
        code = resolve_variable(self.code, context, self.code)
        
        final_code = highlight(code, PythonLexer(), HtmlFormatter())
        return final_code

@register.filter(name="highlight_markdown")
def highlight_markdown(value):
    from django_utils import pygment_helpers
    return pygment_helpers.highlight_markdown(value)