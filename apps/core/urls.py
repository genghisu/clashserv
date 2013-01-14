from django.conf.urls.defaults import *
from core.views import *

urlpatterns = patterns('core.views',
    url(r'^get_rating/$', 'get_rating', name='get-rating'),
    url(r'^get_tips/$', 'get_tips', name='get-tips'),
    url(r'^add_rating/$', 'add_rating', name='add_rating'),
    url(r'^add_tip/$', 'add_tip', name='add_tip'),
)
