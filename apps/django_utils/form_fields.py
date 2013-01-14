import django.forms as forms
from django_utils.sanitize import sanitize_html

class WMDField(forms.CharField):
    def clean(self, value):
        value = super(WMDField, self).clean(value)
        return sanitize_html(value.replace("&#95;", "_"))