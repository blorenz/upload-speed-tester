from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'uploadTester.views.home', name='home'),
    url(r'^form$', 'uploadTester.views.form_submit', name='form_submit'),
    url(r'^vp$', 'uploadTester.views.videopost', name='videoPost'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
