from django.conf.urls import patterns, include, url

from django.contrib import admin
from surfdata import views

admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'surf.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
   	url(r'^surfdata/', include('surfdata.urls')),

    url(r'^admin/', include(admin.site.urls)),
   
    )
	