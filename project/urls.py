from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    (r'^clashserv/',  include('core.urls')),
    (r'^clashserv/admin/', include(admin.site.urls)),
)

handler500 = 'django.views.defaults.server_error',
handler404 = 'django.views.defaults.page_not_found'

if getattr(settings, 'LOCAL_DEV_SERVER', None):
    from urlparse import urlsplit    
    url = urlsplit(settings.MEDIA_URL).path[1:]
    root = settings.MEDIA_ROOT
    urlpatterns += patterns('django.views.static',
        (r'^%s(?P<path>.*)$' % url, 'serve', {'document_root': root, 'show_indexes': True}),
    )
    url = urlsplit(settings.STATIC_URL).path[1:]
    root = settings.STATIC_ROOT
    urlpatterns += patterns('django.views.static',
        (r'^%s(?P<path>.*)$' % url, 'serve', {'document_root': root, 'show_indexes': True}),
    )
    url = urlsplit(settings.STATIC_LOCAL_URL).path[1:]
    root = settings.STATIC_LOCAL_ROOT
    urlpatterns += patterns('django.views.static',
        (r'^%s(?P<path>.*)$' % url, 'serve', {'document_root': root, 'show_indexes': True}),
    )
    (r'^favicon', None),
