import django.forms as forms
from django.conf import settings
from django.utils.safestring import mark_safe
from django.utils.html import escape, conditional_escape
from django.forms.util import flatatt
from django.utils.encoding import StrAndUnicode, force_unicode

from recaptcha.client.captcha import *

class SmallTextarea(forms.Textarea):
    def __init__(self,  *args,  **kws):
        html_attrs = kws.get('attrs',  {})
        html_attrs.setdefault('cols',  55)
        html_attrs.setdefault('rows',  2)
        kws['attrs'] = html_attrs
        super(SmallTextarea,  self).__init__(*args,  **kws)
        
class StandardTextarea(forms.Textarea):
    def __init__(self,  *args,  **kws):
        html_attrs = kws.get('attrs',  {})
        html_attrs.setdefault('cols',  55)
        html_attrs.setdefault('rows',  3)
        kws['attrs'] = html_attrs
        super(StandardTextarea,  self).__init__(*args,  **kws)
        
class BigTextarea(forms.Textarea):
    def __init__(self,  *args,  **kws):
        html_attrs = kws.get('attrs',  {})
        html_attrs.setdefault('cols',  80)
        html_attrs.setdefault('rows',  10)
        kws['attrs'] = html_attrs
        super(BigTextarea,  self).__init__(*args,  **kws)

class GiantTextarea(forms.Textarea):
    def __init__(self,  *args,  **kws):
        html_attrs = kws.get('attrs',  {})
        html_attrs.setdefault('cols',  80)
        html_attrs.setdefault('rows',  20)
        kws['attrs'] = html_attrs
        super(GiantTextarea,  self).__init__(*args,  **kws)

class DefaultCharfield(forms.TextInput):
    def __init__(self,  *args,  **kws):
        html_attrs = kws.get('attrs',  {})
        kws['attrs'] = html_attrs
        super(DefaultCharfield,  self).__init__(*args,  **kws)
        
class StandardCharfield(forms.TextInput):
    def __init__(self,  *args,  **kws):
        html_attrs = kws.get('attrs',  {})
        html_attrs.setdefault('size',  51)
        kws['attrs'] = html_attrs
        super(StandardCharfield,  self).__init__(*args,  **kws)

class BigCharfield(forms.TextInput):
     def __init__(self,  *args,  **kws):
        html_attrs = kws.get('attrs',  {})
        html_attrs.setdefault('size',  80)
        kws['attrs'] = html_attrs
        super(BigCharfield,  self).__init__(*args,  **kws)
        
class StandardPassfield(forms.PasswordInput):
    def __init__(self,  *args,  **kws):
        html_attrs = kws.get('attrs',  {})
        html_attrs.setdefault('size',  51)
        kws['attrs'] = html_attrs
        super(StandardPassfield,  self).__init__(*args,  **kws)

class WMDTextarea(forms.Textarea):
    def __init__(self,  *args,  **kws):
        self.preview_id = kws.get('preview_id', 'wmd_preview')
        del kws['preview_id']
        html_attrs = kws.get('attrs',  {})
        html_attrs.setdefault('cols',  55)
        html_attrs.setdefault('rows',  12)
        kws['attrs'] = html_attrs
        super(WMDTextarea,  self).__init__(*args,  **kws)
    
    def render(self, name, value, attrs=None):
        if value is None: value = ''
        value = force_unicode(value)
        final_attrs = self.build_attrs(attrs, name=name)
        html = mark_safe(u'<textarea%s>%s</textarea>%s' % (flatatt(final_attrs),
                conditional_escape(force_unicode(value)),  "<div id='%s' class='wmd-preview'></div>" % (self.preview_id)))
        return html

class RecaptchaField(forms.Widget):
    def render(self, name, value, attrs=None):
        return mark_safe(u'%s' % displayhtml(settings.RECAPTCHA_PUBLIC_KEY))