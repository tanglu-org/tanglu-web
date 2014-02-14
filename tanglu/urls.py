from django.conf.urls.defaults import *
from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^i18n/', include('django.conf.urls.i18n')),
    # url(r'^tanglu/', include('tanglu.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

# Translatable pages
urlpatterns += i18n_patterns('',
#     url(r'^$', 'tanglu.views.index', name='index'),
#     url(r'^download/$', 'tanglu.views.download', name='download'),
#     url(r'^contribute/$', 'tanglu.views.contribute', name='contribute'),
#     url(r'^faq/$', 'tanglu.views.faq', name='faq'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('cms.urls')),
)

# Added to make static files work in dev environment
urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns = patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}
        ),
        url(r'', include('django.contrib.staticfiles.urls')),
    ) + urlpatterns
