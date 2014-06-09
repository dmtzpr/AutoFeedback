from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
     url(r'^$', 'make.views.home', name='home'),
     url(r'^(?P<make_id>\d+)/$', 'make.views.make'),
     url(r'^gen/$', 'make.views.model'),
     url(r'^comment/$', 'make.views.generation'),
)
