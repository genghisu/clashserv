from django.conf import settings
import django_defaultcontext.settings as app_settings
from django.contrib.contenttypes.models import ContentType

def defaults(request):
    default_context = {}
    
    if app_settings.ENABLE_STATIC_PATHS:
        default_context['STATIC_URL'] = settings.STATIC_URL
        default_context['MEDIA_URL'] = settings.MEDIA_URL
        default_context['PATH'] = request.path
        
    if app_settings.MODEL_CONTENT_TYPES:
        for model in app_settings.MODEL_CONTENT_TYPES:
            model_content_type = ContentType.objects.get_for_model(model)
            default_context['%s_content_type' % model_content_type.model] = model_content_type.id
            default_context['%s_model' % model_content_type.model] = model_content_type.model
    return default_context

def site_sections(request):
    parts = [x for x in request.path.split('/') if x.strip()]
    if len(parts) == 0:
        SITE_SECTION = 'main'
        SUBSECTION = 'main'
    elif len(parts) == 1:
        SITE_SECTION = parts[0]
        SUBSECTION = parts[0]
    else:
        SITE_SECTION = parts[0]
        SUBSECTION = parts[1]
    return {'SITE_SECTION':SITE_SECTION, 'SUBSECTION':SUBSECTION}