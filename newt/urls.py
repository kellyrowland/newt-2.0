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
    path('admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    path('admin/', admin.site.urls),

    path('api', RootView.as_view()),
    path('api/status/', include('status.urls')),
    path('api/file/', include('file.urls')),
    path('api/auth/', include('authnz.urls')),
    path('api/command/', include('command.urls')),
    path('api/store/', include('store.urls')),
    path('api/account/', include('account.urls')),
    path('api/job/', include('job.urls')),
    path('api/site/', include('website.urls')),

]
