from django import template
from django.template import Node, NodeList, Template, Context, Variable, VariableDoesNotExist
from django.template.loader import render_to_string
from django.template.defaulttags import IfEqualNode

from django_utils.templatetag_helpers import resolve_variable, copy_context

register = template.Library()

@register.tag(name="hide_div")
def do_hide_div(parser,  token):
    try:
        tag,  link_id, div_id = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError,  "%r tag requires 6 arguments" % token.contents.split()[0]
    return HideDiv(link_id, div_id)

class HideDiv(template.Node):
    """
    @link_id
    @div_id
    """

    def __init__(self,  link_id,  div_id):
        self.link_id = link_id
        self.div_id = div_id

    def render(self,  old_context):
        context = copy_context(old_context)
        link_id = resolve_variable(self.link_id, context, self.link_id)
        div_id = resolve_variable(self.div_id,  context, self.div_id)
        
        return render_to_string('django_utils/javascript/hide_div.html',  
                                {'link_id':link_id,  'div_id':div_id},  context)

@register.tag(name="toggle_div")
def do_toggle_div(parser,  token):
    try:
        tag,  link_id,  div_id,  visible_text,  hidden_text = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError,  "%r tag requires 6 arguments" % token.contents.split()[0]
    return ToggleDiv(link_id, div_id,  visible_text,  hidden_text)

class ToggleDiv(template.Node):
    """
    @link_id
    @div_id
    @visible_text
    @hidden_text
    """

    def __init__(self,  link_id,  div_id,  visible_text,  hidden_text):
        self.link_id = link_id
        self.div_id = div_id
        self.visible_text = visible_text
        self.hidden_text = hidden_text

    def render(self,  old_context):
        context = copy_context(old_context)
        link_id = resolve_variable(self.link_id, context, self.link_id)
        div_id = resolve_variable(self.div_id,  context, self.div_id)
        visible_text = resolve_variable(self.visible_text,  context, self.visible_text)
        hidden_text = resolve_variable(self.hidden_text,  context, self.hidden_text)
        
        return render_to_string('django_utils/javascript/toggle_div.html',  
                                {'link_id':link_id,  'div_id':div_id,  'visible_text':visible_text,  'hidden_text':hidden_text},  context)

@register.tag(name="toggle_div_img")
def do_toggle_div_img(parser,  token):
    try:
        tag,  link_id,  div_id,  visible_id,  hidden_id = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError,  "%r tag requires 6 arguments" % token.contents.split()[0]
    return ToggleDivImg(link_id, div_id,  visible_id,  hidden_id)

class ToggleDivImg(template.Node):
    """
    @link_id
    @div_id
    @visible_text
    @hidden_text
    """

    def __init__(self,  link_id,  div_id,  visible_id,  hidden_id):
        self.link_id = link_id
        self.div_id = div_id
        self.visible_id = visible_id
        self.hidden_id = hidden_id

    def render(self,  old_context):
        context = copy_context(old_context)
        link_id = resolve_variable(self.link_id, context, self.link_id)
        div_id = resolve_variable(self.div_id,  context, self.div_id)
        visible_id = resolve_variable(self.visible_id,  context, self.visible_id)
        hidden_id = resolve_variable(self.hidden_id,  context, self.hidden_id)
        
        return render_to_string('django_utils/javascript/toggle_div_img.html',  
                                {'link_id':link_id,  'div_id':div_id,  'visible_id':visible_id,  'hidden_id':hidden_id},  context)


@register.tag(name="wmd")
def do_wmd(parser, token):
    try:
        tag, textarea_id, preview_id = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError,  "%r tag requires two arguments" % token.contents.split()[0]
    return WMD(textarea_id, preview_id)

class WMD(template.Node):
    """
    @textarea_id
    @preview_id
    """

    def __init__(self,  textarea_id, preview_id):
        self.textarea_id = textarea_id
        self.preview_id = preview_id

    def render(self,  old_context):
        context = copy_context(old_context)
        textarea_id = resolve_variable(self.textarea_id, context, self.textarea_id)
        preview_id = resolve_variable(self.preview_id,  context, self.preview_id)
        
        script = """<script type='text/javascript'>createWMD("%s", "%s");</script>""" % (textarea_id, preview_id)
        script = "\n" + script + "\n"
        return script

@register.tag(name="validate_form")
def do_validate_form(parser, token):
    try:
        tag, form_id = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError,  "%r tag requires two arguments" % token.contents.split()[0]
    return Validate(form_id)

class Validate(template.Node):
    """
    @form_id
    """

    def __init__(self,  form_id):
        self.form_id = form_id

    def render(self,  old_context):
        context = copy_context(old_context)
        form_id = resolve_variable(self.form_id, context, self.form_id)
        
        script = """<script type='text/javascript'>$("#%s").validate();</script>""" % (form_id)
        script = "\n" + script + "\n"
        return script