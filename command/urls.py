from django.conf.urls import url
from command.views import CommandView, CommandRootView, ExtraCommandView

urlpatterns = [
    url(r'^$', CommandRootView.as_view()),
    url(r'^(?P<machine_name>[^/]+)$', CommandView.as_view()),
    url(r'^(?P<query>.+)/$', ExtraCommandView.as_view()),
]
    
