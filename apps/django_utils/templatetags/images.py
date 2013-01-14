from django import template
from django.template import Node, NodeList, Template, Context, Variable, VariableDoesNotExist
from django.template.loader import render_to_string
from django.template.defaulttags import IfEqualNode

from photologue.models import PhotoSize,  Photo
from django.conf import settings

register = template.Library()

@register.tag(name="image_with_shadow")
def do_render_image_with_shadow(parser,  token):
    try:
        tag,  image_id,  image_size = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError,  "%r tag requires 2 arguments" % token.contents.split()[0]
    return RenderImageWithShadow(image_id,  image_size)

class RenderImageWithShadow(template.Node):
    """
    image_id - data source
    image_size - image size
    image_class - class assigned to the image
    """

    def __init__(self,  image_id, image_size):
        self.image_id = Variable(image_id)
        self.image_size = image_size

    def render(self,  context):
        try:
            image_id = self.image_id.resolve(context)
        except VariableDoesNotExist:
            image_id = None
            
        if image_id:
            image = Photo.objects.get(id = image_id)
            photosize = PhotoSize.objects.get(name = self.image_size)
            pathname = image.create_and_get(photosize)
            width,  height = self.image_size.split('x')
            shadow_width = int(width) + 2
            shadow_height = int(height) + 2
        else:
            pathname = None
            
        return render_to_string('images/image_with_shadow.html',  {'pathname':pathname,  'shadow_width':shadow_width,  'shadow_height':shadow_height})
        
@register.tag(name="image")
def do_render_image(parser,  token):
    try:
        tag,  image_id,  image_size = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError,  "%r tag requires 2 arguments" % token.contents.split()[0]
    return RenderImage(image_id,  image_size)

class RenderImage(template.Node):
    """
    image_id - data source
    image_size - image size
    image_class - class assigned to the image
    """

    def __init__(self,  image_id, image_size):
        self.image_id = Variable(image_id)
        self.image_size = image_size

    def render(self,  context):
        try:
            image_id = self.image_id.resolve(context)
        except VariableDoesNotExist:
            image_id = None
            
        if image_id:
            image = Photo.objects.get(id = image_id)
            photosize = PhotoSize.objects.get(name = self.image_size)
            pathname = image.create_and_get(photosize)
            dimensions = self.image_size.split('x')
        else:
            pathname = None
            
        return pathname


