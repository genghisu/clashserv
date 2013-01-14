from django.template.loader import render_to_string
from django.template import TemplateDoesNotExist

def render_or_default(target_template, default_template, context):
    try:
        response = render_to_string(target_template, {}, context)
    except TemplateDoesNotExist:
        response = render_to_string(default_template, {}, context)
    return response