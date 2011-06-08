from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('apps.accounts.views',
    url(r'^login/$', 'login', name='login'),
    url(r'^logout/$', 'logout', name='logout'),
    url(r'^register/$', 'register', name='register'),
)
