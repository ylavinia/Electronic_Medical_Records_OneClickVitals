from django.conf.urls import patterns, include, url
from django.contrib import admin
from registration.backends.simple.views import RegistrationView
from django.contrib.auth.views import login, logout
from django.conf import settings

class MyRegistrationView(RegistrationView):
    def get_success_url(self,request, user):
        return '/oneclickvitals/'

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('oneclickvitals.urls')),
    url(r'^accounts/login/$', 'oneclickvitals.views.login_view'),
    url(r'^accounts/logout/$', 'oneclickvitals.views.logout_view'),
    url(r'^accounts/invalid_login/$', 'oneclickvitals.views.invalid_login_view'),
    url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^patient/$', 'oneclickvitals.views.index_patient'),
    url(r'^oneclickvitals/$', 'oneclickvitals.views.index_doctor'),
    url(r'^staff/$', 'oneclickvitals.views.index_staff'),
    )

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),)
        
