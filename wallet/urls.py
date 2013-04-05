__author__ = 'Federico Frenguelli <synasius@gmail.com>'


from django.conf.urls import patterns, url


urlpatterns = patterns('wallet.views',
   url(r'^$', 'wallet_list'),
   url(r'^(?P<pk>[0-9]+)/$', 'wallet_detail'),
)
