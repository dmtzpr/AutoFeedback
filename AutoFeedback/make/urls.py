from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
   
    # Uncomment the next line to enable the admin:
    #url(r'^vw/', 'article.views.vw'),
    #url(r'^audi/', 'article.views.audi'),

     url(r'^$', 'make.views.home', name='home'),
     url(r'^(?P<make_id>\d+)/$', 'make.views.make'),
)
