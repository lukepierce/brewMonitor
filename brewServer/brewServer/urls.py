from django.conf.urls import patterns, include, url
from django.contrib import admin
from ferment.views import Thermo
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'ferment.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^thermo/', Thermo.as_view()),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^data/', 'ferment.views.viewData'),
)

urlpatterns = format_suffix_patterns(urlpatterns)
