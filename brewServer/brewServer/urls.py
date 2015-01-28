from django.conf.urls import patterns, include, url
from django.contrib import admin
from ferment.views import thermo

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'ferment.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^thermo/', thermo.as_view()),
    url(r'^admin/', include(admin.site.urls)),
)
