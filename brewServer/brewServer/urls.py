from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'ferment.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^thermo/', 'ferment.views.thermo', name='thermo'),
    url(r'^admin/', include(admin.site.urls)),
)
