from django.conf.urls import patterns, include, url

from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'CenterClass.core.views.home', name='home'),
        
    url(r'^sobre/', 'CenterClass.core.views.sobre', name='sobre'),    

    url(r'^profilejr/', 'CenterClass.core.views.profilejr', name='profilejr'),
    
    url(r'^profilemarco/', 'CenterClass.core.views.profilemarco', name='profilemarco'),

    url(r'^agenda/', 'CenterClass.agenda.views.lista', name='agenda'),    

    url(r'^adiciona/', 'CenterClass.agenda.views.adiciona'),

    url(r'^item/(?P<nr_item>\d+)/$', 'CenterClass.agenda.views.item'),    

    url(r'^remove/(?P<nr_item>\d+)/$', 'CenterClass.agenda.views.remove'),

    (r'^login/$', 'django.contrib.auth.views.login',
        {'template_name': 'login.html' }),

    (r'^logout/$', 'django.contrib.auth.views.logout_then_login',
        {'login_url': '/login/'}),    

      
)
if settings.DEBUG:
	urlpatterns += patterns('',
		(r'^media/(?P<path>.*)$', 'django.views.static.serve',
			{'document_root': settings.MEDIA_ROOT}),
	)	
	