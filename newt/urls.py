from django.conf.urls import include, url
from newt.views import RootView
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'newt.views.home', name='home'),
    # url(r'^newt/', include('newt.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', admin.site.urls),

    url(r'^api/?$', RootView.as_view()),
    url(r'^api/status', include('status.urls')),
    url(r'^api/file', include('file.urls')),
    url(r'^api/auth', include('authnz.urls')),
    url(r'^api/command', include('command.urls')),
    url(r'^api/store', include('store.urls')),
    url(r'^api/account/', include('account.urls')),
    url(r'^api/job', include('job.urls')),

]
