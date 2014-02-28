from django.conf.urls import patterns, url

from surfdata import views

urlpatterns = patterns('',
	
    # url(r'^blog/', include('blog.urls')),
	url(r'^$', views.index, name ='index'),
	url(r'^test/', views.test, name='test'),
	
	
)