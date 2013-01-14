from django import template
from django.template import Node, NodeList, Template, Context, Variable, VariableDoesNotExist
from django.template.defaulttags import IfEqualNode
from django.template.loader import render_to_string

register = template.Library()
    
@register.tag(name="slideshow")
def do_slideshow(parser,  token):
    try:
        tag,  images,  image_size,  rendered_template = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError,  "%r tag requires two arguments" % token.contents.split()[0]
    return SlideShow(images,  image_size,  rendered_template)

class SlideShow(template.Node):
    def __init__(self,  images,  image_size,  rendered_template):
        self.images = Variable(images)
        self.image_size = image_size
        self.rendered_template = rendered_template
        
    def render(self,  context):
        try:
            images = self.images.resolve(context)
        except VariableDoesNotExist:
            images = None
            
        counter = 1
        image_objects = []
        for image in images:
            image_object = type('ImageObject',  (object,  ),  {})
            image_object.image = image
            image_object.object = image
            image_object.counter = counter
            image_object.css_id = 'dynamic_lead_' + str(counter)
            counter = counter + 1
            image_objects.append(image_object)
        
        rendered_template = render_to_string(self.rendered_template,  {'images':image_objects},  context)
        return rendered_template
        
@register.tag(name="dynamic_lead")
def do_dynamic_lead(parser,  token):
    try:
        tag,  images,  image_size,  rendered_template = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError,  "%r tag requires two arguments" % token.contents.split()[0]
    return DynamicLead(images,  image_size,  rendered_template)

class DynamicLead(template.Node):
    def __init__(self,  images,  image_size,  rendered_template):
        self.images = Variable(images)
        self.image_size = image_size
        self.rendered_template = rendered_template
        
    def render(self,  context):
        try:
            images = self.images.resolve(context)
        except VariableDoesNotExist:
            images = None
            
        counter = 1
        image_objects = []
        for image in images:
            image_object = type('ImageObject',  (object,  ),  {})
            image_object.image = image
            image_object.object = image
            image_object.counter = counter
            image_object.css_id = 'dynamic_lead_' + str(counter)
            if counter == 1:
                image_object.css_class = 'block'
                image_object.style = ''
            else:
                image_object.css_class = 'hidden'
                image_object.style = 'display: none;'
            counter = counter + 1
            image_objects.append(image_object)
        
        rendered_template = render_to_string(self.rendered_template,  {'images':image_objects},  context)
        return rendered_template

@register.tag(name="dl_page")
def do_dl_page(parser,  token):
    try:
        tag,  image,  dl_wrapper = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError,  "%r tag requires two arguments" % token.contents.split()[0]
    return DynamicLeadPage(image,  dl_wrapper)

class DynamicLeadPage(template.Node):
    def __init__(self,  image,  dl_wrapper):
        self.image = Variable(image)
        self.dl_wrapper = dl_wrapper
        
    def render(self,  context):
        try:
            image = self.image.resolve(context)
        except VariableDoesNotExist:
            image = None
        
        link_id = str(image.css_id) + "_link"
        anchor = "<a href='#' class='dl_page' id='" + str(link_id) + "'>" + str(image.counter) + "</a>"
        javascript = "<script type='text/javascript'>" + \
                                    '$("#' + str(link_id) + \
                                    '").bind("click", function() {dl_page("' + str(image.css_id) + '", "' + str(self.dl_wrapper) + '"); return false;});' +\
                                "</script>"
        return '\n' + anchor + '\n' + javascript + '\n'
