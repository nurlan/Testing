from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('apps.tests.views',
    
    url(r'^$', 'list', name='list'),
    url(r'^create/$', 'create_test', name='create'),
    url(r'^(\d+)/edit/$', 'edit_test', name='edit'),
    url(r'^(\d+)/view/$', 'view_test', name='view'),
    url(r'^(\d+)/remove/$', 'remove_test', name='remove'),
)
