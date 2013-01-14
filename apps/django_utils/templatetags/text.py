from django import template
from django.template import Node, NodeList, Template, Context, Variable, VariableDoesNotExist
from django.template.defaulttags import IfEqualNode

from django_utils.templatetag_helpers import resolve_variable, copy_context

register = template.Library()

@register.tag(name="limit_text")
def do_limit_text(parser,  token):
    try:
        tag,  text,  limit,  redirect_url = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError,  "%r tag requires three arguments" % token.contents.split()[0]
    return LimitText(text, limit, redirect_url)

class LimitText(template.Node):
    """
    @text - text to limit
    @limit - number of characters max
    @redirect_url - URL to redirect to
    """
    
    def __init__(self, text, limit,  redirect_url):
        self.text = text
        self.limit = limit
        self.redirect_url = redirect_url
        
    def render(self,  context):
        text = resolve_variable(self.text,  context,  self.text)
        limit = resolve_variable(self.limit,  context,  self.limit)
        redirect_url = resolve_variable(self.redirect_url,  context,  self.redirect_url)
        
        if len(text) <= int(limit):
            return text
        else:
            if redirect_url.strip():
                return "%s...<a href='%s'>view more</a>" (text[0:limit],  redirect_url)
            else:
                return text[0:limit] + "..."
