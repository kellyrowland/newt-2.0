from django.conf.urls import url
from status.views import StatusView, ExtraStatusView

urlpatterns = [
    url(r'^$', StatusView.as_view()),
    url(r'^(?P<machine_name>[^/]+)$', StatusView.as_view()),
    url(r'^(?P<query>.+)/$', ExtraStatusView.as_view()),
]
    
