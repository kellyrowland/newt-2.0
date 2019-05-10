from django.conf.urls import url
from file.views import FileView, FileRootView, ExtraFileView


urlpatterns = [
    url(r'^$', FileRootView.as_view()),
    url(r'^(?P<machine_name>[^/]+)(?P<path>/.*)$', FileView.as_view()),
    url(r'^(?P<query>.+)/$', ExtraFileView.as_view()),
]
    
