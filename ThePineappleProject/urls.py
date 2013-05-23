from django.conf.urls import patterns, include, url

from web import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.index, name="home"),
    url(r'^about$', views.about, name="about"),
    url(r'^join$', views.join, name="join"),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
