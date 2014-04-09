from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'insociaaa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # Login links
    url(r'^$', 'insociaaa.views.login', name='login'),
    url(r'^login$', 'insociaaa.views.login', name='login'),

    # SSN links
    url(r'^facebook$', 'insociaaa.views.facebook', name='facebook'),
    #url(r'^linkedin$', 'insociaaa.views.linkedin', name='linkedin'),
    url(r'^linkedin$', 'app_linkedin.views.get_news', name='get_news'),
    url(r'^twitter$', 'insociaaa.views.twitter', name='twitter'),

    # News links
    url(r'^cnn$', 'app_cnn.views.cnn', name='cnn'),
    url(r'^et$', 'app_et.views.et', name='et'),
    url(r'^forbes$', 'app_forbes.views.forbes', name='forbes'),

    # ECommerce links
    url(r'^amazon$', 'app_amazon.views.amazon', name='amazon'),
    url(r'^ebay$', 'app_ebay.views.ebay', name='ebay'),

    # Travel links
    url(r'^expedia$', 'app_expedia.views.expedia', name='expedia'),

    url(r'^admin/', include(admin.site.urls)),
)
