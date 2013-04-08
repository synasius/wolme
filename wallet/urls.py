__author__ = 'Federico Frenguelli <synasius@gmail.com>'


from django.conf.urls import patterns, url

from rest_framework.urlpatterns import format_suffix_patterns

from wallet import views


urlpatterns = patterns('',
   url(r'^$', views.WalletList.as_view()),
   url(r'^(?P<pk>[0-9]+)/$', views.WalletDetail.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)
