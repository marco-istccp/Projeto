from django.conf.urls import patterns, include, url

from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'CenterClass.core.views.home', name='home'),
    # url(r'^CenterClass/', include('CenterClass.foo.urls')),
    
    url(r'^sobre/', 'CenterClass.core.views.sobre', name='sobre'),    

    #url(r'^cursos/', 'CenterClass.CadastraCurso.views.cursos', name='cursos'),

    url(r'^agenda/', 'CenterClass.agenda.views.lista', name='agenda'),    

    url(r'^adiciona/', 'CenterClass.agenda.views.adiciona'),

    url(r'^item/(?P<nr_item>\d+)/$', 'CenterClass.agenda.views.item'),    

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls'),    
)
if settings.DEBUG:
	urlpatterns += patterns('',
		(r'^media/(?P<path>.*)$', 'django.views.static.serve',
			{'document_root': settings.MEDIA_ROOT}),
	)	
	