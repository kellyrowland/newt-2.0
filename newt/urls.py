from django.urls import include, path
from newt.views import RootView
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'newt.views.home', name='home'),
    # url(r'^newt/', include('newt.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    path(r'admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    path(r'admin/', admin.site.urls),

    path(r'api', RootView.as_view()),
    path(r'api/status', include('status.urls')),
    path(r'api/file', include('file.urls')),
    path(r'api/auth', include('authnz.urls')),
    path(r'api/command', include('command.urls')),
    path(r'api/store', include('store.urls')),
    path(r'api/account', include('account.urls')),
    path(r'api/job', include('job.urls')),

]
