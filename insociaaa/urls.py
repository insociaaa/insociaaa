from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'insociaaa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'insociaaa.views.login', name='login'),
    url(r'^login$', 'insociaaa.views.login', name='login'),
    url(r'^facebook$', 'insociaaa.views.facebook', name='facebook'),
    url(r'^google$', 'insociaaa.views.google', name='google'),
    url(r'^linkedin$', 'insociaaa.views.linkedin', name='linkedin'),
    url(r'^twitter$', 'insociaaa.views.twitter', name='twitter'),
    url(r'^yahoo$', 'insociaaa.views.yahoo', name='yahoo'),

    url(r'^admin/', include(admin.site.urls)),
)
