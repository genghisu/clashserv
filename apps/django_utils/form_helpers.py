import django.forms as forms
from django.core.exceptions import ObjectDoesNotExist
from django.forms import ValidationError
from django.forms.util import flatatt, ErrorDict, ErrorList, ValidationError
from django.conf import settings

import hashlib, re
from django_utils import request_helpers
from recaptcha.client import captcha

class DivForm(forms.Form):
    """forms.Form with additional helpers"""
    class Media:
        js = ('forms.js', )

    def as_div(self):
        normal_row =  u"<div class='form_row'><div class='form_left'>%(label)s</div> \
                    <div class='form_right'>%(field)s<span class='help_text'>%(help_text)s</span>%(errors)s</div></div>"
        error_row = u"<div class='form_row'>%s</div>"
        row_end = "</div>"
        help_text = u"%s"
        return self._html_output(normal_row,  error_row,  row_end,  help_text,  False)

class DynamicRequestForm(DivForm):
    def __init__(self, data=None, files=None, request = None,  auto_id='id_%s', prefix=None,
                 initial=None, error_class=ErrorList, label_suffix=':',
                 empty_permitted=False):
        self.request = request
        super(DynamicRequestForm,  self).__init__(data, files,  auto_id, prefix, initial, error_class, label_suffix, empty_permitted)

class RecaptchaForm(DynamicRequestForm):
    def clean_captcha(self):
        value = None
        if self.request:
            challenge = self.data['recaptcha_challenge_field']
            response = self.data['recaptcha_response_field']
            captcha_response = captcha.submit(challenge,  response,  settings.RECAPTCHA_PRIVATE_KEY,  request_helpers.get_ip(self.request))
        if not captcha_response.is_valid:
            raise forms.ValidationError("Incorrect response entered.")
        return value
    
class FormValidator(object):
    def validate_username(username):
        match = False
        name_pattern = re.compile('[a-zA-Z_0-9]+')
        if name_pattern.findall(username):
            match = True
        else:
            match = False
        return match
    validate_username = staticmethod(validate_username)
    
    def validate_name(name):
        match = False
        name_pattern = re.compile('[a-zA-Z_0-9]+')
        if name_pattern.findall(name):
            match = True
        else:
            match = False
        return match
    validate_name = staticmethod(validate_name)

    def validate_unique(model,  field,  value):
        eval_query = 'model.objects.get(field = value)'
        try:
            eval(eval_query)
            return False
        except ObjectDoesNotExist:
            return True

def disable_form(form):
    for name, field in form.base_fields.items():
        field.widget.attrs['readonly'] = True
        field.widget.attrs['disabled'] = True
        field.help_text = "Disabled.  Use as reference."