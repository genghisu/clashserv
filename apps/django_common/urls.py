from django.conf.urls.defaults import *

urlpatterns = patterns('django_common.views',
    url(r'^content_redirect_by_id/(?P<content_type>.+)/(?P<id>.+)/$',  'content_redirect_by_id',  name='content-redirect-by-id'),
    url(r'^content_list_redirect/(?P<content_type>.+)/$', 'content_list_redirect', name='content-list-redirect'),
)